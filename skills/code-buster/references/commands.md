# Command selection

Use `cb <command> --help` as the authority for the installed version.

## Repository map

| Question                                      | Command                  |
| --------------------------------------------- | ------------------------ |
| What languages, coverage, and findings exist? | `cb summary`             |
| How is the repository organized?              | `cb quality --structure` |
| What depends on what?                         | `cb graph --format json` |
| Where is concentrated change or quality risk? | `cb quality --hotspots`  |

## Focused investigation

| Question                                         | Command                         |
| ------------------------------------------------ | ------------------------------- |
| Why and how was a file analyzed?                 | `cb inspect <path>`             |
| What code is related to this file?               | `cb inspect --related <path>`   |
| Why is this path selected or reachable?          | `cb inspect --why <path>`       |
| How are two paths connected?                     | `cb inspect --path <from> <to>` |
| What does a rule mean and where does it abstain? | `cb rules <rule-id>`            |
| Which rules are active?                          | `cb rules`                      |
| Which configuration is effective?                | `cb config`                     |

## Quality and change review

| Goal                               | Command                                    |
| ---------------------------------- | ------------------------------------------ |
| Find unreachable production code   | `cb dead`                                  |
| Find repeated source blocks        | `cb duplication`                           |
| Inspect function complexity        | `cb quality --complexity`                  |
| Review feature flags               | `cb review --only feature-flag --advisory` |
| Score repository quality           | `cb quality --score`                       |
| Inspect aggregate quality measures | `cb quality --format json`                 |
| Produce a structured action list   | `cb review --format actions`               |
| Produce a prioritized plan         | `cb review --format plan`                  |
| Review worktree changes            | `cb review --changed --advisory`           |
| Review pull-request scope          | `cb review --pr --advisory`                |

Prefer `--format json` for supported machine-readable reports. `quality --score`, `rules <rule-id>`, and `review --format plan` emit text; use `quality --format json` for structured quality measures. `review --format actions` already emits JSON. Include tests, examples, or vendored files only when the task explicitly needs those source roles. Use `--all` deliberately to expand source classifications and `--no-cache` for a fresh analysis. `--force` authorizes replacement where supported; it is not a precision or cache setting.
