# accessibility-skill

A comprehensive accessibility skill for coding agents — covers motor, cognitive, visual, and communication disabilities with WCAG 2.2 AA compliance guidance, production CSS utilities, copy-paste JavaScript patterns, and 10 standalone audit scripts.

This is not a checklist of contrast ratios. It covers switch access, eye gaze, keyboard-only navigation, fatigue detection, dyslexia-friendly typography, neurodivergent alt text, forced colors mode, and more. The motor accessibility section comes from years of building assistive technology products — eye gaze systems, communication boards, brain-computer interfaces — for people where every interaction with a computer costs time and effort.

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

### Claude Code

This skill is submitted to the [anthropics/skills](https://github.com/anthropics/skills) community repo. To use it directly in a project:

```bash
# Clone into your project's skills directory
git clone https://github.com/lukeslp/accessibility-skill.git .claude/skills/accessibility
```

Or copy the files manually — Claude Code reads `SKILL.md` from `.claude/skills/*/`.

### OpenAI Codex CLI

Codex reads `AGENTS.md` at the repo root. Clone this repo into your project or copy the files:

```bash
# Option 1: Copy AGENTS.md to your project root (lightweight — just the rules)
cp AGENTS.md your-project/AGENTS.md

# Option 2: Copy everything (full skill + scripts + reference files)
cp -r . your-project/.agents/accessibility/
```

`AGENTS.md` summarizes the key rules and points Codex at `SKILL.md` and the reference files for deeper guidance.

### Manus

Manus also reads `AGENTS.md`. Same setup as Codex — drop the files into your project.

### Cursor

A `.cursorrules` file is included. Copy it to your project root:

```bash
cp .cursorrules your-project/.cursorrules
```

### Other agents

Most coding agents that read markdown instructions can use `SKILL.md` directly. It's self-contained — point your agent's custom instructions at it.

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
| [accessibility-devkit-llm](https://github.com/lukeslp/accessibility-devkit-llm) | LLM-powered alt text generation and WCAG auditing CLI tools + MCP server |
| [awesome-accessibility](https://github.com/lukeslp/awesome-accessibility) | Curated list of accessibility resources and tools |
| [accessibility-atlas](https://github.com/lukeslp/accessibility-atlas) | 53 datasets on disability demographics, web accessibility, and assistive technology usage |

## License

MIT. Luke Steuber.
