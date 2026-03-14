# Repository Guidelines

## Project Structure & Module Organization
This repository packages accessibility skills for coding agents. Treat the top-level files as the source of truth:

- `SKILL.md` contains the combined skill used for clone-based installs.
- `reference/` holds shared CSS and pattern docs.
- `scripts/` contains standalone Python audit tools (`*-audit.py`, `*-check.py`).
- `plugins/accessibility/` contains the plugin-ready copy of the same content, organized into domain skills such as `motor/`, `visual/`, and `testing/`.
- `.claude-plugin/` stores marketplace metadata.

When you update shared guidance or scripts, keep the mirrored files under `plugins/accessibility/skills/` in sync.

## Build, Test, and Development Commands
There is no build step and no npm task runner in this repo; `package.json` is metadata only. Use direct commands instead:

```bash
python3 scripts/contrast-checker.py "#333333" "#f5f5f5"
python3 scripts/alt-text-audit.py index.html
python3 scripts/target-size-check.py --threshold 44 index.html
python3 scripts/link-text-audit.py --format json page.html
```

Use these as smoke tests after changing audit logic. For plugin metadata changes, validate `plugins/accessibility/plugin.json` and `.claude-plugin/plugin.json` manually before committing.

## Coding Style & Naming Conventions
Python scripts use 4-space indentation, type hints where useful, `argparse` CLIs, and standard-library-only imports. Keep scripts dependency-free and executable with `python3`.

Use descriptive snake_case for Python identifiers and kebab-case for script filenames such as `focus-order-check.py`. Markdown files should stay concise, instructional, and example-driven.

## Testing Guidelines
There is no formal automated test suite yet. Verify changes by running the affected script against a representative HTML file and, when applicable, checking both text and `--format json` output.

For content changes, review both the root files and their packaged copies under `plugins/accessibility/skills/` to avoid drift.

## Commit & Pull Request Guidelines
Recent history favors short conventional messages such as `feat: add humanize skill from dreamer` and `fix: restructure to match official plugin marketplace layout`. Follow `type: summary` where practical; keep checkpoints out of shared history.

Pull requests should explain the user-facing impact, list mirrored paths updated, and include sample command output when script behavior changes. Link related issues and add screenshots only when documentation or marketplace metadata changes affect presentation.
