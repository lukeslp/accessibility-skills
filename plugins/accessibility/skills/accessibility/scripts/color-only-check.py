#!/usr/bin/env python3
"""
Color-Only Information Checker

Scan HTML for patterns where color may be the sole means of conveying information.
Flags: form validation using only red/green borders, status indicators using only
color dots, links distinguished only by color (no underline).

WCAG 1.4.1 (Level A): Color must not be the only visual means of conveying
information, indicating an action, prompting a response, or distinguishing
a visual element.

No dependencies — stdlib only.

Usage:
    python3 color-only-check.py index.html
    python3 color-only-check.py --format json page.html
"""

import argparse
import json
import os
import re
import sys
from html.parser import HTMLParser


COLOR_KEYWORDS = {
    "red", "green", "blue", "yellow", "orange", "purple",
    "#ff0000", "#00ff00", "#0000ff", "#ff0", "#0f0", "#00f",
    "rgb(255,0,0)", "rgb(0,255,0)", "rgb(0,128,0)",
}

# Patterns that suggest color-only information
STATUS_PATTERNS = [
    re.compile(r'class="[^"]*\b(success|error|warning|danger|info)\b[^"]*"', re.I),
    re.compile(r'class="[^"]*\b(red|green|blue|yellow|orange)\b[^"]*"', re.I),
    re.compile(r'class="[^"]*\b(text-danger|text-success|text-warning|text-info)\b[^"]*"', re.I),
    re.compile(r'class="[^"]*\b(bg-danger|bg-success|bg-warning|bg-info)\b[^"]*"', re.I),
    re.compile(r'class="[^"]*\b(badge-danger|badge-success|badge-warning)\b[^"]*"', re.I),
    re.compile(r'class="[^"]*\b(alert-danger|alert-success|alert-warning)\b[^"]*"', re.I),
]


