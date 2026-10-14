---
layout: default
title: Discreet Log Contracts (DLC) Directory
description: A directory of Discreet Log Contracts (DLC) reading material, talks, specifications, implementations, applications, oracle implementations, and community channels. Bitcoin-native smart contracts settled via oracle attestations.
permalink: /
---

# Discreet Log Contracts (DLC) Resources

Discreet log contract is an oracle contract scheme proposed by Tadge in [this whitepaper](https://adiabat.github.io/dlc.pdf).

## What are Discreet Log Contracts?

A Discreet Log Contract (DLC) is a bitcoin smart contract whose outcome is determined by an oracle's published nonce, signed off over an event (a price, a sports result, etc.). The contract is "discreet" because the oracle only sees the nonce, not the contract details — and "log" because of the discrete-log construction that ties the oracle's signature to the contract's outcome.

## Where to start

Read [the whitepaper](https://adiabat.github.io/dlc.pdf) first if you're comfortable with cryptography. Otherwise start with the [Introduction to Discreet Log Contracts](https://github.com/discreetlogcontracts/dlcspecs/blob/master/Introduction.md) on GitHub, then [Suredbits' three-part walkthrough](https://suredbits.com/discreet-log-contracts-part-1-what-is-a-discreet-log-contract/) for intuition. For protocol implementations, the [dlc-specs repo](https://github.com/discreetlogcontracts/dlcspecs) is the canonical reference.

This directory is organized by category. Pick the slice that matches what you're looking for.

## Browse by category

- [Reading]({{ '/reading/' | relative_url }}) — introductions, deep dives, Optech, DLCVM, oracle-based conditional payments
- [Talks and podcasts]({{ '/talks-and-podcasts/' | relative_url }}) — Tadge Dryja at Dev++/MIT, Bitcoin 2022, Stephan Livera, Bitcoin Explained
- [Specs]({{ '/specs/' | relative_url }}) — the dlc-specs repo and Tadge's whitepaper
- [Implementations]({{ '/implementations/' | relative_url }}) — rust-dlc, cfd-dlc, NDLC, bitcoin-s, node-dlc, DLC Dev Kit
- [Applications]({{ '/applications/' | relative_url }}) — 10101, Itchy Sats, Atomic Finance, Lava, Kruut, DLC Markets
- [Oracles]({{ '/oracles/' | relative_url }}) — krystal bull, sibyls, p2pderivatives-oracle, Kormir, Pythia
- [Community]({{ '/community/' | relative_url }}) — dlc-dev mailing list, LDK Discord DLC chat, DLC telegram

## Related Resources

To explore other aspects of the Bitcoin and freedom tech ecosystem:

- [nostr.net](https://www.nostr.net) — A complete guide to Nostr, projects, implementations, developer tools
- [liquidnetwork.wiki](https://liquidnetwork.wiki) — Liquid Network resources, libraries, tools and applications
- [pubky.tech](https://pubky.tech) — Pubky, an open protocol for censorship resistant web applications
- [lightning-network.tech](https://www.lightning-network.tech/) — Essential tools, guides, and communities for Bitcoin Lightning node operators
- [ungovernable.tech](https://ungovernable.tech) — Encryption, privacy tools, and decentralized technologies
- [ark-protocol.com](https://ark-protocol.com) — A directory of Ark protocol resources, libraries, tools and applications

## Contributing

If you'd like to add something to this list, please submit a [Pull Request on GitHub](https://github.com/aljazceru/discreet-log-contracts).

This directory is maintained by [aljaz](https://disobey.dev/contact/). Your contributions help keep this information up-to-date and valuable.
