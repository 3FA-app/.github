# 3FA-app organization handbook

> Shared operating defaults for repositories maintained under **3FA-app**. Repository-local policy may strengthen these rules but should not silently weaken them.

## Mission

3FA-app maintains authentication, multi-device identity, and security-sensitive client and service software. This `.github` repository is the canonical home for organization-wide community health files, reusable templates, engineering policy, and planning links.

## Repository contract

Each active repository must document purpose, ownership, maturity, supported platforms, local development and test commands, authoritative protocols and schemas, release and rollback procedures, compatibility policy, and GitHub Project/Linear links. Authentication components must also document trust boundaries, key lifecycle, enrollment and recovery flows, replay protection, device revocation, offline behavior, audit events, and failure modes.

## Change and review workflow

1. Anchor work in an issue, Linear item, or documented maintenance objective.
2. Keep branches and pull requests focused.
3. Explain motivation, scope, threat model impact, validation, compatibility, migration, and rollback.
4. Test success, denial, replay, expiry, recovery, revocation, concurrency, and degraded-network paths as relevant.
5. Resolve conflicts semantically by reconstructing both sides' intent.
6. Prefer squash merges for focused work unless commit structure materially improves security auditability.

## Evidence and quality

Pull requests should include reproducible commands, environments, expected and observed results, negative-path coverage, documentation updates, and CI or local-equivalent evidence. Protocol or key-format changes require consumer impact analysis, versioning, migration guidance, and rollback.

## Security and data

Never commit credentials, private keys, seed material, recovery codes, production identities, or sensitive logs. Follow `SECURITY.md` for private vulnerability reporting. Prefer well-reviewed cryptographic primitives and protocols; do not invent cryptography. Pin dependencies, actions, containers, and generated inputs where supply-chain integrity matters.

## Documentation and decisions

Keep examples executable and sanitized, links current, assumptions explicit, and trust boundaries clear. Record protocol, cryptographic, compatibility, privacy, recovery, and operational decisions that future maintainers would otherwise have to rediscover.

## Planning ownership

GitHub owns code, reviews, checks, releases, and delivery evidence. Linear owns priority, dependencies, sequencing, and cross-project planning. The organization GitHub Project is the cross-repository execution view; see `PROJECTS.md` for routing details.

## Organization health

- [ ] Profile, descriptions, topics, and READMEs are current.
- [ ] Contribution, security, support, governance, issue, and PR guidance is present.
- [ ] Required checks reflect authentication and supply-chain risk.
- [ ] Supported protocols, clients, and releases are explicit.
- [ ] Stale repositories are archived or clearly marked.
- [ ] Project links resolve and completed work is reflected in GitHub and Linear.
