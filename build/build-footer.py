#!/usr/bin/env python3
"""
Install one standard footer on every page.

Why a script: the site runs four different design systems (teal, gold, orange,
and the Academy's own). A pixel-identical footer would mean unifying all of
them. What actually matters for local SEO is that the NAP text is identical
everywhere and present on every page, so this standardises structure and
content while letting each page's palette style it.

Colour resolution uses nested CSS custom-property fallbacks:
    var(--accent, var(--gold, var(--orange, #4DC9F5)))
Each page supplies whichever variable it defines; the last value is the
fallback for pages that define none. Every page on the site is dark-themed, so
white-alpha text works throughout.

Idempotent — safe to re-run. Replaces whatever is between the markers.

    python3 build/build-footer.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BEGIN, END = "<!--TZ-FOOTER:BEGIN-->", "<!--TZ-FOOTER:END-->"
HEAD_BEGIN, HEAD_END = "<!--TZ-HEAD:BEGIN-->", "<!--TZ-HEAD:END-->"
CSS_BEGIN, CSS_END = "/*TZ-FOOTER-CSS:BEGIN*/", "/*TZ-FOOTER-CSS:END*/"

GBP = "https://maps.google.com/?cid=6350256215350330460"
FB = "https://www.facebook.com/p/Training-Zone-Utah-61558927589881/"
YELP = "https://www.yelp.com/biz/training-zone-herriman"
BOOK = "https://book.trainingzoneutah.com"

HEAD = f"""{HEAD_BEGIN}
<!-- Trustpilot bootstrap. Async, so it never blocks render. Explicit https
     rather than the protocol-relative // form Trustpilot still ships. -->
