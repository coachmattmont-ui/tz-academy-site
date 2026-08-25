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
IG = "https://www.instagram.com/trainingzoneutah/"
X = "https://x.com/TrainingZoneUt"
YT = "https://www.youtube.com/@TrainingZoneUtah"
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
.tz-foot__social{{max-width:1180px;margin:30px auto 0;display:flex;gap:12px;align-items:center}}
.tz-foot__social a{{display:inline-flex;align-items:center;justify-content:center;width:38px;height:38px;
  border:1px solid rgba(255,255,255,.16);border-radius:9px;color:rgba(255,255,255,.72)}}
.tz-foot__social a:hover{{color:var(--tzf);border-color:var(--tzf)}}
.tz-foot__social svg{{width:18px;height:18px;fill:currentColor;display:block}}
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

  <div class="tz-foot__social">
    <a href="{FB}" target="_blank" rel="noopener" aria-label="Training Zone on Facebook" title="Facebook">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M9.101 23.691v-7.98H6.627v-3.667h2.474v-1.58c0-4.085 1.848-5.978 5.858-5.978.401 0 .955.042 1.468.103a8.68 8.68 0 0 1 1.141.195v3.325a8.623 8.623 0 0 0-.653-.036 26.805 26.805 0 0 0-.733-.009c-.707 0-1.259.096-1.675.309a1.686 1.686 0 0 0-.679.622c-.258.42-.374.995-.374 1.752v1.297h3.919l-.386 2.103-.287 1.564h-3.246v8.245C19.396 23.238 24 18.179 24 12.044c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.628 3.874 10.35 9.101 11.647Z"/></svg>
    </a>
    <a href="{IG}" target="_blank" rel="noopener" aria-label="Training Zone on Instagram" title="Instagram">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 0C8.74 0 8.333.015 7.053.072 5.775.132 4.905.333 4.14.63c-.789.306-1.459.717-2.126 1.384S.935 3.35.63 4.14C.333 4.905.131 5.775.072 7.053.012 8.333 0 8.74 0 12s.015 3.667.072 4.947c.06 1.277.261 2.148.558 2.913.306.788.717 1.459 1.384 2.126.667.666 1.336 1.079 2.126 1.384.766.296 1.636.499 2.913.558C8.333 23.988 8.74 24 12 24s3.667-.015 4.947-.072c1.277-.06 2.148-.262 2.913-.558.788-.306 1.459-.718 2.126-1.384.666-.667 1.079-1.335 1.384-2.126.296-.765.499-1.636.558-2.913.06-1.28.072-1.687.072-4.947s-.015-3.667-.072-4.947c-.06-1.277-.262-2.149-.558-2.913-.306-.789-.718-1.459-1.384-2.126C21.319 1.347 20.651.935 19.86.63c-.765-.297-1.636-.499-2.913-.558C15.667.012 15.26 0 12 0zm0 2.16c3.203 0 3.585.016 4.85.071 1.17.055 1.805.249 2.227.415.562.217.96.477 1.382.896.419.42.679.819.896 1.381.164.422.36 1.057.413 2.227.057 1.266.07 1.646.07 4.85s-.015 3.585-.074 4.85c-.061 1.17-.256 1.805-.421 2.227-.224.562-.479.96-.899 1.382-.419.419-.824.679-1.38.896-.42.164-1.065.36-2.235.413-1.274.057-1.649.07-4.859.07-3.211 0-3.586-.015-4.859-.074-1.171-.061-1.816-.256-2.236-.421-.569-.224-.96-.479-1.379-.899-.421-.419-.69-.824-.9-1.38-.165-.42-.359-1.065-.42-2.235-.045-1.26-.061-1.649-.061-4.844 0-3.196.016-3.586.061-4.861.061-1.17.255-1.814.42-2.234.21-.57.479-.96.9-1.381.419-.419.81-.689 1.379-.898.42-.166 1.051-.361 2.221-.421 1.275-.045 1.65-.06 4.859-.06zm0 3.678a6.162 6.162 0 1 0 0 12.324 6.162 6.162 0 0 0 0-12.324zM12 16c-2.21 0-4-1.79-4-4s1.79-4 4-4 4 1.79 4 4-1.79 4-4 4zm7.846-10.405a1.441 1.441 0 1 1-2.883 0 1.441 1.441 0 0 1 2.883 0z"/></svg>
    </a>
    <a href="{X}" target="_blank" rel="noopener" aria-label="Training Zone on X" title="X">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M18.901 1.153h3.68l-8.04 9.19L24 22.846h-7.406l-5.8-7.584-6.638 7.584H.474l8.6-9.83L0 1.154h7.594l5.243 6.932ZM17.61 20.644h2.039L6.486 3.24H4.298Z"/></svg>
    </a>
    <a href="{YT}" target="_blank" rel="noopener" aria-label="Training Zone on YouTube" title="YouTube">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
    </a>
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
