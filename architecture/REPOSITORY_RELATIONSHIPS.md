# `3FA-app` repository relationships

Generated from reviewed policy and the current **public** repository inventory.

- Public repositories declared: **3**
- Private repository names withheld: **11**
- Relationship edges: **7**

## Repository roles

| Repository | Role | Lifecycle |
|---|---|---|
| [`.github`](https://github.com/3FA-app/.github) | `organization_governance` | `active` |
| [`3FA-desktop.rs`](https://github.com/3FA-app/3FA-desktop.rs) | `application` | `active` |
| [`3fa-app.github.io`](https://github.com/3FA-app/3fa-app.github.io) | `site` | `active` |

## Declared edges

| From | Relationship | To | Status/basis |
|---|---|---|---|
| `3FA-app/.github` | `governs` | `3FA-app/3fa-app.github.io` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `3FA-app/.github` | `governs` | `3FA-app/3FA-desktop.rs` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `organization://3FA-app` | `coordinates_via` | `capability://fiducia-cloud/distributed-coordination` | `platform-default` / `explicit-platform-decision`: locks, leases, idempotency, elections, schedules, budgets, and task claims |
| `organization://3FA-app` | `authenticates_via` | `capability://shared-auth/human-identity` | `platform-default` / `explicit-platform-decision`: platform human identity and session authority |
| `organization://3FA-app` | `interoperates_with` | `organization://cliptown` | `declared` / `explicit-product-decision`: secure clipboard-item exchange |
| `organization://3FA-app` | `deployed_via` | `platform://ORESoftware/k8s-cluster` | `platform-default` / `platform-policy`: immutable artifacts are promoted by digest through GitOps |
| `organization://3FA-app` | `packaged_via` | `platform://zed-pkg` | `platform-default` / `platform-policy`: Zed resolves artifacts while submodules compose editable source |

## Composition, service, and observability contract

Git submodules compose editable source; Zed packages resolve packages/artifacts; dual-managed commits must match. Production deploys immutable image digests, not runtime source builds. Cross-service access uses APIs/SDKs/events rather than another service database. MCP uses the product API/SDK. Services emit OpenTelemetry traces, bounded metrics, and correlated structured logs.

## Privacy boundary

This public registry deliberately omits private repository names and edges; the count above makes the boundary explicit.
