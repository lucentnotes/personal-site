"""Regression checks for release identity across the full reader navigation."""
import sys
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from build_professional_insights import SLUGS, release_version

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.documents = []
        self.assets = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        href = attrs.get('href', '')
        if tag == 'a' and href and not href.startswith('#'):
            if urlsplit(href).path.endswith('/'):
                self.documents.append(href)
        if tag == 'link' and attrs.get('rel') == 'stylesheet':
            self.assets.append(href)
        if tag == 'script' and attrs.get('src'):
            self.assets.append(attrs['src'])

class ReaderNavigation(unittest.TestCase):
    def test_every_document_link_keeps_current_release(self):
        section = ROOT / 'site-dist/professional-insights'
        for path in [section / 'index.html'] + [section / slug / 'index.html' for slug in SLUGS]:
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
        articles = [href for href in parsed.documents if urlsplit(href).path != './']
        self.assertEqual(len(articles), 4)
        self.assertEqual({urlsplit(href).path for href in articles}, {f'./{slug}/' for slug in SLUGS})

    def test_legacy_redirects_target_current_release(self):
        for rel in ['index.html', 'work-log/index.html']:
            source = (ROOT / 'site-dist' / rel).read_text()
            self.assertIn(f'professional-insights/?v={release_version()}', source)

if __name__ == '__main__':
    unittest.main()
