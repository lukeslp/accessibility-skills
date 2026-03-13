# Accessible Theme Switcher

Toggle between themes with screen reader announcements, localStorage persistence, and OS preference detection.

```js
function initThemeSwitcher(storageKey = 'theme', defaultTheme = 'light') {
  const saved = localStorage.getItem(storageKey) || defaultTheme;
  applyTheme(saved);

  document.querySelectorAll('[data-theme-toggle]').forEach(btn => {
    const theme = btn.dataset.themeToggle;
    btn.setAttribute('aria-pressed', theme === saved ? 'true' : 'false');

    btn.addEventListener('click', () => {
      applyTheme(theme);
      localStorage.setItem(storageKey, theme);

      // Update button states
      document.querySelectorAll('[data-theme-toggle]').forEach(b => {
        b.setAttribute('aria-pressed', b.dataset.themeToggle === theme ? 'true' : 'false');
      });

      announce(`Theme changed to ${btn.textContent.trim()}`);
    });
  });
}

function applyTheme(theme) {
  document.documentElement.setAttribute('data-theme', theme);
}
```

## Theme Presets for Accessibility

```css
/* High contrast dark (default accessible) */
[data-theme="dark"] {
  --bg: #000000;
  --text: #ffffff;
  --accent: #58a6ff;
  --focus-ring: #ffff00;
}

/* CVI-optimized (Cortical Visual Impairment) */
[data-theme="cvi"] {
  --bg: #000000;
  --text: #ffff00;
  --accent: #ffff00;
  --focus-ring: #00ffff;
}

/* Low-light / photophobia friendly */
[data-theme="low-light"] {
  --bg: #0d1117;
  --text: #8b949e;
  --accent: #4a6fa5;
  --focus-ring: #6a9bcc;
}

/* Deuteranopia-friendly (red-green color blindness) */
[data-theme="deuteranopia"] {
  --bg: #1a1a1a;
  --text: #e0e0e0;
  --accent: #ff8c00; /* orange instead of green */
  --focus-ring: #ffff00;
}
```
