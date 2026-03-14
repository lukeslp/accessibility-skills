---
name: testing
description: "Accessibility testing: full WCAG 2.2 AA checklist, manual testing methodology, 10 Python audit scripts (stdlib-only), common issues reference table."
---

Complete accessibility testing toolkit. Includes the full WCAG 2.2 AA checklist, manual testing methodology, all 10 Python audit scripts, and a common issues reference table.

> **Related skills:** `/accessibility:motor` (motor patterns), `/accessibility:visual` (contrast, alt text), `/accessibility:cognitive` (plain language, reduced motion), `/accessibility:screen-reader` (semantic structure, ARIA)

## When to Use This Skill

- Auditing an existing interface for accessibility compliance
- Setting up CI pipelines for accessibility checks
- Performing manual accessibility testing
- Reviewing pull requests for accessibility issues

## WCAG 2.2 AA Checklist

Use this as a quick audit checklist when reviewing any interface. Includes WCAG 2.2 criteria (marked with *2.2*).

### Perceivable
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

### Operable
- [ ] All functionality available via keyboard
- [ ] No keyboard traps — focus can always move away
- [ ] Skip navigation link present
- [ ] Page titles are descriptive
- [ ] Focus indicator visible on every interactive element
- [ ] No time limits (or user can extend)
- [ ] No content flashing more than 3 times per second
- [ ] Multipoint/path-based gestures have single-point alternatives (2.5.1)
- [ ] Down-events don't trigger actions — use up-events for pointer cancellation (2.5.2)
- [ ] *2.2* Focus is not entirely obscured by sticky headers, banners, or overlays (2.4.11)
- [ ] *2.2* Interactive targets are at least 24x24px with adequate spacing (2.5.8)
- [ ] *2.2* Dragging operations have single-pointer alternatives (2.5.7)
- [ ] *2.2* Help mechanisms are consistent across pages (3.2.6)
- [ ] At least two ways to locate a page: navigation, search, sitemap, TOC, or links (2.4.5)

### Understandable
- [ ] `<html lang="en">` (or appropriate language) is set
- [ ] Navigation is consistent across pages
- [ ] Form inputs have clear labels and instructions
- [ ] Inputs for personal data have `autocomplete` attributes (1.3.5)
- [ ] Error messages are specific and suggest fixes
- [ ] *2.2* Redundant entry: don't require re-entering information already provided (3.3.7)

### Robust
- [ ] HTML validates (no duplicate IDs, proper nesting)
- [ ] ARIA attributes used correctly (roles, states, properties)
- [ ] Custom controls expose name, role, and value to assistive technology
- [ ] Status messages are programmatically determinable

## Testing Methodology

Automated tools catch about 30% of accessibility issues. Manual testing is essential.

### Automated (Run First)
```bash
# Lighthouse (built into Chrome DevTools)
npx lighthouse <url> --only-categories=accessibility

# axe-core (more thorough)
npx @axe-core/cli <url>

# pa11y (CI-friendly)
npx pa11y <url>
```

### Included Scripts

This skill includes 14 standalone Python scripts (stdlib only — no pip install needed) for targeted audits. All accept HTML files as arguments and support `--format json` for CI integration.

| Script | Domain | What it checks |
|--------|--------|---------------|
| `contrast-checker.py` | Visual | WCAG contrast ratio between two hex colors |
| `cvi-contrast-check.py` | CVI / Low vision | CVI-safe contrast (10:1+), photophobia, deuteranopia presets |
| `alt-text-audit.py` | Visual / SR | Missing, empty, or suspicious alt text on images |
| `heading-outline.py` | Cognitive / SR | Heading hierarchy — skipped levels, missing h1, empty headings |
| `landmark-audit.py` | SR | ARIA landmark structure — missing main, unlabeled duplicates |
| `link-text-audit.py` | SR / Cognitive | Vague link text ("click here"), empty links, image-only links |
| `focus-order-check.py` | Motor / Keyboard | Positive tabindex, non-focusable interactive elements, aria-hidden conflicts |
| `target-size-check.py` | Motor | Undersized touch targets (WCAG 2.5.8: 24px AA, 44px AAA) |
| `color-only-check.py` | Color blindness | Patterns where color is the sole information carrier |
| `timing-audit.py` | Motor / Cognitive | setTimeout, autoplay, animations without reduced-motion support |
| `form-label-audit.py` | SR / Cognitive | Missing form labels or accessible names (aria-label) |
| `language-audit.py` | SR | Presence and validity of lang attribute on <html> element |
| `duplicate-id-check.py` | SR / Robustness | Duplicate IDs that break ARIA associations |
| `table-accessibility-audit.py` | SR | Table headers (<th>), scope attributes, and captions |

