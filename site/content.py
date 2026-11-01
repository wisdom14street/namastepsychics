"""Namaste Psychics: Namaste Bookshop's psychic readers, explained by the kind of reading they give, with phone sessions for people outside NYC."""
import json, os
import engine as G
E = G.E
BUSINESS_TYPE = 'LocalBusiness'
THEME_COLOR = '#5a1630'
FONTS = 'https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@400;600;700&display=swap'
ORG_DESC = 'Namaste Psychics introduces the psychic, intuitive and mediumship readers of Namaste Bookshop in Manhattan, with sessions in person at 14th Street or over the phone.'
LLMS_NOTE = ('Namaste Psychics is a Wealth Edge Ventures Inc. brand connected to Namaste Bookshop, 2 West 14th Street, New York, where its readers work. '
             'Bookings and payments go through Namaste Bookshop\'s Square booking pages. Remote sessions are offered by phone.')
R = json.load(open(os.path.join(os.path.dirname(__file__), 'readers.json')))
TYPES = [
 ('clairvoyant', 'Clairvoyant readings', 'Clairvoyant', 'Readers who describe what they "see" as images or scenes while they read for you.',
  'In a clairvoyant session the reader describes impressions that come to them as pictures. Many of Namaste\'s clairvoyant readers also lay tarot cards, using the spread as a frame for what they pick up.',
  [('catherine-marks', 'Describes herself as a clairvoyant dimensional coach and conscious channel; reports psychic memories from early childhood.'),
   ('brinly-erin', 'Clairvoyant and clairaudient; many of her sessions center on self-worth, healing and confidence.'),
   ('andrea-dopewitchkira', 'Clairvoyant and claircognizant, with a background in anthropology and psychology she brings into the conversation.')]),
 ('clairaudient', 'Clairaudient readings', 'Clairaudient', 'Readers who work from what they "hear": words, phrases or a voice of guidance.',
  'Clairaudience is the sense of receiving information as sound or words. A clairaudient reader may pause, listen and then repeat a phrase that came through.',
  [('rebecca-martinez', 'Hears guidance while she reads the cards, and works in Spanish as easily as English.'),
   ('brinly-erin', 'Hears guides as well as seeing images; also reads on love, money, career and friendship.')]),
 ('mediumship', 'Mediumship', 'Mediumship', 'Sessions that reach toward loved ones who have passed, or toward spirit guides.',
  'A mediumship reading is aimed at messages from loved ones who have passed or from guides. It can be emotional, so many people prefer a longer session. No reader can promise that a particular person will come through.',
  [('catherine-marks', 'Works as a medium as well as a psychic tarot reader.'),
   ('lizanne', 'An intuitive medium for about ten years; begins with your question and blends cards with mediumship.'),
   ('sophia-strange', 'A psychic medium and poet; her Ancestral reading focuses on loved ones, and each session ends with a poem written for you.'),
   ('high-priestess-judith', 'Combines tarot, astrology and mediumship and works with spirit guides from the traditions she was initiated in.')]),
 ('astrology', 'Astrology readings', 'Astrology', 'Sessions built on a chart of the sky when you were born, and on where the planets sit now.',
  'An astrologer needs your birth date, and usually your birth time and city, to cast a chart. Expect a session about timing, themes and cycles more than yes-or-no answers.',
  [('priya', 'Comes from a family of astrologers, has two decades of client work behind her, and blends Eastern and Western charts; Chiron is her specialty.'),
   ('casey-deamoira', 'Hellenistic astrology combined with the Thoth tarot; natal readings or this-week transits.'),
   ('alexander-d-santiago', 'Reads both Western and Vedic charts, with gemstone, mantra or flower-essence suggestions.'),
   ('mychal-a-bryan', 'Teaches astrology through a school he started and has written books on traditional and medical astrology; his chart sessions last an hour.'),
   ('dainichi-lazuli', 'Vedic astrology alongside tarot, numerology, runes and aura readings.')]),
 ('oracle-and-lenormand', 'Oracle and Lenormand readings', 'Oracle & Lenormand', 'Card readings that use decks other than tarot.',
  'Each oracle deck invents its own cards and rules, so two oracle readings can feel nothing alike. Lenormand uses 36 small, literal cards that combine into short, concrete answers.',
  [('lu-camy', 'Reads with the Soul Synergy Oracle Deck, which she wrote and illustrated, focusing on patterns and subconscious emotions.'),
   ('mallika', 'Uses Lenormand for what is happening and tarot for why, in sessions she keeps non-judgmental and action-focused.')]),
 ('hypnosis-and-energy-work', 'Hypnosis and energy work', 'Hypnosis & energy', 'Sessions for people who want to work below the conscious mind rather than get a reading.',
  'These are not readings in the usual sense. Hypnotherapy uses guided relaxation and suggestion; energy cleansing is a short hands-off session. They are wellness practices, not medical treatment.',
  [('jennifer-shanteau', 'A certified hypnotherapist offering 75-minute hypnotherapy, including past-life and higher-self work, and a 15-minute energy cleansing.'),
   ('lu-camy', 'A clinical hypnotist; her hour-long hypnosis can focus on goals, letting go of old feelings, past lives or the inner child.')]),
]
NAV = [('/kinds-of-readings/', 'Kinds of readings'), ('/readers/', 'Readers'), ('/by-phone/', 'By phone'), ('/before-you-book/', 'Before you book')]

