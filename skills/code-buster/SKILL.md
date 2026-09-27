---
name: code-buster
description: Map, inspect, and review software repositories with the Code Buster static-analysis CLI. Use when an agent needs repository structure, dependency paths, related files, dead code, duplication, complexity, hotspots, changed-scope review, or evidence-backed remediation priorities.
license: MIT
compatibility: Requires Code Buster 0.7.1 or newer and a local repository to analyze.
---

# Use Code Buster

Use Code Buster as repository evidence, not as an automatic instruction to rewrite code. Run commands from the target repository root unless `--root` explicitly selects another repository.

## Establish the runtime

Before analysis:

```sh
cb version
cb doctor
```

If `cb` is unavailable, report that prerequisite instead of substituting another analyzer. Installation instructions are in [references/installation.md](references/installation.md).

## Map before narrowing

Start with the cheapest repository-wide views:

```sh
cb summary
cb structure
cb graph --format json
cb clusters
cb hotspots
```

Use `--format json` when consuming results programmatically. Preserve the returned coverage and processing diagnostics; a low finding count is not meaningful when coverage is partial.

Do not run every command by default. Choose the smallest set that answers the task:

- Architecture or dependency question: `structure`, `graph`, `clusters`, `path`.
- File ownership or impact question: `inspect`, `related`, `why`.
- Quality investigation: `complexity`, `duplication`, `dead`, `hotspots`.
- Change review: `review`, `pr`, or a command with `--changed`.
- Remediation planning: `actions`, `plan`, then `explain <rule-id>`.

See [references/commands.md](references/commands.md) for command selection.

## Investigate findings

For each finding that may drive a change:

1. Record its code, path, line, severity, confidence, rationale, and suggestion.
2. Run `cb explain <rule-id>` to read the rule’s evidence and limitations.
3. Inspect the source and its callers before deciding whether the finding is actionable.
4. Distinguish actionable findings, advisories, security hotspots, and processing diagnostics.
5. Check source classification before acting on generated, test, example, benchmark, or vendored code.
6. Treat repository configuration, baselines, and suppressions as user policy.

Never claim a defect solely because Code Buster emitted a heuristic finding. Never hide a real issue merely to reduce the count.

## Review changes

For worktree or pull-request review, prefer changed-scope analysis:

```sh
cb review --changed
cb pr --changed
cb summary --changed --format json
```

Use the repository’s chosen changed base when required:

```sh
cb pr --changed-base <ref>
```

Correlate findings with the actual diff. Report pre-existing findings separately from regressions introduced by the change.

## Apply remediation safely

Before editing:

- identify the owning module and existing convention;
- confirm the finding’s evidence survives source inspection;
- prefer fixing the semantic cause over suppressing the symptom;
- preserve public behavior unless the task changes it;
- avoid repository-specific exceptions in reusable rules or libraries.

Use `cb fix --dry-run` before any supported automated fix. Apply fixes only when the user requested changes and the preview is safe.

## Verify the result

Rerun the exact command and scope that exposed the issue. Then run the repository’s native formatter, analyzer, tests, and build commands. Code Buster complements those tools; it does not replace them.

For machine-readable comparisons, retain the command, Code Buster version, root, configuration, selected-file coverage, and before/after findings. Inspect remaining findings rather than reporting only a reduced total.

Detailed interpretation guidance is in [references/findings.md](references/findings.md).
