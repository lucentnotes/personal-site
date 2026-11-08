"""Build approved runtime only, independently of the portfolio homepage."""
from pathlib import Path
import shutil, hashlib
ROOT = Path(__file__).resolve().parents[1]
SOURCE, OUTPUT = ROOT/'artworks/inside', ROOT/'inside-dist'
if OUTPUT.exists():
    shutil.rmtree(OUTPUT)
OUTPUT.mkdir()
for name in ('index.html', 'immersive-preview.html', 'style.css', 'immersive.css',
             'film.js', 'immersive.js', 'content.js', 'content.json', 'timing.js',
             'timing.json', 'score-cue.json', 'crowd-candidates.json', 'README.md'):
    shutil.copy2(SOURCE/name, OUTPUT/name)
shutil.copytree(SOURCE/'assets', OUTPUT/'assets',
                ignore=shutil.ignore_patterns('ballroom-murmur.mp3'))
shutil.copytree(SOURCE/'audition', OUTPUT/'audition')
# Content hashes prevent a returning viewer from running an earlier scene script.
for entry in ('index.html', 'immersive-preview.html'):
    text = (OUTPUT/entry).read_text()
    for asset in ('style.css', 'immersive.css', 'content.js', 'timing.js', 'film.js', 'immersive.js'):
        digest = hashlib.sha256((OUTPUT/asset).read_bytes()).hexdigest()[:12]
        text = text.replace(f'"{asset}"', f'"{asset}?v={digest}"')
    (OUTPUT/entry).write_text(text)
(OUTPUT/'.nojekyll').touch()
print(f'What Stays: {OUTPUT}')
