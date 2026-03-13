# Motor Accessibility Patterns

Copy-paste ready implementations for keyboard navigation, focus management, and switch access.

## Skip Links

The first focusable element on every page. Lets keyboard and switch users bypass repeated navigation.

```html
<!-- Place immediately after <body> -->
<a href="#main-content" class="skip-link">Skip to main content</a>

<header>
  <nav aria-label="Primary navigation">
    <!-- navigation links -->
  </nav>
</header>

<main id="main-content" tabindex="-1">
  <!-- page content -->
</main>
```

Enhanced focus behavior (ensures all browsers move focus correctly):

```js
document.querySelectorAll('.skip-link').forEach(link => {
  link.addEventListener('click', function(e) {
    const targetId = this.getAttribute('href').substring(1);
    const target = document.getElementById(targetId);
    if (target) {
      e.preventDefault();
      if (!target.hasAttribute('tabindex')) {
        target.setAttribute('tabindex', '-1');
      }
      target.focus();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});
```

---

## Focus Trap

Trap focus inside modal dialogs. Tab cycles through the modal's focusable elements. Escape closes. Focus restores to the trigger element on close.

```js
class FocusTrap {
  constructor(element) {
    this.element = element;
    this.focusableSelector =
      'a[href], button:not([disabled]), textarea:not([disabled]), ' +
      'input:not([disabled]), select:not([disabled]), [tabindex]:not([tabindex="-1"])';
    this.previousFocus = null;
  }

  activate() {
    this.previousFocus = document.activeElement;
    const focusable = Array.from(
      this.element.querySelectorAll(this.focusableSelector)
    );
    if (focusable.length > 0) {
      focusable[0].focus();
    }
    this.element.addEventListener('keydown', this._handleKeydown);
  }

  deactivate() {
    this.element.removeEventListener('keydown', this._handleKeydown);
    if (this.previousFocus && this.previousFocus.focus) {
      this.previousFocus.focus();
    }
  }

  _handleKeydown = (e) => {
    if (e.key !== 'Tab') return;

    const focusable = Array.from(
      this.element.querySelectorAll(this.focusableSelector)
    );
    const first = focusable[0];
    const last = focusable[focusable.length - 1];

    if (e.shiftKey && document.activeElement === first) {
      e.preventDefault();
      last.focus();
    } else if (!e.shiftKey && document.activeElement === last) {
      e.preventDefault();
      first.focus();
    }
  };
}

// Usage:
// const trap = new FocusTrap(document.getElementById('modal'));
// trap.activate();   // on open
// trap.deactivate();  // on close
```

---

## Roving Tabindex

For composite widgets like tab lists, toolbars, and menus. One element is tabbable (tabindex="0"), the rest are tabindex="-1". Arrow keys move focus within the group.

```js
class RovingTabindex {
  constructor(container, itemSelector, orientation = 'horizontal') {
    this.container = container;
    this.items = Array.from(container.querySelectorAll(itemSelector));
    this.orientation = orientation;
    this.currentIndex = 0;

    // Set initial state
    this.items.forEach((item, i) => {
      item.setAttribute('tabindex', i === 0 ? '0' : '-1');
    });

    container.addEventListener('keydown', (e) => this._handleKeydown(e));
  }

  _handleKeydown(e) {
    const prev = this.orientation === 'horizontal' ? 'ArrowLeft' : 'ArrowUp';
    const next = this.orientation === 'horizontal' ? 'ArrowRight' : 'ArrowDown';
    let newIndex = this.currentIndex;

    switch (e.key) {
      case next:
        e.preventDefault();
        newIndex = (this.currentIndex + 1) % this.items.length;
        break;
      case prev:
        e.preventDefault();
        newIndex = (this.currentIndex - 1 + this.items.length) % this.items.length;
        break;
      case 'Home':
        e.preventDefault();
        newIndex = 0;
        break;
      case 'End':
        e.preventDefault();
        newIndex = this.items.length - 1;
        break;
      default:
        return;
    }

    this.items[this.currentIndex].setAttribute('tabindex', '-1');
    this.items[newIndex].setAttribute('tabindex', '0');
    this.items[newIndex].focus();
    this.currentIndex = newIndex;
  }
}

// Usage:
// new RovingTabindex(
//   document.querySelector('[role="tablist"]'),
//   '[role="tab"]',
//   'horizontal'
// );
```
