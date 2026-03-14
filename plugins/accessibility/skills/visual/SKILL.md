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

### Non-text Contrast (WCAG 1.4.11)

UI components and graphical objects need 3:1 contrast against adjacent colors:

- **Form inputs**: Border of text input must have 3:1 contrast against the background. Common failure: light gray borders (#ccc) on white (#fff) = 1.6:1 (fails).
- **Custom checkboxes/radios**: The visual indicator (checkmark, dot) must have 3:1 contrast against its container.
- **Focus indicators**: The focus outline itself must meet 3:1 against both the background and the element's unfocused state.
- **Icons**: Meaningful icons need 3:1 contrast. Decorative icons are exempt.
- **Charts**: Data series in graphs need 3:1 contrast between adjacent segments, not just against the background.

## Color Independence

Never convey information through color alone. Add icons, patterns, text labels, or shapes alongside color:
- Status indicators: green dot + "Active" text label
- Form errors: red border + error icon + text message
- Data visualizations: color + pattern fills + direct labels

## Specialized Vision Needs

### CVI (Cortical Visual Impairment)

CVI is a brain-based visual impairment (damage to visual cortex/pathways), not an eye condition — standard eye exams often show normal acuity. It's the leading cause of visual impairment in children in developed countries.

- **Color preference**: Bright, saturated single colors against black backgrounds. Yellow and red are typically most salient.
- **Visual clutter is the primary barrier**: Reduce elements on screen to 3-5 at a time. Add generous spacing (2x normal). Remove decorative elements, gradients, and background images entirely.
- **Movement for attention**: Unlike most accessibility guidance, gentle movement (slow pulsing, not rapid flashing) can help CVI users locate elements. Use sparingly and always with `prefers-reduced-motion` override.
- **Visual field preferences**: Many CVI users have a preferred visual field (often lower-left). Allow configurable placement of primary actions.
- **Visual latency**: CVI users are slow to process visual input — allow extra time for recognition before changing content.
- **Familiar imagery**: CVI users recognize familiar items before novel ones. Use consistent iconography across the application.
- *Basis: Christine Roman-Lantzy's CVI Range assessment (10 characteristics), standard in pediatric vision therapy.*

### Other Vision Needs
- **Photophobia**: Offer low-brightness themes with muted colors
- **Color blindness**: Test with deuteranopia (red-green, ~8% of males) and protanopia simulators. Never use red/green as the only differentiator.

## Alt Text

Four styles for different contexts:

- **Concise** (social media, thumbnails): ~125 characters. Describe the essential content and purpose. "Bar chart showing renewable energy adoption doubling between 2020 and 2025"
- **Detailed** (documentation, educational content): ~300 characters. Describe purpose first, then visual details. "Scatter plot comparing student test scores to study hours. Positive correlation visible — students studying 10+ hours score 20% higher on average. Outliers at low study hours suggest other factors."
- **Functional** (interface elements): Describe what it does, not what it looks like. "Submit form" not "Blue button with arrow icon"
- **Neurodivergent** (social/emotional support): Explicitly describe facial expressions AND their likely meanings ("smiling, suggesting friendliness"), spell out body language, describe social cues and power dynamics, flag potential misunderstandings. Helps autistic users and others who find nonverbal cues difficult to interpret.
  - Photos with people: "Two people shaking hands in an office. Both are smiling, suggesting a positive professional interaction."
  - Group dynamics: "Person at center is speaking while others face them, suggesting they are leading the discussion."
  - Ambiguous expressions: Flag uncertainty — "Person's expression is neutral, which could indicate concentration, disinterest, or tiredness depending on context."
  - Social media: Describe engagement cues — "Comment section showing laughing emoji reactions, indicating the post was received as humorous."
  - *Basis: social communication challenges documented in DSM-5 criteria for ASD; pragmatic language research.*

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

## Reflow (WCAG 1.4.10)

Content must reflow at 320px width (equivalent to 400% zoom of 1280px) without horizontal scrolling. No two-dimensional scrolling except for content that requires spatial layout (data tables, maps, diagrams).

- Don't use fixed-width containers in px — use `max-width: 100%` and `overflow-wrap: break-word`
- Test by setting browser width to 320px and verifying single-column layout

## Content on Hover or Focus (WCAG 1.4.13)

Tooltip, popup, or dropdown content that appears on hover/focus must be:

- **Dismissible**: User can dismiss without moving pointer/focus (typically Escape key)
- **Hoverable**: User can move pointer over the new content without it disappearing
- **Persistent**: Content stays visible until user dismisses, moves focus/pointer, or it's no longer valid

CSS `title` attributes fail all three requirements. Use `aria-describedby` with visible tooltip elements instead. Magnifier users need to pan to tooltips, so they must stay visible when the viewport moves.

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
- [ ] Non-text contrast meets 3:1 for UI components and graphics (1.4.11)
- [ ] Content reflows at 320px width without horizontal scrolling (1.4.10)
- [ ] Text spacing can be overridden without content loss (1.4.12)
- [ ] Hover/focus content is dismissible, hoverable, and persistent (1.4.13)
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
