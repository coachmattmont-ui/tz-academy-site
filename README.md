# tz-academy-site

Marketing site for the TZ Academy. Deployed via Cloudflare Pages at `trainingzoneutah.com/academy`.

## Stack

- Plain HTML / CSS / JS
- No build step required to serve (pages are pre-built and committed)
- Cloudflare Pages handles hosting + deploys on push to `main`
- Kit handles email capture (Phase 3 — TODO)

## Structure

```
/index.html              → /academy (Basketball, default)
/soccer/index.html       → /academy/soccer
/volleyball/index.html   → /academy/volleyball
/css/styles.css          → shared stylesheet
/js/sport-content.js     → shared content registry + renderer
/images/                 → logos, hero photos, coach headshots
/_redirects              → Cloudflare Pages redirect rules
/build/build-pages.py    → Generate the three HTML pages from one template
```

## Local dev

```bash
# Serve locally
python3 -m http.server 8080
# Then open http://localhost:8080
```

## Editing content

**Pillar copy, FAQ, coaches, testimonial** → `js/sport-content.js` (data registry at top of file)

**Page structure / hero / meta tags** → `build/build-pages.py` (template), then run:

```bash
python3 build/build-pages.py
```

That regenerates `index.html`, `soccer/index.html`, `volleyball/index.html`.

**Styles** → `css/styles.css`

## Deploy

Pushes to `main` auto-deploy to Cloudflare Pages.

## Phase status

- [x] Phase 1 — Skeleton + styled Basketball/Soccer/Volleyball pages
- [ ] Phase 2 — Real hero images, coach headshots, testimonial content
- [ ] Phase 3 — Kit forms wired (replace placeholder forms + CTA anchors)
- [ ] Phase 4 — Mobile polish, SEO, page-speed audit
- [ ] Phase 5 — Cutover from Clickfunnels (301 redirects live, cancel Clickfunnels)
