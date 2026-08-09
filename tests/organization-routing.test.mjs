import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';

const json = (path) => readFile(path, 'utf8').then(JSON.parse);
const routing = await json('organization-routing.json');
const schema = await json('schema/organization-routing.schema.json');
const artifactSchema = await json('schema/project-registry-artifact.schema.json');

const expectedRepositories = new Map([
  ['.github', 'governance'], ['3fa-interfaces', 'interfaces'], ['3fa-clients', 'clients'],
  ['3FA-app-cli', 'cli'], ['3fa-backend.rs', 'backend'], ['3fa-web-server.rs', 'web'],
  ['3FA-desktop.rs', 'desktop'], ['3fa-app-sync', 'sync'], ['3fa-infra', 'infra'],
  ['3fa-app-e2e', 'e2e'], ['3FA-mcp-server.rs', 'mcp'],
  ['3fa-app.github.io', 'website'], ['3fa-app-chrome-extension', 'extension'],
  ['threefa-monorepo', 'monorepo'],
]);

test('canonical owner, project, Linear, and Slack identities are exact', () => {
  assert.deepEqual(routing.github.organization, {
    login: '3FA-app', id: 292943121, type: 'Organization', url: 'https://github.com/3FA-app',
  });
  assert.equal(routing.verifiedAt, '2026-08-08');
  assert.equal(routing.github.project.number, 1);
  assert.equal(routing.github.project.title, '3FA-app-project');
  assert.equal(routing.github.project.url, 'https://github.com/orgs/3FA-app/projects/1');
  assert.equal(routing.github.project.status, 'active');
  assert.equal(routing.github.project.automationAccess, 'insufficient');
  assert.equal(routing.github.project.linearIssue, 'DEN-2439');
  assert.equal(routing.linear.projectId, '4aff8a2b-092b-40c8-8af6-820e1538c4a7');
  assert.equal(routing.linear.teamId, 'eb8ab169-5afe-4b6f-9cab-3f2aa3e887dc');
  assert.equal(routing.slack.channelId, 'C0BL6BEDYFK');
});

test('routing precedence is deterministic and fails closed', () => {
  assert.deepEqual(routing.routingPolicy.precedence, ['repositoryOverride', 'ownerContext']);
  assert.equal(routing.routingPolicy.unresolved, 'reject');
  assert.equal(routing.routingPolicy.ambiguous, 'reject');
});

test('the repository family is complete, unique, and role-aligned', () => {
  assert.equal(routing.repositories.length, expectedRepositories.size);
  assert.equal(new Set(routing.repositories.map(({ name }) => name)).size, routing.repositories.length);
  assert.equal(new Set(routing.repositories.map(({ fullName }) => fullName)).size, routing.repositories.length);
  assert.equal(new Set(routing.repositories.map(({ role }) => role)).size, routing.repositories.length);
  for (const entry of routing.repositories) {
    assert.equal(entry.fullName, `3FA-app/${entry.name}`);
    assert.equal(entry.role, expectedRepositories.get(entry.name), `unexpected role for ${entry.name}`);
  }
  assert.deepEqual([...routing.repositories.map(({ name }) => name)].sort(), [...expectedRepositories.keys()].sort());
});

test('the local projection uses an opaque locator for the central registry authority', () => {
  assert.equal(routing.authority.ownerRegistry, 'private-registry://canonical/registry/project-contexts.json');
  assert.equal(routing.authority.portfolioLinks, 'private-registry://canonical/registry/portfolio-links.csv');
  assert.match(routing.authority.localProjection, /3FA-app\/\.github\/blob\/main\/organization-routing\.json$/u);
  const forbiddenPrivateRepository = ['ORESoftware', 'project-registry'].join('/');
  assert.equal(JSON.stringify(routing).includes(forbiddenPrivateRepository), false);
});

test('schemas pin the same canonical identities, role set, and exact inventory size', () => {
  assert.equal(schema.$schema, 'https://json-schema.org/draft/2020-12/schema');
  assert.equal(schema.properties.github.properties.organization.properties.id.const, 292943121);
  assert.equal(schema.properties.github.properties.project.properties.number.const, 1);
  assert.equal(schema.properties.linear.properties.projectId.const, routing.linear.projectId);
  assert.equal(schema.properties.slack.properties.channelId.const, routing.slack.channelId);
  assert.equal(schema.properties.repositories.minItems, expectedRepositories.size);
  assert.equal(schema.properties.repositories.maxItems, expectedRepositories.size);
  assert.deepEqual(
    schema.properties.repositories.items.properties.role.enum,
    [...expectedRepositories.values()],
  );
  assert.equal(artifactSchema.properties.artifactVersion.const, 1);
  assert.equal(artifactSchema.properties.repositories.minItems, expectedRepositories.size);
  assert.equal(artifactSchema.properties.repositories.maxItems, expectedRepositories.size);
});

test('permanent routing sources contain no personal-access-token material', async () => {
  const paths = [
    'README.md', 'ORG_CONTEXT.md', 'ORGANIZATION_ROUTING.md', 'docs/PROJECTS.md',
    'organization-routing.json', 'profile/README.md', 'schema/organization-routing.schema.json',
    'schema/project-registry-artifact.schema.json',
  ];
  const content = (await Promise.all(paths.map((path) => readFile(path, 'utf8')))).join('\n');
  assert.doesNotMatch(content, /\bgh[pousr]_[A-Za-z0-9_]{20,}\b/u);
  assert.doesNotMatch(content, /github_pat_[A-Za-z0-9_]{20,}/u);
  assert.doesNotMatch(content, /lin_api_[A-Za-z0-9]{20,}/u);
  assert.doesNotMatch(content, /cfat_[A-Za-z0-9_-]{20,}/u);
});

test('documentation preserves Project #1, CLI routing, and forbids duplicate creation', async () => {
  const [routingDoc, projectDoc, readme] = await Promise.all([
    readFile('ORGANIZATION_ROUTING.md', 'utf8'),
    readFile('docs/PROJECTS.md', 'utf8'),
    readFile('README.md', 'utf8'),
  ]);
  for (const content of [routingDoc, projectDoc, readme]) {
    assert.match(content, /3FA-app-project/u);
    assert.match(content, /orgs\/3FA-app\/projects\/1/u);
    assert.match(content, /3FA-app\/3FA-app-cli/u);
    assert.match(content, /project registry/iu);
    assert.match(content, /(?:Do\s+(?:\*\*)?not(?:\*\*)?|must\s+not)\s+create\s+a\s+duplicate/iu);
    assert.match(content, /DEN-2439/u);
  }
});
