---
layout: default
title: DLC Oracle Implementations
description: Oracle implementations for Discreet Log Contracts: krystal bull, sibyls (numeric events), p2pderivatives-oracle (Go), Kormir (Rust), Pythia, Mycelia Signal (Lightning/USDC), NOAA oracle, and the PoW-gated pow-attest.
permalink: /oracles/
---

## Oracles

- [suredbits oracle explorer](https://oracle.suredbits.com/)
- [krystal bull](https://github.com/bitcoin-s/krystal-bull) - A full-featured DLC Oracle
- [dlc-oracle-nodejs](https://github.com/mit-dci/dlc-oracle-nodejs) - A library for making Discreet Log Contracts oracles in NodeJS
- [sibyls](https://github.com/lava-xyz/sibyls) - An oracle implementation for numerical events based on rust-dlc
- [p2pderivatives-oracle](https://github.com/p2pderivatives/p2pderivatives-oracle) - An oracle implementation for numerical events written in Go
- [Cassandra (conduition.io oracle)](https://conduition.io/code/cassandra/)
- [kormir](https://github.com/bennyhodl/kormir) - A basic DLC Oracle written in Rust
- [tee8z/noaa-oracle](https://github.com/tee8z/noaa-oracle) - NOAA data oracle, queryable from browser; can attest to events for a Bitcoin DLC in dlctix style
- [Pythia](https://github.com/dlc-markets/pythia) - Rust implementation of p2p-derivative-oracle for DLC trading
- [Mycelia Signal](https://github.com/jonathanbulkeley/Mycelia-Signal-Sovereign-Oracle) - Sovereign oracle protocol with DLC attestations over Lightning sats and USDC on Base
- [pow-attest](https://attest.powforge.dev) - GitHub event oracle (PR-merged / issue-closed) emitting BIP-340 Schnorr attestations; `/announcement` endpoint exposes R-point + outcome_hash for DLC CET adaptor signing; PoW-gated, no account
