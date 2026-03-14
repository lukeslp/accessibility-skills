---
name: motor
description: "Motor accessibility patterns from AAC development: touch targets, keyboard navigation, switch access, eye gaze, fatigue detection, pointer gestures. WCAG 2.2 AA."
---

Motor accessibility patterns for web interfaces, drawn from building AAC (Augmentative and Alternative Communication) tools for non-verbal individuals. Covers keyboard-only navigation, switch access, eye gaze, sip-and-puff, fatigue detection, and WCAG 2.2 motor-related criteria.

> **Related skills:** `/accessibility:visual` (contrast, color), `/accessibility:cognitive` (plain language, reduced motion), `/accessibility:screen-reader` (semantic structure, ARIA), `/accessibility:testing` (full WCAG checklist + all audit scripts)

## When to Use This Skill

- Building or reviewing interactive components (modals, forms, menus, custom widgets)
- Adding drag-and-drop, gestures, or timed interactions
- Any project where users may have motor impairments, tremor, or use alternative input devices

## Core Principles

1. **If your UI works fully with a keyboard, it works with most alternative input devices.** Keyboard accessibility is the foundation of motor accessibility.
2. **Never rely on mouse hover, drag, or right-click as the only way to do something.**
3. **Never require timed responses.** Always allow users to extend or disable time limits.
4. **Debounce for tremor.** Distinguish intentional clicks from accidental touches.

## Touch Targets

- **Minimum 44x44px** for all interactive elements (WCAG 2.5.5)
- **48x48px on mobile** — fingers are less precise than cursors
- Add padding around targets, not just visual size — the tap area matters
- Space interactive elements at least 8px apart to prevent accidental activation

## Keyboard-Only Navigation

- Every interactive element must be **reachable and operable via keyboard alone**
- Tab moves between elements, Enter/Space activates, Escape dismisses
- Arrow keys navigate within composite widgets (tabs, menus, grids)
- Never require mouse hover, drag, or right-click as the only way to do something

## Switch Access

Switch users navigate by scanning — the interface highlights elements one at a time, and the user activates a switch to select.

- **One-switch mode**: Auto-scan advances through elements; single switch = select
- **Two-switch mode**: One switch = next, other switch = select
- **Design for scanning groups**: Organize elements in logical clusters (navigation, content, actions) so scanning doesn't require stepping through every element individually
- **Row-column scanning**: For grids, scan by row first (highlight entire row), then scan individual cells within the selected row. Reduces selections from N to √N.
- **Group-item scanning**: Organize UI into 3-5 scanning groups. Switch first selects a group, then scans items within it. Standard approach in Tobii Dynavox Communicator, Grid 3, and TD Snap.
- **Directed scanning**: User controls direction (next/previous) rather than waiting for auto-advance — faster for experienced users but requires two switches.
- **Predictable layouts**: Grid-based layouts work best — random/overlapping positioning breaks scanning
- **Linear order matters**: DOM order must match visual order. CSS layout tricks that reorder visually but not in the DOM confuse switch users.

## Alternative Input Devices

Eye gaze trackers, head tracking, sip-and-puff devices, and joystick controllers all typically map to keyboard events.

**Eye gaze** (infrared tracking of iris position):
- Selection via dwell: user looks at an element for a configurable duration (300–2000ms, start at 800ms) to activate it
- Requires generous hit areas — gaze is less precise than a mouse cursor
- Elements should not trigger on hover alone — dwell-click users will accidentally activate hover menus
- Screen can be divided into gaze zones for scroll control (look at top edge = scroll up)
- Calibration typically uses 9 points, collecting samples at each to build a screen coordinate mapping

**Head tracking** (camera tracks reflective dots or facial features):
- Maps head movement to mouse cursor position with dwell-click selection
- Similar to eye gaze but generally less precise — needs even larger targets
- Cursor jitter is common — apply smoothing (Kalman-like filtering) to gaze/head predictions

