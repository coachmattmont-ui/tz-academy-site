/* ========================================================================
   TZ Academy — Sport Content Renderer
   Each page (/, /soccer/, /volleyball/) calls TZAcademy.init('basketball'|'soccer'|'volleyball')
   ======================================================================== */

(function () {
  'use strict';

  const SPORT_DATA = {
    basketball: {
      label: 'Basketball',
      emoji: '🏀',
      color: '#F58030',
      url: '/',
      heroAccent: 'BASKETBALL ACADEMY',
      pillars: [
        {
          icon: '🎯',
          title: 'Individual skill',
          body: 'Day-one evaluation. Custom plan covering handle, footwork, finishing, and shot mechanics — including dedicated time in the Shot Lab with our shooting coach.'
        },
        {
          icon: '🧠',
          title: 'Game IQ & reads',
          body: 'Daily 1v1, 3v3, and 5v5 game work. Film study. Athletes practice reading the game in real time, not just drilling in isolation.'
        },
        {
          icon: '⚡',
          title: 'Mental performance',
          body: 'Weekly work with sports performance coach Dr. Bobby Low. Focus, composure, confidence under pressure.'
        },
        {
          icon: '💨',
          title: 'Strength & speed',
          body: 'Athletic foundation built for basketball. Movement patterns, speed, strength, and mobility that transfer to the court.'
        }
      ],
      coaches: [
        { initials: 'HC', name: 'Head Coach', role: 'Basketball' },
        { initials: 'HS', name: 'High School Coach', role: 'HS Academy' },
        { initials: 'SC', name: 'Shooting Coach', role: 'Shot Lab' },
        { initials: 'BL', name: 'Dr. Bobby Low', role: 'Mental Performance' }
      ],
      testimonial: {
        quote: "This is the best decision we've made for our son.",
        attr: 'Tom, academy parent'
      },
      faq: [
        {
          q: 'What actually happens at the academy?',
          a: "Day one is an evaluation. From there, every athlete gets an individual program. Each day blends individual skill, group game work, and rotating mental performance and strength sessions."
        },
        {
          q: 'How does hybrid school actually work?',
          a: "Your athlete takes some classes on campus and some online through your district. Most families keep core classes on campus and move electives online. We'll walk you through the counselor conversation on your call."
        },
        {
          q: 'Why does High School cost more?',
          a: "HS athletes get a dedicated coach working with them 1-on-1 or in small groups of 2–3, plus custom programming built around their A/B day schedule. It's a more personalized model than the Junior High cohort."
        },
        {
          q: 'Is this the right fit for my athlete?',
          a: "The academy is for athletes who've played competitive ball, have real goals, and have shown focus to train at a high level. If your athlete has never played comp or struggles to focus through a workout, we can point you to a better starting place."
        },
        {
          q: 'What if we already have a TZ membership?',
          a: "You'll be upgraded to the Academy Membership — our top tier. Includes a Family Pass so siblings can still attend large-group trainings."
        },
        {
          q: 'Why is there a cap of 25?',
          a: "Because individual coaching and real feedback don't scale past that. We'd rather run multiple cohorts than dilute coaching."
        }
      ]
    },

    soccer: {
      label: 'Soccer',
      emoji: '⚽',
      color: '#8DC864',
      url: '/soccer/',
      heroAccent: 'SOCCER ACADEMY',
      pillars: [
        {
          icon: '🎯',
          title: 'Individual skill',
          body: 'Day-one evaluation. Custom plan covering first touch, footwork, ball control under pressure, finishing, and passing in tight spaces. Position-specific work — defenders, midfielders, and attackers train differently.'
        },
        {
          icon: '🧠',
          title: 'Game IQ & reads',
          body: 'Daily small-sided games — 1v1, 3v3, and 5v5 in tight space. Film study of pro and college matches. Athletes learn to scan and decide before the ball arrives.'
        },
        {
          icon: '⚡',
          title: 'Mental performance',
          body: 'Weekly work with sports performance coach Dr. Bobby Low. Focus through 90 minutes. Composure after a mistake. Confidence to demand the ball when it matters.'
        },
        {
          icon: '💨',
          title: 'Strength & speed',
          body: 'Soccer-specific athletic development. Repeat sprint capacity, change of direction, deceleration, and the lower-body strength that protects against common youth injuries.'
        }
      ],
      coaches: [
        { initials: 'HC', name: 'Head Coach', role: 'Soccer' },
        { initials: 'HS', name: 'High School Coach', role: 'HS Academy' },
        { initials: 'SK', name: 'Skills Coach', role: 'Position Work' },
        { initials: 'BL', name: 'Dr. Bobby Low', role: 'Mental Performance' }
      ],
      testimonial: null,
      comingSoonMessage: 'Launching September 2026. Be one of our founding athletes.',
      faq: [
        {
          q: 'What actually happens at the academy?',
          a: "Day one is an evaluation. From there, every athlete gets an individual program. Each day blends individual skill, group game work, and rotating mental performance and strength sessions."
        },
        {
          q: 'How does hybrid school actually work?',
          a: "Your athlete takes some classes on campus and some online through your district. Most families keep core classes on campus and move electives online. We'll walk you through the counselor conversation on your call."
        },
        {
          q: 'When does soccer actually start?',
          a: "September 2026. We're enrolling our first cohort now. Founding athletes lock in launch pricing and get first pick of training slots."
        },
        {
          q: 'Why does High School cost more?',
          a: "HS athletes get a dedicated coach working with them 1-on-1 or in small groups of 2–3, plus custom programming built around their A/B day schedule. It's a more personalized model than the Junior High cohort."
        },
        {
          q: 'Is this the right fit for my athlete?',
          a: "The academy is for athletes who've played competitive soccer, have real goals (club, ECNL, college), and have shown focus to train at a high level. If your athlete is brand new to the sport, we can point you to a better starting place."
        },
        {
          q: 'Why is there a cap of 25?',
          a: "Because individual coaching and real feedback don't scale past that. We'd rather run multiple cohorts than dilute coaching."
        }
      ]
    },

    volleyball: {
      label: 'Volleyball',
      emoji: '🏐',
      color: '#4DC9F5',
      url: '/volleyball/',
      heroAccent: 'VOLLEYBALL ACADEMY',
      pillars: [
        {
          icon: '🎯',
          title: 'Individual skill',
          body: 'Day-one evaluation. Custom plan covering passing, setting, hitting approach, swing mechanics, blocking, and serve. Position-specific work — outsides, middles, setters, and liberos get different programs from day one.'
        },
        {
          icon: '🧠',
          title: 'Game IQ & reads',
          body: 'Daily live rep work — 6v6 play, situational drills, serve-receive scenarios. Athletes learn to read the hitter, anticipate the set, and recognize block timing.'
        },
        {
          icon: '⚡',
          title: 'Mental performance',
          body: 'Weekly work with sports performance coach Dr. Bobby Low. Focus point-to-point. Composure after an error. Confidence to take the big swing in the big moment.'
        },
        {
          icon: '💨',
          title: 'Strength & speed',
          body: 'Volleyball-specific athletic development. Vertical jump, repeat jump capacity, shoulder health, core stability, and the explosive patterns that show up on every contact.'
        }
      ],
      coaches: [
        { initials: 'HC', name: 'Head Coach', role: 'Volleyball' },
        { initials: 'HS', name: 'High School Coach', role: 'HS Academy' },
        { initials: 'SK', name: 'Skills Coach', role: 'Position Work' },
        { initials: 'BL', name: 'Dr. Bobby Low', role: 'Mental Performance' }
      ],
      testimonial: null,
      comingSoonMessage: 'Launching September 2026. Be one of our founding athletes.',
      faq: [
        {
          q: 'What actually happens at the academy?',
          a: "Day one is an evaluation. From there, every athlete gets an individual program. Each day blends individual skill, group game work, and rotating mental performance and strength sessions."
        },
        {
          q: 'How does hybrid school actually work?',
          a: "Your athlete takes some classes on campus and some online through your district. Most families keep core classes on campus and move electives online. We'll walk you through the counselor conversation on your call."
        },
        {
          q: 'When does volleyball actually start?',
          a: "September 2026. We're enrolling our first cohort now. Founding athletes lock in launch pricing and get first pick of training slots."
        },
        {
          q: 'Why does High School cost more?',
          a: "HS athletes get a dedicated coach working with them 1-on-1 or in small groups of 2–3, plus custom programming built around their A/B day schedule. It's a more personalized model than the Junior High cohort."
        },
        {
          q: 'Is this the right fit for my athlete?',
          a: "The academy is for athletes who've played competitive volleyball, have real goals (club, college, beyond), and have shown focus to train at a high level. If your athlete is brand new to the sport, we can point you to a better starting place."
        },
        {
          q: 'Why is there a cap of 25?',
          a: "Because individual coaching and real feedback don't scale past that. We'd rather run multiple cohorts than dilute coaching."
        }
      ]
    }
  };

  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c];
    });
  }

  function renderPillars(data) {
    const grid = document.getElementById('pillar-grid');
    if (!grid) return;
    grid.innerHTML = data.pillars.map(function (p) {
      return (
        '<article class="card pillar">' +
          '<div class="pillar__icon" aria-hidden="true">' + p.icon + '</div>' +
          '<h3 class="pillar__title">' + escapeHtml(p.title) + '</h3>' +
          '<p class="pillar__body">' + escapeHtml(p.body) + '</p>' +
        '</article>'
      );
    }).join('');
  }

  function renderCoaches(data) {
    const grid = document.getElementById('coach-grid');
    if (!grid) return;
    grid.innerHTML = data.coaches.map(function (c) {
      return (
        '<div class="coach">' +
          '<div class="coach__avatar" aria-hidden="true">' + escapeHtml(c.initials) + '</div>' +
          '<div class="coach__name">' + escapeHtml(c.name) + '</div>' +
          '<div class="coach__role">' + escapeHtml(c.role) + '</div>' +
        '</div>'
      );
    }).join('');
  }

  function renderResults(data) {
    const block = document.getElementById('results-block');
    if (!block) return;
    if (data.testimonial) {
      block.innerHTML = (
        '<blockquote class="testimonial">' +
          '<p class="testimonial__quote">&ldquo;' + escapeHtml(data.testimonial.quote) + '&rdquo;</p>' +
          '<footer class="testimonial__attr">— ' + escapeHtml(data.testimonial.attr.toUpperCase()) + '</footer>' +
        '</blockquote>' +
        '<p class="placeholder-note">Placeholder — video testimonial + parent screenshots go here.</p>'
      );
    } else {
      block.innerHTML = (
        '<div class="results-coming-soon">' +
          '<p>' + escapeHtml(data.comingSoonMessage) + '</p>' +
        '</div>'
      );
    }
  }

  function renderFAQ(data) {
    const wrap = document.getElementById('faq-list');
    if (!wrap) return;
    wrap.innerHTML = data.faq.map(function (item) {
      return (
        '<details class="faq__item">' +
          '<summary>' + escapeHtml(item.q) + '</summary>' +
          '<p>' + escapeHtml(item.a) + '</p>' +
        '</details>'
      );
    }).join('');
  }

  function wireSportTabs(currentSport) {
    const tabs = document.querySelectorAll('.sport-tab');
    tabs.forEach(function (tab) {
      const s = tab.dataset.sport;
      if (s === currentSport) {
        tab.classList.add('is-active');
        tab.setAttribute('aria-current', 'page');
      } else {
        tab.classList.remove('is-active');
        tab.removeAttribute('aria-current');
      }
      tab.addEventListener('click', function () {
        const data = SPORT_DATA[s];
        if (data && data.url) window.location.href = data.url;
      });
    });
  }

  function init(sport) {
    const data = SPORT_DATA[sport];
    if (!data) {
      console.error('Unknown sport:', sport);
      return;
    }
    document.body.dataset.sport = sport;
    renderPillars(data);
    renderCoaches(data);
    renderResults(data);
    renderFAQ(data);
    wireSportTabs(sport);
  }

  // Mobile nav toggle (works on every page)
  function wireMobileNav() {
    const toggle = document.querySelector('.nav__menu-toggle');
    const links = document.querySelector('.nav__links');
    if (!toggle || !links) return;
    toggle.addEventListener('click', function () {
      const isOpen = links.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', String(isOpen));
    });
  }

  // Kit form submission is handled by ck.5.js (loaded in <head>).
  // The script binds to forms with class .formkit-form, reads data-uid/data-sv-form,
  // intercepts submit, POSTs to Kit's internal endpoint with proper auth tokens,
  // shows the data-options.success_message on success, and writes errors into
  // the [data-element="errors"] list.
  //
  // Don't add a fetch handler here — Kit's JS would conflict with it.

  // Countdown to Year 2 launch (9/1/2026, Mountain Time)
  function wireCountdown() {
    const stat = document.getElementById('countdown-stat');
    const num = document.getElementById('countdown-num');
    const label = document.getElementById('countdown-label');
    if (!stat || !num || !label) return;

    const target = new Date(stat.dataset.countdownTarget).getTime();
    if (Number.isNaN(target)) return;

    function tick() {
      const now = Date.now();
      const diff = target - now;

      if (diff <= 0) {
        stat.classList.add('is-live');
        num.textContent = 'LIVE';
        label.textContent = 'Year 2 has begun';
        return;
      }

      const days = Math.floor(diff / (1000 * 60 * 60 * 24));
      const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));

      if (days >= 1) {
        num.textContent = String(days);
        label.textContent = days === 1 ? 'Day to Year 2' : 'Days to Year 2';
      } else {
        num.textContent = String(hours);
        label.textContent = hours === 1 ? 'Hour to Year 2' : 'Hours to Year 2';
      }
    }

    tick();
    // Update every 60s — sub-minute precision unnecessary for a date countdown
    setInterval(tick, 60000);
  }

  document.addEventListener('DOMContentLoaded', function () {
    wireMobileNav();
    wireCountdown();
  });

  window.TZAcademy = { init: init };
})();
