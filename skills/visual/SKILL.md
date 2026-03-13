---
name: visual
description: "Visual accessibility: contrast ratios, color independence, CVI/photophobia/color blindness, alt text (4 styles), forced colors, text scaling. WCAG 2.2 AA."
---

Visual accessibility patterns for web interfaces. Covers contrast requirements, color independence, specialized vision needs (CVI, photophobia, color blindness), alt text best practices, forced colors mode, and text scaling.

> **Related skills:** `/accessibility:motor` (touch targets, keyboard, switch access), `/accessibility:cognitive` (plain language, reduced motion), `/accessibility:screen-reader` (semantic structure, ARIA), `/accessibility:testing` (full WCAG checklist + all audit scripts)

## When to Use This Skill

- Working with color, contrast, or theming
- Adding images, icons, charts, or data visualizations
- Supporting Windows High Contrast or forced colors mode
- Writing alt text for any image content

## Core Principles

1. **Never convey information through color alone.** Add icons, patterns, text labels, or shapes alongside color.
2. **Test with real vision simulations.** Chrome DevTools > Rendering > Emulate vision deficiency.
3. **Alt text describes purpose, not appearance.** "Submit form" not "Blue button with arrow icon."

## Contrast

- **Normal text**: 4.5:1 contrast ratio against background
- **Large text** (18px+ regular, or 14px+ bold): 3:1 contrast ratio
- **UI components and graphics**: 3:1 contrast ratio for borders, icons, and interactive states

## Color Independence

Never convey information through color alone. Add icons, patterns, text labels, or shapes alongside color:
- Status indicators: green dot + "Active" text label
- Form errors: red border + error icon + text message
- Data visualizations: color + pattern fills + direct labels

## Specialized Vision Needs

- **CVI (Cortical Visual Impairment)**: Support high-contrast themes — yellow text on black background works well
- **Photophobia**: Offer low-brightness themes with muted colors
- **Color blindness**: Test with deuteranopia (red-green, ~8% of males) and protanopia simulators. Never use red/green as the only differentiator.

## Alt Text

Four styles for different contexts:

- **Concise** (social media, thumbnails): ~125 characters. Describe the essential content and purpose. "Bar chart showing renewable energy adoption doubling between 2020 and 2025"
- **Detailed** (documentation, educational content): ~300 characters. Describe purpose first, then visual details. "Scatter plot comparing student test scores to study hours. Positive correlation visible — students studying 10+ hours score 20% higher on average. Outliers at low study hours suggest other factors."
- **Functional** (interface elements): Describe what it does, not what it looks like. "Submit form" not "Blue button with arrow icon"
- **Neurodivergent** (social/emotional support): Explicitly describe facial expressions AND their likely meanings ("smiling, suggesting friendliness"), spell out body language, describe social cues and power dynamics, flag potential misunderstandings. Helps autistic users and others who find nonverbal cues difficult to interpret.

Rules:
- Decorative images: empty `alt=""` always — never omit the attribute entirely
- Charts and graphs: describe the trend or insight, not every data point
- Complex images: use `aria-describedby` pointing to a longer text description nearby
- Icons with text labels: `alt=""` on the icon (the label does the work)
- Icons without text labels: `alt="Description of action"` or `aria-label`

Output validation (post-processing generated alt text):
- Strip common prefixes: "alt text:", "description:", "image shows:", "a photo of", "an image of"
- Ensure terminal punctuation — add a period if the text doesn't end with `.` `!` or `?`
- Truncate at sentence boundaries, never mid-word — readability over character count
- Normalize whitespace and fix sentence spacing (single space after periods)
- Never wrap the output in quotation marks
- Length limits: ~125 characters for social media; 125–300 characters for web content depending on context

## System Integration

- **Forced colors mode**: Windows High Contrast mode overrides your styles. Test that borders, outlines, and focus indicators remain visible. Use the `forced-colors: active` media query (the `-ms-high-contrast` query is deprecated). Embrace CSS system colors (`Canvas`, `CanvasText`, `LinkText`, `ButtonFace`, etc.) which auto-adapt.
- **Contrast mode**: Use `@media (prefers-contrast: more)` to provide increased contrast when the OS requests it. This is distinct from forced colors — it enhances your existing theme rather than overriding it.
- **Text scaling**: UI must remain functional at 200% browser zoom with no content loss or overlap (WCAG 1.4.4)
- **No images of text**: Use real text styled with CSS. Images of text can't be resized, searched, or read by screen readers.

## WCAG 2.2 AA — Perceivable Checklist

- [ ] Images have descriptive alt text (or empty `alt=""` for decorative)
- [ ] Video has synchronized captions
- [ ] Color is not the sole means of conveying information
- [ ] Text contrast meets 4.5:1 (normal) / 3:1 (large)
- [ ] Text resizable to 200% without loss
- [ ] No images of text

## Included Scripts

| Script | What it checks |
|--------|---------------|
| `contrast-checker.py` | WCAG contrast ratio between two hex colors |
| `cvi-contrast-check.py` | CVI-safe contrast (10:1+), photophobia, deuteranopia presets |
| `color-only-check.py` | Patterns where color is the sole information carrier |
| `alt-text-audit.py` | Missing, empty, or suspicious alt text on images |

```bash
python3 scripts/contrast-checker.py "#333333" "#f5f5f5"
python3 scripts/cvi-contrast-check.py --preset cvi
python3 scripts/color-only-check.py index.html
python3 scripts/alt-text-audit.py index.html
```

## Reference Files

- `reference/visual.css` — Forced colors media query for Windows High Contrast
- `reference/theme-switcher.md` — Accessible theme switcher with CVI, photophobia, and deuteranopia presets

## Common Issues and Fixes

| Issue | Fix |
|-------|-----|
| Missing alt text | Add descriptive `alt` attribute |
| Low contrast text | Increase to 4.5:1 ratio |
| Div-based buttons | Use `<button>` element instead |
| Auto-playing media | Add pause/stop controls, no autoplay |
