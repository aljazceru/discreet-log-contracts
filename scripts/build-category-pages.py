#!/usr/bin/env python3
"""Build Jekyll category pages from README.md.

Single source of truth: README.md. This script reads the README's H2/H3
sections and emits one Jekyll page per category under ``pages/`` with
``title``/``description``/``permalink`` frontmatter. It is intentionally a
generator, not a curator: nothing here hand-maintains a list of resources.

Usage::

        python3 build-category-pages.py <repo_dir> [--out pages] [--config .category-pages.yml]

If ``.category-pages.yml`` is absent, the script derives a one-line
description for every H3 from the section heading and uses the kebab-case
slug as the permalink.

The output files are build artifacts and are not part of the README diff.
Run this from the cron that sweeps the directory; do not commit the
generated pages/*.md as hand-maintained content.
"""
import argparse
import os
import re
import sys
from collections import OrderedDict


SECTION_HEADER = re.compile(r"^(#{2,3})\s+(.+?)\s*$")
LINK_LINE = re.compile(r"^\s*-\s+\[")
SKIP_SECTIONS = {
    "Contents", "Table of Contents", "Introduction", "Contributing",
    "Contributors", "Related Resources", "Related",
    "What is the Lightning Network?", "Where to start",
    "What is Pubky?", "What is Nostr?",
    "What is the Liquid Network?", "What are Discreet Log Contracts?",
    "What is the Ark protocol?", "What is crypto anarchy?",
    "About This Project", "Last verified",
}


def slugify(text):
    s = re.sub(r"[^\w/]+", "-", text.strip().lower())
    s = re.sub(r"/+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s


def derive_description(section_title, lines):
    """Build a short description for the page meta tag from the section."""
    if lines and lines[0].strip() and not LINK_LINE.match(lines[0]):
        blurb = lines[0].strip()
        # Strip trailing markdown punctuation
        blurb = blurb.rstrip(".")
        if len(blurb) > 240:
            blurb = blurb[:237] + "..."
        return blurb
    return f"{section_title} - resources catalogued in README.md."


def parse_readme(readme_path):
    """Walk README.md and emit (level, title, lines[]) tuples per section."""
    text = open(readme_path, encoding="utf-8").read()
    out = []
    current = None
    for line in text.splitlines():
        m = SECTION_HEADER.match(line)
        if m:
            if current is not None:
                out.append(current)
            current = (len(m.group(1)), m.group(2).strip(), [])
        elif current is not None:
            current[2].append(line)
    if current is not None:
        out.append(current)
    return out


def collect_categories(sections):
    """Pick the sections to render as their own category page."""
    # Prefer H3 under an H2, fall back to H2 itself.
    h2 = None
    cats = OrderedDict()
    for level, title, lines in sections:
        if level == 2:
            h2 = title
            if title in SKIP_SECTIONS:
                continue
            if not lines:
                continue
            has_links = any(LINK_LINE.match(l) for l in lines)
            if has_links and title not in cats:
                cats[title] = {"level": 3, "h2": None, "lines": lines, "title": title}
        elif level == 3:
            if title in SKIP_SECTIONS:
                continue
            if not any(LINK_LINE.match(l) for l in lines):
                continue
            cats[title] = {"level": 3, "h2": h2, "lines": lines, "title": title}
    return cats


def render_page(slug, title, lines, description):
    body = f"# {title}\n\n"
    body += f"{description}\n\n"
    in_list = False
    for line in lines:
        if LINK_LINE.match(line):
            body += line.rstrip() + "\n"
            in_list = True
        elif line.strip() == "":
            body += "\n"
            in_list = False
        else:
            body += line.rstrip() + "\n"
            in_list = False
    frontmatter = (
        "---\n"
        f"layout: default\n"
        f"title: {title}\n"
        f"description: {description}\n"
        f"permalink: /{slug}/\n"
        "---\n\n"
    )
    return frontmatter + body


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("repo_dir")
    ap.add_argument("--out", default="pages")
    ap.add_argument("--readme", default="README.md")
    args = ap.parse_args()

    readme = os.path.join(args.repo_dir, args.readme)
    sections = parse_readme(readme)
    cats = collect_categories(sections)
    out_dir = os.path.join(args.repo_dir, args.out)
    os.makedirs(out_dir, exist_ok=True)

    for title, info in cats.items():
        slug = slugify(title)
        description = derive_description(title, info["lines"])
        page = render_page(slug, title, info["lines"], description)
        path = os.path.join(out_dir, f"{slug}.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(page)
        print(f"wrote {path}")

    print(f"\n{len(cats)} pages written. README.md is the single source of truth.")


if __name__ == "__main__":
    sys.exit(main())