**BCI (Brain-Computer Interface)**:
- P300 speller: a grid of characters flashes rows/columns; the user attends to their target letter, and the EEG detects the P300 evoked potential (~300ms post-stimulus) to identify the selection. Requires large, high-contrast grid cells with consistent positions.
- SSVEP (Steady-State Visual Evoked Potentials): elements flicker at distinct frequencies (e.g., 7Hz, 10Hz); the user gazes at their target and the BCI detects the corresponding frequency in occipital EEG. Stay under 3Hz for seizure safety (WCAG 2.3.1) if adding flicker to your own UI.
- Motor imagery: user imagines left/right hand movement to navigate binary choices — maps to keyboard events like sip-and-puff. Design menus as binary trees when supporting this modality.
- BCI is slow (~5-15 characters/minute for P300). Minimize required selections, support word prediction, and never use BCI as the sole input for time-sensitive actions.
- All BCI paradigms ultimately map to keyboard or click events through driver software. Full keyboard accessibility remains the foundation.
- *Basis: Farwell & Donchin 1988 paradigm, commercialized by g.tec (intendiX) and Tobii Dynavox.*

**Sip-and-puff** (air pressure through a tube):
- Sip = one action (e.g., advance/next), puff = another (e.g., select)
- Maps to keyboard events — software interprets pressure as key presses
- Requires full keyboard accessibility — no multi-key shortcuts, no mouse-only interactions

**Switch scanning timing** (configurable per user):
- Auto-scan interval: 500–3000ms (start at 1500ms, adjust based on user speed)
- Selection dwell: 200–1000ms (how long the switch must be held to confirm)
- Faster users can reduce intervals; users with slower motor control need longer intervals
- Always allow users to configure these values — there is no single correct timing

## Drag-and-Drop

- Always provide a keyboard alternative: arrow keys + Enter, or a menu-based "move to" action
- Sortable lists need "move up" / "move down" buttons as keyboard alternatives
- Never make drag-and-drop the only way to reorder or organize content

## Tremor and Spasticity Handling

- **Debounce**: 150-300ms delay before accepting a second tap (configurable per user)
- **Guard time**: Ignore accidental activations within N ms of the last intentional action
- **Sticky keys pattern**: For keyboard shortcuts requiring modifier keys (Ctrl+S), allow sequential pressing rather than simultaneous — matches iOS AssistiveTouch, Windows Sticky Keys, macOS Accessibility Keyboard
- **Spasticity vs. fatigue distinction**: Spasticity produces sudden, involuntary movements (high-velocity errors) while fatigue produces gradual degradation (increasing response time). Track pointer velocity to distinguish — high-velocity off-target clicks suggest spasticity (increase debounce), steadily rising response times suggest fatigue (enlarge targets, reduce options).

## Timing and Precision

- **Never require timed responses.** Always allow users to extend or disable time limits (WCAG 2.2.1)
- **Debounce click/tap events** to handle tremor — distinguish intentional clicks from accidental touches
- **Don't trigger actions on hover** — dwell-click users will accidentally activate hover-triggered menus
- Provide generous click/tap areas and avoid requiring precise cursor positioning

## Fatigue Detection

Motor fatigue degrades accuracy over time. Adaptive interfaces can detect and respond to fatigue in real time:

- **Metrics to monitor**: Response time (primary signal), error rate (missed targets, repeated taps), pause frequency (longer pauses between actions)
- **Weighted formula**: Response time (50%), error rate (30%), pause frequency (20%)
- **Adaptive responses**: As metrics degrade, enlarge touch targets, slow scanning intervals, reduce the number of options shown, increase spacing between elements
- **Implementation**: Track a rolling window of the last 10-20 interactions. Compare against the user's baseline from their first few minutes of use.
- **Baseline calibration**: Use first 2-3 minutes of interaction to establish personal baseline metrics
- **Recovery detection**: If metrics return to baseline after a break, restore original UI density
- **Graduated response**: Fatigue onset is gradual — use a sliding scale of adaptations (first: increase spacing, then: enlarge targets, then: reduce visible options, finally: suggest a break)
- *Basis: Koester & Levine (2000) research on motor fatigue in AAC; Fitts's Law — movement time = a + b * log2(distance/width + 1). As fatigue increases, both constants rise, so reduce distance (cluster elements toward center) and increase width (enlarge targets).*

