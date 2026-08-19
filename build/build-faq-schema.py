#!/usr/bin/env python3
"""
Generate the FAQPage JSON-LD for /faq/ directly from the visible Q&A markup.

Why: Google penalizes (and ignores) FAQ schema whose answerText doesn't match
what a user actually sees on the page. Hand-maintaining two copies guarantees
drift. This derives one from the other.

Run from repo root after editing faq/index.html:
    python3 build/build-faq-schema.py

Idempotent — safe to re-run. Replaces whatever is currently between the
FAQ_JSONLD markers.
"""
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FAQ = ROOT / "faq" / "index.html"

START = "<!-- FAQPage schema (generated from the visible Q&A below — do not hand-edit) -->"
PLACEHOLDER = "<!--FAQ_JSONLD-->"
BEGIN_MARK = "<!--FAQ_JSONLD:BEGIN-->"
END_MARK = "<!--FAQ_JSONLD:END-->"


def strip_tags(fragment: str) -> str:
    """Flatten inner HTML to the plain text a reader sees."""
    text = re.sub(r"<br\s*/?>", " ", fragment)
    text = re.sub(r"</p>\s*<p[^>]*>", " ", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def main() -> int:
    src = FAQ.read_text(encoding="utf-8")

    pairs = re.findall(
        r'<h3 class="q">(.*?)</h3>\s*<div class="a">(.*?)</div>',
        src,
        flags=re.S,
    )
    if not pairs:
        print("ERROR: no Q&A pairs found — did the markup change?", file=sys.stderr)
        return 1

    entities = []
    for raw_q, raw_a in pairs:
        q, a = strip_tags(raw_q), strip_tags(raw_a)
        if not q or not a:
            print(f"ERROR: empty question or answer near: {q[:60]!r}", file=sys.stderr)
            return 1
        entities.append(
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
        )

    names = [e["name"] for e in entities]
    dupes = {n for n in names if names.count(n) > 1}
    if dupes:
        print(f"ERROR: duplicate questions: {sorted(dupes)}", file=sys.stderr)
        return 1

    payload = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "url": "https://trainingzoneutah.com/faq/",
        "name": "Training Zone — Frequently Asked Questions",
        "mainEntity": entities,
    }

    block = (
        f"{BEGIN_MARK}\n"
        '<script type="application/ld+json">\n'
        f"{json.dumps(payload, indent=2, ensure_ascii=False)}\n"
        "</script>\n"
        f"{END_MARK}"
    )

    if BEGIN_MARK in src:
        out = re.sub(
            re.escape(BEGIN_MARK) + r".*?" + re.escape(END_MARK),
            lambda _: block,
            src,
            flags=re.S,
        )
    elif PLACEHOLDER in src:
        assert src.count(PLACEHOLDER) == 1
        out = src.replace(PLACEHOLDER, block)
    else:
        print("ERROR: no placeholder or existing block to replace.", file=sys.stderr)
        return 1

    FAQ.write_text(out, encoding="utf-8")
    print(f"OK — wrote {len(entities)} Q&A pairs into faq/index.html")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
