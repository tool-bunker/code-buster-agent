# Interpreting Code Buster results

## Finding classes

- **Actionable finding:** evidence is intended to support a direct code or configuration change.
- **Advisory finding:** evidence identifies design pressure or a review candidate; source inspection decides whether change is warranted.
- **Security hotspot:** a capability or trust boundary requiring review, not proof of exploitation.
- **Processing diagnostic:** analysis was incomplete or recovered from malformed input; it affects confidence in coverage.

## Evidence checklist

Before recommending a change, confirm:

1. The reported path and line identify live, owned source.
2. The source role is appropriate for the rule.
3. The message matches the actual syntax and control flow.
4. The rule limitations do not describe the observed case.
5. Framework, generated-code, test, or configuration context does not make the construct intentional.
6. Related files and dependency paths support the claimed impact.
7. The proposed fix addresses ownership, trust, lifecycle, or behavior rather than merely silencing the finding.

## Reporting

Include the Code Buster version, command, root, selected-file coverage, and processing status. Separate confirmed issues from review candidates. When comparing runs, report representative added, removed, and remaining findings—not only totals.