def shell(pg):
    nav = ''.join(f'<a href="{h}"' + (' class="on"' if pg['path'].startswith(h) else '') + f'>{t}</a>' for h, t in NAV)
    return (f'<body><a class="skip" href="#main">Skip to content</a><header class="hd"><a class="logo" href="/"><svg viewBox="0 0 40 40" aria-hidden="true"><circle cx="20" cy="20" r="17" fill="none" stroke="currentColor" stroke-width="2"/>'
            f'<path d="M6 20c5-7 23-7 28 0-5 7-23 7-28 0z" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="20" cy="20" r="4.5" fill="#e8a0b4"/></svg>Namaste Psychics</a>'
            f'<a class="call" href="tel:{G.TEL}">{G.PHONE}</a><nav class="nv" aria-label="Main">{nav}</nav></header>'
            f'<main id="main">{pg["body"]}</main>'
            f'<footer class="fo"><div><p class="logo2">Namaste Psychics</p><p>The psychic readers of Namaste Bookshop. In person at {G.ADDR}, or by phone.</p></div>'
            f'<div><p>Namaste Psychics is a Wealth Edge Ventures Inc. brand. Bookings are made with Namaste Bookshop.</p><p><a href="mailto:{G.EMAIL}">{G.EMAIL}</a> &middot; <a href="/about/">About</a> &middot; <a href="/privacy/">Privacy</a></p></div></footer>'
            f'<nav class="bar" aria-label="Quick actions"><a href="{G.BOOK}">Book</a><a href="/by-phone/">Phone session</a><a href="tel:{G.TEL}">Call shop</a></nav></body></html>')

def person(k, line):
    r = R[k]
    return (f'<li class="pr"><img src="{E(G.img(r["img"], 200))}" alt="{E(r["name"])}" width="72" height="72" loading="lazy"><div><b>{E(r["name"])}</b><span>{E(line)}</span>'
            f'<span class="fr">from ${r["from"]}' + (' &middot; phone sessions' if r['phone'] else '') + f'</span><a href="{E(r["book"])}">See times and book</a></div></li>')

