# Training Zone blog — build & deploy notes

Hand this folder to Claude Code (or any dev) to commit into the trainingzoneutah.com repo.

## What's here

```
export/
├─ index.html                  # blog hub ("The Zone")
├─ what-is-the-academy.html    # post template + sample post
├─ assets/
│  ├─ blog.css                 # all styles for both pages
│  ├─ hero-gym.png             # hub hero photo (wide gym shot)
│  └─ academy-featured.png     # Academy key art (featured image + post hero)
└─ BUILD-NOTES.md              # this file
```

Both pages are static HTML + one stylesheet. No build step, no JS. Google Fonts load from CDN (Barlow Condensed, Barlow, IBM Plex Mono).

## Deploy targets

- Hub: `/blog/` → `index.html`
- Post: `/blog/what-is-the-academy/` → `what-is-the-academy.html`
- Assets: `/blog/assets/`

Links between the two pages are relative (`index.html`, `what-is-the-academy.html`). If the site uses pretty URLs with trailing-slash directories, change them to `/blog/` and `/blog/what-is-the-academy/` and update `assets/blog.css` paths to `/blog/assets/blog.css`.

Header, footer, and the ticker are duplicated in both files. If the site has a templating layer (Astro/Eleventy/Next/WP), extract these into a shared layout:
- `.ticker` block
- `header.site-head`
- `nav.cats`
- `footer.site-foot`

## Current content state

**Live:** "What is the Academy?" — this is a working sample. Client will supply the real Academy article; replace the body copy inside `<article>` and keep the block structure.

**Coming soon (6 cards on the hub):** shooting flaws, how to pick a trainer in Herriman, what college coaches watch, offseason strength for guards, 24/7 smart-gym rebuild, player spotlight. These render as dimmed `.card--soon` cards with a COMING SOON badge and no link. To publish one: remove the `card--soon` class, drop the `.soon` badge, wrap the `<h3>` text in a link, swap the placeholder `.card__slot` for an `<img>`, and add a date to `.meta`.

## Adding a new post

1. Copy `what-is-the-academy.html` → `your-slug.html`.
2. Update: `<title>`, `meta description`, `link rel=canonical`, OG tags, the JSON-LD block, breadcrumb category, `<h1>`, and the `.byline` values.
3. Write the body inside `<article>`. Available blocks (all optional, use what the piece needs):
   - `p.lede` — one opening paragraph, larger type
   - `h2` + `p` — normal sections; give each `h2` an `id` and mirror it in `.side__toc`
   - `div.stats` — up to 3 stat cards (auto-stacks under 620px)
   - `dl.rows` — label + description rows for schedules, phases, tiers
   - `figure` — image + caption
   - `blockquote` — parent/player testimonial
   - `div.endcap` — orange CTA band; keep this on every post
4. Add a card to the hub grid and, if it belongs there, the Most Read rail.

## Category colors

Defined as CSS variables in `blog.css`. Each category keeps one color across badge, card bar, and rank number:

| Category | Variable |
| --- | --- |
| Shooting | `--cat-shooting` (orange, brand) |
| Recruiting | `--cat-recruiting` (blue) |
| Strength | `--cat-strength` (yellow) |
| Academy | `--cat-academy` (green) |
| Facility | `--cat-facility` (violet) |
| Spotlights | `--cat-spotlights` (pink) |
| Parent Guide | `--cat-parent` (teal) |

The category strip links are anchors (`#shooting`, etc.) — they are placeholders. Wire them to real category archive pages, or add client-side filtering, whichever the stack supports.

## Responsive behavior

- Hub hero is **hidden below 700px** — mobile opens on the category strip, then the featured post.
- Featured + rail and article + sidebar collapse to one column at 860px.
- Stat strip goes 1-up at 620px.
- Main nav links hide below 900px. **TODO for dev:** add a mobile menu (hamburger) — none is built.

## Local SEO notes

- `index.html` carries `Blog` JSON-LD with a `SportsActivityLocation` publisher (address, phone).
- `what-is-the-academy.html` carries `BlogPosting` JSON-LD.
- Update `datePublished` per post, and add `dateModified` when a post is edited.
- Keep "Herriman" / "Utah" in titles and H1s where it reads naturally; don't stuff it.
- Add each new post URL to the sitemap.
- Photo alt text should describe the athlete and the facility, not the keyword.

## Known gaps / decisions for the client

- No mobile nav menu yet (see above).
- Category strip is not functional — needs archive pages or JS filtering.
- Author block uses a placeholder avatar; supply a coach headshot.
- Placeholder image slots in the post body and coming-soon cards are labeled `[ ... ]` — swap for real photos before launch.
- Academy and 1-on-1 sales pages are not built yet; the CTA blocks currently point to the existing `/free-session/` page.


---

## Build log — shipped 2026-08-18

Deployed into `coachmattmont-ui/tz-academy-site` at `/blog/`. Changes made from
the Design export during integration:

**Paths & URLs**
- Pretty URLs: `/blog/` and `/blog/what-is-the-academy/` (directory + `index.html`).
- All internal links converted to root-relative (`/academy/`, `/faq/`, …).
- Canonicals and OG URLs switched from `www.trainingzoneutah.com` to the apex
  `trainingzoneutah.com` — every other page on the site canonicalizes to apex,
  and split signals would have been self-competing.

**Images**
- `hero-gym.png` (3.2 MB) → `hero-gym.webp`, 2000px wide, 129 KB.
- `academy-featured.png` (5.8 MB) → `academy-featured.webp`, 2000px wide, 74 KB.
- Added `og-blog.jpg` and `og-academy.jpg`, both 1200×630 JPEG. OG cards stay
  JPEG because WebP support in link-preview scrapers is still uneven.
- `width`/`height` added to both `<img>` tags to reserve layout space.

**Resolved from "Known gaps"**
- Mobile nav built (burger + panel under 900px). Styles appended to `blog.css`,
  ~15 lines of JS inline in each page.
- Category strip now filters client-side against the cards on the page. Cards
  carry `data-cat`; the strip reads `location.hash`. Replace with real archive
  pages when the post count outgrows one hub.

**Content corrections**
The Design export contained placeholder specifics that would have gone live as
fact. Replaced with claims the site already publishes:
- Ticker items (`tryout window opens Sept 2`, `4 spots left this cycle`,
  `booking through October`) → Academy Year 2 start, Sept 2026 soccer/volleyball
  launch, 10-spot Shot Program cap, 5am–12am rentals, free evaluation.
- Article weekly schedule (invented Mon/Wed/Tue/Thu split) → the 7–9th and
  10–12th grade blocks published on `/academy/`.
- Stat strip `12 months` / `3 tracks` → `25 per cohort` / `4 days a week`.

**Still open**
- Article body is Design's sample prose. Matt is writing the real Academy post;
  keep the block structure and swap the copy inside `<article>`.
- Author avatar is still a placeholder swatch — needs a coach headshot.
- Six coming-soon cards use `[ ... ]` placeholder slots — swap for real photos
  as each post is written.
- "Keep reading" links in the post sidebar have no `href` yet (targets unwritten).
- `/academy/` and `/private-training/` both exist now, so the note about CTA
  blocks falling back to `/free-session/` is stale.
