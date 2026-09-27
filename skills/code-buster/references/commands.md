# Command selection

Use `cb <command> --help` as the authority for the installed version.

## Repository map

| Question                                      | Command                  |
| --------------------------------------------- | ------------------------ |
| What languages, coverage, and findings exist? | `cb summary`             |
| How is the repository organized?              | `cb structure`           |
| What depends on what?                         | `cb graph --format json` |
| Which files form dependency communities?      | `cb clusters`            |
| Where is concentrated change or quality risk? | `cb hotspots`            |

## Focused investigation

| Question                                         | Command                |
| ------------------------------------------------ | ---------------------- |
| Why and how was a file analyzed?                 | `cb inspect <path>`    |
| What code is related to this file?               | `cb related <path>`    |
| Why is this path selected or reachable?          | `cb why <path>`        |
| How are two paths connected?                     | `cb path <from> <to>`  |
| What does a rule mean and where does it abstain? | `cb explain <rule-id>` |
| Which rules are active?                          | `cb rules`             |
| Which configuration is effective?                | `cb config explain`    |

## Quality and change review

| Goal                             | Command                    |
| -------------------------------- | -------------------------- |
| Find unreachable production code | `cb dead`                  |
| Find repeated source blocks      | `cb duplication`           |
| Inspect function complexity      | `cb complexity`            |
| Review feature flags             | `cb flags`                 |
| Score repository quality         | `cb score` or `cb quality` |
| Produce prioritized work         | `cb actions` or `cb plan`  |
| Review worktree changes          | `cb review --changed`      |
| Review pull-request scope        | `cb pr --changed`          |

Prefer `--format json` for automation. Include tests, examples, or vendored files only when the task explicitly needs those source roles. Use `--all` and `--force` deliberately; they change scope or cache behavior rather than improving precision automatically.
