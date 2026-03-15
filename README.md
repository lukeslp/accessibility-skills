# accessibility-skills

[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![WCAG 2.2 AA](https://img.shields.io/badge/WCAG-2.2_AA-blue.svg)](https://www.w3.org/TR/WCAG22/)
[![Works with](https://img.shields.io/badge/works_with-Claude_·_Codex_·_Cursor-blue.svg)](#use-with-coding-agents)

### Real-world motor accessibility for complex access needs

Accessibility skill for coding agents — motor, cognitive, visual, and communication disabilities. WCAG 2.2 AA guidance, production CSS, copy-paste JS patterns, 14 audit scripts. Drop it into Claude Code, Manus, Cursor, Codex, or anything that reads markdown.

Not a checklist. Covers switch access, eye gaze, BCI (P300, SSVEP, motor imagery), sip-and-puff, fatigue detection, tremor handling, CVI, dyslexia-friendly typography, neurodivergent alt text, forced colors mode. The motor section comes from years of building AT products — the kind of stuff most accessibility guides skip entirely.

### You do NOT want accessibility technical debt. TRUST ME. Plus, it's the right thing to do!

## What's in here

```
.claude-plugin/
├── plugin.json                   # Plugin manifest
└── marketplace.json              # Self-hosted marketplace catalog
plugins/accessibility/            # The plugin
├── plugin.json
└── skills/                       # 7 skills (1 combined + 6 domain-specific)
    ├── accessibility/             # Combined skill — full accessibility coverage (~350 lines)
    ├── motor/                    # /accessibility:motor — switch access, eye gaze, touch targets
    ├── visual/                   # /accessibility:visual — contrast, alt text, forced colors
    ├── cognitive/                # /accessibility:cognitive — plain language, reduced motion
    ├── screen-reader/            # /accessibility:screen-reader — landmarks, ARIA, forms
    ├── testing/                  # /accessibility:testing — full WCAG checklist + all scripts
    └── humanize/                 # /accessibility:humanize — strip robot language from docs
SKILL.md                          # Combined skill — backward compat for clone-based installs
reference/
├── accessibility.css             # Full CSS (focus, SR-only, touch targets, reduced motion, forced colors)
└── patterns.md                   # Full JS/HTML patterns (focus trap, roving tabindex, dialog, SR announcements)
scripts/                          # 14 Python scripts — stdlib only, no pip install
├── contrast-checker.py           # WCAG contrast ratio calculator
├── cvi-contrast-check.py         # High-contrast and color vision presets
├── alt-text-audit.py             # Image alt text validation
├── heading-outline.py            # Heading hierarchy checker
├── landmark-audit.py             # ARIA landmark structure
├── link-text-audit.py            # Vague/empty link text detection
├── focus-order-check.py          # Tabindex and focusability issues
├── target-size-check.py          # Touch target size (24px AA / 44px AAA)
├── color-only-check.py           # Color as sole information carrier
├── timing-audit.py               # Animation/timing without reduced-motion support
├── form-label-audit.py           # Input and label associations
├── language-audit.py             # Document language (lang attribute)
├── duplicate-id-check.py         # ID uniqueness for ARIA associations
└── table-accessibility-audit.py  # Table headers, scope, and captions
```

## Install as a plugin (Claude Code)

```bash
# Add the marketplace
/plugin marketplace add lukeslp/accessibility-skills

# Install the plugin
/plugin install accessibility@accessibility-skills
```

Then use skills:
- `/accessibility` — Everything (motor, visual, cognitive, screen reader, testing — the full ~350 line skill)
- `/accessibility:motor` — Switch access, eye gaze, touch targets, keyboard nav, fatigue detection
- `/accessibility:visual` — Contrast, color independence, CVI/photophobia, alt text (4 styles), forced colors
- `/accessibility:cognitive` — Plain language, dyslexia-friendly text, reduced motion, captions, AAC
- `/accessibility:screen-reader` — Landmarks, headings, ARIA live regions, forms, data tables
- `/accessibility:testing` — Full WCAG 2.2 AA checklist, manual testing methodology, all 14 audit scripts
- `/accessibility:humanize` — Strip robot language from docs and user-facing content

## Other agents (clone method)

`SKILL.md` is self-contained. Clone it or copy it however your agent expects markdown.

```bash
# Claude Code
git clone https://github.com/lukeslp/accessibility-skills.git .claude/skills/accessibility

# Codex / others
cp -r . your-project/.agents/accessibility/

# Cursor / Windsurf — all-in-one or pick a domain
cp SKILL.md your-project/.cursorrules
cp plugins/accessibility/skills/motor/SKILL.md your-project/.cursorrules
```

## Audit scripts

14 Python scripts, stdlib only. Each takes HTML files and supports `--format json` for CI.

```bash
python3 scripts/contrast-checker.py "#333333" "#f5f5f5"
python3 scripts/alt-text-audit.py index.html
python3 scripts/target-size-check.py --threshold 44 index.html

# Run everything at once
for script in scripts/*-audit.py scripts/*-check.py; do
  python3 "$script" index.html
done
```

## Related projects

| Project | What it does |
|---------|-------------|
| [accessibility-devkit](https://github.com/lukeslp/accessibility-devkit) | TypeScript — focus traps, contrast math, color blindness simulation, axe-core |
| [accessibility-devkit-llm](https://github.com/lukeslp/accessibility-devkit-llm) | Alt text generation and WCAG auditing via LLM, CLI + MCP server |
| [awesome-accessibility](https://github.com/lukeslp/awesome-accessibility) | Curated accessibility resources |
| [accessibility-atlas](https://github.com/lukeslp/accessibility-atlas) | 53 datasets — disability demographics, web accessibility, AT usage |

## License

MIT. Luke Steuber.
