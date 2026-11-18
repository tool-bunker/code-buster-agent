---
name: code-buster
description: Map, inspect, and review software repositories with the Code Buster static-analysis CLI. Use when an agent needs repository structure, dependency paths, related files, dead code, duplication, complexity, hotspots, changed-scope review, or evidence-backed remediation priorities.
license: MIT
compatibility: Requires Code Buster 0.14.0 or newer and a local repository to analyze.
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
cb quality --structure
cb graph --format json
cb quality --hotspots
```

Prefer `--format json` for machine-readable analysis reports, but confirm the chosen view's output before parsing: some focused views emit text. Preserve the returned coverage and processing diagnostics; a low finding count is not meaningful when coverage is partial.

Do not run every command by default. Choose the smallest set that answers the task:

- Architecture or dependency question: `quality --structure`, `graph`, `inspect --path`.
- File ownership or impact question: `inspect`, `inspect --related`, `inspect --why`.
- Quality investigation: `quality --complexity`, `duplication`, `dead`, `quality --hotspots`.
- Change review: `review --changed`, `review --pr`, or `review --changed-base <ref>`.
- Remediation planning: `review --format actions`, `review --format plan`, then `rules <rule-id>`.

See [references/commands.md](references/commands.md) for command selection.

## Investigate findings

For each finding that may drive a change:

1. Record its code, path, line, severity, confidence, rationale, and suggestion.
2. Run `cb rules <rule-id>` to read the rule's evidence and limitations.
3. Inspect the source and its callers before deciding whether the finding is actionable.
4. Distinguish actionable findings, advisories, security hotspots, and processing diagnostics.
5. Check source classification before acting on generated, test, example, benchmark, or vendored code.
6. Treat repository configuration, baselines, and suppressions as user policy.
7. Use `--advisory` to inspect detailed advisory evidence; summary counts alone are not a review.

Never claim a defect solely because Code Buster emitted a heuristic finding. Never hide a real issue merely to reduce the count.

## Review changes

For worktree or pull-request review, prefer changed-scope analysis:

```sh
cb review --changed --advisory --format json
cb review --pr --advisory --format json
cb summary --changed --format json
```

Use the repository’s chosen changed base when required:

```sh
cb review --changed-base <ref> --advisory --format json
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
