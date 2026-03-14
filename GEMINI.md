# GEMINI.md - Accessibility Skills Project Context

This project is a comprehensive accessibility toolkit designed for AI coding agents (like Gemini, Claude Code, Cursor, etc.). It provides instructional "skills" in Markdown and a suite of standalone Python audit scripts to help developers build and test WCAG 2.2 AA compliant web interfaces.

## Project Overview

- **Purpose:** To provide AI agents with the domain-specific knowledge required to build accessible interfaces for people with motor, cognitive, visual, and communication disabilities.
- **Key Focus Areas:**
  - **Motor Accessibility:** Switch access, eye gaze, touch targets, and fatigue detection (derived from AAC product development).
  - **Cognitive Accessibility:** Plain language, dyslexia-friendly typography, and reduced motion.
  - **Visual Accessibility:** Contrast ratios, color independence, CVI (Cortical Visual Impairment) support, and detailed alt-text strategies.
  - **Screen Reader Compatibility:** ARIA landmarks, semantic HTML, and focus management.
  - **Inclusive Testing:** Manual and automated testing methodologies.

## Core Components

- **Skills (Markdown):**
  - `SKILL.md`: The primary, self-contained instructional file for AI agents.
  - `plugins/accessibility/skills/`: Domain-specific sub-skills (e.g., `motor/SKILL.md`, `visual/SKILL.md`).
- **Audit Scripts (Python):** 14 standalone scripts in `scripts/` using only the Python standard library.
- **Reference Material:** 
  - `reference/accessibility.css`: Production-ready CSS for common accessibility needs.
  - `reference/patterns.md`: Reusable HTML/JS patterns for accessible components (modals, focus traps, etc.).

## Key Commands and Usage

### Running Audit Scripts
The scripts in `scripts/` are designed to be run against HTML files or with specific color values.

```bash
# Check contrast between two hex colors
python3 scripts/contrast-checker.py "#333333" "#f5f5f5"

# Audit an HTML file for accessibility issues
python3 scripts/alt-text-audit.py index.html
python3 scripts/target-size-check.py index.html

# Run all HTML audits at once
for script in scripts/*-audit.py scripts/*-check.py; do
  python3 "$script" index.html
done

# Output in JSON format for CI/CD
python3 scripts/link-text-audit.py --format json index.html
```

## Development Conventions

- **Python Scripts:** Must strictly use the Python **standard library** only (no `pip install` required). They should support `--format json` for automation.
- **Accessibility Standards:** All guidance and scripts align with **WCAG 2.2 AA**.
- **Instructional Style:** Skills are designed to be "system prompts" or "instructions" for AI agents, focusing on actionable patterns rather than simple checklists.
- **File Structure:**
  - `plugins/accessibility/`: Follows the Claude plugin structure.
  - `scripts/`: Implementation of audit logic.
  - `reference/`: Best-practice implementations and snippets.

## Important Project Context for Gemini

When working in this codebase, prioritize accessibility and WCAG 2.2 AA compliance. If the user asks to build a UI component, refer to the guidance in `SKILL.md` and the patterns in `reference/patterns.md` to ensure it is inclusive by design.
