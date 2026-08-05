# 3FA-app organization context

Verified: **2026-08-05**

## Canonical identifiers

- GitHub organization: [`3FA-app`](https://github.com/3FA-app)
- GitHub owner ID: `292943121`
- GitHub owner type: `Organization`
- GitHub Project: [`3FA-app-project`](https://github.com/orgs/3FA-app/projects/1), project `1`, recorded active by the central registry and prior GraphQL verification
- Linear project: [`github.com/3FA-app`](https://linear.app/denman/project/githubcom3fa-app-c3db52220894)
- Linear project ID: `4aff8a2b-092b-40c8-8af6-820e1538c4a7`
- Linear team: Denman (`DEN`), ID `eb8ab169-5afe-4b6f-9cab-3f2aa3e887dc`
- Slack channel: [`#3fa-app`](https://oresoftware-workspace.slack.com/archives/C0BL6BEDYFK), ID `C0BL6BEDYFK`

## Authority and routing

[`ORESoftware/project-registry`](https://github.com/ORESoftware/project-registry) is authoritative for owner-to-Linear and portfolio-link routing. [`organization-routing.json`](organization-routing.json) is the tested org-local projection. Repository overrides take precedence over owner context; unresolved or ambiguous routing is rejected.

Linear owns planning and dependencies. GitHub Project #1 is the cross-repository execution view. GitHub repositories own code, reviews, checks, releases, artifacts, and runtime evidence. Slack is the dispatch and status surface.

The current repository-scoped Actions token cannot inspect or administer organization Projects. This is an automation-permission gap, not evidence that Project #1 is absent. Do not create a duplicate board; reconcile access through [DEN-2439](https://linear.app/denman/issue/DEN-2439/3fa-app-grant-projects-v2-access-and-reconcile-canonical-project-1) and [GitHub issue #9](https://github.com/3FA-app/.github/issues/9).

See [ORGANIZATION_ROUTING.md](ORGANIZATION_ROUTING.md) for the complete 13-repository role map and operating contract.

<!-- ore-org-baseline:begin -->
| Field | Value |
|---|---|
| GitHub owner | [`3FA-app`](https://github.com/3FA-app) |
| Mapping ID | `context:3fa-app` |
| GitHub owner ID | `292943121` |
| Linear project ID | `4aff8a2b-092b-40c8-8af6-820e1538c4a7` |
| Linear team ID | `eb8ab169-5afe-4b6f-9cab-3f2aa3e887dc` |
| Account type | `organization` |
| Default-community repository | [`3FA-app/.github`](https://github.com/3FA-app/.github) |
| Linear project | [github.com/3FA-app](https://linear.app/denman/project/githubcom3fa-app-c3db52220894) |
| Public repository graph | [`repository-relationships.json`](repository-relationships.json) |
| Reviewed relationship declarations | [`repository-relationships.manual.json`](repository-relationships.manual.json) |
| Baseline version | `2026-08-04` |

## Authority and synchronization

GitHub is authoritative for source code, public organization context, policy files, repository relationship declarations, and merged implementation history. Linear is the planning and delivery ledger. Material Linear changes that alter architecture, policy, or repository ownership should be represented by a GitHub issue or pull request; merged GitHub changes should be reflected in the linked Linear project.

This file is public. Do not place credentials, customer data, legal records, private operational details, security-sensitive topology, or unpublished business information here. Use the approved private project registry or another approved private system for member-only context. The public graph may identify that a private mirror exists, but it must not name private sibling repositories or reveal private-only edges.
<!-- ore-org-baseline:end -->
