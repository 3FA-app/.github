# 3FA-app

This organization maintains software, infrastructure, interfaces, clients, services, and supporting documentation under a shared engineering baseline.

## Working principles

- Keep changes reviewable, tested, and reversible.
- Treat security, privacy, compatibility, and data durability as design constraints.
- Resolve merge conflicts semantically: reconstruct both sides' intent, preserve compatible behavior, and document deliberate trade-offs.
- Prefer canonical repositories and short, stable names; deprecate duplicates with migration notes rather than silently deleting history.
- Keep cross-repository dependencies explicit and pinned where reproducibility matters.

Organization-wide contribution and security guidance lives in this `.github` repository.

<!-- org-project-routing:start -->
## Planning and delivery

- [GitHub Project: 3FA-app-project #1](https://github.com/orgs/3FA-app/projects/1)
- [Linear planning project](https://linear.app/denman/project/githubcom3fa-app-c3db52220894)
- [Detailed organization routing contract](../ORGANIZATION_ROUTING.md)
- [Machine-readable routing projection](../organization-routing.json)
- [GitHub Projects and Linear operating guide](../docs/PROJECTS.md)

Linear owns planning, priorities, dependencies, and long-form status. GitHub Project #1 provides the cross-repository execution view; repositories remain authoritative for code, review, CI, releases, artifacts, and runtime evidence.

A restricted repository token may not see the organization Project. Do not create a duplicate board. Projects access and field reconciliation are tracked in [DEN-2439](https://linear.app/denman/issue/DEN-2439/3fa-app-grant-projects-v2-access-and-reconcile-canonical-project-1) and [GitHub issue #9](https://github.com/3FA-app/.github/issues/9).
<!-- org-project-routing:end -->
