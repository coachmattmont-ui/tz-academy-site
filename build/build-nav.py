#!/usr/bin/env python3
"""
Install one standard primary navigation on every page.

Same approach as build-footer.py: the site runs four design systems, so this
standardises structure, links and behaviour while letting each page's palette
colour it via nested custom-property fallbacks.

Height is fixed and published as --tz-nav-h on :root so sticky elements
elsewhere (the blog category strip, article sidebars, anchor scroll offsets)
can position against it instead of hard-coded pixel values.

Idempotent — safe to re-run.

    python3 build/build-nav.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BEGIN, END = "<!--TZ-NAV:BEGIN-->", "<!--TZ-NAV:END-->"
CSS_BEGIN, CSS_END = "/*TZ-NAV-CSS:BEGIN*/", "/*TZ-NAV-CSS:END*/"
BOOK = "https://book.trainingzoneutah.com"

# href -> label. Order is the site's own priority, not alphabetical.
LINKS = [
    ("/private-training/", "Private Training"),
    ("/shot-program/", "Shot Program"),
    ("/academy/", "Academy"),
    ("/blog/", "Blog"),
    ("/faq/", "FAQ"),
    ("/contact/", "Contact"),
]

CSS = f"""{CSS_BEGIN}
:root{{--tz-nav-h:66px}}
@media(max-width:720px){{:root{{--tz-nav-h:58px}}}}
.tz-nav{{--tzn:var(--accent,var(--gold,var(--orange,#4DC9F5)));
  position:sticky;top:0;z-index:200;height:var(--tz-nav-h);box-sizing:border-box;
  display:flex;align-items:center;gap:26px;padding:0 28px;
  background:rgba(8,10,12,.86);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);
  border-bottom:1px solid rgba(255,255,255,.10);font-family:inherit}}
.tz-nav *{{box-sizing:border-box}}
.tz-nav a{{text-decoration:none;transition:color .15s,background .15s,border-color .15s}}
.tz-nav__brand{{display:flex;align-items:center;gap:10px;flex-shrink:0}}
.tz-nav__mark{{display:inline-flex;align-items:center;justify-content:center;width:32px;height:32px;
  border:2px solid var(--tzn);border-radius:8px;color:var(--tzn);
  font-size:15px;font-weight:800;letter-spacing:.5px;line-height:1}}
.tz-nav__word{{font-size:17px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:#fff;white-space:nowrap}}
.tz-nav__links{{display:flex;align-items:center;gap:22px;margin-left:auto;
  font-size:13.5px;font-weight:700;letter-spacing:.06em;text-transform:uppercase}}
.tz-nav__links a{{color:rgba(255,255,255,.70);white-space:nowrap}}
.tz-nav__links a:hover{{color:#fff}}
.tz-nav__links a[aria-current="page"]{{color:var(--tzn)}}
.tz-nav__right{{display:flex;align-items:center;gap:14px;flex-shrink:0}}
.tz-nav__login{{font-size:13px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:rgba(255,255,255,.62);white-space:nowrap}}
.tz-nav__login:hover{{color:#fff}}
.tz-nav__cta{{background:var(--tzn);color:#04222e;font-size:13px;font-weight:800;letter-spacing:.06em;
  text-transform:uppercase;padding:11px 18px;border-radius:8px;white-space:nowrap}}
.tz-nav__cta:hover{{filter:brightness(1.08);color:#04222e}}
.tz-nav__burger{{display:none;background:none;border:0;padding:8px 2px;cursor:pointer;flex-direction:column;gap:5px}}
.tz-nav__burger span{{display:block;width:22px;height:2px;background:#fff;border-radius:2px;transition:transform .2s,opacity .2s}}
.tz-nav__burger[aria-expanded="true"] span:nth-child(1){{transform:translateY(7px) rotate(45deg)}}
.tz-nav__burger[aria-expanded="true"] span:nth-child(2){{opacity:0}}
.tz-nav__burger[aria-expanded="true"] span:nth-child(3){{transform:translateY(-7px) rotate(-45deg)}}
.tz-nav__panel{{display:none;position:fixed;left:0;right:0;top:var(--tz-nav-h);z-index:199;
  flex-direction:column;padding:8px 22px 20px;background:#0a1116;
  border-bottom:1px solid rgba(255,255,255,.12);max-height:calc(100vh - var(--tz-nav-h));overflow-y:auto}}
.tz-nav__panel.is-open{{display:flex}}
.tz-nav__panel a{{padding:14px 2px;font-size:15px;font-weight:700;letter-spacing:.05em;
  text-transform:uppercase;color:#fff;border-bottom:1px solid rgba(255,255,255,.08)}}
.tz-nav__panel a[aria-current="page"]{{color:var(--tzn)}}
.tz-nav__panel .tz-nav__cta{{margin-top:14px;text-align:center;padding:15px;border-bottom:0;color:#04222e}}
@media(max-width:1000px){{
  .tz-nav__links{{display:none}}
  .tz-nav__burger{{display:flex;margin-left:auto}}
  .tz-nav__login{{display:none}}
}}
@media(max-width:400px){{.tz-nav__word{{display:none}}}}
{CSS_END}"""

SCRIPT = """<script>
(function(){
  var b=document.querySelector('.tz-nav__burger'), p=document.getElementById('tzNavPanel');
  if(!b||!p) return;
  function set(o){
    b.setAttribute('aria-expanded',o?'true':'false');
    b.setAttribute('aria-label',o?'Close menu':'Open menu');
    p.classList.toggle('is-open',o);
  }
  b.addEventListener('click',function(){ set(b.getAttribute('aria-expanded')!=='true'); });
  p.addEventListener('click',function(e){ if(e.target.tagName==='A') set(false); });
  document.addEventListener('keydown',function(e){ if(e.key==='Escape') set(false); });
  addEventListener('resize',function(){ if(innerWidth>1000) set(false); });
})();
</script>"""


def build_html(current: str) -> str:
    def mark(href: str) -> str:
        return ' aria-current="page"' if current.startswith(href) and href != "/" else ""

    desktop = "\n      ".join(
        f'<a href="{h}"{mark(h)}>{label}</a>' for h, label in LINKS
    )
    panel = "\n    ".join(
        f'<a href="{h}"{mark(h)}>{label}</a>' for h, label in LINKS
    )
    return f"""{BEGIN}
<nav class="tz-nav" aria-label="Primary">
  <a class="tz-nav__brand" href="/" aria-label="Training Zone home">
    <span class="tz-nav__mark">TZ</span>
    <span class="tz-nav__word">Training Zone</span>
  </a>

  <div class="tz-nav__links">
      {desktop}
  </div>

  <div class="tz-nav__right">
    <a class="tz-nav__login" href="{BOOK}" target="_blank" rel="noopener">Log In</a>
    <a class="tz-nav__cta" href="/free-session/">Free Evaluation</a>
    <button class="tz-nav__burger" aria-label="Open menu" aria-expanded="false" aria-controls="tzNavPanel">
      <span></span><span></span><span></span>
    </button>
  </div>
</nav>

<div class="tz-nav__panel" id="tzNavPanel">
    {panel}
    <a href="{BOOK}" target="_blank" rel="noopener">Log In</a>
    <a class="tz-nav__cta" href="/free-session/">Free Evaluation</a>
</div>
{SCRIPT}
{END}"""


# Old markup to strip. Each is anchored on a distinct wrapper so nothing else matches.
STRIP = [
    r'[ \t]*<div class="ticker">.*?</div></div>\n</div>\n',          # blog promo bar
    r'[ \t]*<header class="site-head">.*?</header>\n',               # blog header
    r'[ \t]*<nav class="nav"[^>]*>.*?</nav>\n',                      # every other page
    r'[ \t]*<div class="mobile-menu"[^>]*>.*?</div>\n',              # old mobile panels
    r'[ \t]*<script>\s*\(function\s*\(\)\s*\{\s*var (?:burger|b)\s*=\s*document\.getElementById\(\'nav(?:Burger|Toggle)\'\).*?\}\)\(\);\s*</script>\n',
]


def install(path: Path, url_path: str) -> str:
    s = path.read_text(encoding="utf-8")
    before = s

    if CSS_BEGIN in s:
        s = re.sub(re.escape(CSS_BEGIN) + r".*?" + re.escape(CSS_END), lambda _: CSS, s, flags=re.S)
    else:
        assert s.count("</head>") == 1, f"{path}: no unique </head>"
        s = s.replace("</head>", f"<style>\n{CSS}\n</style>\n</head>")

    html = build_html(url_path)
    if BEGIN in s:
        s = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END), lambda _: html, s, flags=re.S)
    else:
        for pat in STRIP:
            s = re.sub(pat, "", s, flags=re.S)
        assert s.count("<body>") == 1, f"{path}: no unique <body>"
        s = s.replace("<body>", f"<body>\n{html}\n", 1)

    path.write_text(s, encoding="utf-8")
    return "unchanged" if s == before else "updated"


def main() -> int:
    pages = sorted(p for p in ROOT.glob("**/*.html") if ".git" not in p.parts)
    if not pages:
        print("no pages found", file=sys.stderr)
        return 1
    for p in pages:
        rel = p.relative_to(ROOT).as_posix().replace("index.html", "")
        url = "/" + rel
        print(f"  {install(p, url):<10} {url}")
    print(f"\n{len(pages)} pages carry the standard nav")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
