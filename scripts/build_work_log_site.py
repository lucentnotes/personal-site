"""Build the single approved production page without publishing historical drafts."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'public' / 'work-log'
OUTPUT = ROOT / 'site-dist'
URL = 'https://suojin311-creator.github.io/personal-site/'

assert SOURCE.is_dir()
# This generated output is deliberately separate from the historical Vite build.
if OUTPUT.exists():
    shutil.rmtree(OUTPUT)
shutil.copytree(SOURCE, OUTPUT)
(OUTPUT / '.nojekyll').touch()
html = (OUTPUT / 'index.html').read_text()
html = html.replace('</head>', f'  <link rel="canonical" href="{URL}">\n</head>')
(OUTPUT / 'index.html').write_text(html)

# Preserve the last shared link as a redirect, not a second content page.
redirect = OUTPUT / 'work-log' / 'index.html'
redirect.parent.mkdir()
redirect.write_text('''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="refresh" content="0;url=../">
<meta name="robots" content="noindex">
<title>前往工作 Log</title>
<script>const destination=new URL('../',location.href);destination.search=location.search;destination.hash=location.hash;location.replace(destination.href);</script>
</head><body><a href="../">前往工作 Log</a></body></html>''')

assert sorted(p.relative_to(OUTPUT).as_posix() for p in OUTPUT.rglob('*.html')) == [
    'index.html', 'work-log/index.html'
]
print(f'Production build: {OUTPUT}; one content page plus the old-link redirect.')