def pages():
    home = (f'<section class="split"><div><p class="tag">Namaste Bookshop &middot; Manhattan</p><h1>Psychic readers you can meet in person or hear by phone</h1>'
            f'<p>Namaste Psychics is the home of the psychic, intuitive and mediumship readers who work at Namaste Bookshop on 14th Street. Read up on the kinds of readings they give, then choose how you want to sit with them.</p></div>'
            f'<div class="doors"><a class="door" href="{G.BOOK}"><b>In the shop</b><span>Take a seat at the shop a block from Union Square.</span></a>'
            f'<a class="door alt" href="/by-phone/"><b>On the phone</b><span>Book a phone session and your reader calls you, wherever you live.</span></a></div></section>'
            f'<section class="kinds"><h2>Six kinds of readings</h2><ul>' + ''.join(f'<li><a href="/kinds-of-readings/{t[0]}/"><b>{t[2]}</b><span>{t[3]}</span></a></li>' for t in TYPES) + '</ul></section>'
            f'<section class="honest"><h2>What a psychic reading is, and is not</h2><p>A reading can help you think through a relationship, a job or a loss with someone who listens differently. It cannot guarantee an outcome, '
            f'and it never replaces a doctor, lawyer, therapist or financial adviser. Every Namaste reader posts their prices before you book. <a href="/before-you-book/">More before you book</a>.</p></section>')
    G.add('/', 'Namaste Psychics | Psychic Readings in NYC & by Phone',
          'Psychic, clairvoyant, mediumship and astrology readings with Namaste Bookshop readers in Manhattan, or by phone from anywhere. See reading types and book online.', home,
          ld=[G.shop_ld('LocalBusiness')])
    idx = ('<section class="pg"><h1>Kinds of psychic readings</h1><p class="lead">Readers do not all work the same way. Some see, some hear, some read a chart. Knowing the difference makes it easier to pick someone.</p>'
           + ''.join(f'<article class="kt"><h2><a href="/kinds-of-readings/{t[0]}/">{t[1]}</a></h2><p>{t[3]}</p><p class="who">' + ', '.join(R[k]["name"] for k, _ in t[5]) + '</p></article>' for t in TYPES) + '</section>')
    G.add('/kinds-of-readings/', 'Types of Psychic Readings Explained | Namaste Psychics',
          'Clairvoyant, clairaudient, mediumship, astrology, oracle and Lenormand readings, plus hypnosis and energy work: how each works and which Namaste readers offer it.', idx,
          crumbs=[('Home', '/'), ('Kinds of readings', '/kinds-of-readings/')])
    for slug, title, short, one, para, people in TYPES:
        body = (f'<section class="pg"><p class="tag">Kinds of readings</p><h1>{title} at Namaste</h1><p class="lead">{one}</p><p>{para}</p>'
                f'<h2>Who offers it</h2><ul class="people">' + ''.join(person(k, l) for k, l in people) + '</ul>'
                f'<p class="note">Schedules change, so each booking button shows live open times on Namaste Bookshop\'s booking system.</p><p><a href="/kinds-of-readings/">All kinds of readings</a></p></section>')
        G.add(f'/kinds-of-readings/{slug}/', f'{title} in NYC with Namaste Bookshop Readers | Namaste Psychics',
              f'{one} Learn how {short.lower()} sessions work and see which Namaste Bookshop readers offer them.', body,
              crumbs=[('Home', '/'), ('Kinds of readings', '/kinds-of-readings/'), (title, f'/kinds-of-readings/{slug}/')])
    groups = [('Psychic and intuitive', ['catherine-marks', 'rebecca-martinez', 'brinly-erin', 'andrea-dopewitchkira']),
              ('Mediums', ['lizanne', 'sophia-strange', 'high-priestess-judith']),
              ('Astrologers', ['priya', 'casey-deamoira', 'alexander-d-santiago', 'mychal-a-bryan', 'dainichi-lazuli']),
              ('Oracle, Lenormand and hypnosis', ['lu-camy', 'mallika', 'jennifer-shanteau'])]
    lines = {k: l for t in TYPES for k, l in t[5]}
    rd = ('<section class="pg"><h1>Namaste\'s psychic readers</h1><p class="lead">All of them read at Namaste Bookshop. Readers marked "phone sessions" also take bookings by phone.</p>'
          + ''.join(f'<h2>{g}</h2><ul class="people">' + ''.join(person(k, lines[k]) for k in ks) + '</ul>' for g, ks in groups)
          + '<p class="note">Looking for someone not listed? Only readers taking bookings now appear here. Call the shop to ask about anyone else.</p></section>')
    G.add('/readers/', 'Psychic Readers, Mediums & Astrologers | Namaste Psychics',
          'Meet the psychic readers, mediums and astrologers who read at Namaste Bookshop in Manhattan, with starting prices and phone options.', rd,
          crumbs=[('Home', '/'), ('Readers', '/readers/')])
    phone_people = [k for k in R if R[k]['phone']]
    pf = [('Do phone readings cost more?', 'No. A reader charges the same for a call as for a seat at the table.'),
          ('Who calls whom?', 'The reader calls the number on your booking at the appointment time.'),
          ('What about video?', 'Remote readings are booked as phone sessions right now. If you would prefer video, ring ' + G.PHONE + ' to ask about it.'),
          ('Can I change the time?', 'The booking page asks for at least six hours\' notice to cancel or reschedule.')]
    ph = (f'<section class="pg"><h1>Psychic readings by phone</h1><p class="lead">Living outside the city is no barrier to a Namaste reader. Book a phone session, pay ahead, and your reader rings you at the time you picked.</p>'
          f'<ol class="steps"><li><b>Choose a reader</b> below.</li><li><b>Pick "Phone Session"</b> and a length: 15, 30, 45 or 60 minutes (not every reader offers every length).</li>'
          f'<li><b>Pay when you book.</b> Times show in your own time zone.</li><li><b>Pick up when they call.</b> A quiet room and a charged phone help.</li></ol>'
          f'<h2>Readers taking phone bookings</h2><ul class="people">' + ''.join(person(k, lines.get(k, 'Takes calls as well as in-shop sittings.')) for k in phone_people) + '</ul>'
          f'<h2>Phone session questions</h2><dl class="faq">' + ''.join(f'<dt>{q}</dt><dd>{a}</dd>' for q, a in pf) + '</dl>'
          f'<p><a class="cta" href="{G.PHONE_PAGE}">Open the phone booking page</a></p></section>')
    G.add('/by-phone/', 'Phone Psychic Readings with NYC Readers | Namaste Psychics',
          'Book a psychic or tarot reading by phone with a Namaste Bookshop reader. Same prices as in person; pay ahead and the reader calls you.', ph,
          ld=[G.faq_ld(pf)], crumbs=[('Home', '/'), ('By phone', '/by-phone/')])
    bq = [('How do I choose a reader?', 'Decide first what sort of session appeals to you. If you want images and impressions, try a clairvoyant; if you want timing and cycles, an astrologer; if you hope to hear from someone who has died, a medium.'),
          ('What should I bring?', 'A question or two, written down. For astrology, your birth date, time and city.'),
          ('What if something feels off?', 'You can end a session whenever you like. If you have a concern about a session afterward, contact the shop at ' + G.EMAIL + '.'),
          ('Are readings medical or legal advice?', 'No. A reading is for reflection and perspective. Health, legal, money and mental-health decisions belong with qualified professionals.')]
    bb = ('<section class="pg"><h1>Before you book a psychic reading</h1><p class="lead">A few honest notes so the session feels worth it.</p><dl class="faq">'
          + ''.join(f'<dt>{q}</dt><dd>{a}</dd>' for q, a in bq) + f'</dl><h2>Prices</h2><p>Most Namaste readers start around $35 for fifteen minutes. Some specialists charge more; for example, one-hour astrology sessions can run several hundred dollars. '
          f'Your total appears on the booking screen before any payment.</p><p><a class="cta" href="{G.BOOK}">See readers and open times</a></p></section>')
    G.add('/before-you-book/', 'Before You Book a Psychic Reading: Honest Answers | Namaste Psychics',
          'How to choose a psychic reader, what to bring, typical prices at Namaste Bookshop, and what a psychic reading cannot do.', bb,
          ld=[G.faq_ld(bq)], crumbs=[('Home', '/'), ('Before you book', '/before-you-book/')])
    G.add('/about/', 'About Namaste Psychics', 'Namaste Psychics is the psychic-reader brand of Namaste Bookshop, run by Wealth Edge Ventures Inc.',
          f'<section class="pg"><h1>About Namaste Psychics</h1><p>Namaste Psychics is a guide to the psychic and intuitive readers at Namaste Bookshop, {G.ADDR}. Behind it is Wealth Edge Ventures Inc., the bookshop\'s parent company.</p>'
          f'<p>Reader details are drawn from each reader\'s own page on namastebookshop.com. This site carries no star ratings and no client quotes.</p>'
          f'<p><a href="tel:{G.TEL}">{G.PHONE}</a> &middot; <a href="mailto:{G.EMAIL}">{G.EMAIL}</a></p></section>', crumbs=[('Home', '/'), ('About', '/about/')])
    G.add('/privacy/', 'Privacy | Namaste Psychics', 'Analytics and booking privacy on namastepsychics.com.',
          '<section class="pg">' + G.privacy('namastepsychics.com does not take payments or ask for personal details itself; it links you to booking pages.') + '</section>',
          crumbs=[('Home', '/'), ('Privacy', '/privacy/')])

