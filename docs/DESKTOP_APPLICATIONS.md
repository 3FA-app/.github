# Desktop application allocation

Verified **2026-08-05**.

3FA uses the paired native desktop application standard:

- Rust: [`3FA-app/3FA-desktop.rs`](https://github.com/3FA-app/3FA-desktop.rs) — **live**.
- Flutter: [`3FA-app/3fa-desktop-flutter`](https://github.com/3FA-app/3fa-desktop-flutter) — **planned**, not yet verified as a published repository.

The Flutter URL is an allocation target, not proof that the remote exists. Do not mark it live until the repository, native targets, tests, packaging, and supported-platform matrix are verified.

The live Rust repository records the companion contract in [`COMPANION_DESKTOP.md`](https://github.com/3FA-app/3FA-desktop.rs/blob/main/COMPANION_DESKTOP.md), merged through [PR #21](https://github.com/3FA-app/3FA-desktop.rs/pull/21).

## Product boundary

Both implementations should support semantic parity for authentication, multi-factor and multi-device flows, Signal Protocol state, device enrollment and revocation, recovery, secure local storage, notifications, offline behavior, and shared account/device contracts.

The Rust and Flutter implementations remain independently buildable, testable, releasable applications. Shared schemas, clients, cryptographic test vectors, fixtures, device-state models, and conformance tests should be versioned deliberately.

## Feature-delivery rule

Every desktop-facing change must inspect both implementations, define shared acceptance criteria, update both or record an explicit no-change rationale, and report Rust and Flutter status separately.

## Project routing

- GitHub Project: [`3FA-app-project` — Project 1](https://github.com/orgs/3FA-app/projects/1)
- Linear project: `github.com/3FA-app`
- Central registry: [`ORESoftware/project-registry`](https://github.com/ORESoftware/project-registry/blob/main/registry/desktop-applications.json)
- Portfolio rollout: [`DEN-2469`](https://linear.app/denman/issue/DEN-2469/roll-out-paired-rust-flutter-desktop-repositories-across-the-portfolio)

Repository creation, renames, transfers, archival, or platform-status changes must update this document, Linear, the central registry, and both companion repositories together.
