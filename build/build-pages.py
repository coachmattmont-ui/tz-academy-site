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
        "is_basketball": True,
    },
    "soccer": {
        "label": "Soccer",
        "url_path": "/soccer/",
        "out": "soccer/index.html",
        "asset_prefix": "../",
        "title": "TZ Academy — Soccer | Launching September 2026",
        "description": "Hybrid-school soccer academy in Herriman, Utah, launching September 2026. Led by former D1 player Nik Kizerian. 25 seats per cohort. Reserve yours now.",
        "hero_eyebrow": "SOCCER ACADEMY",
        "hero_accent": "SOCCER.",
        "og_image": "/images/og/soccer.jpg",
        "is_basketball": False,
        "launch_headline": "The Soccer Academy launches September.",
        "launch_body": "<strong>Nik Kizerian</strong>, former D1 college player, will be one of our featured Soccer Trainers. The Academy model — hybrid school, four-pillar training, capped at 25 athletes — comes to soccer this fall.",
        "coach_hero_image": "Nik-College.webp",
        "coach_hero_image_dir": "coaches",
        "coach_hero_alt": "Nik Kizerian playing college soccer",
        "training_dir": "soccer",
        "training_photos": [
            ("nik-training.webp", "Nik coaching young soccer players on the field"),
            ("emma-training.webp", "Young athlete dribbling through cones"),
            ("soccer-training.webp", "Soccer training session"),
        ],
    },
    "volleyball": {
        "label": "Volleyball",
        "url_path": "/volleyball/",
        "out": "volleyball/index.html",
        "asset_prefix": "../",
        "title": "TZ Academy — Volleyball | Launching September 2026",
        "description": "Hybrid-school volleyball academy in Herriman, Utah, launching September 2026. Led by former D1 player Jessica Finai. 25 seats per cohort. Reserve yours now.",
        "hero_eyebrow": "VOLLEYBALL ACADEMY",
        "hero_accent": "VOLLEYBALL.",
        "og_image": "/images/og/volleyball.jpg",
        "is_basketball": False,
        "launch_headline": "The Volleyball Academy launches September.",
        "launch_body": "<strong>Jessica Finai</strong>, former D1 college player and high school coach, will be leading the Volleyball Academy. The Academy model — hybrid school, four-pillar training, capped at 25 athletes — comes to volleyball this fall.",
        "coach_hero_image": "Jessica.webp",
        "coach_hero_image_dir": "coaches",
        "coach_hero_alt": "Jessica Finai mid-block at the net",
        "training_dir": "volleyball",
        "training_photos": [
            ("vball-training.webp", "Volleyball athlete in a defensive position"),
            ("vball-training-2.webp", "Volleyball athlete jumping for an attack"),
            ("jessica-college-2.webp", "Jessica Finai celebrating with college teammates"),
        ],
    },
}


