# accessibility-skills

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![WCAG 2.2 AA](https://img.shields.io/badge/WCAG-2.2_AA-blue.svg)](https://www.w3.org/TR/WCAG22/)
[![Python](https://img.shields.io/badge/python-3.6+-blue.svg)](scripts/)
[![Works with](https://img.shields.io/badge/works_with-Claude_·_Codex_·_Cursor-blue.svg)](#install-as-a-plugin-claude-code)

WCAG 2.2 AA skill for coding agents. Motor, cognitive, visual, and communication accessibility — with 14 audit scripts and production CSS/JS you can drop straight into a project.

I built this because most accessibility guides stop at "add alt text and check contrast." They skip motor accessibility entirely. This one covers switch access, eye gaze, BCI (P300, SSVEP, motor imagery), sip-and-puff, fatigue detection, tremor handling, CVI, dyslexia-friendly typography, neurodivergent alt text, forced colors mode — the kind of stuff I dealt with daily building AAC products.

You do NOT want accessibility technical debt. Trust me. Plus, it's the right thing to do.

## Features

- Teaches coding agents switch access, eye gaze, and BCI design patterns from real AAC clinical practice
- Checks 14 WCAG criteria with standalone Python scripts (stdlib only, no install needed)
- Ships production CSS for focus indicators, skip links, touch targets, reduced motion, forced colors, dyslexia-friendly text
- Includes copy-paste JS patterns: focus traps, roving tabindex, accessible tooltips, screen reader announcements, modal dialogs
- Covers neurodivergent alt text (describes facial expressions, body language, social dynamics for autistic users)
- Detects motor fatigue in real time and adapts the UI (target sizes, scanning speed, option count)
- Splits into 6 skills so agents only load what they need for the current task

## Install as a plugin (Claude Code)

```bash
/plugin marketplace add lukeslp/accessibility-skills
/plugin install accessibility@accessibility-skills
```

Then use the skills:

| Skill | What it covers |
|-------|---------------|
| `/accessibility` | Everything — the full ~360 line combined skill |
| `/accessibility:motor` | Switch access, eye gaze, BCI, touch targets, keyboard nav, fatigue detection |
| `/accessibility:visual` | Contrast, CVI, color blindness, alt text (4 styles), forced colors, reflow |
| `/accessibility:cognitive` | Plain language, dyslexia, reduced motion, AAC vocabulary, executive function |
| `/accessibility:screen-reader` | Landmarks, headings, ARIA, forms, data tables, input purpose |
| `/accessibility:testing` | Full WCAG 2.2 AA checklist, manual testing, all 14 scripts |

## Other agents

`SKILL.md` is self-contained. Clone it or copy it however your agent expects markdown.

```bash
# Claude Code (clone method)
git clone https://github.com/lukeslp/accessibility-skills.git .claude/skills/accessibility

# Codex / others
cp -r . your-project/.agents/accessibility/

# Cursor / Windsurf
cp SKILL.md your-project/.cursorrules
```

## Audit scripts

14 Python scripts. stdlib only — no pip, no venv, just run them.

```bash
python3 scripts/contrast-checker.py "#333333" "#f5f5f5"
python3 scripts/alt-text-audit.py index.html
python3 scripts/target-size-check.py --threshold 44 index.html
python3 scripts/form-label-audit.py index.html       # fieldset/legend + aria-describedby validation
python3 scripts/language-audit.py index.html          # nested lang attributes + BCP 47
python3 scripts/focus-order-check.py --show-all index.html  # skip link detection

# Run everything at once
for script in scripts/*-audit.py scripts/*-check.py; do
  python3 "$script" index.html
done

# JSON output for CI
python3 scripts/alt-text-audit.py --format json index.html
```

## What's in here

```
SKILL.md                          # Combined skill (~360 lines) — works with any agent
reference/
├── accessibility.css             # Focus, SR-only, touch targets, reduced motion, forced colors, reflow, text spacing
└── patterns.md                   # Focus trap, roving tabindex, tooltip, modal, SR announcements
scripts/                          # 14 Python scripts — stdlib only
├── contrast-checker.py           # WCAG contrast ratio calculator
├── cvi-contrast-check.py         # CVI-safe contrast (10:1+), photophobia, deuteranopia
├── alt-text-audit.py             # Missing/suspicious alt text
├── heading-outline.py            # Heading hierarchy, skipped levels
├── landmark-audit.py             # ARIA landmarks, unlabeled duplicates
├── link-text-audit.py            # Vague link text, vague aria-labels
├── focus-order-check.py          # Tabindex issues, skip link detection
├── target-size-check.py          # Touch targets (24px AA / 44px AAA), label-aware
├── color-only-check.py           # Color as sole information carrier
├── timing-audit.py               # Animations without reduced-motion
├── form-label-audit.py           # Labels, fieldset/legend, aria-describedby refs
├── language-audit.py             # lang attribute, nested lang, BCP 47
├── duplicate-id-check.py         # Duplicate IDs that break ARIA
└── table-accessibility-audit.py  # Table headers, scope, captions
plugins/accessibility/skills/     # 6 skills for Claude Code plugin system
```

## Related projects

| Project | What it does |
|---------|-------------|
| [accessibility-devkit](https://github.com/lukeslp/accessibility-devkit) | TypeScript — focus traps, contrast math, color blindness simulation, axe-core |
| [accessibility-devkit-llm](https://github.com/lukeslp/accessibility-devkit-llm) | Alt text generation and WCAG auditing via LLM, CLI + MCP server |
| [awesome-accessibility](https://github.com/lukeslp/awesome-accessibility) | Curated accessibility resources |
| [accessibility-atlas](https://github.com/lukeslp/accessibility-atlas) | 53 datasets — disability demographics, web accessibility, AT usage |

## Author

**Luke Steuber**
- Website: [dr.eamer.dev](https://dr.eamer.dev)
- Bluesky: [@lukesteuber.com](https://bsky.app/profile/lukesteuber.com)
- Email: luke@lukesteuber.com

## License

MIT License — see [LICENSE](LICENSE) for details.
