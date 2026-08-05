# Organization routing

Verified: **2026-08-05**

This document is the human-readable reciprocal projection of the authoritative portfolio records in [`approved-private-registry`](private-registry://canonical). The machine-readable local projection is [`organization-routing.json`](organization-routing.json).

## Canonical identity

| System | Canonical target |
|---|---|
| GitHub organization | [`3FA-app`](https://github.com/3FA-app), owner ID `292943121` |
| GitHub Project | [`3FA-app-project`](https://github.com/orgs/3FA-app/projects/1), project `1` |
| Linear project | [`github.com/3FA-app`](https://linear.app/denman/project/githubcom3fa-app-c3db52220894), ID `4aff8a2b-092b-40c8-8af6-820e1538c4a7` |
| Linear team | Denman (`DEN`), ID `eb8ab169-5afe-4b6f-9cab-3f2aa3e887dc` |
| Slack channel | [`#3fa-app`](https://oresoftware-workspace.slack.com/archives/C0BL6BEDYFK), ID `C0BL6BEDYFK` |
| Organization defaults | [`3FA-app/.github`](https://github.com/3FA-app/.github) |

## Source-of-truth boundaries

- **Linear** owns planning, priority, ownership, dependencies, milestones, decisions, and long-form project status.
- **GitHub Project #1** is the cross-repository execution projection. It surfaces issues, pull requests, CI/review state, releases, and delivery evidence without replacing Linear planning.
- **GitHub repositories** remain authoritative for commits, reviews, checks, artifacts, releases, deployments, and runtime evidence.
- **Slack** is the dispatch and status surface. Slack work must resolve to this organization and Linear project before creating or updating tasks.

Routing precedence is `repositoryOverride` followed by `ownerContext`. Missing or ambiguous targets fail closed; automation must not guess.

## GitHub Projects access boundary

The central registry and the merged `.github` project-link PRs identify Project #1 as active. A repository-scoped `GITHUB_TOKEN` cannot currently list or administer organization Projects and was denied Projects v2 creation. That is a credential-scope limitation, not evidence that Project #1 is absent.

Do **not** create a duplicate board. Projects access and field reconciliation are tracked in:

- [Linear DEN-2439](https://linear.app/denman/issue/DEN-2439/3fa-app-grant-projects-v2-access-and-reconcile-canonical-project-1)
- [GitHub issue #9](https://github.com/3FA-app/.github/issues/9)

An authorized verification uses:

```bash
gh project view 1 --owner 3FA-app --format json
gh project field-list 1 --owner 3FA-app --format json --limit 100
gh project item-list 1 --owner 3FA-app --format json --limit 100
```

The board should contain exactly one reciprocal field for `Linear issue`, `Linear project`, and `Repository role`.

## Repository roles

| Repository | Role | Primary boundary |
|---|---|---|
| [`3FA-app/.github`](https://github.com/3FA-app/.github) | `governance` | organization policy, routing, community health, and reciprocal documentation |
| [`3FA-app/3fa-interfaces`](https://github.com/3FA-app/3fa-interfaces) | `interfaces` | schemas and cross-language wire contracts |
| [`3FA-app/3fa-clients`](https://github.com/3FA-app/3fa-clients) | `clients` | generated and hand-written client SDKs |
| [`3FA-app/3fa-backend.rs`](https://github.com/3FA-app/3fa-backend.rs) | `backend` | authenticated backend and device/sync APIs |
| [`3FA-app/3fa-web-server.rs`](https://github.com/3FA-app/3fa-web-server.rs) | `web` | web-facing Rust service |
| [`3FA-app/3FA-desktop.rs`](https://github.com/3FA-app/3FA-desktop.rs) | `desktop` | desktop authenticator application |
| [`3FA-app/3fa-app-sync`](https://github.com/3FA-app/3fa-app-sync) | `sync` | portable offline and replication mechanics |
| [`3FA-app/3fa-infra`](https://github.com/3FA-app/3fa-infra) | `infra` | desired state, deployment policy, and GitOps |
| [`3FA-app/3fa-app-e2e`](https://github.com/3FA-app/3fa-app-e2e) | `e2e` | black-box and cross-repository certification |
| [`3FA-app/3FA-mcp-server.rs`](https://github.com/3FA-app/3FA-mcp-server.rs) | `mcp` | MCP tools and read-only automation surface |
| [`3FA-app/3fa-app.github.io`](https://github.com/3FA-app/3fa-app.github.io) | `website` | public website and release discovery |
| [`3FA-app/3fa-app-chrome-extension`](https://github.com/3FA-app/3fa-app-chrome-extension) | `extension` | browser extension and user-intent boundary |
| [`3FA-app/threefa-monorepo`](https://github.com/3FA-app/threefa-monorepo) | `monorepo` | exact gitlink composition of application repositories |

## Work-item propagation

A repository branch and pull request should include the owning Linear identifier when one exists, for example `DEN-2439`. Pull-request bodies should link the Linear issue, state the repository role, list exact validation evidence, and identify any GitHub Project item when the authorized Projects integration is available.

Documentation changes follow the organization branching and semantic-conflict policy. Project metadata never overrides failed checks, unresolved reviews, missing environment approvals, or contradictory evidence.