def build_book_a_call_section():
    """The phone-call form. Same content regardless of page — used as the primary
    CTA on every page, but positioned differently:
    - Basketball: between Pricing and FAQ (right after the buyer sees price)
    - Soccer/Volleyball: at the bottom (after the launch section, as the only CTA)
    """
    return """
    <!-- BOOK A CALL -->
    <section class="final-cta" id="book-a-call">
      <p class="eyebrow">Ready to talk?</p>
      <h2 class="section__title">Book a call.</h2>
      <p class="final-cta__copy">Give us your info and we'll reach out. We'll learn about your athlete, answer your questions, and help you figure out if the academy is the right fit.</p>
      <form
        class="tz-form tz-form--cta formkit-form"
        action="https://app.kit.com/forms/9451557/subscriptions"
        method="post"
        data-tz-form="phone-call"
        data-sv-form="9451557"
        data-uid="273d13f418"
        data-format="inline"
        data-version="5"
        data-options='{{"settings":{{"after_subscribe":{{"action":"message","success_message":"Got it. We\u0027ll reach out at the time you mentioned — usually within one business day. Check your email to confirm.","redirect_url":""}}}},"version":"5"}}'
        min-width="400 500 600 700 800"
      >
        <div class="tz-form__grid">
          <label class="tz-form__field">
            <span class="tz-form__label">First name <span aria-hidden="true" class="tz-form__req">*</span></span>
            <input type="text" name="fields[first_name]" required autocomplete="given-name" placeholder="Your first name" />
          </label>
          <label class="tz-form__field">
            <span class="tz-form__label">Email <span aria-hidden="true" class="tz-form__req">*</span></span>
            <input type="email" name="email_address" required autocomplete="email" placeholder="you@example.com" />
          </label>
          <label class="tz-form__field">
            <span class="tz-form__label">Phone <span aria-hidden="true" class="tz-form__req">*</span></span>
            <input type="tel" name="fields[phone_number]" required autocomplete="tel" placeholder="(801) 555-0100" inputmode="tel" />
          </label>
          <label class="tz-form__field">
            <span class="tz-form__label">Sport of interest <span aria-hidden="true" class="tz-form__req">*</span></span>
            <select name="fields[sport_of_interest]" required>
              <option value="">Pick a sport</option>
              <option value="Basketball">Basketball</option>
              <option value="Soccer">Soccer</option>
              <option value="Volleyball">Volleyball</option>
            </select>
          </label>
          <label class="tz-form__field">
            <span class="tz-form__label">Athlete's grade</span>
            <input type="text" name="fields[athlete_s_grade]" placeholder="e.g. 7th, 11th" />
          </label>
          <label class="tz-form__field">
            <span class="tz-form__label">Best time to call</span>
            <input type="text" name="fields[best_time_to_call]" placeholder="Weekday evenings, mornings, etc." />
          </label>
        </div>
        <ul class="formkit-alert formkit-alert-error tz-form__kit-errors" data-element="errors" data-group="alert" hidden></ul>
        <button type="submit" class="tz-form__submit tz-form__submit--large formkit-submit" data-element="submit">
          <span class="tz-form__submit-label">Request a call →</span>
          <span class="tz-form__submit-spinner formkit-spinner" aria-hidden="true"><div></div><div></div><div></div></span>
        </button>
      </form>
    </section>
"""


def build_launch_section(cfg, asset):
    """Slim 'launching September' section for soccer/volleyball.

    Strategy: one bold launch headline + 1-2 line coach intro + coach hero photo +
    a small training-photo strip + urgency line + CTAs. The whole section sells
    'we're filling seats now for September' rather than 'coming soon, no info yet.'
    """
    sport_label = cfg["label"]
    photo_strip = "\n".join([
        f'<figure class="launch__photo-item"><img src="{asset}images/{cfg["training_dir"]}/{fn}" alt="{alt}" loading="lazy" /></figure>'
        for fn, alt in cfg["training_photos"]
    ])
    return f"""
    <!-- LAUNCH SECTION (soccer/volleyball) — actively selling for September -->
    <section class="section section--elevated" id="launch">
      <div class="launch">
        <div class="launch__intro">
          <p class="eyebrow">Launching September 2026</p>
          <h2 class="section__title">{cfg['launch_headline']}</h2>
          <p class="launch__body">{cfg['launch_body']}</p>
        </div>
        <div class="launch__coach-photo">
          <img src="{asset}images/{cfg['coach_hero_image_dir']}/{cfg['coach_hero_image']}" alt="{cfg['coach_hero_alt']}" loading="lazy" />
        </div>
      </div>

      <div class="launch__urgency">
        <p class="launch__urgency-line">We have 25 seats. <strong>We're filling them now.</strong></p>
        <p class="launch__urgency-sub">If you wait until September, you'll be on a waitlist for 2027.</p>
        <div class="launch__ctas">
          <a href="#book-a-call" class="btn btn--primary">Book a Call</a>
          <a href="/" class="btn btn--secondary">See how the Academy works →</a>
        </div>
      </div>

      <div class="launch__photo-strip" aria-label="{sport_label} training">
        {photo_strip}
      </div>
    </section>
"""


