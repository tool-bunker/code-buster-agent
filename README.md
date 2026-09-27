# Code Buster Agent

Portable agent skills and plugin packaging for using [Code Buster](https://github.com/tool-bunker/code-buster) to map, inspect, and review software repositories.

This repository packages one canonical `code-buster` skill for multiple agent ecosystems. It does not contain the Code Buster analyzer itself; `cb` must be installed separately.

## Requirements

- Code Buster 0.7.1 or newer
- A local repository to analyze

Verify the CLI before invoking the skill:

```sh
cb version
cb doctor
```

## Install as an Agent Skill

The open Agent Skills CLI installs the skill for supported agents including Codex, Claude Code, Cursor, Gemini CLI, GitHub Copilot, and others:

```sh
npx skills add tool-bunker/code-buster-agent@code-buster -g -y
```

List installed skills:

```sh
npx skills list -g
```

Project-local installation is also supported by omitting `-g`.

## Install in Pi

Install the npm package and reload Pi:

```sh
pi install npm:code-buster-agent
```

Invoke the skill explicitly with `/skill:code-buster`, or let Pi load it when a repository-analysis task matches its description.

## Install in Cursor

The repository is packaged as a Cursor plugin. After it is accepted into the Cursor Marketplace, install `code-buster` from **Cursor → Customize → Plugins**.

The same canonical skill remains available through the Agent Skills CLI:

```sh
npx skills add tool-bunker/code-buster-agent@code-buster -g -y
```

## Install as a Claude Code plugin

Add this repository as a marketplace and install the plugin:

```sh
claude plugin marketplace add tool-bunker/code-buster-agent
claude plugin install code-buster@tool-bunker
```

The Claude plugin uses the same canonical skill under `skills/code-buster/`; there is no second copy to drift.

## What the skill provides

- Repository mapping with `summary`, `structure`, `graph`, and `clusters`
- Focused impact analysis with `inspect`, `related`, `why`, and `path`
- Quality investigation with `dead`, `duplication`, `complexity`, and `hotspots`
- Changed-scope review with `review`, `pr`, and `--changed`
- Evidence-based interpretation of actionable findings, advisories, security hotspots, and processing diagnostics
- Safe remediation and verification guidance

The skill treats Code Buster findings as evidence requiring source inspection. It does not instruct agents to blindly remove findings or suppress heuristics.

## Repository layout

```text
.claude-plugin/
  marketplace.json
  plugin.json
skills/
  code-buster/
    SKILL.md
    references/
tool/
  verify_package.py
```

## Development

Validate manifests, links, skill metadata, and optional CLI compatibility:

```sh
python3 tool/verify_package.py
CODE_BUSTER_EXECUTABLE=/path/to/cb python3 tool/verify_package.py
```

Check formatting and skill discovery:

```sh
npx prettier --check README.md AGENTS.md skills .claude-plugin
npx skills list
```

## Versioning

The plugin package and Code Buster CLI have independent versions. Plugin `0.1.x` currently supports Code Buster `>=0.7.1`. Compatibility changes must update the skill frontmatter, plugin manifest, README, and validator together.

## License

MIT
