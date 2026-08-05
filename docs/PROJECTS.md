<!-- org-project-routing:start -->
# Project routing

- **GitHub organization:** [3FA-app](https://github.com/3FA-app)
- **Canonical GitHub Project:** [3FA-app-project](https://github.com/orgs/3FA-app/projects/1) (project 1)
- **Canonical Linear project:** [planning workspace](https://linear.app/denman/project/githubcom3fa-app-c3db52220894)
- **Organization documentation repository:** [3FA-app/.github](https://github.com/3FA-app/.github)

## Source-of-truth boundaries

GitHub is authoritative for repositories, commits, pull requests, reviews, CI checks, releases, deployable artifacts, and runtime evidence. Linear is authoritative for product planning, priorities, ownership, dependencies, milestones, and status reporting. The GitHub Project is the organization-level execution board and should contain the governance issue maintained by this repository.

## Change and merge policy

Documentation branches must be reviewed through pull requests and merged after checks pass. Concurrent edits are reconciled semantically against the latest default branch: this managed routing block is regenerated while all unrelated prose outside the block is preserved. Do not resolve conflicts by blindly choosing one side.
<!-- org-project-routing:end -->

## Execution snapshot — 2026-08-05

### Client release and supply-chain baseline

`3FA-app/3fa-clients` now has a truthful and fail-closed release/test baseline:

- ten-target Zed packing and native package acceptance;
- Dart retained as a Zed target without advertising a false pub.dev route;
- Rust native packaging blocked only by the exact unpublished `threefa-interfaces` dependency owned by Linear issue `DEN-320`;
- RustSec, npm advisory, and digest-pinned committed-secret scanning;
- immutable GitHub Actions references, read-only permissions, disabled checkout credential persistence, and bounded concurrency;
- clean-consumer Swift packaging and source-level language tests kept as separate evidence boundaries.

### Merged maintenance tranche

| Area | Pull request | Merge commit |
|---|---:|---|
| BEAM runner action | `3fa-clients#17` | `b84b1ed1b06f6c3fd5a93c1d0615b071d74bb3cb` |
| Zed artifact upload action | `3fa-clients#18` | `598e4ba80a32b6e272168544d7106bab419bde12` |
| Go runner action | `3fa-clients#20` | `095b0d24726cdca2944ea8e1ace58064091a9c16` |
| Python runner actions and immutable checkout | `3fa-clients#35` | `3199d36b77cd525ee5f092032df7f9286d4c5f30` |
| TypeScript Node development types | `3fa-clients#36` | `764fe51ba4ef76e104acb9cff1cf15cb7fa8eb95` |

Stale Dependabot branches `#19` and `#21` were closed only after their valid intent was rebuilt on current `main`. The replacements preserve newer runtime exports and immutable-action policy rather than mechanically rebasing obsolete file versions.

### Declared Opto Sync boundary

Pull request `3fa-clients#28` merged as `8c60b9d6ffc1fac7096014a9d2fbf5be46480cbc` and records a metadata-only Opto Sync adoption boundary at rollout phase `declared`.

The manifest:

- pins `opto-sync/opto-sync-clients` version `0.2.0` at immutable commit `068414c8ff7d4262d0a395959b5209d5908f0fcc`;
- declares Dart, Gleam, Rust, and TypeScript surfaces;
- scopes synchronization to device-directory state, encrypted-message metadata, key-bundle metadata, and causal checkpoints;
- declares IndexedDB/SQLite and HTTP/WebSocket/Supabase Realtime expectations;
- requires authenticated transport, encrypted local storage, tombstones, timestamp reconciliation, and keyed array merging;
- explicitly excludes private keys, OTP seeds, plaintext message content, passwords, and access/refresh tokens.

The declaration does not claim a queue, transport implementation, key-material synchronization, or production readiness. Linear issue `DEN-2459` records the completed declaration. Advance to `local-queue` only after restart, duplicate-delivery, stale-update, tombstone/delete, concurrent-device, and causal-replay fixtures are enforced.

### Active project lanes

1. **Publish immutable interfaces (`DEN-320`).** Decide licensing/visibility, publish `threefa-interfaces`, restore genuine Rust crates.io and Dart pub.dev routes, and record artifact provenance.
2. **Implement the declared Opto Sync metadata boundary.** Build durable metadata queues and multi-device replay/concurrency proof under a follow-up to `DEN-2459`; do not synchronize private keys, OTP seeds, plaintext, passwords, or tokens.
3. **Local OTP transfer.** Coordinate client issue `3fa-clients#4` with backend issue `3fa-backend.rs#7`; treat Bluetooth/Wi-Fi discovery, user-presence approval, encryption, and platform bridges as a multi-repository feature rather than an HTTP SDK shortcut.
4. **Actions admission and execution evidence.** A workflow marked failed with no job steps is runner-allocation evidence, not a test failure. Project status must record whether checks executed before calling a branch green or red.
5. **Release artifacts.** A release is complete only when packed artifacts, native dry-runs, checksums/provenance, and clean-consumer installation evidence map to one reviewed commit.

### Board hygiene

- Link GitHub pull requests and exact merge commits to the corresponding Linear issue.
- Keep dependency-only PRs separate from product features.
- Close stale branches only after preserving any unique semantic change on current `main`.
- Do not place personal access tokens, expiring artifact URLs, or write-capable bootstrap workflows in project documentation or permanent CI.