NOTFOUND_DESC = 'Page not found on namastepsychics.com.'
NOTFOUND = '<section class="pg"><h1>We did not see that one coming</h1><p>This page is missing. Try <a href="/readers/">the readers</a> or <a href="/by-phone/">phone readings</a>.</p></section>'

CSS = """:root{--wine:#5a1630;--rose:#e8a0b4;--blush:#fbf3f1;--ink:#2a1a20}
*{box-sizing:border-box}body{margin:0;background:var(--blush);color:var(--ink);font:16px/1.65 'DM Sans',system-ui,sans-serif;padding-bottom:58px}a{color:#8c2450}
h1,h2{font-family:'DM Serif Display',Georgia,serif;font-weight:400;line-height:1.15;color:var(--wine)}h1{font-size:clamp(2rem,7vw,3rem);margin:.2em 0 .3em}
.skip{position:absolute;left:-999px}.skip:focus{left:6px;top:6px;background:#fff;padding:6px}
.hd{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;padding:12px 16px 0;background:var(--wine);color:#fff}
.logo{display:flex;align-items:center;gap:8px;color:#fff;text-decoration:none;font:1.35rem 'DM Serif Display',serif}.logo svg{width:32px;height:32px}
.call{color:var(--rose);font-weight:700;text-decoration:none}.nv{flex-basis:100%;display:flex;gap:18px;overflow-x:auto;padding:12px 0}.nv a{color:#f6dbe3;text-decoration:none;white-space:nowrap;font-weight:600;padding-bottom:4px}
.nv a.on{border-bottom:2px solid var(--rose);color:#fff}
main{max-width:1040px;margin:0 auto;padding:0 16px}
.split{display:grid;gap:20px;padding:26px 0}@media(min-width:820px){.split{grid-template-columns:1.2fr 1fr;align-items:center}}
.tag{text-transform:uppercase;letter-spacing:.14em;font-size:.74rem;font-weight:700;color:#a2486d;margin:0}
.doors{display:grid;gap:12px}.door{display:block;background:#fff;border-radius:18px;padding:18px;text-decoration:none;color:var(--ink);border:2px solid var(--wine)}.door b{display:block;font:1.4rem 'DM Serif Display',serif;color:var(--wine)}
.door.alt{background:var(--wine);color:#f6dbe3}.door.alt b{color:#fff}
.kinds ul{list-style:none;padding:0;display:grid;gap:10px}@media(min-width:700px){.kinds ul{grid-template-columns:repeat(3,1fr)}}
.kinds a{display:block;background:#fff;border-radius:14px;padding:14px;text-decoration:none;color:var(--ink);height:100%;border-bottom:4px solid var(--rose)}.kinds b{display:block;color:var(--wine);font-size:1.05rem}
.honest{background:#fff;border-left:6px solid var(--wine);padding:6px 18px 14px;border-radius:0 14px 14px 0;margin:26px 0}
.pg{max-width:780px;padding:18px 0 30px}.lead{font-size:1.12rem}.kt{border-bottom:1px solid #ecd6dc;padding:4px 0 10px}.who{color:#7a5562;font-size:.9rem}
.people{list-style:none;padding:0;display:grid;gap:10px}.pr{display:flex;gap:12px;background:#fff;border-radius:14px;padding:12px}.pr img{border-radius:12px;object-fit:cover;flex:none}
.pr div{display:flex;flex-direction:column;gap:2px}.pr b{color:var(--wine)}.fr{font-size:.86rem;color:#7a5562}.note{font-size:.9rem;color:#6a4b56}
.steps li{margin:.5em 0}.faq dt{font-weight:700;margin-top:.9em;color:var(--wine)}.faq dd{margin:.2em 0 0}
.cta{display:inline-block;background:var(--wine);color:#fff;padding:12px 20px;border-radius:99px;text-decoration:none;font-weight:700}
.fo{background:#3d0e20;color:#f0d5dd;padding:24px 16px;display:grid;gap:12px;margin-top:30px}.fo a{color:var(--rose)}.logo2{font:1.3rem 'DM Serif Display',serif;color:#fff;margin:0}@media(min-width:760px){.fo{grid-template-columns:1fr 1fr;padding:28px 6vw}}
.bar{position:fixed;left:0;right:0;bottom:0;display:flex;background:#fff;border-top:1px solid #e4c6cf;z-index:9}.bar a{flex:1;text-align:center;padding:14px 4px;font-weight:700;text-decoration:none;color:var(--wine)}.bar a:first-child{background:var(--wine);color:#fff}
@media(min-width:900px){.bar{display:none}body{padding-bottom:0}}
"""
