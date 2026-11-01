"""Render the provided final Markdown into five standalone, refreshable pages."""
from pathlib import Path
from html import escape
from hashlib import sha256
import json
import re
import posixpath

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / 'content/professional-insights'
PAGES = ROOT / 'public/professional-insights'
SLUGS = ['real-world-adoption', 'parents-expectations', 'ai-product-experience', 'purchase-and-educational-value']
BASE = 'https://suojin311-creator.github.io/eportfolio/professional-insights/'

def release_version():
    """Change document URLs when copy, layout, or navigation changes."""
    digest = sha256()
    for path in [Path(__file__), CONTENT / 'Professional-Insights-Final.md', CONTENT / 'Professional-Insights-zh.md', CONTENT / 'cards.json', PAGES / 'style.css', PAGES / 'reading.js']:
        digest.update(path.read_bytes())
    return digest.hexdigest()[:12]

def versioned(path):
    return f'{path}?v={release_version()}'

def articles(lang='en'):
    raw = (CONTENT / ('Professional-Insights-zh.md' if lang == 'zh' else 'Professional-Insights-Final.md')).read_text()
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

def render_body(blocks, inserts=None, source_blocks=None):
    output, toc, used = [], [], set()
    for index, block in enumerate(blocks):
        match = re.match(r'^(#{2,3}) (.+)$', block)
        if match:
            level, title = len(match[1]), match[2]
            source_title = re.sub(r'^#{2,3} ', '', source_blocks[index]) if source_blocks else title
            ident = re.sub(r'[^a-z0-9]+', '-', source_title.lower()).strip('-')
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

UI = {
    'en': dict(brand='Professional Insights', heading='Seeing products<br>through experience.', background='Early-stage EdTech experience across platform operations, user and sales feedback, AI response testing, and product coordination.', description='Four perspectives from early-stage EdTech experience.', skip='Skip to content', back='← All insights', toc='In this essay', previous='← Previous essay', next='Next essay →', complete='Series complete', all='All insights →', read='Read essay', language='Language', navigation='Essay navigation', categories=['User adoption', 'Family expectations', 'AI product design', 'Product value']),
    'zh': dict(brand='产品思考', heading='在实践中，<br>理解产品。', background='在早期教育科技公司，参与平台运营、用户与销售反馈、AI 回答测试及产品协调工作。', description='来自早期教育科技工作经历的四篇产品思考。', skip='跳至正文', back='← 返回列表', toc='本文目录', previous='← 上一篇', next='下一篇 →', complete='已读至最后一篇', all='返回列表 →', read='阅读文章', language='语言', navigation='文章导航', categories=['用户使用', '家长期待', 'AI 产品设计', '产品价值'])
}
MEDIA_ZH = {
    'Scenario simulation': '场景模拟',
    'Digital human · Teacher Ale': '数字人阿乐老师建议',
    'Growth Centre · Parent dashboard': '成长中心 · 家长端',
    'Animation library': '动画内容',
    'Animation series · Detail': '动画详情',
    'Mini-program shop · Interface reference': '小乐商城 · 界面示例',
    'Product animation: brushing teeth': '产品动画：刷牙主题',
    'Product animation · Brushing teeth': '产品动画示例 · 刷牙主题',
    'Watch the animation': '播放动画',
    'Enlarge ': '放大查看：',
    ' mini-program interface': '小程序界面'
}

def language_path(lang, slug=''):
    return ('zh/' if lang == 'zh' else '') + (slug + '/' if slug else '')

def language_href(current, target, slug=''):
    start = language_path(current, slug) or '.'
    destination = language_path(target, slug) or '.'
    return versioned(posixpath.relpath(destination, start) + '/')

def asset_prefix(lang, detail):
    return ('../../' if detail else '../') if lang == 'zh' else ('../' if detail else './')

def translated_media(index, lang, source_blocks, translated_blocks):
    inserts = article_media(index)
    if lang == 'en':
        return inserts
    pairs = dict(zip(source_blocks, translated_blocks))
    result = {}
    for source, media in inserts.items():
        media = media.replace('../media/', '../../media/')
        for english, chinese in MEDIA_ZH.items():
            media = media.replace(english, chinese)
        result[pairs[source]] = media
    return result