```bash
# Run individual checks
python3 scripts/contrast-checker.py "#333333" "#f5f5f5"
python3 scripts/cvi-contrast-check.py --preset cvi
python3 scripts/alt-text-audit.py index.html
python3 scripts/heading-outline.py index.html
python3 scripts/landmark-audit.py index.html
python3 scripts/link-text-audit.py index.html
python3 scripts/focus-order-check.py --show-all index.html
python3 scripts/target-size-check.py --threshold 44 index.html
python3 scripts/color-only-check.py index.html
python3 scripts/timing-audit.py index.html app.js styles.css

# Run all HTML audits at once
for script in scripts/*-audit.py scripts/*-check.py; do
  python3 "$script" index.html
done

# JSON output for CI pipelines
python3 scripts/alt-text-audit.py --format json index.html | jq '.issues'
```

### Manual Testing Checklist

1. **Keyboard**: Tab through the entire page. Can you reach and operate every interactive element? Is focus order logical? Is the focus indicator always visible?
2. **Screen reader**: Test with NVDA (Windows), VoiceOver (Mac/iOS), or TalkBack (Android). Are all elements announced correctly? Do dynamic updates get announced?
3. **Zoom**: Set browser zoom to 200%. Does anything overflow, overlap, or become inaccessible?
4. **Motion**: Enable `prefers-reduced-motion` in your OS or browser dev tools. Do all animations stop?
5. **Color**: Use a color blindness simulator (Chrome DevTools > Rendering > Emulate vision deficiency). Is all information still conveyed?
6. **Switch simulation**: Tab through the page one element at a time. Does the order make sense for someone who can only go forward? Are elements grouped logically?
7. **Forced colors**: Enable Windows High Contrast mode or emulate it (Edge DevTools > Rendering > Emulate forced-colors: active). Are borders, outlines, and focus indicators still visible?
8. **Target size**: Measure interactive elements — are they at least 24x24px (WCAG 2.2 AA) or 44x44px (AAA)?
9. **Cognitive walkthrough**: Can a first-time user complete the primary task without documentation? Are error states clear and recoverable?

## Common Issues and Fixes

| Issue | Who It Affects | Fix |
|-------|---------------|-----|
| Missing alt text | Screen reader users | Add descriptive `alt` attribute |
| Low contrast text | Low vision, aging eyes | Increase to 4.5:1 ratio |
| No focus indicator | Keyboard/switch users | Add `:focus-visible` outline (3px+) |
| Missing form labels | Screen reader users | Associate `<label>` with `for` attribute |
| Div-based buttons | All AT users | Use `<button>` element instead |
| Hover-only content | Motor impaired, touch users | Make content keyboard/touch accessible |
| Auto-playing media | Cognitive, screen reader | Add pause/stop controls, no autoplay |
| Missing skip link | Keyboard/switch users | Add skip link as first focusable element |
| ARIA misuse | Screen reader users | Remove ARIA if native HTML works; validate roles |
| Inaccessible modals | Keyboard/switch users | Use native `<dialog>` with `showModal()` — handles focus automatically. For custom modals: trap focus, Escape to close, restore focus on dismiss |
| Small touch targets | Motor impaired, tremor | Minimum 24x24px (WCAG 2.2 AA), 44x44px preferred, 48px on mobile |
| Actions on pointer down | Motor impaired, tremor | Use `click` events (up-event), not `mousedown`/`touchstart` — allows cancellation by moving away |
| Hover-only menus | Eye gaze, switch users | Open menus on click/Enter, not hover. Hover menus fire accidentally with dwell-click |
| Inconsistent layout | Motor impaired, cognitive | Keep navigation and key actions in fixed positions across all pages — muscle memory matters |
