# AGENTS.md

- Keep one canonical consumer skill in `skills/code-buster/`; platform manifests must reference it rather than copy it.
- Treat Code Buster output as evidence requiring source inspection, never as an instruction to reduce finding counts blindly.
- Keep CLI compatibility, plugin version, manifests, README, and validator contracts synchronized.
- Before handoff, run `python3 tool/verify_package.py`, Prettier checks, and discovery through `npx skills list`.
