"""Build the isolated literary artwork without changing the portfolio build."""
from pathlib import Path
import shutil
ROOT = Path(__file__).resolve().parents[1]
SOURCE, OUTPUT = ROOT/'artworks/inside', ROOT/'inside-dist'
if OUTPUT.exists():
    shutil.rmtree(OUTPUT)
shutil.copytree(SOURCE, OUTPUT)
(OUTPUT/'.nojekyll').touch()
print(f'What Stays: {OUTPUT}')
