"""Build only the approved game case; never rebuild or replace existing site pages."""
from pathlib import Path
import re
import shutil

root = Path(__file__).resolve().parents[1]
source = root / 'public' / 'gaming-the-system'
target = root / 'case-dist' / 'gaming-the-system'
if target.exists():
    shutil.rmtree(target)
shutil.copytree(source, target)
for path in (target / 'index.html', target / 'style.css', target / 'page.js', target / 'translations.js'):
    assert path.is_file(), path
html = (target / 'index.html').read_text()
for filename in re.findall(r'(?:src|data-image)="(assets/[^\"]+)"', html):
    assert (target / filename).is_file(), filename
assert 'feedback-private' not in html
assert '备用入口' not in html
print(f'Case-only output: {target}')
print('Publish this directory at /gaming-the-system/; preserve all other deployed paths.')
