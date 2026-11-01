"""Render the provided final Markdown into five standalone, refreshable pages."""
from pathlib import Path
from html import escape
import json
import re

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / 'content/professional-insights'
PAGES = ROOT / 'public/professional-insights'
SLUGS = ['real-world-adoption', 'parents-expectations', 'ai-product-experience', 'purchase-and-educational-value']
BASE = 'https://suojin311-creator.github.io/eportfolio/professional-insights/'

def articles():
    raw = (CONTENT / 'Professional-Insights-Final.md').read_text()
    parts = re.split(r'^## Article \d+\s*$', raw, flags=re.M)[1:]
    assert len(parts) == 4
    metadata = json.loads((CONTENT / 'cards.json').read_text())
    result = []
    for i, part in enumerate(parts):
        blocks = [b.strip() for b in re.split(r'\n\s*\n', part.strip()) if b.strip() and b.strip() != '---']
        assert blocks[0].startswith('# ') and blocks[1].startswith('*')
        result.append(dict(title=blocks[0][2:], subtitle=blocks[1][1:-1], blocks=blocks[2:], slug=SLUGS[i], **metadata[i]))
    return result

def inline(value):
    value = escape(value)
    value = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', value)
    return re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<em>\1</em>', value)

def render_body(blocks, inserts=None):
    output, toc, used = [], [], set()
    for block in blocks:
        match = re.match(r'^(#{2,3}) (.+)$', block)
        if match:
            level, title = len(match[1]), match[2]
            ident = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
            base, n = ident, 2
            while ident in used:
                ident = f'{base}-{n}'; n += 1
            used.add(ident)
            output.append(f'<h{level} id="{ident}">{inline(title)}</h{level}>')
            toc.append(f'<a class="level-{level}" href="#{ident}">{escape(title)}</a>')
        else:
            output.append('<p>' + inline(block.replace('\n', ' ')) + '</p>')
        if inserts and block in inserts:
            output.append(inserts[block])
    return '\n'.join(output), '\n'.join(toc)

def interface_figure(filename, title, width, height, single=False):
    classes = 'ui-screen ui-single' if single else 'ui-screen'
    ident = filename.removesuffix(".webp")
    return f'<figure id="{ident}" class="{classes}"><a href="../media/{filename}" data-screen aria-label="Enlarge {title}"><img src="../media/{filename}" alt="{title} mini-program interface" width="{width}" height="{height}" loading="lazy" decoding="async"></a><figcaption>{title}</figcaption></figure>'

def article_media(index):
    if index == 0:
        screens = []
        for filename, title, width, height in [
            ('scenario.webp', 'Scenario simulation', 1206, 2484),
            ('digital-human.webp', 'Digital human · Teacher Ale', 1206, 2486),
        ]:
            screens.append(interface_figure(filename, title, width, height))
        return {'Three experiences helped me examine that gap: a parenting simulation, an AI digital human, and a companion toy for children.': '<div class="ui-pair">' + ''.join(screens) + '</div>'}
    if index == 1:
        return {'I would also consider the work the product introduces. Selecting content, configuring goals, interpreting reports, and deciding what to do next can require parental effort. Those activities may be worthwhile, but they belong in any assessment of a promise to reduce supervision.': interface_figure('growth-home.webp', 'Growth Centre · Parent dashboard', 1206, 2483, single=True)}
    if index == 2:
        return {
            'The team later explored positioning the toy as a habit-building assistant for children aged three to six.': '<div class="ui-pair">' + interface_figure('growth-library.webp', 'Animation library', 1206, 2458) + interface_figure('growth-detail.webp', 'Animation series · Detail', 1206, 2467) + '</div>',
            'The experience combined animated educational content, parental goal-setting, scheduled reminders, NFC cards, and question-based interactions. This provided a more specific context for the product than open-ended conversation alone.': '<figure class="product-animation"><video controls playsinline preload="none" poster="../media/animation-poster.webp" width="1024" height="576" aria-label="Product animation: brushing teeth"><source src="../media/theme-animation.mp4" type="video/mp4"><a href="../media/theme-animation.mp4">Watch the animation</a></video><figcaption>Product animation · Brushing teeth</figcaption></figure>'}
    if index == 3:
        return {'This was also where commercial communication and product design met. The way a capability was presented helped define the standard against which the family would judge it.': interface_figure('shop.webp', 'Mini-program shop · Interface reference', 1206, 2461, single=True)}
    return {}

