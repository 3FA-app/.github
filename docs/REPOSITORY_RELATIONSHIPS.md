<!-- ore-org-baseline:begin -->
# Repository relationships for `3FA-app`

This file is rendered from `repository-relationships.json`. The JSON registry is authoritative.

- Audience: `public`
- Repositories represented: **3**
- Relationships represented: **3**
- Inventory digest: `sha256:1898a1e63e5ed5eb8fbc91d1541633814383679bfd7b8dc4036048069116453c`

## Immutable routing identity

| Field | Value |
|---|---|
| Mapping ID | `context:3fa-app` |
| GitHub owner ID | `292943121` |
| Linear project ID | `4aff8a2b-092b-40c8-8af6-820e1538c4a7` |
| Linear team ID | `eb8ab169-5afe-4b6f-9cab-3f2aa3e887dc` |

## Repositories

| Repository | Visibility | Roles | Archived |
|---|---|---|---|
| `3FA-app/.github` | `public` | `community-health`, `governance`, `relationship-registry` | no |
| `3FA-app/3fa-app.github.io` | `public` | `documentation-site` | no |
| `3FA-app/3FA-desktop.rs` | `public` | `repository` | no |

## Relationships

| From | Type | To | Status | Required |
|---|---|---|---|---|
| `3FA-app/.github` | `governs` | `3FA-app/3fa-app.github.io` | `declared` | yes |
| `3FA-app/.github` | `governs` | `3FA-app/3FA-desktop.rs` | `declared` | yes |
| `3FA-app/3fa-app.github.io` | `documents` | `3FA-app/.github` | `inferred` | no |

## Editing relationships

Put reviewed public declarations in `repository-relationships.manual.json`; do not edit the generated registry directly.
Private repository names and private-only relationships belong in the private `approved-private-registry` mirror.
Inferred edges are advisory and must remain visibly labeled until reviewed.
<!-- ore-org-baseline:end -->