def shell(title, inner, detail=False, slug='', description='', lang='en'):
    ui = UI[lang]
    prefix = asset_prefix(lang, detail)
    list_path = '../' if detail else './'
    language_links = []
    for target, label, code in [('en', 'English', 'en'), ('zh', '中文', 'zh-CN')]:
        selected = ' aria-current="page"' if lang == target else ''
        language_links.append(f'<a class="language-link" data-language="{target}" href="{language_href(lang, target, slug)}" lang="{code}" hreflang="{code}"{selected}>{label}</a>')
    language_nav = f'<nav class="languages" aria-label="{ui["language"]}">' + ''.join(language_links) + '</nav>'
    title_text = title if title == ui['brand'] else title + ' · ' + ui['brand']
    canonical = BASE + language_path(lang, slug)
    return f'''<!doctype html>
<html lang="{'zh-CN' if lang == 'zh' else 'en'}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#f7f9f3"><title>{escape(title_text)}</title>
<meta name="description" content="{escape(description, quote=True)}">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="en" href="{BASE + language_path('en', slug)}">
<link rel="alternate" hreflang="zh-CN" href="{BASE + language_path('zh', slug)}">
<link rel="alternate" hreflang="x-default" href="{BASE + language_path('en', slug)}">
<link rel="icon" href="{prefix}mark.svg" type="image/svg+xml">
<link rel="stylesheet" href="{versioned(prefix + 'style.css')}"><script src="{versioned(prefix + 'reading.js')}" defer></script></head>
<body><a class="skip" href="#main">{ui['skip']}</a><div class="site"><header class="top"><a class="brand" href="{versioned(list_path)}">{MARK}{ui['brand']}</a>{language_nav}</header>
{inner}</div></body></html>'''

def build():
    source = articles()
    for lang in ['en', 'zh']:
        data = source if lang == 'en' else articles('zh')
        ui = UI[lang]
        destination = PAGES / language_path(lang)
        destination.mkdir(parents=True, exist_ok=True)
        cards = []
        for i, item in enumerate(data):
            assert len(item['blocks']) == len(source[i]['blocks']), 'Translation must preserve paragraph alignment'
            arrow = ARROW.replace('Read essay', ui['read'])
            cards.append(f'''<a class="entry" href="{versioned('./' + item['slug'] + '/')}">{ICONS[i]}<span class="meta">{i+1:02d} / {ui['categories'][i]}</span><h2>{escape(item['title'])}</h2><span class="entryfoot">{arrow}</span></a>''')
        overview = f'<main class="wrap" id="main"><div class="hero"><div><h1>{ui["heading"]}</h1></div></div><section class="context" aria-label="{ "工作背景" if lang == "zh" else "Work background" }"><p class="sub">{ui["background"]}</p></section><div class="grid">' + '\n'.join(cards) + '</div></main>'
        (destination / 'index.html').write_text(shell(ui['brand'], overview, description=ui['description'], lang=lang))
        photo_info = {
            1: ('family-illustration.jpg', '孩子与小乐在书桌前的场景示意' if lang == 'zh' else 'Child with Xiaole in a study setting', 'AI 生成场景示意' if lang == 'zh' else 'AI-generated illustration'),
            2: ('exhibition.jpg', '展会现场展示小乐及配套小程序' if lang == 'zh' else 'Xiaole and its mini program demonstrated at an exhibition', ''),
            3: ('toy-store.jpg', '玩具店中的小乐产品陈列' if lang == 'zh' else 'Xiaole display in a toy store', '')
        }
        for i, item in enumerate(data):
            media = translated_media(i, lang, source[i]['blocks'], item['blocks'])
            body, toc = render_body(item['blocks'], media, source[i]['blocks'])
            prefix = asset_prefix(lang, True)
            photo = ''
            if i in photo_info:
                filename, alt, caption = photo_info[i]
                photo = f'<figure class="article-photo"><img src="{prefix}photos/{filename}" alt="{alt}" width="{1672 if i == 1 else 1078 if i == 2 else 1517}" height="{830 if i == 1 else 525 if i == 2 else 753}">' + (f'<figcaption>{caption}</figcaption>' if caption else '') + '</figure>'
            previous = (f'<a rel="prev" href="{versioned("../" + data[i-1]["slug"] + "/")}"><span>{ui["previous"]}</span>{escape(data[i-1]["title"])}</a>' if i else '<span></span>')
            following = (f'<a rel="next" href="{versioned("../" + data[i+1]["slug"] + "/")}"><span>{ui["next"]}</span>{escape(data[i+1]["title"])}</a>' if i+1 < len(data) else f'<a href="{versioned("../")}"><span>{ui["complete"]}</span>{ui["all"]}</a>')
            page = f'''<main class="wrap detail" id="main"><a class="back" href="{versioned('../')}">{ui['back']}</a><header class="articleheader">{ICONS[i]}<p class="meta">{i+1:02d} / {ui['categories'][i]}</p><h1>{escape(item['title'])}</h1></header>
<div class="reading"><aside class="toc"><nav aria-label="{ui['toc']}"><p class="meta">{ui['toc']}</p>{toc}</nav></aside><div class="reading-column"><details class="mobile-toc"><summary>{ui['toc']}</summary><nav aria-label="{ui['toc']}">{toc}</nav></details>{photo}<article class="body">{body}</article><nav class="articleend" aria-label="{ui['navigation']}">{previous}{following}</nav></div></div></main>'''
            target = destination / item['slug']; target.mkdir(exist_ok=True)
            (target / 'index.html').write_text(shell(item['title'], page, True, item['slug'], item['subtitle'], lang))
    print('Rendered ten Professional Insights pages: English by default, plus Chinese.')

if __name__ == '__main__':
    build()
