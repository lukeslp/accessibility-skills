# Accessibility Skill

When working on web UI code in this project, follow the accessibility guidelines in `SKILL.md`.

## Key Rules

1. **Every interactive element** needs keyboard access — no mouse-only interactions
2. **Every image** needs alt text (or `alt=""` for decorative images)
3. **Focus indicators** must be visible — never `outline: none` without a replacement
4. **Touch targets** minimum 24x24px (AA), prefer 44x44px (AAA)
5. **Color is never the only indicator** — always pair with text, icons, or patterns
6. **Animations** respect `prefers-reduced-motion` — reduce or disable motion when set
7. **Dynamic content** uses ARIA live regions to announce changes to screen readers

## Reference Files

- `SKILL.md` — Full accessibility guidance organized by disability domain (motor, cognitive, visual, communication) + WCAG 2.2 checklist
- `reference/accessibility.css` — Production CSS for focus indicators, screen-reader-only content, touch targets, reduced motion, forced colors mode
- `reference/patterns.md` — Copy-paste JavaScript/HTML patterns for focus traps, roving tabindex, native dialogs, screen reader announcements, skip links

## Audit Scripts

Run these against HTML files to check for common issues. All use Python stdlib only.

```bash
python3 scripts/alt-text-audit.py index.html
python3 scripts/heading-outline.py index.html
python3 scripts/landmark-audit.py index.html
python3 scripts/focus-order-check.py index.html
python3 scripts/target-size-check.py index.html
python3 scripts/contrast-checker.py "#333333" "#f5f5f5"
```

All scripts support `--format json` for CI integration.
