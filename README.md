# Code Buster Agent

Portable agent skills and plugin packaging for using [Code Buster](https://github.com/tool-bunker/code-buster) to map, inspect, and review software repositories.

This repository packages one canonical `code-buster` skill for multiple agent ecosystems. It does not contain the Code Buster analyzer itself; `cb` must be installed separately.

## Requirements

- Code Buster 0.14.0 or newer
- A local repository to analyze

Verify the CLI before invoking the skill:

```sh
cb version
cb doctor
```

## Install with the Agent Skills CLI

The open Agent Skills CLI installs the canonical skill for Codex, Claude Code,
Cursor, Gemini CLI, GitHub Copilot, and other compatible agents:

```sh
npx skills add tool-bunker/code-buster-agent@code-buster -g -y
```

Omit `-g` for a project-local installation. Confirm discovery with:

```sh
npx skills list -g
```

## Install as a native plugin

The repository also includes native discovery manifests for hosts that support
repository plugins. Every manifest points to `skills/code-buster/`; none carries
a second copy of the instructions.

### Claude Code

```text
/plugin marketplace add tool-bunker/code-buster-agent
/plugin install code-buster@tool-bunker
```

### Codex

```sh
codex plugin marketplace add tool-bunker/code-buster-agent
codex plugin add code-buster@tool-bunker
```

### GitHub Copilot CLI

```sh
copilot plugin marketplace add tool-bunker/code-buster-agent
copilot plugin install code-buster@tool-bunker
```

### Gemini CLI and compatible extension hosts

```sh
gemini extensions install https://github.com/tool-bunker/code-buster-agent
```

### Kimi Code

```text
/plugins install https://github.com/tool-bunker/code-buster-agent
```

Reload Kimi or start a new session after installation.

### Devin CLI

```sh
devin plugins install tool-bunker/code-buster-agent
```

### Grok Build

```sh
grok plugin install tool-bunker/code-buster-agent --trust
```

Enable the plugin in Grok after installation.

## Install in Pi

Install the npm package and reload Pi:

```sh
pi install npm:code-buster-agent
```

Invoke the skill explicitly with `/skill:code-buster`, or let Pi load it when a
repository-analysis task matches its description.

## Install in Cursor

The repository includes a Cursor plugin manifest. After marketplace acceptance,
install `code-buster` from **Cursor → Customize → Plugins**. Until then, use the
Agent Skills CLI installation above.

## Why there are no copied rules or settings hooks

Code Buster is task-triggered analysis, not an always-on coding persona. It does
not need lifecycle hooks, per-agent settings, or duplicated rule files. Keeping
one canonical skill avoids drift and lets each host activate it only for
repository-analysis work.

## What the skill provides

- Repository mapping with `summary`, `quality --structure`, and `graph`
- Focused impact analysis with `inspect`, `inspect --related`, `inspect --why`, and `inspect --path`
- Quality investigation with `dead`, `duplication`, `quality --complexity`, and `quality --hotspots`
- Changed-scope review with `review --changed`, `review --pr`, and `review --changed-base <ref>`
- Evidence-based interpretation of actionable findings, advisories, security hotspots, and processing diagnostics
- Safe remediation and verification guidance

The skill treats Code Buster findings as evidence requiring source inspection. It does not instruct agents to blindly remove findings or suppress heuristics.

## Repository layout

```text
.agents/plugins/       Shared marketplace discovery
.claude-plugin/        Claude Code plugin and marketplace
.codex-plugin/         Codex plugin
.cursor-plugin/        Cursor plugin
.devin-plugin/         Devin plugin
.github/plugin/        GitHub Copilot CLI plugin and marketplace
.grok-plugin/          Grok Build marketplace
.kimi-plugin/          Kimi Code plugin
gemini-extension.json  Gemini CLI extension
skills/
  plugin.json          Generic skill collection manifest
  code-buster/
    SKILL.md            Canonical instructions
    references/
tool/
  verify_package.py    Cross-manifest and skill validation
```

## Development

Validate manifests, links, skill metadata, and optional CLI compatibility:

```sh
python3 tool/verify_package.py
CODE_BUSTER_EXECUTABLE=/path/to/cb python3 tool/verify_package.py
```

Check formatting and skill discovery:

```sh
npx prettier --check README.md AGENTS.md skills .agents .claude-plugin .codex-plugin .cursor-plugin .devin-plugin .github/plugin .grok-plugin .kimi-plugin gemini-extension.json package.json
npx skills list
```

## Versioning

The agent package and Code Buster CLI have independent versions. Package `0.2.x` supports Code Buster `>=0.14.0`. Compatibility changes must update the skill frontmatter, every versioned manifest, README, and validator together. CI verifies the minimum supported CLI and the latest published release.

## License

MIT
