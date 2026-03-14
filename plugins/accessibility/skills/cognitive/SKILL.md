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

## AAC Vocabulary Organization

When building communication interfaces or tools that interact with AAC users:

- **Core vocabulary**: ~200-400 high-frequency words cover ~80% of daily communication (I, want, go, more, stop, help). These should always be visible/accessible without navigation.
- **Fringe vocabulary**: Topic-specific words (medical terms, school subjects, hobbies). Organized in category pages, accessed from core page.
- **Motor planning preservation**: Same word = same motor sequence to reach it, always. Changing word positions destroys months of learned motor plans.
- **Progressive vocabulary**: Start with fewer items per page, add more as user demonstrates proficiency.
- **Message window**: Always show the composed message and allow editing before sending. AAC users construct messages word by word.
- **Rate enhancement**: Support word prediction and abbreviation expansion. "gm" expanding to "good morning" reduces selections by 10x.
- *Basis: core vocabulary research by Banajee, DiCarlo, & Stricklin (2003); LAMP (Language Acquisition through Motor Planning) by PRC-Saltillo.*

## Executive Function Support

Users with TBI, ADHD, autism, or developmental disabilities may struggle with planning, sequencing, and task-switching:

- **Progressive disclosure**: Show only the current step. Don't expose all form fields at once in a multi-step process.
- **Undo over confirmation**: "Are you sure?" dialogs require evaluating consequences. An undo action after the fact is easier to understand and lower cognitive load.
- **Consistent affordances**: Interactive elements should always look interactive. Don't use flat, borderless buttons that look like text.
- **Task persistence**: If a user navigates away mid-task, preserve their progress. Don't clear form data on back-button.
- **Decision fatigue**: Limit choices per screen to 5-7 options (Miller's Law). Use smart defaults to reduce required decisions.

## Input Purpose and Autocomplete (WCAG 1.3.5)

Use HTML `autocomplete` attributes so browsers and AT can auto-fill known fields:
- Common values: `name`, `email`, `tel`, `street-address`, `postal-code`, `cc-number`, `bday`
- Benefits motor-impaired users (fewer keystrokes) and cognitive users (less to remember)
- Input purpose also enables AT to show familiar icons alongside fields

## Multiple Ways to Navigate (WCAG 2.4.5)

Provide at least two ways to reach any page: navigation menu + search, or navigation + sitemap, or TOC + breadcrumbs. Site search should have a clear, labeled input and visible submit button.

## Consistent Help (WCAG 3.2.6)

If a help mechanism exists (chat, FAQ link, phone number), place it in the same relative position on every page. Contact info, self-help options, and support links must appear in consistent order.

## Text Spacing (WCAG 1.4.12)

Users must be able to override text spacing without losing content: line-height 1.5x font size, paragraph spacing 2x font size, letter-spacing 0.12em, word-spacing 0.16em. Test by applying these values — if content clips or overlaps, the site fails. Don't use fixed heights on text containers.

## Communication and Speech

- **No voice-only interfaces**: Always provide text or touch alternatives to voice input
- **Captions and transcripts**: All audio and video content needs synchronized captions. Provide full transcripts for audio-only content.
- **AAC integration**: If building communication tools, follow the Modified Fitzgerald Key color conventions (see `/accessibility:motor` for the full table) and support standard symbol systems (PCS by Tobii Dynavox, SymbolStix by n2y, Blissymbolics by BCI — 6,000+ symbols with Unicode code points)
- **Text-to-speech considerations**: Keep text content well-structured so TTS reads it in logical order. Avoid layout tables and CSS order tricks that break reading flow.

## WCAG 2.2 AA — Understandable Checklist

- [ ] `<html lang="en">` (or appropriate language) is set
- [ ] Navigation is consistent across pages
- [ ] Form inputs have clear labels and instructions
- [ ] Inputs for personal data have `autocomplete` attributes (1.3.5)
- [ ] At least two ways to reach any page (2.4.5)
- [ ] Help mechanisms appear in consistent position across pages (3.2.6)
- [ ] Error messages are specific and suggest fixes
- [ ] *2.2* Redundant entry: don't require re-entering information already provided (3.3.7)

## Reference Files

- `reference/cognitive.css` — Reduced motion media query, dyslexia-friendly text styles

## Audit Scripts

- `scripts/timing-audit.py` — Flags animations and transitions missing `prefers-reduced-motion` support
- `scripts/link-text-audit.py` — Detects vague link text ("click here", "read more") that fails plain language standards
- `scripts/heading-outline.py` — Validates heading hierarchy for proper content chunking
- `scripts/focus-order-check.py` — Checks focus order and visibility for predictable keyboard navigation

## Common Issues and Fixes

| Issue | Fix |
|-------|-----|
| Auto-playing media | Add pause/stop controls, no autoplay |
| Hover-only content | Make content keyboard/touch accessible |
| Inconsistent layout | Keep navigation and key actions in fixed positions across all pages |