<script type="text/javascript" src="https://widget.trustpilot.com/bootstrap/v5/tp.widget.bootstrap.min.js" async></script>
{HEAD_END}"""

CSS = f"""{CSS_BEGIN}
.tz-foot{{--tzf:var(--accent,var(--gold,var(--orange,#4DC9F5)));
  border-top:1px solid rgba(255,255,255,.10);margin-top:0;padding:52px 24px 30px;
  font-family:inherit;font-size:15px;line-height:1.65;color:rgba(255,255,255,.62)}}
.tz-foot a{{color:rgba(255,255,255,.72);text-decoration:none;transition:color .15s}}
.tz-foot a:hover{{color:var(--tzf)}}
.tz-foot__in{{max-width:1180px;margin:0 auto;display:grid;
  grid-template-columns:minmax(240px,1.15fr) repeat(3,minmax(130px,.95fr));gap:34px}}
.tz-foot__name{{font-size:19px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;
  color:#fff;margin-bottom:12px}}
.tz-foot address{{font-style:normal;margin-bottom:12px}}
.tz-foot address a{{display:inline-block}}
.tz-foot__meta{{font-size:13.5px;color:rgba(255,255,255,.48);margin-top:10px}}
.tz-foot__h{{font-size:11px;font-weight:800;letter-spacing:.16em;text-transform:uppercase;
  color:var(--tzf);margin-bottom:14px}}
.tz-foot__col{{display:flex;flex-direction:column;gap:9px;font-size:14.5px}}
.tz-foot__tp{{margin-top:8px;min-width:180px}}
.tz-foot__legal{{max-width:1180px;margin:34px auto 0;padding-top:20px;
  border-top:1px solid rgba(255,255,255,.07);font-size:13px;color:rgba(255,255,255,.42)}}
@media(max-width:900px){{.tz-foot__in{{grid-template-columns:1fr 1fr}}}}
@media(max-width:600px){{.tz-foot__in{{grid-template-columns:1fr;gap:28px}}
  .tz-foot{{padding:40px 22px 26px}}}}
{CSS_END}"""

# NAP text below is the single source of truth and must match the Google
# Business Profile character for character.
HTML = f"""{BEGIN}
<footer class="tz-foot">
  <div class="tz-foot__in">
    <div>
      <div class="tz-foot__name">Training Zone</div>
      <address>
        <a href="{GBP}" target="_blank" rel="noopener">5639 Mirabella Dr<br>Herriman, UT 84096</a><br>
        <a href="tel:+13857869324">385-786-9324</a>
      </address>
      <div class="tz-foot__meta">Open 5am&ndash;12am daily<br>Members have 24/7 gym access</div>
      <div class="tz-foot__meta">Serving Herriman, South Jordan, Riverton, Bluffdale and the southwest Salt Lake Valley.</div>
    </div>

    <nav class="tz-foot__col" aria-label="Programs">
      <div class="tz-foot__h">Programs</div>
      <a href="/private-training/">Private Training</a>
      <a href="/shot-program/">90 Day Shot Program</a>
      <a href="/academy/">Academy</a>
      <a href="/academy/soccer/">Soccer Academy</a>
      <a href="/academy/volleyball/">Volleyball Academy</a>
    </nav>

    <nav class="tz-foot__col" aria-label="Visit">
      <div class="tz-foot__h">Visit</div>
      <a href="/free-session/">Free Evaluation</a>
      <a href="/contact/">Contact &amp; Directions</a>
      <a href="/faq/">FAQ</a>
      <a href="/blog/">The Zone</a>
      <a href="{BOOK}" target="_blank" rel="noopener">Book a Court</a>
    </nav>

    <nav class="tz-foot__col" aria-label="Find us">
      <div class="tz-foot__h">Find Us</div>
      <a href="{GBP}" target="_blank" rel="noopener">Google Business Profile</a>
      <a href="{FB}" target="_blank" rel="noopener">Facebook</a>
      <a href="{YELP}" target="_blank" rel="noopener">Yelp</a>

      <!-- Trustpilot review collector -->
      <div class="trustpilot-widget tz-foot__tp" data-locale="en-US"
           data-template-id="56278e9abfbbba0bdcd568bc"
           data-businessunit-id="6a8ba0ccb1b4ac4deeef6970"
           data-style-height="52px" data-style-width="100%"
           data-token="f8b31dbe-cc84-4635-931a-7fb51903dc8e">
        <a href="https://www.trustpilot.com/review/trainingzoneutah.com" target="_blank" rel="noopener">Trustpilot</a>
      </div>
    </nav>
  </div>

  <div class="tz-foot__legal">
    &copy; 2026 Training Zone. All rights reserved. &middot;
    5639 Mirabella Dr, Herriman, UT 84096 &middot;
    <a href="tel:+13857869324">385-786-9324</a>
  </div>
</footer>
{END}"""


def install(path: Path) -> str:
    s = path.read_text(encoding="utf-8")
    before = s

    # --- CSS: replace existing block, else insert just before </head> ---
    if CSS_BEGIN in s:
        s = re.sub(re.escape(CSS_BEGIN) + r".*?" + re.escape(CSS_END), lambda _: CSS, s, flags=re.S)
    else:
        assert s.count("</head>") == 1, f"{path}: no unique </head>"
        s = s.replace("</head>", f"<style>\n{CSS}\n</style>\n</head>")

    # --- head snippet: replace existing block, else insert before </head> ---
    if HEAD_BEGIN in s:
        s = re.sub(re.escape(HEAD_BEGIN) + r".*?" + re.escape(HEAD_END), lambda _: HEAD, s, flags=re.S)
    else:
        s = s.replace("</head>", f"{HEAD}\n</head>")

    # --- HTML: replace our block, else the page's existing footer, else append ---
    if BEGIN in s:
        s = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END), lambda _: HTML, s, flags=re.S)
    else:
        existing = re.search(r"[ \t]*<footer\b.*?</footer>", s, re.S)
        if existing:
            s = s[: existing.start()] + HTML + s[existing.end():]
        else:
            assert s.count("</body>") == 1, f"{path}: no unique </body>"
            s = s.replace("</body>", f"{HTML}\n</body>")

    path.write_text(s, encoding="utf-8")
    return "unchanged" if s == before else "updated"


def main() -> int:
    pages = sorted(p for p in ROOT.glob("**/*.html") if ".git" not in p.parts)
    if not pages:
        print("no pages found", file=sys.stderr)
        return 1
    for p in pages:
        print(f"  {install(p):<10} {p.relative_to(ROOT)}")
    print(f"\n{len(pages)} pages carry the standard footer")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
