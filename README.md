# accessibility-multiskill

[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![WCAG 2.2 AA](https://img.shields.io/badge/WCAG-2.2_AA-blue.svg)](https://www.w3.org/TR/WCAG22/)
[![Works with](https://img.shields.io/badge/works_with-Claude_·_Codex_·_Cursor-blue.svg)](#use-with-coding-agents)

### Handles a lot of the more complex access issues that aren't talked about much

An accessibility skill for coding agents -- covers motor, cognitive, visual, and communication disabilities with WCAG 2.2 AA compliance guidance, production CSS utilities, copy-paste JavaScript patterns, and 10 standalone audit scripts. Works with Claude Code, Manus, Cursor, Codex, and any agent that reads markdown instructions.

This is not a checklist of contrast ratios. It covers switch access, eye gaze, keyboard-only navigation, fatigue detection, dyslexia-friendly typography, neurodivergent alt text, forced colors mode, and more. The motor accessibility section comes from years of building assistive technology products — eye gaze access, BCI, physical switch access, and more. 

### You do NOT want accessibility technical debt. TRUST ME. Plus, it's the right thing to do!

## What's in here

```
SKILL.md                          # ~350 lines — organized by disability domain + WCAG 2.2 checklist
reference/
├── accessibility.css             # Production CSS (focus indicators, SR-only, touch targets, reduced motion, forced colors)
└── patterns.md                   # Copy-paste JS/HTML (focus trap, roving tabindex, native dialog, SR announcements, skip links)
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

## Use with coding agents

`SKILL.md` is the core file -- it's self-contained and works with any agent that reads markdown instructions. Clone the repo or copy the files into your project however your platform expects them.

### Claude Code

```bash
git clone https://github.com/lukeslp/accessibility-multiskill.git .claude/skills/accessibility
```

Claude Code reads `SKILL.md` from `.claude/skills/*/`.

### Codex / other agents

Clone into your project root or `.agents/` directory. Most agents read markdown files automatically.

```bash
cp -r . your-project/.agents/accessibility/
```

### Cursor / Windsurf

Copy `SKILL.md` to your project root as `.cursorrules` or point your custom instructions at it.

```bash
cp SKILL.md your-project/.cursorrules
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
