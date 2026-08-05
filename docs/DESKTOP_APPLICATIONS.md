# Desktop application allocation

Verified **2026-08-05**.

3FA uses the paired native desktop application standard:

- Rust: [`3FA-app/3FA-desktop.rs`](https://github.com/3FA-app/3FA-desktop.rs) — **live**.
- Current Flutter companion: [`ORESoftware/3fa-client-ui.dart`](https://github.com/ORESoftware/3fa-client-ui.dart) — **live** and currently cross-owned.
- Target organization-owned Flutter repository: [`3FA-app/3fa-desktop-flutter`](https://github.com/3FA-app/3fa-desktop-flutter) — **planned**, not yet verified as a published repository.

The current cross-owner Flutter implementation must continue receiving desktop feature review until migration is complete. The target URL is an allocation target, not proof that the remote exists. Do not mark the target live until the repository, migrated history and functionality, native targets, tests, packaging, and supported-platform matrix are verified.

Repository-local reciprocal documentation was expanded through:

- Rust companion and migration guidance: [`3FA-app/3FA-desktop.rs` PR #22](https://github.com/3FA-app/3FA-desktop.rs/pull/22)
- Current Flutter companion guidance: [`ORESoftware/3fa-client-ui.dart` PR #14](https://github.com/ORESoftware/3fa-client-ui.dart/pull/14)

The earlier Rust repository contract was introduced in [`3FA-app/3FA-desktop.rs` PR #21](https://github.com/3FA-app/3FA-desktop.rs/pull/21).

## Product boundary

The Rust and current/target Flutter implementations should support semantic parity for authentication, multi-factor and multi-device flows, Signal Protocol state, device enrollment and revocation, recovery, secure local storage, notifications, offline behavior, and shared account/device contracts.

The Rust and Flutter implementations remain independently buildable, testable, releasable applications. Shared schemas, clients, cryptographic test vectors, fixtures, device-state models, and conformance tests should be versioned deliberately.

## Feature-delivery rule

Every desktop-facing change must inspect the live Rust repository and the current live Flutter repository, define shared acceptance criteria, update both or record an explicit no-change rationale, and report Rust and Flutter status separately. Migration work must also assess and update the target repository once it exists.

Completion in Rust is not full desktop parity while the current Flutter implementation is unchanged. Creating an empty target repository is not completion of the migration.

## Project routing

- GitHub Project: [`3FA-app-project` — Project 1](https://github.com/orgs/3FA-app/projects/1)
- Linear project: `github.com/3FA-app`
- Central registry: [`ORESoftware/project-registry`](https://github.com/ORESoftware/project-registry/blob/main/registry/desktop-applications.json)
- Portfolio rollout: [`DEN-2469`](https://linear.app/denman/issue/DEN-2469/roll-out-paired-rust-flutter-desktop-repositories-across-the-portfolio)

The central registry intentionally records the organization-owned target repository. This document and the repository-local contracts record the current cross-owner implementation during migration.

Repository creation, migration, renames, transfers, archival, or platform-status changes must update this document, Linear, the central registry, and every current or target companion repository together.
