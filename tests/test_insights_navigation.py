"""Regression checks for release identity across the full reader navigation."""
import sys
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from build_professional_insights import SLUGS, release_version, articles, render_body, language_href

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.documents = []
        self.assets = []
        self.entries = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        href = attrs.get('href', '')
        if tag == 'a' and href and not href.startswith('#'):
            if attrs.get('class') == 'entry':
                self.entries.append(href)
            if urlsplit(href).path.endswith('/'):
                self.documents.append(href)
        if tag == 'link' and attrs.get('rel') == 'stylesheet':
            self.assets.append(href)
        if tag == 'script' and attrs.get('src'):
            self.assets.append(attrs['src'])

class ReaderNavigation(unittest.TestCase):
    def test_every_document_link_keeps_current_release(self):
        section = ROOT / 'site-dist/professional-insights'
        for path in section.rglob('index.html'):
            parsed = Links()
            parsed.feed(path.read_text())
            self.assertTrue(parsed.documents)
            for href in parsed.documents + parsed.assets:
                with self.subTest(page=path, href=href):
                    self.assertEqual(parse_qs(urlsplit(href).query).get('v'), [release_version()])
                    target = path.parent / urlsplit(href).path
                    self.assertTrue(target.exists())

    def test_entry_has_four_distinct_versioned_article_links(self):
        parsed = Links()
        parsed.feed((ROOT / 'site-dist/professional-insights/index.html').read_text())
        self.assertEqual(len(parsed.entries), 4)
        self.assertEqual({urlsplit(href).path for href in parsed.entries}, {f'./{slug}/' for slug in SLUGS})

    def test_legacy_redirects_target_current_release(self):
        for rel in ['index.html', 'work-log/index.html']:
            source = (ROOT / 'site-dist' / rel).read_text()
            self.assertIn(f'professional-insights/?v={release_version()}', source)

    def test_default_stays_english(self):
        self.assertIn('<html lang="en">', (ROOT / 'site-dist/professional-insights/index.html').read_text())
        for rel in ['index.html', 'work-log/index.html']:
            self.assertNotIn('professional-insights/zh/', (ROOT / 'site-dist' / rel).read_text())

    def test_language_links_target_corresponding_pages(self):
        section = ROOT / 'site-dist/professional-insights'
        for lang in ['en', 'zh']:
            for slug in [''] + SLUGS:
                current = section / ('zh' if lang == 'zh' else '') / slug
                for other in ['en', 'zh']:
                    href = language_href(lang, other, slug)
                    destination = (current / urlsplit(href).path / 'index.html').resolve()
                    expected = (section / ('zh' if other == 'zh' else '') / slug / 'index.html').resolve()
                    self.assertEqual(destination, expected)
                    self.assertTrue(destination.exists())

    def test_translation_aligns_paragraphs_and_heading_anchors(self):
        import re
        english, chinese = articles(), articles('zh')
        for en, zh in zip(english, chinese):
            self.assertEqual(len(en['blocks']), len(zh['blocks']))
            for a, b in zip(en['blocks'], zh['blocks']):
                self.assertEqual(a.count('**'), b.count('**'))
                self.assertEqual(bool(re.match(r'^#{2,3} ', a)), bool(re.match(r'^#{2,3} ', b)))
            en_html, _ = render_body(en['blocks'])
            zh_html, _ = render_body(zh['blocks'], source_blocks=en['blocks'])
            self.assertEqual(re.findall(r'id="([^"]+)"', en_html), re.findall(r'id="([^"]+)"', zh_html))

if __name__ == '__main__':
    unittest.main()
