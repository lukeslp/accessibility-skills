---
name: cognitive
description: "Cognitive and communication accessibility: plain language, dyslexia-friendly text, reduced motion, error prevention, memory support, captions, AAC integration. WCAG 2.2 AA."
---

Cognitive and communication accessibility patterns for web interfaces. Covers consistent navigation, plain language, dyslexia-friendly typography, reduced motion, error prevention, memory/attention support, captions, and AAC integration.

> **Related skills:** `/accessibility:motor` (touch targets, keyboard, switch access), `/accessibility:visual` (contrast, color, alt text), `/accessibility:screen-reader` (semantic structure, ARIA), `/accessibility:testing` (full WCAG checklist + all audit scripts)

## When to Use This Skill

- Writing user-facing copy, labels, or error messages
- Designing multi-step flows or complex forms
- Adding animations, transitions, or auto-playing content
- Building communication tools or interfaces with audio/video

## Core Principles

1. **Plain language first.** Short sentences, common words, avoid jargon — explain technical terms when needed.
2. **Don't surprise users.** Buttons should do what they say. Links should go where they describe.
3. **Don't require memory.** Show context inline. Avoid multi-step processes that depend on recalling earlier choices.
4. **Respect motion preferences.** Some users experience motion sickness from animations.

## Cognitive Accessibility

- **Consistent navigation**: Same layout on every page, predictable behavior, visible breadcrumbs
- **Plain language**: Short sentences, common words, avoid jargon — explain technical terms when needed
- **Dyslexia-friendly options**: Offer increased letter-spacing (0.12em+), word-spacing (0.16em+), relaxed line height (1.5+), and medium font weight. See `reference/cognitive.css` for a `.dyslexia-friendly` class.
- **Dyslexia font stack**: `Atkinson Hyperlegible, Lexend, OpenDyslexic, Aptos, Calibri, sans-serif`. Atkinson Hyperlegible (Braille Institute — designed for low vision, distinct letterforms), Lexend (research shows ~20% reading fluency improvement over Times New Roman), OpenDyslexic (weighted letterforms to reduce rotation), Aptos (Microsoft's accessibility-focused default). Offer as a user preference, not a forced default.
- **Reduced motion**: Respect `prefers-reduced-motion` — disable all animations and transitions. See `reference/cognitive.css` for the media query pattern. Provide on-page controls too — not all users know about OS-level settings.
- **Visible focus**: Bold, high-contrast (3:1 minimum) focus outlines so users always know where they are in the page
- **Error prevention**: Confirm destructive actions, validate inline before submission, provide clear recovery paths with specific guidance
- **Chunking**: Break content into small, digestible sections with descriptive headings — don't present walls of text
- **Predictability**: Buttons should do what they say. Links should go where they describe. Don't surprise users.
- **Memory support**: Don't require users to remember information from a previous step. Show context inline. Avoid multi-step processes that depend on recalling earlier choices.
- **Attention support**: Minimize distractions. No auto-playing media, no flashing content, no unexpected pop-ups. Allow users to pause or suppress non-critical notifications.

## Communication and Speech

- **No voice-only interfaces**: Always provide text or touch alternatives to voice input
- **Captions and transcripts**: All audio and video content needs synchronized captions. Provide full transcripts for audio-only content.
- **AAC integration**: If building communication tools, follow the Modified Fitzgerald Key color conventions (see `/accessibility:motor` for the full table) and support standard symbol systems (PCS by Tobii Dynavox, SymbolStix by n2y, Blissymbolics by BCI — 6,000+ symbols with Unicode code points)
- **Text-to-speech considerations**: Keep text content well-structured so TTS reads it in logical order. Avoid layout tables and CSS order tricks that break reading flow.

## WCAG 2.2 AA — Understandable Checklist

- [ ] `<html lang="en">` (or appropriate language) is set
- [ ] Navigation is consistent across pages
- [ ] Form inputs have clear labels and instructions
- [ ] Error messages are specific and suggest fixes
- [ ] *2.2* Redundant entry: don't require re-entering information already provided (3.3.7)

## Reference Files

- `reference/cognitive.css` — Reduced motion media query, dyslexia-friendly text styles

## Common Issues and Fixes

| Issue | Fix |
|-------|-----|
| Auto-playing media | Add pause/stop controls, no autoplay |
| Hover-only content | Make content keyboard/touch accessible |
| Inconsistent layout | Keep navigation and key actions in fixed positions across all pages |
