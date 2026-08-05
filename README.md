# 3FA-app organization defaults

This public `.github` repository contains organization-wide community health files, contributor guidance, shared agent policy, and explicit repository, planning, and delivery contracts.

Repository-local policy wins when it is stricter or more specific. Existing project history must be preserved during consolidation and conflict resolution.

## Routing and operations

- [Canonical organization routing](ORGANIZATION_ROUTING.md)
- [Machine-readable routing projection](organization-routing.json)
- [Routing schema](schema/organization-routing.schema.json)
- [GitHub Projects and Linear operating contract](docs/PROJECTS.md)
- [Repository boundaries](REPOSITORY_BOUNDARIES.md)
- [Branching and GitOps policy](BRANCHING_AND_DEPLOYMENT.md)

The canonical execution board is [GitHub Project `3FA-app-project` #1](https://github.com/orgs/3FA-app/projects/1). The planning system of record is the [Linear project `github.com/3FA-app`](https://linear.app/denman/project/githubcom3fa-app-c3db52220894). Projects access reconciliation is tracked in [DEN-2439](https://linear.app/denman/issue/DEN-2439/3fa-app-grant-projects-v2-access-and-reconcile-canonical-project-1) and [GitHub issue #9](https://github.com/3FA-app/.github/issues/9); restricted automation must not create a duplicate board.

<!-- ore-org-baseline:begin -->
## Account-wide defaults

This public repository is the canonical source for GitHub-supported fallback community files, organization profile content, reusable workflow examples, and public contributor guidance for [`3FA-app`](https://github.com/3FA-app).

- GitHub owner: [`3FA-app`](https://github.com/3FA-app)
- Linear project: [github.com/3FA-app](https://linear.app/denman/project/githubcom3fa-app-c3db52220894)
- Public context: [`ORG_CONTEXT.md`](ORG_CONTEXT.md)
- Canonical agent policy for this repository: [`agents.md`](agents.md)
- Governance: [`GOVERNANCE.md`](GOVERNANCE.md)
- Public repository graph: [`repository-relationships.json`](repository-relationships.json)
- Relationship guide: [`docs/REPOSITORY_RELATIONSHIPS.md`](docs/REPOSITORY_RELATIONSHIPS.md)
- Security reporting: [`SECURITY.md`](SECURITY.md)

GitHub applies only its documented fallback community files automatically. Agent instructions, relationship files, and reusable workflows are **not copied into sibling repositories**; repositories that need local enforcement must carry their own lowercase `agents.md` and explicitly call or copy the provided workflow.

`repository-relationships.json` is generated from GitHub owner membership plus reviewed declarations in `repository-relationships.manual.json`. It is public-safe: private repository names are omitted. The complete graph is synchronized separately to the approved private project registry.

## Safety baseline

Changes are pull-request driven. Contributors and agents must preserve concurrent work, avoid destructive Git operations, resolve conflicts semantically with full history and cross-repository context, validate affected contracts, and never claim a remote action completed without authoritative evidence.

Generated baseline version: `2026-08-04`.
<!-- ore-org-baseline:end -->
