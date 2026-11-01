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
    # Hide the phone status bar in presentation without changing screenshot pixels.
    crop = ' class="screen-crop" data-crop-top="13.266998" style="--crop-top:13.266998%"' if filename == 'chat-detail.webp' else ''
    return f'<figure id="{ident}" class="{classes}"><a href="../media/{filename}" data-screen{crop} aria-label="Enlarge {title}"><img src="../media/{filename}" alt="{title} mini-program interface" width="{width}" height="{height}" loading="lazy" decoding="async"></a><figcaption>{title}</figcaption></figure>'

def article_media(index):
    if index == 0:
        screens = []
        for filename, title, width, height in [
            ('scenario.webp', 'Scenario simulation', 1206, 2484),
            ('digital-human.webp', 'Digital human · Teacher Ale', 1206, 2486),
        ]:
            screens.append(interface_figure(filename, title, width, height))
        return {
            'Three experiences helped me examine that gap: a parenting simulation, an AI digital human, and a companion toy for children.': '<div class="ui-pair">' + ''.join(screens) + '</div>',
            'Another challenge emerged when I worked on an AI digital human feature for parents. My responsibilities included designing prompts, defining response boundaries, testing answer quality, and examining unsatisfactory responses.': interface_figure('ai-experts.webp', 'AI expert directory', 1206, 2468, single=True)}
    if index == 1:
        return {
            'In this scenario, the parent would not need to be physically present throughout the learning process. Instead, technology could take on some routine responsibilities while allowing the parent to remain informed and make decisions when necessary.': '<div class="ui-pair">' + interface_figure('chat-records.webp', 'Chat records · Parent view', 1206, 2464) + interface_figure('chat-detail.webp', 'Chat detail', 1206, 2622) + '</div>',
            'This expectation is different from simply asking a product to deliver better academic results. It places value on the experience of learning together.': '<div class="ui-pair">' + interface_figure('editorial.webp', 'Educational content · Articles and audio', 1206, 2462) + interface_figure('article.webp', 'Article reading', 1206, 2473) + '</div>',
            'First, products should identify which educational responsibilities parents actually want to delegate. Routine practice, progress tracking, reminders, and basic feedback may be suitable areas for technological support. However, these functions should not be assumed to replace every form of parental guidance. A product that generates progress reports, for example, should help parents understand what the information means and what they can do with it, rather than merely adding another monitoring task.': interface_figure('growth-home.webp', 'Growth Centre · Parent dashboard', 1206, 2483, single=True)}
    if index == 2:
        return {
            "The team introduced a habit-building package that connected the parent-facing mini-program with the child's interaction with the toy.": '<div class="ui-pair">' + interface_figure('growth-library.webp', 'Animation library', 1206, 2458) + interface_figure('growth-detail.webp', 'Animation series · Detail', 1206, 2467) + '</div>',
            'Parents could access a growth-goal section in the mini-program. Children first watched short animations created by the team, covering habits and everyday safety topics such as brushing teeth and looking at traffic lights before crossing the road. After an animation, the system generated a corresponding growth goal for the parent to review and confirm.': '<figure class="product-animation"><video controls playsinline preload="none" poster="../media/animation-poster.webp" width="1024" height="576" aria-label="Product animation: brushing teeth"><source src="../media/theme-animation.mp4" type="video/mp4"><a href="../media/theme-animation.mp4">Watch the animation</a></video><figcaption>Product animation · Brushing teeth</figcaption></figure>'}
    if index == 3:
        return {
            'However, once a product reaches an acceptable level of quality and can reliably fulfil its main purpose, the factors influencing further growth may change. Sales, marketing, distribution channels, and operational execution can become increasingly important.': '<div class="ui-pair">' + interface_figure('shop.webp', 'Mini-program shop · Interface reference', 1206, 2461) + interface_figure('camp.webp', 'Third-party study camp · Product detail', 1206, 2471) + '</div>',
            "In other words, product quality establishes the foundation for market entry, while go-to-market execution can become more important for expanding market reach once the product meets the market's minimum expectations.": '<figure id="store-operations" class="context-photo"><img src="../photos/store-operations.jpg" alt="Xiaole products on a toy-store shelf" width="865" height="1021" loading="lazy" decoding="async"><figcaption>Toy-store scene</figcaption></figure>',
            'Continued usage: Whether users continue to engage with the product after the initial purchase.': interface_figure('points-shop.webp', 'Points shop · Interface reference', 1206, 2475, single=True)}
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
    'AI expert directory': 'AI 专家',
    'Growth Centre · Parent dashboard': '成长中心 · 家长端',
    'Chat records · Parent view': '家长端 · 聊天记录',
    'Chat detail': '对话详情',
    'Educational content · Articles and audio': '教育资讯 · 文章与音频',
    'Article reading': '文章阅读',
    'Animation library': '动画内容',
    'Animation series · Detail': '动画详情',
    'Mini-program shop · Interface reference': '小乐商城 · 界面示例',
    'Third-party study camp · Product detail': '第三方研学产品 · 商品详情',
    'Points shop · Interface reference': '积分商城 · 界面示例',
    'Xiaole products on a toy-store shelf': '玩具店货架上的小乐产品',
    'Toy-store scene': '玩具店现场',
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
        media = media.replace('../media/', '../../media/').replace('../photos/', '../../photos/')
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
            assert set(media).issubset(item['blocks']), 'Every media placement must match a current paragraph'
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
