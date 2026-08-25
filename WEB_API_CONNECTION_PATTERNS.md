# 3FA web/API connection patterns

Status: organization architecture guidance, tracked by [DEN-4264](https://linear.app/denman/issue/DEN-4264/document-3fa-app-webapi-connection-patterns).

This policy applies to traditional customer/admin web/BFF, API, enrollment, recovery, audit, and background services. Authentication and factor state receive the most restrictive routing.

## Four supported avenues

| Avenue | Appropriate use | Boundary |
| --- | --- | --- |
| Direct database read | Named non-sensitive public/reference projection with a measured need | Never identity, factor, credential, enrollment, recovery, session, device, audit, challenge, authorization, or write data; require distinct `SELECT`-only, `READ ONLY`, non-owner, `NOBYPASSRLS` access |
| Stateless HTTP/JSON | Default synchronous web-to-API path | Required for every identity/factor/session read, authentication operation, enrollment, recovery, administration, and mutation |
| Stateful TCP | Measured authorized status/subscription stream with no secret or factor material | Never authentication, challenge, credential, recovery, enrollment, or authorization authority; require ADR, mTLS/delegated identity, bounded frames, deadlines, backpressure, and reconnect policy |
| NATS/message queue | Durable post-commit audit export, notification, or downstream effect | Never login, factor verification, recovery, authorization, session creation, or immediate response; require transactional outbox and idempotent consumers |

HTTP is the default. There is no direct-database exception for identity, factor, credential, or session data.

## Decision and ownership

1. All identity, factor, credential, session, challenge, enrollment, recovery, authorization, audit-detail, and mutation traffic uses the API over HTTP.
2. Immediate authoritative answers use HTTP with typed/versioned interfaces, strict bounds/deadlines, correlation context, and mutation idempotency.
3. Durable effects are inserted into a transactional outbox and delivered through NATS after commit.
4. A non-secret measured status stream may use TCP only after an ADR and API authorization.
5. Direct reads remain limited to documented non-sensitive public/reference projections under a restricted role.

The web/BFF owns HTML, opaque secure sessions, CSRF, and authorization-code plus PKCE. The API owns authentication operations, local product authorization, factor policy, recovery, and state transitions. A core/data package owns typed queries and mappings. The canonical migration repository owns DDL; services verify compatibility and never migrate production at boot.

Shared Auth proves federated identity and assurance where used; it does not own 3FA product permissions or local factor policy. Validate realm, issuer, audience, tenant, app/client, scopes, session, freshness, and assurance. Protected introspection keeps the service credential and user's token separate. Never log tokens, cookies, codes, PKCE verifiers, challenges, factor secrets, recovery material, credentials, or raw introspection results.

Pin Shared Auth and other dependencies to immutable revisions. `opto-sync` supports only declared synchronization/outbox workflows, `ores-otel` propagates redacted trace/metric context, and `zed-pkg` records dependency provenance. None may bypass API authorization or factor policy.

## Operational requirements

- Bound bodies, frames, deadlines, retries, queues, and buffers; propagate correlation and trace context.
- Require idempotency for state changes and duplicate-safe consumers.
- Fail closed; never substitute a direct query for unavailable authentication or authorization.
- Re-authorize TCP subscriptions on reconnect/expiry and prohibit secret payloads.
- Code comments identify the avenue and the identity/factor constraint it satisfies.
- Direct-read and TCP exceptions require an ADR, owner, measurements, and review/expiry date.

This document is the durable organization policy; repository ADRs may impose stricter controls.