MARK = '<svg class="insights-mark" viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M3 27V5h12v42M18 5h11v11H18v11h11"/><circle cx="9" cy="11" r="1.5" fill="currentColor" stroke="none"/></svg>'
ICONS = ['<svg class="theme-icon" viewBox="0 0 56 56" fill="none" stroke="currentColor" stroke-width="1.35" stroke-linejoin="round" stroke-linecap="round" aria-hidden="true"><path d="M7 28h12l10-16h12M19 28l10 16h12"/><circle cx="7" cy="28" r="4"/><circle cx="43" cy="12" r="4"/><circle cx="43" cy="44" r="4"/></svg>', '<svg class="theme-icon" viewBox="0 0 56 56" fill="none" stroke="currentColor" stroke-width="1.35" stroke-linejoin="round" stroke-linecap="round" aria-hidden="true"><circle cx="21" cy="28" r="15"/><circle cx="35" cy="28" r="15"/><path d="M28 16v44"/></svg>', '<svg class="theme-icon" viewBox="0 0 56 56" fill="none" stroke="currentColor" stroke-width="1.35" stroke-linejoin="round" stroke-linecap="round" aria-hidden="true"><path d="M8 10h40v49H25L13 48v-9H8z"/><path d="M28 17v15M21 24h14"/></svg>', '<svg class="theme-icon" viewBox="0 0 56 56" fill="none" stroke="currentColor" stroke-width="1.35" stroke-linejoin="round" stroke-linecap="round" aria-hidden="true"><path d="M7 28l21-21 21 21-21 21z"/><path d="M18 28h20m-7-7 7 7-7 7"/></svg>']
ARROW = '<span aria-label="Read essay"><svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="currentColor"><path d="M4 14 14 4M4 4h10v10"/></svg></span>'

def shell(title, inner, detail=False, slug='', description=''):
    prefix = '../' if detail else './'
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#f7f9f3"><title>{escape(title)} · Professional Insights</title>
<meta name="description" content="{escape(description, quote=True)}">
<link rel="canonical" href="{BASE + (slug + '/' if slug else '')}">
<link rel="icon" href="{prefix}mark.svg" type="image/svg+xml">
<link rel="stylesheet" href="{prefix}style.css?v=insights6"><script src="{prefix}reading.js?v=insights6" defer></script></head>
<body><a class="skip" href="#main">Skip to content</a><div class="site"><header class="top"><a class="brand" href="{prefix}">{MARK}Professional Insights</a></header>
{inner}</div></body></html>'''

def build():
    data = articles()
    PAGES.mkdir(parents=True, exist_ok=True)
    cards = []
    for i, item in enumerate(data):
        cards.append(f'''<a class="entry" href="./{item['slug']}/">{ICONS[i]}<span class="meta">{i+1:02d} / {escape(item['category'])}</span><h2>{escape(item['title'])}</h2><span class="entryfoot">{ARROW}</span></a>''')
    overview = '<main class="wrap" id="main"><div class="hero"><div><h1>Seeing products<br>through experience.</h1></div></div><section class="context" aria-label="Work background"><p class="sub">Early-stage EdTech experience across platform operations, user and sales feedback, AI response testing, and product coordination.</p></section><div class="grid">' + '\n'.join(cards) + '</div></main>'
    (PAGES / 'index.html').write_text(shell('Professional Insights', overview, description='Four perspectives from early-stage EdTech experience.'))
    photo_info = {
        1: ('family-illustration.jpg', 'Child with Xiaole in a study setting', 'AI-generated illustration'),
        2: ('exhibition.jpg', 'Xiaole and its mini program demonstrated at an exhibition', ''),
        3: ('toy-store.jpg', 'Xiaole display in a toy store', '')
    }
    for i, item in enumerate(data):
        body, toc = render_body(item['blocks'], article_media(i))
        photo = ''
        if i in photo_info:
            filename, alt, caption = photo_info[i]
            photo = f'<figure class="article-photo"><img src="../photos/{filename}" alt="{alt}" width="{1672 if i == 1 else 1078 if i == 2 else 1517}" height="{830 if i == 1 else 525 if i == 2 else 753}">' + (f'<figcaption>{caption}</figcaption>' if caption else '') + '</figure>'
        previous = (f'<a rel="prev" href="../{data[i-1]["slug"]}/"><span>← Previous essay</span>{escape(data[i-1]["title"])}</a>' if i else '<span></span>')
        following = (f'<a rel="next" href="../{data[i+1]["slug"]}/"><span>Next essay →</span>{escape(data[i+1]["title"])}</a>' if i+1 < len(data) else '<a href="../"><span>Series complete</span>All insights →</a>')
        page = f'''<main class="wrap detail" id="main"><a class="back" href="../">← All insights</a><header class="articleheader">{ICONS[i]}<p class="meta">{i+1:02d} / {escape(item['category'])}</p><h1>{escape(item['title'])}</h1></header>
<div class="reading"><aside class="toc"><nav aria-label="In this essay"><p class="meta">In this essay</p>{toc}</nav></aside><div class="reading-column"><details class="mobile-toc"><summary>In this essay</summary><nav aria-label="Article contents">{toc}</nav></details>{photo}<article class="body">{body}</article><nav class="articleend" aria-label="Essay navigation">{previous}{following}</nav></div></div></main>'''
        target = PAGES / item['slug']; target.mkdir(exist_ok=True)
        (target / 'index.html').write_text(shell(item['title'], page, True, item['slug'], item['subtitle']))
    print('Rendered five Professional Insights pages from the final Markdown.')

if __name__ == '__main__':
    build()