## Pointer Gestures and Cancellation

WCAG 2.1 requires alternatives for complex pointer interactions:

- **2.5.1 Pointer Gestures (Level A)**: Any functionality using multipoint (pinch) or path-based (swipe) gestures must also work with single-point activation (tap/click). People with motor disabilities may only be able to perform single-tap gestures.
- **2.5.2 Pointer Cancellation (Level A)**: Don't trigger actions on the down-event (mousedown/touchstart). Use up-events (mouseup/touchend/click) so users can abort by moving away. This is critical for tremor — users who accidentally tap can move their finger away to cancel.
- **2.5.4 Motion Actuation (Level A)**: Don't require shaking, tilting, or device gestures. If you support them, provide button alternatives and let users disable motion triggers.

## AAC Color Coding (Modified Fitzgerald Key)

Communication boards follow the Modified Fitzgerald Key — the dominant color-coding standard in AAC:

| Color | Word Type | Example |
|-------|-----------|---------|
| Green | Verbs (actions) | go, want, eat |
| Orange | Nouns (things) | ball, cup, dog |
| Yellow | Pronouns | I, you, he, she |
| Blue | Adjectives (descriptors) | big, hot, happy |
| Brown | Adverbs (manner) | quickly, here |
| Purple | Questions | who, what, where |
| Pink | Prepositions, social words | in, on, hello, please |
| Red | Important, negation, emergency | stop, no, help, more |
| White/Gray | Determiners, conjunctions | the, a, and, or |

Respect these conventions in any communication-focused interface. Users and clinicians rely on color consistency across tools.

## Spatial Consistency for Muscle Memory

Fixed positions for recurring actions build motor memory and eventually automaticity:

- **Communication boards**: Core vocabulary (WHO/WHAT/WHERE/WHEN) should always occupy the same spatial positions across all pages/screens
- **Navigation elements**: Search, home, back, and primary actions should never move between pages — users with motor impairments develop muscle memory for frequently-used controls
- **Grid layouts**: Keep the same grid dimensions across pages. Changing grid size forces motor re-planning, which is cognitively and physically expensive for switch and gaze users.
- **General principle**: Consistency between pages leads to motor-plan development. The more consistent the layout, the less motor and cognitive effort required over time.

## WCAG 2.2 AA — Operable Checklist

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

## Included Scripts

| Script | What it checks |
|--------|---------------|
| `focus-order-check.py` | Positive tabindex, non-focusable interactive elements, aria-hidden conflicts |
| `target-size-check.py` | Undersized touch targets (WCAG 2.5.8: 24px AA, 44px AAA) |
| `timing-audit.py` | setTimeout, autoplay, animations without reduced-motion support |

```bash
python3 scripts/focus-order-check.py --show-all index.html
python3 scripts/target-size-check.py --threshold 44 index.html
python3 scripts/timing-audit.py index.html app.js styles.css
```

## Reference Files

- `reference/motor.css` — Focus indicators, skip links, touch targets, mobile accessibility
- `reference/motor-patterns.md` — Focus trap, roving tabindex, skip links (copy-paste JS/HTML)

## Common Issues and Fixes

| Issue | Fix |
|-------|-----|
| No focus indicator | Add `:focus-visible` outline (3px+) |
| Hover-only content | Make content keyboard/touch accessible |
| Missing skip link | Add skip link as first focusable element |
| Inaccessible modals | Use native `<dialog>` with `showModal()` — handles focus automatically. For custom modals: trap focus, Escape to close, restore focus on dismiss |
| Small touch targets | Minimum 24x24px (WCAG 2.2 AA), 44x44px preferred, 48px on mobile |
| Actions on pointer down | Use `click` events (up-event), not `mousedown`/`touchstart` — allows cancellation by moving away |
| Hover-only menus | Open menus on click/Enter, not hover. Hover menus fire accidentally with dwell-click |
| Inconsistent layout | Keep navigation and key actions in fixed positions across all pages — muscle memory matters |
