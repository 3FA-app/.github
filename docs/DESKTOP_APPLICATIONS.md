# Desktop application allocation

Verified **2026-08-06**.

3FA uses the paired desktop application standard:

- Rust: [`3FA-app/3FA-desktop.rs`](https://github.com/3FA-app/3FA-desktop.rs) — **live**.
- Current Flutter companion: [`ORESoftware/3fa-client-ui.dart`](https://github.com/ORESoftware/3fa-client-ui.dart) — **live** and currently cross-owned.
- Canonical organization-owned Flutter target: `3FA-app/3fa-flutter` — **planned**, not yet verified as a published repository.

The current cross-owner Flutter implementation must continue receiving desktop feature review until migration is complete. Do not mark the target live until repository history/functionality, native targets, tests, packaging, signing, and platform support are verified.

## Why both Rust and Flutter remain active

The two applications are first-class side-by-side implementations used to compare security, startup and memory use, OS integration, accessibility, developer velocity, release engineering, mobile reuse, and long-term maintenance. Neither is a disposable prototype.

Every desktop-facing feature must inspect both live codebases, share acceptance criteria and fixtures, and normally update both. A one-sided change requires an explicit no-change rationale and recorded parity gap. Completion in Rust alone is not full desktop completion, and creating an empty Flutter target is not migration completion.

## Rust desktop kit: Slint

**Selected strategy:** Slint with Rust.

**WebView policy:** prohibited.

3FA handles TOTP/HOTP seeds, encrypted vaults, recovery state, authentication, and device credentials. Slint keeps the UI compiled and native, has a low runtime footprint, and lets security-sensitive state remain in Rust without introducing a browser engine or DOM attack surface. The existing implementation already uses this strategy.

The Rust repository must maintain `docs/DESKTOP_TOOLKIT.md` describing the Slint major-version policy, platform adapters, security boundary, deep-link handling, tests, and the Flutter companion. Changing toolkits requires an ADR and coordinated updates across both repositories, this organization document, Linear, and the central strategy document.

## HTTPS-first deep linking

Deep links are shared product contracts, not framework-specific routes.

Canonical form:

```text
https://<verified-3fa-owned-host>/open/<route>?<bounded-query>
```

Fallback scheme:

```text
threefa://<route>?<bounded-query>
```

Requirements:

- define route types in `3fa-interfaces` and use the same parser/fixtures in Rust and Flutter;
- support cold start and already-running/single-instance delivery;
- validate the exact HTTPS host, route, identifiers, action, and bounded query parameters;
- never place passwords, access tokens, recovery secrets, TOTP/HOTP seeds, vault material, or private account data in a URL;
- use short-lived, one-time, audience-bound codes for sign-in or transfer handoffs;
- preserve a pending route safely through authentication; and
- test macOS, Windows, Linux, Android, and iOS app/universal-link behavior plus browser fallback.

Slint receives validated URLs through small OS-specific Rust adapters; URL parsing and privileged actions never live in the view layer.

## Product boundary

The Rust and current/target Flutter implementations should support semantic parity for authentication, multi-factor and multi-device flows, Signal Protocol state, device enrollment and revocation, recovery, secure local storage, notifications, offline behavior, deep links, and shared account/device contracts.

Shared schemas, clients, cryptographic test vectors, route fixtures, device-state models, and conformance tests must be versioned deliberately.

## Repository-local documentation

- Rust companion and migration guidance: [`3FA-app/3FA-desktop.rs` PR #22](https://github.com/3FA-app/3FA-desktop.rs/pull/22)
- Current Flutter companion guidance: [`ORESoftware/3fa-client-ui.dart` PR #14](https://github.com/ORESoftware/3fa-client-ui.dart/pull/14)
- Central toolkit assignments: [`rust-desktop-strategies.md`](https://github.com/ORESoftware/project-registry/blob/main/docs/rust-desktop-strategies.md)

## Project routing

- GitHub Project: [`3FA-app-project` — Project 1](https://github.com/orgs/3FA-app/projects/1)
- Linear project: `github.com/3FA-app`
- Central registry: [`approved-private-registry`](private-registry://canonical/registry/desktop-applications.json)
- Portfolio rollout: [`DEN-2469`](https://linear.app/denman/issue/DEN-2469/roll-out-paired-rust-flutter-desktop-repositories-across-the-portfolio)

Repository creation, migration, renames, toolkit changes, deep-link contract changes, transfers, archival, or platform-status changes must update this document, Linear, the central registry/strategy, and every current or target companion repository together.