class ColorOnlyChecker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.issues = []
        self._in_style = False
        self._style_content = ""

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        line = self.getpos()[0]
        style = attrs_dict.get("style", "")
        class_attr = attrs_dict.get("class", "")
        role = attrs_dict.get("role", "")

        if tag == "style":
            self._in_style = True
            self._style_content = ""
            return

        # Check for color-only status patterns in classes
        full_tag = f'class="{class_attr}"' if class_attr else f"<{tag}>"
        for pattern in STATUS_PATTERNS:
            match = pattern.search(f'class="{class_attr}"')
            if match:
                has_icon = any(k in attrs_dict for k in ["aria-label", "aria-describedby"])
                if not has_icon:
                    self.issues.append({
                        "line": line, "severity": "warning",
                        "element": f'<{tag} class="{class_attr[:50]}">',
                        "issue": f"Status class '{match.group(1)}' may rely on color alone",
                        "fix": "Add an icon, text label, or aria-label alongside the color "
                               "indicator"
                    })

        # Check for inline color on spans/divs that might be status indicators
        if style and tag in ("span", "div", "p", "td", "li"):
            color_match = re.search(
                r'(?:background-)?color:\s*(#[0-9a-fA-F]{3,6}|red|green|blue|orange|yellow)',
                style, re.I
            )
            if color_match and not attrs_dict.get("aria-label"):
                self.issues.append({
                    "line": line, "severity": "info",
                    "element": f'<{tag} style="...{color_match.group(0)}...">',
                    "issue": "Inline color styling — verify this isn't the only indicator",
                    "fix": "If color conveys meaning, add a text label, icon, or pattern"
                })

        # Check for links without underline
        if tag == "a" and style:
            if "text-decoration" in style and "none" in style:
                if "color" in style or class_attr:
                    self.issues.append({
                        "line": line, "severity": "warning",
                        "element": f'<a style="text-decoration:none"...',
                        "issue": "Link with removed underline may rely on color alone",
                        "fix": "If links are only distinguished by color, add underline, "
                               "bold, or other non-color indicator"
                    })

        # Check for required field indicators that might be color-only
        if tag in ("input", "select", "textarea"):
            if "required" in attrs_dict or attrs_dict.get("aria-required") == "true":
                # We can't easily check siblings in a streaming parser, but we can 
                # flag it for manual verification to ensure a text indicator exists.
                self.issues.append({
                    "line": line, "severity": "info",
                    "element": f'<{tag} ... required>',
                    "issue": "Required field detected — verify a non-color indicator exists",
                    "fix": "Ensure an asterisk (*) or '(required)' text is present in the "
                           "label, not just a red border or color change."
                })

    def handle_data(self, data):
        if self._in_style:
            self._style_content += data

    def handle_endtag(self, tag):
        if tag == "style" and self._in_style:
            self._in_style = False
            # Check for link styling that removes underlines — handles
            # nested blocks (@media), compound selectors, and variants like
            # "a {", "a.nav {", "a[href] {", ".foo a {", "button, a {"
            self._check_link_underlines(self._style_content)

    def _check_link_underlines(self, css):
        """Walk CSS blocks (including nested @-rules) looking for anchor
        selectors paired with text-decoration: none."""
        depth = 0
        i = 0
        selector_start = 0
        while i < len(css):
            ch = css[i]
            if ch == '{':
                if depth == 0:
                    selector = css[selector_start:i]
                    # At-rules like @media: recurse into their body
                    if selector.strip().startswith('@'):
                        # Find matching close brace for this at-rule
                        inner_depth = 1
                        j = i + 1
                        while j < len(css) and inner_depth > 0:
                            if css[j] == '{':
                                inner_depth += 1
                            elif css[j] == '}':
                                inner_depth -= 1
                            j += 1
                        self._check_link_underlines(css[i+1:j-1])
                        i = j
                        selector_start = i
                        continue
                depth += 1
            elif ch == '}':
                depth -= 1
                if depth == 0:
                    body = css[css.index('{', selector_start)+1:i]
                    selector = css[selector_start:css.index('{', selector_start)]
                    if re.search(r'(?:^|[\s,>+~])a(?:$|[\s,>+~:.\[{])', selector) and \
                       re.search(r'text-decoration:\s*none', body, re.I):
                        self.issues.append({
                            "line": 0, "severity": "warning",
                            "element": f"<style> ({selector.strip()})",
                            "issue": "Link underline removal detected in stylesheet",
                            "fix": "Links distinguished only by color fail WCAG 1.4.1. "
                                   "Add underline on hover/focus at minimum, or use another indicator."
                        })
                    selector_start = i + 1
            i += 1


def audit_file(filepath):
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()
    checker = ColorOnlyChecker()
    checker.feed(content)
    return checker.issues


def main():
    parser = argparse.ArgumentParser(
        description="Check for color-only information patterns (WCAG 1.4.1)."
    )
    parser.add_argument("files", nargs="+", help="HTML files to check")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    args = parser.parse_args()

    all_results = {}
    total_issues = 0

    for filepath in args.files:
        if not os.path.isfile(filepath):
            print(f"Warning: {filepath} not found, skipping", file=sys.stderr)
            continue
        issues = audit_file(filepath)
        all_results[filepath] = {"issues": issues}
        total_issues += len(issues)

    if args.format == "json":
        print(json.dumps(all_results, indent=2))
    else:
        for filepath, result in all_results.items():
            issues = result["issues"]
            print(f"\n{'='*60}")
            print(f"  {filepath} — Color-Only Information Check")
            print(f"  Potential issues: {len(issues)}")
            print(f"{'='*60}")
            for issue in issues:
                icon = {"error": "ERR", "warning": "WRN", "info": "INF"}[issue["severity"]]
                print(f"  [{icon}] Line {issue['line']}: {issue['issue']}")
                print(f"        {issue['element']}")
                print(f"        fix: {issue['fix']}")
            if not issues:
                print("  No color-only patterns detected.")
                print("  Note: This tool checks HTML patterns only. Visual-only color")
                print("  indicators in external CSS require manual review.")
            print()

    sys.exit(1 if total_issues > 0 else 0)


if __name__ == "__main__":
    main()
