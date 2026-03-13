# accessibility-skills

[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![WCAG 2.2 AA](https://img.shields.io/badge/WCAG-2.2_AA-blue.svg)](https://www.w3.org/TR/WCAG22/)
[![Works with](https://img.shields.io/badge/works_with-Claude_·_Codex_·_Cursor-blue.svg)](#use-with-coding-agents)

### Helps address complex computer access issues and the multiply disabled

An accessibility skill for coding agents that covers motor, cognitive, visual, and communication disabilities with WCAG 2.2 AA compliance guidance, production CSS utilities, copy-paste JavaScript patterns, and 10 standalone audit scripts. Works with Claude Code, Manus, Cursor, Codex, and anything else thank can take a markdown prompt with python stapled to it.

This is not a checklist. It covers switch access, eye gaze, keyboard-only navigation, fatigue detection, dyslexia-friendly typography, neurodivergent alt text, forced colors mode, and more. The motor accessibility section comes from years of building assistive technology products — eye gaze access, BCI, physical switch access, and more. 

### You do NOT want accessibility technical debt. TRUST ME. Plus, it's the right thing to do!

## What's in here

```
.claude-plugin/
├── plugin.json                   # Plugin manifest for Claude Code
└── marketplace.json              # Self-hosted marketplace catalog
skills/                           # 5 domain subskills
├── motor/                        # /accessibility:motor — switch access, eye gaze, touch targets
├── visual/                       # /accessibility:visual — contrast, alt text, forced colors
├── cognitive/                    # /accessibility:cognitive — plain language, reduced motion
├── screen-reader/                # /accessibility:screen-reader — landmarks, ARIA, forms
└── testing/                      # /accessibility:testing — full WCAG checklist + all scripts
SKILL.md                          # Combined skill (~350 lines) — backward compatible
reference/
├── accessibility.css             # Full CSS (focus, SR-only, touch targets, reduced motion, forced colors)
└── patterns.md                   # Full JS/HTML patterns (focus trap, roving tabindex, dialog, SR announcements)
scripts/                          # 10 Python scripts — stdlib only, no pip install
├── contrast-checker.py           # WCAG contrast ratio calculator
├── cvi-contrast-check.py         # High-contrast and color vision presets
├── alt-text-audit.py             # Image alt text validation
├── heading-outline.py            # Heading hierarchy checker
├── landmark-audit.py             # ARIA landmark structure
├── link-text-audit.py            # Vague/empty link text detection
├── focus-order-check.py          # Tabindex and focusability issues
├── target-size-check.py          # Touch target size (24px AA / 44px AAA)
├── color-only-check.py           # Color as sole information carrier
└── timing-audit.py               # Animation/timing without reduced-motion support
```

## Install as a plugin (Claude Code)

```bash
# Add the marketplace
/plugin marketplace add lukeslp/accessibility-skills

# Install the plugin
/plugin install accessibility@accessibility-skills
```

Then use individual skills:
- `/accessibility:motor` — Switch access, eye gaze, touch targets, keyboard nav, fatigue detection
- `/accessibility:visual` — Contrast, color independence, CVI/photophobia, alt text (4 styles), forced colors
- `/accessibility:cognitive` — Plain language, dyslexia-friendly text, reduced motion, captions, AAC
- `/accessibility:screen-reader` — Landmarks, headings, ARIA live regions, forms, data tables
- `/accessibility:testing` — Full WCAG 2.2 AA checklist, manual testing methodology, all 10 audit scripts

## Use with coding agents (legacy)

`SKILL.md` is the core file -- it's self-contained and works with any agent that reads markdown instructions. Clone the repo or copy the files into your project however your platform expects them.

### Claude Code (clone method)

```bash
git clone https://github.com/lukeslp/accessibility-skills.git .claude/skills/accessibility
```

Claude Code reads `SKILL.md` from `.claude/skills/*/`.

### Codex / other agents

Clone into your project root or `.agents/` directory. Most agents read markdown files automatically.

```bash
cp -r . your-project/.agents/accessibility/
```

### Cursor / Windsurf

Copy `SKILL.md` to your project root as `.cursorrules`, or use individual subskills:

```bash
# All-in-one
cp SKILL.md your-project/.cursorrules

# Or pick specific domains
cp skills/motor/SKILL.md your-project/.cursorrules
```

## Audit scripts

All 10 scripts use Python stdlib only — no pip install needed. Each accepts HTML files as arguments and supports `--format json` for CI pipelines.

```bash
python3 scripts/contrast-checker.py "#333333" "#f5f5f5"
python3 scripts/alt-text-audit.py index.html
python3 scripts/target-size-check.py --threshold 44 index.html

# Run all HTML audits at once
for script in scripts/*-audit.py scripts/*-check.py; do
  python3 "$script" index.html
done
```

## Related projects

| Project | What it does |
|---------|-------------|
| [accessibility-devkit](https://github.com/lukeslp/accessibility-devkit) | TypeScript packages — focus traps, contrast math, color blindness simulation, axe-core auditing |
| [accessibility-devkit-llm](https://github.com/lukeslp/accessibility-devkit-llm) | Alt text generation and WCAG auditing CLI tools + MCP server, works with any LLM provider |
| [awesome-accessibility](https://github.com/lukeslp/awesome-accessibility) | Curated list of accessibility resources and tools |
| [accessibility-atlas](https://github.com/lukeslp/accessibility-atlas) | 53 datasets on disability demographics, web accessibility, and assistive technology usage |

## License

MIT. Luke Steuber.
