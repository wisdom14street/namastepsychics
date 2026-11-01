"""Namaste Psychics: a psychic reading practice in Manhattan, organized by the kind of reading each psychic gives, with phone sessions for people outside NYC."""
import json, os
import engine as G
E = G.E
BUSINESS_TYPE = 'LocalBusiness'
THEME_COLOR = '#5a1630'
FONTS = 'https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@400;600;700&display=swap'
ORG_DESC = 'Namaste Psychics is a team of psychic, intuitive and mediumship readers in Manhattan, giving sessions in person on West 14th Street or over the phone.'
LLMS_NOTE = ('Namaste Psychics is a psychic reading practice operated by Wealth Edge Ventures Inc. Its readers sit inside Namaste Bookshop, 2 West 14th Street, New York, and in Suite 1104 at 80 Fifth Avenue. '
             'Each psychic has a profile on this site; sessions are reserved through the reader\'s Square scheduling page. Remote sessions are offered by phone.')
R = json.load(open(os.path.join(os.path.dirname(__file__), 'readers.json')))
TYPES = [
 ('clairvoyant', 'Clairvoyant readings', 'Clairvoyant', 'Readers who describe what they "see" as images or scenes while they read for you.',
  'In a clairvoyant session the reader describes impressions that come to them as pictures. Several of our clairvoyant readers also lay tarot cards, using the spread as a frame for what they pick up.',
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
NAV = [('/kinds-of-readings/', 'Kinds of readings'), ('/readers/', 'Readers'), ('/by-phone/', 'By phone'), ('/tools/', 'Tools & books'), ('/before-you-book/', 'Before you book')]
CART = True
SHOP_PATH = '/tools/'
import re
import minishop as MS
BK = ('books', 'Books', 'Book', 'Spiritual Book')
COLLECTIONS = []
STYLES = []
KINDS = {'pendulum': ('Pendulum', 'Pendulums'), 'board': ('Pendulum board or dowsing rod', 'Boards & dowsing rods'), 'rune': ('Rune set', 'Runes'),
         'scry': ('Scrying tool', 'Scrying mirrors & crystal balls'), 'psybook': ('Psychic development book', 'Psychic & mediumship books'),
         'divbook': ('Divination book', 'Divination books'), 'astro': ('Astrology book', 'Astrology & numerology books')}
def SELECT(p, C):
    t = p['title']; ty = (p.get('product_type') or '').strip(); tl = t.lower()
    if re.search(r'wholesale|display of \d+', tl): return None
    if ty in ('Pendulum', 'Pendulum44.95') or (ty == '' and re.search(r'pendulum.*kit', tl)): return 'pendulum'
    if ty in ('Pendulum Board', 'Dowsing Rod'): return 'board'
    if ty in ('Runes', 'Rune Set') or (ty in ('Oracle Deck', 'Oracle Cards') and re.search(r'\brunes?\b', tl)): return 'rune'
    if ty in ('Scrying Mirror', 'Spirit Board') or (re.search(r'crystal ball|scrying', tl) and ty not in BK + ('Suncatchers', 'Incense Burner', 'Home Decor', 'Tarot Deck', 'Oracle Cards')): return 'scry'
    if ty in BK and 'tarot' not in tl:
        if re.search(r'astrolog|horoscope|birth ?chart|zodiac|\bplanets?\b|numerolog|sun signs?|moon signs?|natal|\bvedic|jyotish|\btransits?\b', tl): return 'astro'
        if re.search(r'pendulum|dowsing|\brunes?\b|i ching|palmistry|palm reading|tea leaf|tasseography|scrying|crystal ball|divination|\boracle\b|lenormand|dream (dictionary|symbol|interpret|meaning)', tl): return 'divbook'
        if re.search(r'psychic|medium(ship)?\b|clairvoy|clairaud|claircog|intuiti|empath|spirit guides?|afterlife|channel(ing|led)?\b|\baura|sixth sense|third eye|precognit|telepath|akashic|past lives?|spirit communication', tl): return 'psybook'
    return None
SHELVES = [('pendulums', '/tools/pendulums/', ('pendulum', 'board'), 'Pendulums', 'Pendulums and Pendulum Boards',
            'Crystal, metal and wood pendulums for yes-or-no questions, plus printed boards to swing them over and copper rods for dowsing.'),
           ('runes-and-scrying', '/tools/runes-and-scrying/', ('rune', 'scry'), 'Runes & scrying', 'Runes, Scrying Mirrors and Crystal Balls',
            'Stone rune sets and rune card decks for casting, black obsidian mirrors and crystal balls for gazing, and a spirit board.'),
           ('psychic-books', '/tools/psychic-development-books/', ('psybook',), 'Psychic & mediumship books', 'Books on Psychic Development and Mediumship',
            'Books for building your own intuition: clairvoyance, mediumship, auras, spirit guides, empaths and the Akashic records.'),
           ('divination-books', '/tools/divination-books/', ('divbook',), 'Divination books', 'Books on Pendulums, Runes and Other Divination',
            'How-to books for the methods beyond tarot: pendulums, runes, the I Ching, palmistry, tea leaves, crystal balls and dream symbols.'),
           ('astrology-books', '/tools/astrology-books/', ('astro',), 'Astrology & numerology', 'Astrology and Numerology Books',
            'Birth charts, transits, Vedic astrology and numerology, from first guides to the references our astrologers reach for.')]
def p_intro(x):
    k = x['kind']
    if k in ('pendulum', 'board'): return '<p class="pnote">New to pendulums? Hold the chain still, ask it to show you "yes", then "no", and note the swing before asking a real question.</p>'
    if k == 'astro': return '<p class="pnote">Want a chart read for you? Our <a href="/kinds-of-readings/astrology/">astrologers</a> take bookings in person and by phone.</p>'
    if k == 'psybook': return '<p class="pnote">Curious how a working reader does it? Book a session with one of our <a href="/readers/">psychics and mediums</a>.</p>'
    return '<p class="pnote">Each method has its own rules. If you would like to see one in use first, ask a reader during a <a href="/readers/">session</a>.</p>'
def tools_pages():
    return MS.build(SELECT, COLLECTIONS, STYLES, KINDS, SHELVES, '/tools/', 'Pendulums, Runes, Scrying Mirrors & Psychic Books | Namaste Psychics',
                    'Tools and books for practicing on your own: pendulums, rune sets, obsidian scrying mirrors, and books on psychic development, divination and astrology.',
                    'Tools and books for your own practice',
                    '<p>For people who want to practice between sessions: something to swing, cast or gaze into, and something to read. '
                    'Every item ships from New York City.</p>', p_intro, feature_kinds=('pendulum', 'rune', 'scry', 'psybook'), feat_h='Pendulums, runes and mirrors in stock',
                    note='Your cart stays on this site while you browse. Payment happens once, at a secure checkout run by Namaste Bookshop, which also ships the order.',
                    search=('Find a pendulum, stone or book', 'Look up a stone, a method or an author, such as amethyst, runes or mediumship.'))

def shell(pg):
    nav = ''.join(f'<a href="{h}"' + (' class="on"' if pg['path'].startswith(h) else '') + f'>{t}</a>' for h, t in NAV)
    return (f'<body><a class="skip" href="#main">Skip to content</a><header class="hd"><a class="logo" href="/"><svg viewBox="0 0 40 40" aria-hidden="true"><circle cx="20" cy="20" r="17" fill="none" stroke="currentColor" stroke-width="2"/>'
            f'<path d="M6 20c5-7 23-7 28 0-5 7-23 7-28 0z" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="20" cy="20" r="4.5" fill="#e8a0b4"/></svg>Namaste Psychics</a>'
            f'<span class="hr"><a class="call" href="tel:{G.TEL}">{G.PHONE}</a>{G.cart_button()}</span><nav class="nv" aria-label="Main">{nav}</nav></header>'
            f'<main id="main">{pg["body"]}</main>'
            f'<footer class="fo"><div><p class="logo2">Namaste Psychics</p><p>Psychic readings in person on West 14th Street, or by phone.</p></div>'
            f'<div><p>Sessions inside Namaste Bookshop, {G.ADDR}. Operated by Wealth Edge Ventures Inc.</p><p><a href="mailto:{G.EMAIL}">{G.EMAIL}</a> &middot; <a href="/about/">About</a> &middot; <a href="/privacy/">Privacy</a></p></div></footer>'
            f'<nav class="bar" aria-label="Quick actions"><a href="/readers/">Book</a><a href="/by-phone/">Phone session</a><a href="tel:{G.TEL}">Call</a></nav></body></html>')

def person(k, line):
    r = R[k]
    return (f'<li class="pr"><img src="{E(G.headshot(k, 200))}" alt="{E(r["name"])}" width="72" height="72" loading="lazy"><div><b>{E(r["name"])}</b><span>{E(line)}</span>'
            f'<span class="fr">from ${r["from"]}' + (' &middot; phone sessions' if r['phone'] else '') + f'</span><a href="/psychics/{k}/">Profile and booking</a></div></li>')

def profiles(lines):
    kinds = {}
    for t in TYPES:
        for k, _ in t[5]: kinds.setdefault(k, []).append((t[0], t[2]))
    for k in R:
        if R[k]['phone'] and k not in kinds: kinds[k] = []
    for k, ks in kinds.items():
        r = R[k]; first = r['name'].split()[0]
        where = {'upstairs': 'Sees clients in a private room at 80 Fifth Avenue, Suite 1104.', 'bookshop': f'Reads at a table inside Namaste Bookshop, {G.ADDR}.',
                 'remote': 'Reads remotely at the moment.', 'both': 'Splits the week between the Suite 1104 rooms and the 14th Street tables.'}[r['home']]
        body = (f'<section class="pg"><p class="tag">Psychic profile</p><div class="pf"><img src="{E(G.headshot(k, 400))}" alt="{E(r["name"])}" width="160" height="160">'
                f'<div><h1>{E(r["name"])}</h1><p class="lead">{E(lines[k])}</p><p class="who">' + ' &middot; '.join(f'<a href="/kinds-of-readings/{s}/">{n}</a>' for s, n in ks) + '</p></div></div>'
                f'<h2>Where</h2><p>{where}' + (' Also reads by phone; see <a href="/by-phone/">phone sessions</a>.' if r['phone'] else '') + '</p>'
                f'<h2>What a session costs</h2>{G.services_list(k, "chips")}'
                f'<p><a class="cta" href="{E(r["book"])}" rel="nofollow noopener">Choose a time with {E(first)}</a></p>'
                f'<p class="note">The button opens {E(first)}\'s scheduling page on Square with live open times; you pay there to confirm. Questions first? Call {G.PHONE}.</p>'
                f'<p><a href="/readers/">All psychics</a></p></section>')
        G.add(f'/psychics/{k}/', f'{r["name"]}: Psychic Readings in NYC | Namaste Psychics', f'{r["name"]} of Namaste Psychics. {lines[k]} Prices start at ${r["from"]}; book live times online.', body,
              ld=[G.person_ld(k, f'/psychics/{k}/')], crumbs=[('Home', '/'), ('Psychics', '/readers/'), (r['name'], f'/psychics/{k}/')])

def pages():
    tools_pages()
    home = (f'<section class="split"><div><p class="tag">Namaste Psychics &middot; Manhattan</p><h1>Psychic readers you can meet in person or hear by phone</h1>'
            f'<p>Namaste Psychics is a group of psychic, intuitive and mediumship readers working just west of Union Square. Learn how each kind of reading works, meet the psychic who fits, then choose how you want to sit with them.</p></div>'
            f'<div class="doors"><a class="door" href="/readers/"><b>In person</b><span>Sit across the table on West 14th Street.</span></a>'
            f'<a class="door alt" href="/by-phone/"><b>On the phone</b><span>Book a phone session and your reader calls you, wherever you live.</span></a></div></section>'
            f'<section class="kinds"><h2>Six kinds of readings</h2><ul>' + ''.join(f'<li><a href="/kinds-of-readings/{t[0]}/"><b>{t[2]}</b><span>{t[3]}</span></a></li>' for t in TYPES) + '</ul></section>'
            f'<section class="practice"><h2>Practice between sessions</h2><p>Want to try it yourself? We stock pendulums, rune stones, black obsidian mirrors, and reading on mediumship, intuition and astrology.</p>'
            f'<p><a class="cta" href="/tools/">Browse tools and books</a></p></section>'
            f'<section class="honest"><h2>What a psychic reading is, and is not</h2><p>A reading can help you think through a relationship, a job or a loss with someone who listens differently. It cannot guarantee an outcome, '
            f'and it never replaces a doctor, lawyer, therapist or financial adviser. Each psychic\'s prices are on their profile before you book. <a href="/before-you-book/">More before you book</a>.</p></section>')
    G.add('/', 'Namaste Psychics | Psychic Readings in NYC & by Phone',
          'Namaste Psychics: clairvoyant, clairaudient, mediumship and astrology readings in Manhattan, or by phone from anywhere. Meet each psychic and reserve online.', home,
          ld=[G.shop_ld()])
    idx = ('<section class="pg"><h1>Kinds of psychic readings</h1><p class="lead">Readers do not all work the same way. Some see, some hear, some read a chart. Knowing the difference makes it easier to pick someone.</p>'
           + ''.join(f'<article class="kt"><h2><a href="/kinds-of-readings/{t[0]}/">{t[1]}</a></h2><p>{t[3]}</p><p class="who">' + ', '.join(R[k]["name"] for k, _ in t[5]) + '</p></article>' for t in TYPES) + '</section>')
    G.add('/kinds-of-readings/', 'Types of Psychic Readings Explained | Namaste Psychics',
          'Clairvoyant, clairaudient, mediumship, astrology, oracle and Lenormand readings, plus hypnosis and energy work: how each works and which of our psychics offer it.', idx,
          crumbs=[('Home', '/'), ('Kinds of readings', '/kinds-of-readings/')])
    for slug, title, short, one, para, people in TYPES:
        body = (f'<section class="pg"><p class="tag">Kinds of readings</p><h1>{title} with Namaste Psychics</h1><p class="lead">{one}</p><p>{para}</p>'
                f'<h2>Who offers it</h2><ul class="people">' + ''.join(person(k, l) for k, l in people) + '</ul>'
                f'<p class="note">Open a profile to see prices; its booking button shows live open times.</p><p><a href="/kinds-of-readings/">All kinds of readings</a></p></section>')
        G.add(f'/kinds-of-readings/{slug}/', f'{title} in NYC | Namaste Psychics',
              f'{one} Learn how {short.lower()} sessions work and see which of our psychics offer them.', body,
              crumbs=[('Home', '/'), ('Kinds of readings', '/kinds-of-readings/'), (title, f'/kinds-of-readings/{slug}/')])
    groups = [('Psychic and intuitive', ['catherine-marks', 'rebecca-martinez', 'brinly-erin', 'andrea-dopewitchkira']),
              ('Mediums', ['lizanne', 'sophia-strange', 'high-priestess-judith']),
              ('Astrologers', ['priya', 'casey-deamoira', 'alexander-d-santiago', 'mychal-a-bryan', 'dainichi-lazuli']),
              ('Oracle, Lenormand and hypnosis', ['lu-camy', 'mallika', 'jennifer-shanteau'])]
    lines = {k: l for t in TYPES for k, l in t[5]}
    lines.update({'anthony-fusco': 'Has read the Voyager deck for some twenty-five years; often asked about work, love and when things will move.', 'damon-stang': 'A professional reader of 25-plus years whose card work draws on folk magic.'})
    profiles(lines)
    rd = ('<section class="pg"><h1>Our psychics</h1><p class="lead">Open a profile for prices and booking. Those marked "phone sessions" also read by phone.</p>'
          + ''.join(f'<h2>{g}</h2><ul class="people">' + ''.join(person(k, lines[k]) for k in ks) + '</ul>' for g, ks in groups)
          + '<p class="note">Looking for someone not listed? Only readers taking bookings now appear here. Call us to ask about anyone else.</p></section>')
    G.add('/readers/', 'Psychic Readers, Mediums & Astrologers | Namaste Psychics',
          'Meet the psychics, mediums and astrologers of Namaste Psychics in Manhattan, with starting prices, phone options and a profile for each.', rd,
          crumbs=[('Home', '/'), ('Readers', '/readers/')])
    phone_people = [k for k in R if R[k]['phone']]
    pf = [('Do phone readings cost more?', 'No. A reader charges the same for a call as for a seat at the table.'),
          ('Who calls whom?', 'The reader calls the number on your booking at the appointment time.'),
          ('What about video?', 'Remote readings are booked as phone sessions right now. If you would prefer video, ring ' + G.PHONE + ' to ask about it.'),
          ('Can I change the time?', 'The booking page asks for at least six hours\' notice to cancel or reschedule.')]
    ph = (f'<section class="pg"><h1>Psychic readings by phone</h1><p class="lead">You don\'t need to live in New York to sit with one of our psychics. Book a phone session, pay ahead, and your reader rings you at the time you picked.</p>'
          f'<ol class="steps"><li><b>Choose a reader</b> below.</li><li><b>Pick "Phone Session"</b> and a length: 15, 30, 45 or 60 minutes (not every reader offers every length).</li>'
          f'<li><b>Pay when you book.</b> Times show in your own time zone.</li><li><b>Pick up when they call.</b> A quiet room and a charged phone help.</li></ol>'
          f'<h2>Readers taking phone bookings</h2><ul class="people">' + ''.join(person(k, lines.get(k, 'Takes calls as well as in-shop sittings.')) for k in phone_people) + '</ul>'
          f'<h2>Phone session questions</h2><dl class="faq">' + ''.join(f'<dt>{q}</dt><dd>{a}</dd>' for q, a in pf) + '</dl>'
          f'<p class="note">Pick a psychic above, open their profile and select a phone session while booking.</p></section>')
    G.add('/by-phone/', 'Phone Psychic Readings with NYC Readers | Namaste Psychics',
          'Book a psychic or tarot reading by phone with a Namaste Psychics reader. Same prices as in person; pay ahead and the reader calls you.', ph,
          ld=[G.faq_ld(pf)], crumbs=[('Home', '/'), ('By phone', '/by-phone/')])
    bq = [('How do I choose a reader?', 'Decide first what sort of session appeals to you. If you want images and impressions, try a clairvoyant; if you want timing and cycles, an astrologer; if you hope to hear from someone who has died, a medium.'),
          ('What should I bring?', 'A question or two, written down. For astrology, your birth date, time and city.'),
          ('What if something feels off?', 'You can end a session whenever you like. If you have a concern about a session afterward, write to ' + G.EMAIL + '.'),
          ('Are readings medical or legal advice?', 'No. A reading is for reflection and perspective. Health, legal, money and mental-health decisions belong with qualified professionals.')]
    bb = ('<section class="pg"><h1>Before you book a psychic reading</h1><p class="lead">A few honest notes so the session feels worth it.</p><dl class="faq">'
          + ''.join(f'<dt>{q}</dt><dd>{a}</dd>' for q, a in bq) + f'</dl><h2>Prices</h2><p>Most of our psychics charge $35 for 15 minutes. Some specialists charge more; a 1-hour astrology chart session, for example, can cost up to about $270. '
          f'Your total appears on the booking screen before any payment.</p><p><a class="cta" href="/readers/">See psychics and prices</a></p></section>')
    G.add('/before-you-book/', 'Before You Book a Psychic Reading: Honest Answers | Namaste Psychics',
          'How to choose a psychic reader, what to bring, typical prices with Namaste Psychics, and what a psychic reading cannot do.', bb,
          ld=[G.faq_ld(bq)], crumbs=[('Home', '/'), ('Before you book', '/before-you-book/')])
    G.add('/about/', 'About Namaste Psychics', 'Namaste Psychics is a psychic reading practice in Manhattan operated by Wealth Edge Ventures Inc.',
          f'<section class="pg"><h1>About Namaste Psychics</h1><p>Namaste Psychics is a psychic reading practice whose readers sit inside Namaste Bookshop, {G.ADDR}, and in private rooms at 80 Fifth Avenue, Suite 1104. Wealth Edge Ventures Inc., owner of the bookshop, runs Namaste Psychics.</p>'
          f'<p>Profiles are based on each psychic\'s own listing. This site carries no star ratings and no client quotes.</p>'
          f'<p><a href="tel:{G.TEL}">{G.PHONE}</a> &middot; <a href="mailto:{G.EMAIL}">{G.EMAIL}</a></p></section>', crumbs=[('Home', '/'), ('About', '/about/')])
    G.add('/privacy/', 'Privacy | Namaste Psychics', 'Analytics and booking privacy on namastepsychics.com.',
          '<section class="pg">' + G.privacy('namastepsychics.com does not take payments or ask for personal details itself; reserving opens your psychic\'s scheduling page.') + '</section>',
          crumbs=[('Home', '/'), ('Privacy', '/privacy/')])

NOTFOUND_DESC = 'Page not found on namastepsychics.com.'
NOTFOUND = '<section class="pg"><h1>We did not see that one coming</h1><p>This page is missing. Try <a href="/readers/">the readers</a> or <a href="/by-phone/">phone readings</a>.</p></section>'

CSS = """.pf{display:grid;gap:16px;align-items:center}@media(min-width:620px){.pf{grid-template-columns:160px 1fr}}.pf img{width:160px;height:160px;border-radius:50%;object-fit:cover;border:3px solid var(--rose)}.pf h1{margin:0}
ul.svc{list-style:none;padding:0;display:flex;flex-wrap:wrap;gap:8px}ul.svc li{background:var(--blush);border:1px solid var(--rose);border-radius:999px;padding:6px 14px}ul.svc b{color:var(--wine)}
:root{--wine:#5a1630;--rose:#e8a0b4;--blush:#fbf3f1;--ink:#2a1a20;--accent:#5a1630;--onaccent:#fff;--onink:#fff;--paper:#fbf3f1;--soft:#f6e6ea;--body:'DM Sans',system-ui,sans-serif;--display:'DM Serif Display',Georgia,serif;--btnr:99px;--r:12px;--line:#e4c6cf;--muted:#6a4b56;--focus:#e8a0b4}
.hr{display:flex;align-items:center;gap:16px}.cartbtn{position:relative;display:block;color:#fff;width:28px;height:28px}.cartbtn svg{width:26px;height:26px}.cartn{position:absolute;top:-6px;right:-9px;background:var(--rose);color:var(--wine);border-radius:99px;font:700 .7rem sans-serif;padding:2px 6px}
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
.practice{background:var(--wine);color:#f6dbe3;border-radius:18px;padding:6px 20px 18px;margin:26px 0}.practice h2{color:#fff}.practice .cta{background:var(--rose);color:var(--wine)}
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
