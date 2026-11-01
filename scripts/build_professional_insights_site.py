"""Publish only the approved Professional Insights section and legacy redirects."""
from pathlib import Path
import shutil
from build_professional_insights import build, SLUGS

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'site-dist'
build()
if OUTPUT.exists():
    shutil.rmtree(OUTPUT)
OUTPUT.mkdir()
shutil.copytree(ROOT / 'public/professional-insights', OUTPUT / 'professional-insights')
(OUTPUT / '.nojekyll').touch()
for path, destination in [('index.html', './professional-insights/'), ('work-log/index.html', '../professional-insights/')]:
    target = OUTPUT / path
    target.parent.mkdir(exist_ok=True)
    target.write_text(f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="refresh" content="0;url={destination}"><meta name="robots" content="noindex"><title>Professional Insights</title>
</head><body><a href="{destination}">Professional Insights →</a></body></html>''')
expected = {'index.html', 'work-log/index.html', 'professional-insights/index.html'} | {f'professional-insights/{slug}/index.html' for slug in SLUGS}
assert {p.relative_to(OUTPUT).as_posix() for p in OUTPUT.rglob('*.html')} == expected
print(f'Production build: {OUTPUT}; five content pages and two legacy redirects.')