def build_page(sport_key, cfg):
    asset = cfg["asset_prefix"]
    is_bb = cfg.get("is_basketball", False)
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
  <meta property="og:url" content="https://academy.trainingzoneutah.com{cfg['url_path']}" />
  <meta property="og:image" content="https://academy.trainingzoneutah.com{cfg['og_image']}" />
  <meta name="twitter:card" content="summary_large_image" />

  <link rel="icon" type="image/svg+xml" href="{asset}images/logos/TZ_Logomark_White.svg" />
  <link rel="stylesheet" href="{asset}css/styles.css" />
  <script src="https://f.convertkit.com/ckjs/ck.5.js" async></script>
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
    <a href="/" class="nav__brand" aria-label="Academy home">
      <img src="{asset}images/logos/TZ_Horizontal_Lockup_White.svg" alt="Training Zone" class="nav__logo" />
    </a>
    <a href="#book-a-call" class="nav__cta">Book a Call →</a>
  </nav>

  <main id="main">

    <!-- HERO -->
    <section class="hero">
      <div class="hero__grid">
        <div class="hero__copy">
          <p class="eyebrow">{cfg['hero_eyebrow']}</p>
          <h1 class="hero__title">TRAIN LIKE A <span class="hero__title-accent">PRO.</span><br />STILL BE A KID.</h1>
          <p class="hero__sub">A different way to train serious young athletes — built around your school day, not against it. Daily individual coaching, live game work, mental performance, and strength training, all in one program.</p>
          <div class="hero__ctas">
            <a href="#book-a-call" class="btn btn--primary">Book a Call</a>
            <a href="#model" class="btn btn--secondary">How It Works</a>
          </div>
          <div class="hero__stats">
            <div class="stat" id="countdown-stat" data-countdown-target="2026-09-01T00:00:00-06:00">
              <div class="stat__num" id="countdown-num">—</div>
              <div class="stat__label" id="countdown-label">Days to Year 2</div>
            </div>
            <div class="stat">
              <div class="stat__num">25</div>
              <div class="stat__label">Per Cohort</div>
            </div>
            <div class="stat">
              <div class="stat__num">4</div>
              <div class="stat__label">Days a Week</div>
            </div>
          </div>
        </div>
        <div class="hero__media">
          <img
            src="{asset}images/hero/academy-year-two.webp"
            alt="TZ Academy athletes — soccer, basketball, baseball, and volleyball players in action with sport-color glow effects. Tagline: Academy Year 2 Starts 9.01."
            class="hero__image"
            width="2400"
            height="1500"
            fetchpriority="high"
          />
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
"""

    # ===== MAIN CONTENT (basketball gets the full academy story; soccer/vball get the slim launch section) =====
    if is_bb:
        html += f"""
    <!-- WHO IT'S FOR -->
    <section class="section section--elevated" id="who">
      <p class="eyebrow">Who it's for</p>
      <h2 class="section__title">Built for serious athletes.</h2>
      <p class="section__sub">Two age groups. Same standard.</p>
      <div class="cohort-grid">
        <article class="cohort-card">
          <div class="cohort-card__photo">
            <img src="{asset}images/cohorts/junior-high.webp" alt="Junior High athletes training" loading="lazy" />
          </div>
          <div class="cohort-card__body">
            <p class="card__eyebrow">7–9th Grade</p>
            <h3 class="card__title">Junior High</h3>
            <p class="card__body">Train 8–10am or 10am–12pm, four days a week with a hybrid school schedule. Cap of 25 athletes.</p>
          </div>
        </article>
        <article class="cohort-card">
          <div class="cohort-card__photo">
            <img src="{asset}images/cohorts/high-school.webp" alt="High School athlete in 1-on-1 coaching" loading="lazy" />
          </div>
          <div class="cohort-card__body">
            <p class="card__eyebrow">10–12th Grade</p>
            <h3 class="card__title">High School</h3>
            <p class="card__body">Custom schedule built around your A/B day. 1-on-1 training, custom programming, and small group (3–6) live work. Cap of 25.</p>
          </div>
        </article>
      </div>
    </section>

    <!-- ORIGIN STORY — built it for Kaylee first -->
    <section class="section section--deep" id="origin">
      <p class="eyebrow">How this started</p>
      <h2 class="section__title">Has to be a better way.</h2>
      <div class="origin">
        <div class="origin__photo">
          <img src="{asset}images/origin/kaylee.webp" alt="Kaylee Montgomery being introduced as a starter for the Sentinels" loading="lazy" />
        </div>
        <div class="origin__story">
          <p>Kaylee was a 7th grader competing at a top level in both soccer and basketball. We watched her run out of hours in the day — training, school, recovery, family time, friends. The traditional schedule wasn\u2019t built for it.</p>
          <p>So we built her a different week. Hybrid school. Mornings in the gym. Afternoons in class. Evenings free for homework, family, and being a kid. We tested it with her for three years before opening the academy.</p>
          <div class="origin__result">
            <p class="origin__result-label">Junior year, age 17</p>
            <p class="origin__result-body">First Team All-State <strong>in both soccer and basketball.</strong></p>
          </div>
          <div class="origin__result">
            <p class="origin__result-label">Now</p>
            <p class="origin__result-body">Has <strong>college offers to play at the next level.</strong></p>
          </div>
          <p class="origin__bridge">We just wrapped year one of the Academy with the same model. Same results.</p>
        </div>
      </div>
    </section>

    <!-- THE ACADEMY MODEL -->
    <section class="section section--base" id="model">
      <p class="eyebrow">The academy model</p>
      <h2 class="section__title">More training. More sleep.<br /><span class="hero__title-accent">Still a kid.</span></h2>
      <div class="model__copy">
        <p>The lie they tell you is that to be great — to chase real dreams — your athlete has to sacrifice the rest of their childhood.</p>
        <p>There's actually another way. Our athletes love it.</p>
        <p>With the Academy, your athlete still has time for all the things that matter — even a little extra sleep. Our athletes use a hybrid school schedule, taking some classes on campus and some online through their district. They train during the school day, when their mind and energy are fresh. Evenings stay open.</p>
        <p class="model__copy-list">Time to be a kid. Time to excel in multiple sports. Time to keep up academically. Time for church or youth groups, and time for family.</p>
        <p class="model__copy-close">Once you come to the Academy, you'll wonder why you didn't start sooner.</p>
      </div>
      <div class="schedule">
        <p class="schedule__label">A typical Junior High week</p>
        <div class="schedule__grid">
          <div class="schedule__block schedule__block--accent">
            <p class="schedule__when">Mon–Thurs AM</p>
            <p class="schedule__what">Academy training</p>
          </div>
          <div class="schedule__block">
            <p class="schedule__when">Afternoons</p>
            <p class="schedule__what">On-campus core classes</p>
          </div>
          <div class="schedule__block">
            <p class="schedule__when">Evenings</p>
            <p class="schedule__what">Homework, family, rest</p>
          </div>
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

    <!-- 2025/26 TEAM — the actual people, framed seasonally -->
    <section class="section section--deep" id="team-section">
      <p class="eyebrow">2025/26 Team</p>
      <h2 class="section__title">Meet the coaches.</h2>
      <p class="section__sub">D1, pro, and semi-pro playing experience. 20+ years of combined youth training.</p>
      <div class="team" id="team-grid"></div>
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
          <span class="price-card__badge">7–9th Grade</span>
          <h3 class="price-card__name">Junior High</h3>
          <div class="price-card__price">$650<span class="price-card__period">/mo</span></div>
          <p class="price-card__desc">4 days/week. Cap of 25.</p>
          <ul class="price-card__features">
            <li>Mon–Thurs, 8–10am or 10am–12pm</li>
            <li>Full pillar curriculum</li>
            <li>Hybrid school schedule</li>
          </ul>
        </article>
        <article class="price-card">
          <span class="price-card__badge">10–12th Grade</span>
          <h3 class="price-card__name">High School</h3>
          <div class="price-card__price">$950<span class="price-card__period">/mo</span></div>
          <p class="price-card__desc">Small groups, custom plan.</p>
          <ul class="price-card__features">
            <li>Custom schedule around A/B day</li>
            <li>1-on-1 training and small groups (3–6)</li>
            <li>Dedicated HS coach</li>
            <li>Monitored self-directed sessions</li>
          </ul>
        </article>
      </div>
      <div class="included-strip">
        <p class="included-strip__heading">Included with every academy membership</p>
        <p class="included-strip__body">Full gym access (5am–midnight, Mon–Sat) · Shot Lab access · All large-group trainings · Family Pass for siblings</p>
      </div>
      <div class="pricing__cta-jump">
        <a href="#book-a-call" class="btn btn--primary">Book a Call</a>
      </div>
    </section>
