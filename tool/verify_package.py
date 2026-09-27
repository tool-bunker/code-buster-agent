#!/usr/bin/env python3
"""Validate the portable Code Buster skill and plugin package."""

from __future__ import annotations

import json
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "code-buster" / "SKILL.md"
PLUGIN = ROOT / ".claude-plugin" / "plugin.json"
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
CURSOR_PLUGIN = ROOT / ".cursor-plugin" / "plugin.json"
PACKAGE = ROOT / "package.json"
REQUIRED_COMMANDS = {
    "summary",
    "graph",
    "dead",
    "duplication",
    "structure",
    "clusters",
    "complexity",
    "hotspots",
    "inspect",
    "related",
    "why",
    "path",
    "plan",
    "actions",
    "review",
    "pr",
    "doctor",
    "explain",
    "version",
}


def fail(message: str) -> None:
    raise ValueError(message)


def load_json(path: Path) -> dict[str, object]:
    try:
        value = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as error:
        fail(f"{path.relative_to(ROOT)}: {error}")
    if not isinstance(value, dict):
        fail(f"{path.relative_to(ROOT)} must contain a JSON object")
    return value


def skill_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if match is None:
        fail("skills/code-buster/SKILL.md has no YAML frontmatter")
    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            fail(f"invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip()
    return values


def validate_links(path: Path, text: str) -> None:
    for target in re.findall(r"\[[^]]+\]\(([^)]+)\)", text):
        if "://" in target or target.startswith("#"):
            continue
        resolved = (path.parent / target.split("#", 1)[0]).resolve()
        if not resolved.is_file():
            fail(f"{path.relative_to(ROOT)} links to missing {target}")


def parse_version(value: str) -> tuple[int, int, int]:
    match = re.search(r"(\d+)\.(\d+)\.(\d+)", value)
    if match is None:
        fail(f"could not parse Code Buster version from {value!r}")
    return tuple(int(part) for part in match.groups())


def validate_cli(executable: str) -> None:
    version = subprocess.run(
        [executable, "version"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    if parse_version(version) < (0, 7, 1):
        fail(f"Code Buster 0.7.1 or newer required; received {version.strip()}")
    help_text = subprocess.run(
        [executable, "--help"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    command_line = next(
        (line for line in help_text.splitlines() if line.startswith("Commands:")),
        "",
    )
    available = set(command_line.removeprefix("Commands:").split())
    missing = sorted(REQUIRED_COMMANDS - available)
    if missing:
        fail(f"installed Code Buster is missing commands: {', '.join(missing)}")


def main() -> int:
    skill_text = SKILL.read_text()
    metadata = skill_frontmatter(skill_text)
    if metadata.get("name") != "code-buster":
        fail("skill name must be code-buster")
    if not metadata.get("description"):
        fail("skill description is required")
    if "0.7.1" not in metadata.get("compatibility", ""):
        fail("skill compatibility must declare Code Buster 0.7.1")
    validate_links(SKILL, skill_text)

    plugin = load_json(PLUGIN)
    marketplace = load_json(MARKETPLACE)
    if plugin.get("name") != "code-buster":
        fail("plugin name must be code-buster")
    if plugin.get("version") != "0.1.0":
        fail("plugin version must be 0.1.0")
    plugins = marketplace.get("plugins")
    if not isinstance(plugins, list) or not any(
        isinstance(entry, dict)
        and entry.get("name") == "code-buster"
        and entry.get("source") == "./"
        for entry in plugins
    ):
        fail("marketplace must expose the root code-buster plugin")

    package = load_json(PACKAGE)
    if package.get("name") != "code-buster-agent":
        fail("npm package name must be code-buster-agent")
    if package.get("version") != plugin.get("version"):
        fail("npm and plugin versions must match")
    keywords = package.get("keywords")
    if not isinstance(keywords, list) or "pi-package" not in keywords:
        fail("npm package must declare the pi-package keyword")
    pi_manifest = package.get("pi")
    if not isinstance(pi_manifest, dict) or pi_manifest.get("skills") != [
        "./skills"
    ]:
        fail("Pi manifest must expose ./skills")

    cursor_plugin = load_json(CURSOR_PLUGIN)
    if cursor_plugin.get("name") != plugin.get("name"):
        fail("Cursor and Claude plugin names must match")
    if cursor_plugin.get("version") != plugin.get("version"):
        fail("Cursor and Claude plugin versions must match")
    if cursor_plugin.get("skills") != "./skills":
        fail("Cursor plugin must expose ./skills")

    for reference in sorted((SKILL.parent / "references").glob("*.md")):
        validate_links(reference, reference.read_text())

    executable = os.environ.get("CODE_BUSTER_EXECUTABLE")
    if executable:
        validate_cli(executable)

    print("code-buster-agent package is valid")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, subprocess.CalledProcessError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(1) from error
