#!/usr/bin/env python3
"""
Form Label Audit

Scan HTML for form inputs that lack accessible names.
Checks for: <label for="id"> matching an <input id="id">, 
inputs wrapped in <label>, aria-label, and aria-labelledby.

WCAG 3.3.2 (Level A): Labels or Instructions are provided when content
requires user input.
WCAG 1.3.1 (Level A): Info and Relationships — labels must be programmatically
determinable.

No dependencies — stdlib only.

Usage:
    python3 form-label-audit.py index.html
    python3 form-label-audit.py --format json page.html
"""

import argparse
import json
import os
import sys
from html.parser import HTMLParser


INPUT_TAGS = {"input", "select", "textarea"}
HIDDEN_INPUT_TYPES = {"hidden", "submit", "reset", "button", "image"}


class FormLabelAuditor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.inputs = []  # List of dicts for each input
        self.labels = []  # List of dicts for each label
        self._in_label = False
        self._current_label = None

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        line = self.getpos()[0]

        if tag == "label":
            self._in_label = True
            self._current_label = {
                "for": attrs_dict.get("for"),
                "line": line,
                "has_input_inside": False
            }
            self.labels.append(self._current_label)

        if tag in INPUT_TAGS:
            input_type = attrs_dict.get("type", "text").lower()
            if input_type in HIDDEN_INPUT_TYPES:
                return

            input_info = {
                "tag": tag,
                "id": attrs_dict.get("id"),
                "name": attrs_dict.get("name"),
                "type": input_type,
                "aria_label": attrs_dict.get("aria-label"),
                "aria_labelledby": attrs_dict.get("aria-labelledby"),
                "title": attrs_dict.get("title"),
                "placeholder": attrs_dict.get("placeholder"),
                "line": line,
                "inside_label": self._in_label
            }
            self.inputs.append(input_info)
            if self._in_label:
                self._current_label["has_input_inside"] = True

    def handle_endtag(self, tag):
        if tag == "label":
            self._in_label = False
            self._current_label = None

    def analyze(self):
        issues = []
        label_fors = [l["for"] for l in self.labels if l["for"]]
        
        for inp in self.inputs:
            has_name = False
            fix_suggestion = "Add a <label> with a 'for' attribute matching the input 'id', or wrap the input in a <label>."

            # 1. Check for explicit label association
            if inp["id"] and inp["id"] in label_fors:
                has_name = True
            
            # 2. Check for implicit label association (wrapping)
            if inp["inside_label"]:
                has_name = True

            # 3. Check for aria-label
            if inp["aria_label"]:
                has_name = True
            
            # 4. Check for aria-labelledby
            if inp["aria_labelledby"]:
                has_name = True

            # 5. Check for title (less preferred but fallback)
            if not has_name and inp["title"]:
                has_name = True
                issues.append({
                    "line": inp["line"], "severity": "warning",
                    "element": f'<{inp["tag"]} id="{inp["id"] or ""}" name="{inp["name"] or ""}">',
                    "issue": "Input uses 'title' for its accessible name",
                    "fix": "Use a <label> or 'aria-label' instead; 'title' is not reliably announced."
                })

            if not has_name:
                # 6. Check for placeholder (common failure)
                if inp["placeholder"]:
                    issues.append({
                        "line": inp["line"], "severity": "error",
                        "element": f'<{inp["tag"]} placeholder="{inp["placeholder"][:30]}">',
                        "issue": "Input lacks a label (placeholder is NOT a label)",
                        "fix": fix_suggestion
                    })
                else:
                    issues.append({
                        "line": inp["line"], "severity": "error",
                        "element": f'<{inp["tag"]} id="{inp["id"] or ""}" name="{inp["name"] or ""}">',
                        "issue": "Input lacks an associated label or accessible name",
                        "fix": fix_suggestion
                    })
        
        return issues


def audit_file(filepath):
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()
    auditor = FormLabelAuditor()
    auditor.feed(content)
    return auditor.analyze(), len(auditor.inputs)


def main():
    parser = argparse.ArgumentParser(
        description="Audit form inputs for label associations (WCAG 3.3.2)."
    )
    parser.add_argument("files", nargs="+", help="HTML files to audit")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    args = parser.parse_args()

    all_results = {}
    total_issues = 0

    for filepath in args.files:
        if not os.path.isfile(filepath):
            print(f"Warning: {filepath} not found, skipping", file=sys.stderr)
            continue
        issues, total_inputs = audit_file(filepath)
        all_results[filepath] = {"issues": issues, "total_inputs": total_inputs}
        total_issues += len(issues)

    if args.format == "json":
        print(json.dumps(all_results, indent=2))
    else:
        for filepath, result in all_results.items():
            issues = result["issues"]
            print(f"\n{'='*60}")
            print(f"  {filepath} — Form Label Audit")
            print(f"  Total inputs: {result['total_inputs']}  Issues: {len(issues)}")
            print(f"{'='*60}")
            for issue in issues:
                icon = {"error": "ERR", "warning": "WRN"}[issue["severity"]]
                print(f"  [{icon}] Line {issue['line']}: {issue['issue']}")
                print(f"        {issue['element']}")
                print(f"        fix: {issue['fix']}")
            if not issues:
                print("  No form label issues detected.")
            print()

    sys.exit(1 if total_issues > 0 else 0)


if __name__ == "__main__":
    main()
