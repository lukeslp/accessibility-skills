---
name: screen-reader
description: "Screen reader compatibility: semantic HTML, landmarks, headings, ARIA live regions, forms, data tables, dynamic content. WCAG 2.2 AA."
---

Screen reader compatibility patterns for web interfaces. Covers semantic structure, landmarks, heading hierarchy, ARIA live regions, forms, data tables, and dynamic content management for SPAs.

> **Related skills:** `/accessibility:motor` (touch targets, keyboard, switch access), `/accessibility:visual` (contrast, color, alt text), `/accessibility:cognitive` (plain language, reduced motion), `/accessibility:testing` (full WCAG checklist + all audit scripts)

## When to Use This Skill

- Building any web UI with interactive elements
- Adding dynamic content updates (SPAs, real-time data, live feeds)
- Creating forms, data tables, or custom widgets
- Reviewing HTML structure and ARIA usage

## Core Principles

1. **Use semantic HTML first.** `<button>` not `<div onclick>`. `<nav>` not `<div class="nav">`.
2. **ARIA is a last resort.** If native HTML works, remove the ARIA. ARIA done wrong is worse than no ARIA.
3. **Dynamic content must be announced.** Screen reader users can't see visual changes — use live regions.

## Semantic Structure

- Use proper landmarks: `<header>`, `<nav>`, `<main>`, `<aside>`, `<footer>`
- Use `aria-label` to differentiate multiple landmarks of the same type (e.g., "Primary navigation" vs "Footer navigation")
- Heading hierarchy: h1 then h2 then h3 — never skip levels. Every section needs a heading.
- Use `<button>` for actions, `<a>` for navigation — not `<div onclick>` or `<span role="button">`

## Dynamic Content

- **Live regions**: Use `aria-live="polite"` for status updates (results count, save confirmation), `"assertive"` for errors and urgent alerts
- **Route changes in SPAs**: Manage focus — move it to the new page's main heading or content area after navigation
- **Loading states**: Use `aria-busy="true"` on containers being updated, announce completion via live region

## Forms

- Every input needs a visible `<label>` element associated via `for`/`id`, or `aria-label` for icon-only inputs
- Group related fields with `<fieldset>` and `<legend>`
- Error messages: associate with `aria-describedby`, announce with `aria-live`
- Required fields: use `aria-required="true"` and visible indicator (not just an asterisk)

### Input Purpose (WCAG 1.3.5)

Add `autocomplete` attributes to inputs that collect personal data. This lets browsers auto-fill and lets AT present familiar icons:
- `autocomplete="name"`, `"given-name"`, `"family-name"`
- `autocomplete="email"`, `"tel"`, `"street-address"`
- `autocomplete="new-password"`, `"current-password"`, `"bday"`

### Consistent Help (WCAG 3.2.6)

If help mechanisms exist (contact info, chat, FAQ link), they must appear in the same relative order on every page. Screen reader users build mental maps of page structure and depend on positional consistency.

## Data Tables

- Use `<th>` with `scope="col"` or `scope="row"` for header cells
- Add `<caption>` describing the table's purpose
- For complex tables, use `id`/`headers` attributes to associate data cells with their headers

## WCAG 2.2 AA — Robust Checklist

- [ ] HTML validates (no duplicate IDs, proper nesting)
- [ ] ARIA attributes used correctly (roles, states, properties)
- [ ] Custom controls expose name, role, and value to assistive technology
- [ ] Status messages are programmatically determinable

## Included Scripts

| Script | What it checks |
|--------|---------------|
| `heading-outline.py` | Heading hierarchy — skipped levels, missing h1, empty headings |
| `landmark-audit.py` | ARIA landmark structure — missing main, unlabeled duplicates |
| `link-text-audit.py` | Vague link text ("click here"), empty links, image-only links |

```bash
python3 scripts/heading-outline.py index.html
python3 scripts/landmark-audit.py index.html
python3 scripts/link-text-audit.py index.html
```

## Reference Files

- `reference/sr.css` — Screen reader-only utilities (`.sr-only`, `.visually-hidden`, `.sr-only-focusable`)
- `reference/sr-patterns.md` — Landmark structure, screen reader announcements, accessible modal dialog (copy-paste JS/HTML)

## Common Issues and Fixes

| Issue | Fix |
|-------|-----|
| Missing form labels | Associate `<label>` with `for` attribute |
| Div-based buttons | Use `<button>` element instead |
| ARIA misuse | Remove ARIA if native HTML works; validate roles |
| Inaccessible modals | Use native `<dialog>` with `showModal()` — handles focus automatically. For custom modals: trap focus, Escape to close, restore focus on dismiss |
