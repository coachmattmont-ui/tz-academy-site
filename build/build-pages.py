#!/usr/bin/env python3
"""
Build the three sport pages from a single template.
Run from repo root: python3 build/build-pages.py
"""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SPORTS = {
    "basketball": {
        "label": "Basketball",
        "url_path": "/",
        "out": "index.html",
        "asset_prefix": "",
        "title": "TZ Academy — Basketball | Train Like a Pro. Still Be a Kid.",
        "description": "Train like a pro. Still be a kid. Hybrid-school basketball academy in Herriman, Utah. Junior High + High School cohorts, capped at 25.",
        "hero_eyebrow": "BASKETBALL ACADEMY",
        "hero_accent": "BASKETBALL.",
        "og_image": "/images/og/basketball.jpg",
    },
    "soccer": {
        "label": "Soccer",
        "url_path": "/soccer/",
        "out": "soccer/index.html",
        "asset_prefix": "../",
        "title": "TZ Academy — Soccer | Launching September 2026",
        "description": "Train like a pro. Still be a kid. Hybrid-school soccer academy in Herriman, Utah. Launching September 2026. Junior High + High School cohorts, capped at 25.",
        "hero_eyebrow": "SOCCER ACADEMY",
        "hero_accent": "SOCCER.",
        "og_image": "/images/og/soccer.jpg",
    },
    "volleyball": {
        "label": "Volleyball",
        "url_path": "/volleyball/",
        "out": "volleyball/index.html",
        "asset_prefix": "../",
        "title": "TZ Academy — Volleyball | Launching September 2026",
        "description": "Train like a pro. Still be a kid. Hybrid-school volleyball academy in Herriman, Utah. Launching September 2026. Junior High + High School cohorts, capped at 25.",
        "hero_eyebrow": "VOLLEYBALL ACADEMY",
        "hero_accent": "VOLLEYBALL.",
        "og_image": "/images/og/volleyball.jpg",
    },
}


def build_page(sport_key, cfg):
    asset = cfg["asset_prefix"]
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{cfg['title']}</title>
  <meta name="description" content="{cfg['description']}" />

  <meta property="og:title" content="{cfg['title']}" />
  <meta property="og:description" content="{cfg['description']}" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="https://trainingzoneutah.com/academy{cfg['url_path'] if cfg['url_path'] != '/' else ''}" />
  <meta property="og:image" content="https://trainingzoneutah.com/academy{cfg['og_image']}" />
  <meta name="twitter:card" content="summary_large_image" />

  <link rel="icon" type="image/svg+xml" href="{asset}images/logos/TZ_Logomark_White.svg" />
  <link rel="stylesheet" href="{asset}css/styles.css" />
