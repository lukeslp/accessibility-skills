# Screen Reader Patterns

Copy-paste ready implementations for landmarks, live regions, and accessible modals.

## Landmark Structure

Screen readers navigate by landmarks. Use semantic HTML5 elements with `aria-label` to differentiate multiples.

```html
<header role="banner">
  <nav role="navigation" aria-label="Primary navigation">...</nav>
</header>

<main role="main" id="main-content" tabindex="-1">
  <h1>Page Title</h1>
  <section>
    <h2>Section Heading</h2>
    <!-- content -->
  </section>
  <nav aria-label="Section navigation">...</nav>
</main>

<aside role="complementary" aria-label="Related resources">...</aside>

<footer role="contentinfo">
  <nav aria-label="Footer navigation">...</nav>
</footer>
```

Rules:
- One `<main>` per page
- One `<header role="banner">` per page (unless inside `<article>`)
- Use `aria-label` when you have multiple `<nav>` elements
- `tabindex="-1"` on skip link targets so they can receive focus

---

## Screen Reader Announcements

Announce dynamic content changes to screen readers via ARIA live regions.

```js
/**
 * Announce a message to screen readers.
 * @param {string} message - What to announce
 * @param {'polite'|'assertive'} priority - polite waits for pause, assertive interrupts
 *
 * When to use each:
 *   polite: Form saved, search results count, theme changed, item added to cart
 *   assertive: Validation errors, session timeout warnings, connection lost
 *
 * Important: Live regions must exist in the DOM BEFORE content is injected.
 * This function handles that by creating the element first, then setting text
 * after a microtask.
 */
function announce(message, priority = 'polite') {
  const el = document.createElement('div');
  el.setAttribute('role', 'status');
  el.setAttribute('aria-live', priority);
  el.setAttribute('aria-atomic', 'true');
  el.className = 'sr-only';
  document.body.appendChild(el);
  // Delay setting text so the live region is registered before populated
  requestAnimationFrame(() => {
    el.textContent = message;
  });
  setTimeout(() => el.remove(), 1000);
}

// Common patterns:
announce('Form submitted successfully');
announce('Error: email is required', 'assertive');
announce(`${count} results found for "${query}"`);
announce('Page loaded: Settings');
announce('Theme changed to High Contrast');
announce(`Showing ${visible} of ${total} items`);
```

For frequent updates (chat, live data), use a persistent live region instead of creating/destroying elements:

```js
// Create once
const liveRegion = document.createElement('div');
liveRegion.id = 'live-updates';
liveRegion.setAttribute('role', 'status');
liveRegion.setAttribute('aria-live', 'polite');
liveRegion.className = 'sr-only';
document.body.appendChild(liveRegion);

// Update as needed
liveRegion.textContent = `New message from ${username}`;
```

---

## Accessible Modal Dialog

### Preferred: Native `<dialog>` Element

The native `<dialog>` element with `showModal()` is the best approach for modern browsers. It handles focus trapping, Escape key, backdrop, and `aria-modal` automatically.

```html
<dialog id="modal" aria-labelledby="modal-title">
  <h2 id="modal-title">Dialog Title</h2>
  <div>
    <!-- modal content -->
  </div>
  <button id="modal-close" aria-label="Close dialog">Close</button>
</dialog>
```

```js
const dialog = document.getElementById('modal');
const trigger = document.querySelector('[data-opens="modal"]');

// Open
trigger.addEventListener('click', () => {
  dialog.showModal(); // Focus traps automatically, adds backdrop
});

// Close via button
dialog.querySelector('#modal-close').addEventListener('click', () => {
  dialog.close(); // Focus returns to trigger automatically
});

// Close via backdrop click
dialog.addEventListener('click', (e) => {
  if (e.target === dialog) dialog.close();
});
```

```css
/* Style the backdrop */
dialog::backdrop {
  background: rgba(0, 0, 0, 0.5);
}
```

### Fallback: Custom Modal with Focus Trap

For browsers that don't support `<dialog>`, or when you need custom behavior.

```html
<div id="modal" role="dialog" aria-modal="true" aria-labelledby="modal-title" hidden>
  <h2 id="modal-title">Dialog Title</h2>
  <div>
    <!-- modal content -->
  </div>
  <button id="modal-close" aria-label="Close dialog">Close</button>
</div>
```

```js
function openModal(modalEl, triggerEl) {
  modalEl.hidden = false;
  modalEl.setAttribute('aria-hidden', 'false');

  // Mark background content as inert (preferred over aria-hidden on siblings)
  document.querySelector('main')?.setAttribute('inert', '');

  const trap = new FocusTrap(modalEl);
  trap.activate();

  const handleEscape = (e) => {
    if (e.key === 'Escape') closeModal(modalEl, triggerEl, trap, handleEscape);
  };
  document.addEventListener('keydown', handleEscape);

  modalEl._trap = trap;
  modalEl._escapeHandler = handleEscape;

  announce('Dialog opened: ' + modalEl.querySelector('[id$="-title"]')?.textContent);
}

function closeModal(modalEl, triggerEl, trap, escapeHandler) {
  modalEl.hidden = true;
  modalEl.setAttribute('aria-hidden', 'true');

  document.querySelector('main')?.removeAttribute('inert');

  trap = trap || modalEl._trap;
  escapeHandler = escapeHandler || modalEl._escapeHandler;

  if (trap) trap.deactivate();
  if (escapeHandler) document.removeEventListener('keydown', escapeHandler);
  if (triggerEl) triggerEl.focus();

  announce('Dialog closed');
}
```
