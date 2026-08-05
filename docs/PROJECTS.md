<!-- org-project-routing:start -->
# Project routing

- **GitHub organization:** [3FA-app](https://github.com/3FA-app)
- **Canonical GitHub Project:** [3FA-app-project](https://github.com/orgs/3FA-app/projects/1) (project 1)
- **Canonical Linear project:** [github.com/3FA-app](https://linear.app/denman/project/githubcom3fa-app-c3db52220894)
- **Slack dispatch channel:** [#3fa-app](https://oresoftware-workspace.slack.com/archives/C0BL6BEDYFK)
- **Organization documentation repository:** [3FA-app/.github](https://github.com/3FA-app/.github)
- **Authoritative portfolio registry:** [ORESoftware/project-registry](https://github.com/ORESoftware/project-registry)
- **Detailed routing and repository-role map:** [ORGANIZATION_ROUTING.md](../ORGANIZATION_ROUTING.md)

## Source-of-truth boundaries

Linear is authoritative for product planning, priorities, ownership, dependencies, milestones, and status reporting. GitHub Project #1 is the organization-level execution projection. GitHub repositories are authoritative for commits, pull requests, reviews, CI checks, releases, deployable artifacts, deployments, and runtime evidence. Slack is the dispatch and status surface.

Repository-specific overrides take precedence over owner context. Missing or ambiguous routing fails closed.

## Projects access boundary

The central portfolio registry and prior GraphQL verification identify `3FA-app-project` #1 as active. The repository-scoped Actions token cannot currently list or administer organization Projects. That permission limitation must not be interpreted as project absence. **Do not create a duplicate board.** Reconcile Projects read/write access and the reciprocal fields through [DEN-2439](https://linear.app/denman/issue/DEN-2439/3fa-app-grant-projects-v2-access-and-reconcile-canonical-project-1) and [GitHub issue #9](https://github.com/3FA-app/.github/issues/9).

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

### Active project lanes

1. **Publish immutable interfaces (`DEN-320`).** Decide licensing/visibility, publish `threefa-interfaces`, restore genuine Rust crates.io and Dart pub.dev routes, and record artifact provenance.
2. **Local OTP transfer.** Coordinate client issue `3fa-clients#4` with backend issue `3fa-backend.rs#7`; treat Bluetooth/Wi-Fi discovery, user-presence approval, encryption, and platform bridges as a multi-repository feature rather than an HTTP SDK shortcut.
3. **Actions admission and execution evidence.** A workflow marked failed with no job steps is runner-allocation evidence, not a test failure. Project status must record whether checks executed before calling a branch green or red.
4. **Release artifacts.** A release is complete only when packed artifacts, native dry-runs, checksums/provenance, and clean-consumer installation evidence map to one reviewed commit.

### Board hygiene

- Link GitHub pull requests and exact merge commits to the corresponding Linear issue.
- Keep dependency-only PRs separate from product features.
- Close stale branches only after preserving any unique semantic change on current `main`.
- Do not place personal access tokens, expiring artifact URLs, or write-capable bootstrap workflows in project documentation or permanent CI.