"""

        # Book a Call sits right after pricing on the basketball page —
        # immediately convertible after the buyer sees the price.
        html += build_book_a_call_section()

        html += """
    <!-- FAQ (rendered by JS) -->
    <section class="section section--base">
      <p class="eyebrow">FAQ</p>
      <h2 class="section__title">Frequently asked.</h2>
      <div class="faq" id="faq-list"></div>
    </section>

    <!-- INTEREST FORM (Waiting List) -->
    <section class="section section--elevated" id="interest">
      <p class="eyebrow">Other sports</p>
      <h2 class="section__title">Be first to know.</h2>
      <p class="interest-form__copy">We're expanding the academy model into more sports. Tell us what your athlete plays and we'll let you know the moment registration opens.</p>
"""
    else:
        # Soccer / Volleyball: slim launch section, skip cohorts/origin/model/pillars/team/results/pricing/FAQ
        html += build_launch_section(cfg, asset)

    # ===== BOTTOM: phone form + footer (shared by all pages) =====
    # Note: for basketball the interest form is still open above; we close it here.
    if is_bb:
        html += f"""
      <form
        class="tz-form formkit-form"
        action="https://app.kit.com/forms/9451552/subscriptions"
        method="post"
        data-tz-form="waiting-list"
        data-sv-form="9451552"
        data-uid="dea8684d64"
        data-format="inline"
        data-version="5"
        data-options='{{"settings":{{"after_subscribe":{{"action":"message","success_message":"You\u0027re on the list. Check your email to confirm your subscription.","redirect_url":""}}}},"version":"5"}}'
        min-width="400 500 600 700 800"
      >
        <div class="tz-form__grid">
          <label class="tz-form__field">
            <span class="tz-form__label">Email <span aria-hidden="true" class="tz-form__req">*</span></span>
            <input type="email" name="email_address" required autocomplete="email" placeholder="you@example.com" />
          </label>
          <label class="tz-form__field">
            <span class="tz-form__label">First name</span>
            <input type="text" name="fields[first_name]" autocomplete="given-name" placeholder="Your first name" />
          </label>
          <label class="tz-form__field">
            <span class="tz-form__label">Athlete's grade</span>
            <input type="text" name="fields[athlete_s_grade]" placeholder="e.g. 5th, 8th, 10th" />
          </label>
          <label class="tz-form__field">
            <span class="tz-form__label">Sport of interest</span>
            <select name="fields[sport_of_interest]">
              <option value="">Pick a sport</option>
              <option value="Football">Football</option>
              <option value="Baseball">Baseball</option>
              <option value="Lacrosse">Lacrosse</option>
              <option value="Junior Academy (3rd–5th)">Junior Academy (3rd–5th)</option>
              <option value="Other">Something else</option>
            </select>
          </label>
        </div>
        <ul class="formkit-alert formkit-alert-error tz-form__kit-errors" data-element="errors" data-group="alert" hidden></ul>
        <button type="submit" class="tz-form__submit formkit-submit" data-element="submit">
          <span class="tz-form__submit-label">Notify me →</span>
          <span class="tz-form__submit-spinner formkit-spinner" aria-hidden="true"><div></div><div></div><div></div></span>
        </button>
      </form>
    </section>
"""

    # ===== PHONE CALL FORM (soccer/volleyball only — basketball got it
    # earlier, between pricing and FAQ) =====
    if not is_bb:
        html += build_book_a_call_section()

    # ===== FOOTER (shared) =====
    html += f"""
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