</head>
<body>
  <a class="sr-only" href="#main">Skip to content</a>

  <!-- TOP UTILITY BAR -->
  <div class="utility-bar" role="contentinfo">
    <span>📞 385-786-9324 · 5639 Mirabella Dr, Herriman, UT 84096</span>
    <span class="utility-bar__status" aria-label="Status">
      <span class="utility-bar__dot" aria-hidden="true"></span>All Courts Playable
    </span>
  </div>

  <!-- NAV -->
  <nav class="nav" aria-label="Primary">
    <a href="https://trainingzoneutah.com" class="nav__brand" aria-label="Training Zone home">
      <img src="{asset}images/logos/TZ_Horizontal_Lockup_White.svg" alt="Training Zone" class="nav__logo" />
    </a>
    <div class="nav__links">
      <a class="nav__link is-active" href="/">Academy</a>
      <a class="nav__link" href="https://trainingzoneutah.com/programs">Programs</a>
      <a class="nav__link" href="https://trainingzoneutah.com/coaches">Coaches</a>
      <a class="nav__link" href="https://trainingzoneutah.com/memberships">Memberships</a>
    </div>
    <button class="nav__menu-toggle" aria-expanded="false" aria-label="Open menu">☰</button>
    <a href="#book-a-call" class="nav__cta">Book a Call →</a>
  </nav>

  <main id="main">

    <!-- HERO -->
    <section class="hero">
      <div class="hero__inner">
        <p class="eyebrow">{cfg['hero_eyebrow']}</p>
        <h1 class="hero__title">TRAIN LIKE A <span class="hero__title-accent">PRO.</span><br />STILL BE A KID.</h1>
        <p class="hero__sub">A different way to train serious young athletes — built around your school day, not against it. Daily individual coaching, live game work, mental performance, and strength training, all in one program.</p>
        <div class="hero__ctas">
          <a href="#book-a-call" class="btn btn--primary">Book a Call</a>
          <a href="#model" class="btn btn--secondary">How It Works</a>
        </div>
        <div class="hero__stats">
          <div><div class="stat__num">25</div><div class="stat__label">Per Cohort</div></div>
          <div><div class="stat__num">4</div><div class="stat__label">Days a Week</div></div>
          <div><div class="stat__num">3</div><div class="stat__label">Sports &amp; Growing</div></div>
        </div>
      </div>
    </section>

    <!-- SPORT SELECTOR -->
    <section class="sport-selector" aria-label="Choose your sport">
      <p class="sport-selector__label">Choose your sport</p>
      <div class="sport-tabs" role="tablist">
        <button class="sport-tab" data-sport="basketball" role="tab"><span aria-hidden="true">🏀</span>Basketball</button>
        <button class="sport-tab" data-sport="soccer" role="tab"><span aria-hidden="true">⚽</span>Soccer</button>
        <button class="sport-tab" data-sport="volleyball" role="tab"><span aria-hidden="true">🏐</span>Volleyball</button>
      </div>
    </section>

    <!-- WHO IT'S FOR -->
    <section class="section section--elevated" id="who">
      <p class="eyebrow">Who it's for</p>
      <h2 class="section__title">Built for two age groups.</h2>
      <p class="section__sub">Same model. Different rhythm.</p>
      <div class="cohort-grid">
        <article class="card">
          <p class="card__eyebrow">Junior High · 7th–8th</p>
          <h3 class="card__title">Group cohort training</h3>
          <p class="card__body">Train 8–10am or 10am–12pm, four days a week. Hybrid school in the afternoon. Cap of 25 athletes per cohort.</p>
        </article>
        <article class="card">
          <p class="card__eyebrow">High School · 9th–12th</p>
          <h3 class="card__title">Small group + dedicated coach</h3>
          <p class="card__body">Custom schedule built around your A/B day. 1-on-1 and small groups (2–3) with a dedicated HS coach. Monitored solo programming. Cap of 25.</p>
        </article>
      </div>
    </section>

    <!-- THE ACADEMY MODEL -->
    <section class="section section--base" id="model">
      <p class="eyebrow">The academy model</p>
      <h2 class="section__title">More training. More sleep.<br />Still a kid.</h2>
      <div class="model__copy">
        <p>Most serious young athletes are stuck choosing: train hard <em>or</em> keep up in school <em>or</em> get enough sleep <em>or</em> have time to be a kid. Pick three.</p>
        <p>The Academy is built so they don't have to pick. Our athletes use a hybrid school schedule — taking some classes on campus and some online through their district. They train during the school day, when the gym is open and the coaches are fresh.</p>
      </div>
      <div class="model__week">
        <p class="model__week-label">A typical Junior High week</p>
        <div class="model__week-grid">
          <span>Mon–Thurs AM</span><span>Academy training</span>
          <span>Afternoons</span><span>On-campus core classes</span>
          <span>Evenings</span><span>Homework, family, rest</span>
        </div>
      </div>
    </section>

    <!-- PILLARS (rendered by JS) -->
    <section class="section section--elevated">
      <p class="eyebrow">What athletes work on</p>
      <h2 class="section__title">Four pillars. Every week.</h2>
      <p class="section__sub">Adapted for {cfg['label'].lower()}.</p>
      <div class="pillars" id="pillar-grid"></div>
    </section>

    <!-- COACHES (rendered by JS) -->
    <section class="section section--deep">
      <p class="eyebrow">The coaches</p>
      <h2 class="section__title">Trained by the best.</h2>
      <div class="coaches" id="coach-grid"></div>
      <p class="placeholder-note">Placeholder — real headshots go here. Names announced closer to launch.</p>
    </section>

    <!-- RESULTS (rendered by JS) -->
    <section class="section section--base">
      <p class="eyebrow">Results</p>
      <h2 class="section__title">What parents are saying.</h2>
      <div id="results-block"></div>
    </section>

    <!-- SCHEDULE & PRICING -->
    <section class="section section--elevated">
      <p class="eyebrow">Schedule &amp; pricing</p>
      <h2 class="section__title">Two tiers. One model.</h2>
      <p class="section__sub">Pick the one that fits your athlete.</p>
      <div class="pricing">
        <article class="price-card">
          <span class="price-card__badge">Jr High · 7th–8th</span>
          <h3 class="price-card__name">Group cohort</h3>
          <div class="price-card__price">$650<span class="price-card__period">/mo</span></div>
          <p class="price-card__desc">4 days/week. Cap of 25.</p>
          <ul class="price-card__features">
            <li>Mon–Thurs, 8–10am or 10am–12pm</li>
            <li>Full pillar curriculum</li>
            <li>Hybrid school schedule</li>
          </ul>
        </article>
        <article class="price-card price-card--featured">
          <p class="price-card__pop-label">★ PREMIUM TIER</p>
          <span class="price-card__badge">High School · 9th–12th</span>
          <h3 class="price-card__name">Dedicated coach</h3>
          <div class="price-card__price">$950<span class="price-card__period">/mo</span></div>
          <p class="price-card__desc">Small groups, custom plan.</p>
          <ul class="price-card__features">
            <li>Custom schedule around A/B day</li>
            <li>1-on-1 and small groups (2–3)</li>
            <li>Dedicated HS coach</li>
            <li>Monitored self-directed sessions</li>
          </ul>
        </article>
      </div>
      <div class="included-strip">
        <p class="included-strip__heading">Included with every academy membership</p>
        <p class="included-strip__body">Full gym access (5am–midnight, Mon–Sat) · Shot Lab access · All large-group trainings · Family Pass for siblings</p>
      </div>
    </section>

    <!-- FAQ (rendered by JS) -->
    <section class="section section--base">
      <p class="eyebrow">FAQ</p>
      <h2 class="section__title">Frequently asked.</h2>
      <div class="faq" id="faq-list"></div>
    </section>

    <!-- INTEREST FORM -->
    <section class="section section--elevated" id="interest">
      <p class="eyebrow">Other sports</p>
      <h2 class="section__title">Be first to know.</h2>
      <p class="interest-form__copy">We're expanding the academy model into more sports. Tell us what your athlete plays and we'll let you know the moment registration opens.</p>
      <!-- Phase 3: Replace inline form with Kit native embed -->
      <form class="interest-form" data-form="interest-capture">
        <div class="interest-form__row">
          <input type="text" name="name" placeholder="Your name" required autocomplete="name" />
          <input type="email" name="email" placeholder="Email" required autocomplete="email" />
          <input type="text" name="grade" placeholder="Athlete's grade" />
          <select name="sport_interest" required>
            <option value="">Sport of interest</option>
            <option value="football">Football</option>
            <option value="baseball">Baseball</option>
            <option value="lacrosse">Lacrosse</option>
            <option value="junior_academy">Junior Academy (3rd–5th)</option>
            <option value="other">Something else</option>
          </select>
        </div>
        <button type="submit" class="interest-form__submit">Notify me →</button>
      </form>
    </section>

    <!-- FINAL CTA / BOOK A CALL -->
    <section class="final-cta" id="book-a-call">
      <p class="eyebrow">Ready to talk?</p>
      <h2 class="section__title">Book a call.</h2>
      <p>Give us your info and we'll reach out. We'll learn about your athlete, answer your questions, and help you figure out if the academy is the right fit.</p>
      <!-- Phase 3: Replace this anchor with Kit form modal or inline embed -->
      <a href="#book-form-placeholder" class="btn btn--primary">Book a Call</a>
    </section>

  </main>

  <!-- FOOTER -->
  <footer class="footer">
    <div class="footer__row">
      <div class="footer__brand">
        <img src="{asset}images/logos/TZ_Horizontal_Lockup_White.svg" alt="Training Zone" class="footer__logo" />
        <span class="footer__brand-text">LOVE THE WORK</span>
      </div>
      <span class="footer__copy">© 2026 Training Zone. All rights reserved.</span>
    </div>
  </footer>

  <script src="{asset}js/sport-content.js"></script>
  <script>TZAcademy.init('{sport_key}');</script>
</body>
</html>
"""
    out_path = ROOT / cfg["out"]
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html, encoding="utf-8")
    print(f"  ✓ {cfg['out']}")


def main():
    print("Building TZ Academy pages...")
    for k, cfg in SPORTS.items():
        build_page(k, cfg)
    print("Done.")


if __name__ == "__main__":
    main()
