#!/usr/bin/env python3
"""Build a deterministic, public-safe GitHub/Linear project registry bundle."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import date
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ROUTING = ROOT / "organization-routing.json"
DEFAULT_OUTPUT = ROOT / "dist" / "project-registry"
ARTIFACT_SCHEMA = (
    "https://github.com/3FA-app/.github/raw/main/"
    "schema/project-registry-artifact.schema.json"
)

EXPECTED_REPOSITORIES: tuple[tuple[str, str], ...] = (
    (".github", "governance"),
    ("3fa-interfaces", "interfaces"),
    ("3fa-clients", "clients"),
    ("3FA-app-cli", "cli"),
    ("3fa-backend.rs", "backend"),
    ("3fa-web-server.rs", "web"),
    ("3FA-desktop.rs", "desktop"),
    ("3fa-app-sync", "sync"),
    ("3fa-infra", "infra"),
    ("3fa-app-e2e", "e2e"),
    ("3FA-mcp-server.rs", "mcp"),
    ("3fa-app.github.io", "website"),
    ("3fa-app-chrome-extension", "extension"),
    ("threefa-monorepo", "monorepo"),
)

SECRET_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"lin_api_[A-Za-z0-9]{20,}"),
    re.compile(r"cfat_[A-Za-z0-9_-]{20,}"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def read_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    require(isinstance(value, dict), f"{path}: expected a JSON object")
    return value


def validate_public_safe(value: Any, label: str) -> None:
    serialized = json.dumps(value, sort_keys=True)
    for pattern in SECRET_PATTERNS:
        require(not pattern.search(serialized), f"{label}: credential-like material detected")


def validate_routing(routing: dict[str, Any]) -> None:
    require(routing.get("schemaVersion") == 1, "unsupported routing schemaVersion")
    verified_at = routing.get("verifiedAt")
    require(isinstance(verified_at, str), "verifiedAt must be a string")
    date.fromisoformat(verified_at)

    github = routing.get("github")
    linear = routing.get("linear")
    slack = routing.get("slack")
    require(isinstance(github, dict), "github routing is missing")
    require(isinstance(linear, dict), "linear routing is missing")
    require(isinstance(slack, dict), "slack routing is missing")

    organization = github.get("organization")
    project = github.get("project")
    require(isinstance(organization, dict), "GitHub organization routing is missing")
    require(isinstance(project, dict), "GitHub Project routing is missing")
    require(organization.get("login") == "3FA-app", "GitHub organization login drift")
    require(organization.get("id") == 292943121, "GitHub organization ID drift")
    require(project.get("number") == 1, "canonical GitHub Project number drift")
    require(project.get("title") == "3FA-app-project", "GitHub Project title drift")
    require(
        project.get("url") == "https://github.com/orgs/3FA-app/projects/1",
        "GitHub Project URL drift",
    )
    require(project.get("linearIssue") == "DEN-2439", "Projects governance issue drift")

    require(linear.get("workspaceSlug") == "denman", "Linear workspace drift")
    require(
        linear.get("projectId") == "4aff8a2b-092b-40c8-8af6-820e1538c4a7",
        "Linear project ID drift",
    )
    require(linear.get("projectName") == "github.com/3FA-app", "Linear project name drift")
    require(linear.get("teamKey") == "DEN", "Linear team key drift")

    require(slack.get("channelId") == "C0BL6BEDYFK", "Slack channel ID drift")
    require(slack.get("channelName") == "3fa-app", "Slack channel name drift")

    repositories = routing.get("repositories")
    require(isinstance(repositories, list), "repositories must be an array")
    actual = tuple((entry.get("name"), entry.get("role")) for entry in repositories)
    require(actual == EXPECTED_REPOSITORIES, "repository inventory or ordering drift")

    names: set[str] = set()
    full_names: set[str] = set()
    roles: set[str] = set()
    for entry in repositories:
        require(isinstance(entry, dict), "repository entry must be an object")
        name = entry.get("name")
        full_name = entry.get("fullName")
        role = entry.get("role")
        require(isinstance(name, str) and name, "repository name is missing")
        require(full_name == f"3FA-app/{name}", f"{name}: fullName mismatch")
        require(isinstance(role, str) and role, f"{name}: role is missing")
        require(name not in names, f"duplicate repository name: {name}")
        require(full_name not in full_names, f"duplicate repository fullName: {full_name}")
        require(role not in roles, f"duplicate repository role: {role}")
        names.add(name)
        full_names.add(full_name)
        roles.add(role)

    validate_public_safe(routing, "organization-routing.json")


def build_artifact(routing: dict[str, Any]) -> dict[str, Any]:
    validate_routing(routing)
    roles = [entry[1] for entry in EXPECTED_REPOSITORIES]
    repositories = [
        {
            **entry,
            "url": f"https://github.com/{entry['fullName']}",
        }
        for entry in routing["repositories"]
    ]

    artifact: dict[str, Any] = {
        "$schema": ARTIFACT_SCHEMA,
        "artifactVersion": 1,
        "verifiedAt": routing["verifiedAt"],
        "source": {
            "repository": "3FA-app/.github",
            "path": "organization-routing.json",
            "url": "https://github.com/3FA-app/.github/blob/main/organization-routing.json",
        },
        "github": routing["github"],
        "linear": routing["linear"],
        "slack": routing["slack"],
        "systemOfRecord": {
            "planning": "Linear",
            "executionBoard": "GitHub Project #1",
            "deliveryEvidence": "GitHub repositories",
            "dispatch": "Slack #3fa-app",
        },
        "projectFields": [
            {"name": "Linear issue", "type": "text"},
            {"name": "Linear project", "type": "text"},
            {"name": "Repository role", "type": "singleSelect", "options": roles},
        ],
        "repositories": repositories,
    }
    validate_public_safe(artifact, "project registry artifact")
    return artifact


def render_markdown(artifact: dict[str, Any]) -> str:
    organization = artifact["github"]["organization"]
    project = artifact["github"]["project"]
    linear = artifact["linear"]
    slack = artifact["slack"]

    lines = [
        "# 3FA-app GitHub and Linear project registry",
        "",
        f"Verified: **{artifact['verifiedAt']}**",
        "",
        "> Generated deterministically from `organization-routing.json`. Do not edit the artifact by hand.",
        "",
        "## Canonical routing",
        "",
        "| System | Canonical target |",
        "|---|---|",
        f"| GitHub organization | [{organization['login']}]({organization['url']}) (owner ID `{organization['id']}`) |",
        f"| GitHub Project | [{project['title']}]({project['url']}) (project `{project['number']}`) |",
        f"| Linear project | [{linear['projectName']}]({linear['projectUrl']}) (ID `{linear['projectId']}`) |",
        f"| Linear team | `{linear['teamKey']}` (ID `{linear['teamId']}`) |",
        f"| Slack dispatch | [#{slack['channelName']}]({slack['channelUrl']}) (ID `{slack['channelId']}`) |",
        "",
        "## Systems of record",
        "",
        "- Linear owns planning, priority, dependencies, milestones, ownership, and long-form status.",
        "- GitHub Project #1 is the cross-repository execution projection.",
        "- GitHub repositories own commits, reviews, checks, releases, artifacts, deployments, and runtime evidence.",
        "- Slack `#3fa-app` is the dispatch and status surface.",
        "",
        "## Canonical repository inventory",
        "",
        "| Repository | Role |",
        "|---|---|",
    ]
    for repository in artifact["repositories"]:
        lines.append(
            f"| [{repository['fullName']}]({repository['url']}) | `{repository['role']}` |"
        )

    lines.extend(
        [
            "",
            "## Required GitHub Project fields",
            "",
            "| Field | Type | Options |",
            "|---|---|---|",
        ]
    )
    for field in artifact["projectFields"]:
        options = ", ".join(f"`{option}`" for option in field.get("options", [])) or "—"
        lines.append(f"| `{field['name']}` | `{field['type']}` | {options} |")

    lines.extend(
        [
            "",
            "## Reconciliation boundary",
            "",
            "Do not create a duplicate board. Project administration remains tracked by `DEN-2439` and GitHub issue `3FA-app/.github#9` until an organization-authorized Projects v2 credential verifies and reconciles Project #1.",
            "",
            "```bash",
            "gh project view 1 --owner 3FA-app --format json",
            "gh project field-list 1 --owner 3FA-app --format json --limit 100",
            "gh project item-list 1 --owner 3FA-app --format json --limit 100",
            "```",
            "",
            "The workflow bundle contains this Markdown document, a machine-readable JSON projection, and `SHA256SUMS`.",
            "",
        ]
    )
    markdown = "\n".join(lines)
    validate_public_safe(markdown, "project registry Markdown")
    return markdown


def write_bundle(routing_path: Path, output_dir: Path) -> tuple[Path, Path, Path]:
    routing = read_json(routing_path)
    artifact = build_artifact(routing)
    output_dir.mkdir(parents=True, exist_ok=True)

    json_path = output_dir / "3fa-app-project-registry.json"
    markdown_path = output_dir / "3fa-app-project-registry.md"
    checksums_path = output_dir / "SHA256SUMS"

    json_path.write_text(
        json.dumps(artifact, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    markdown_path.write_text(render_markdown(artifact), encoding="utf-8")

    checksum_lines = []
    for path in sorted((json_path, markdown_path), key=lambda item: item.name):
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        checksum_lines.append(f"{digest}  {path.name}")
    checksums_path.write_text("\n".join(checksum_lines) + "\n", encoding="utf-8")

    return json_path, markdown_path, checksums_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--routing", type=Path, default=DEFAULT_ROUTING)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    paths = write_bundle(args.routing, args.output_dir)
    print(f"built {len(paths)} project registry files in {args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
