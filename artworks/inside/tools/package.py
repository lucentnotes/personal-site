"""Build bilingual standalone files and subtitles from the current source."""
from pathlib import Path
import base64, json, zipfile, mimetypes
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'deliverables'
OUT.mkdir(exist_ok=True)
html = (ROOT/'index.html').read_text()
for lang in ['zh', 'en']:
    page = html
    for name in ['style.css', 'immersive.css']:
        page = page.replace(f'<link rel="stylesheet" href="{name}">', '<style>'+(ROOT/name).read_text()+('\n/* '+(ROOT/'assets/fonts/OFL-Cormorant-Garamond.txt').read_text()+' */' if name=='immersive.css' else '')+'</style>')
    for name in ['content.js', 'timing.js', 'film.js', 'immersive.js']:
        js = (ROOT/name).read_text()
        if name == 'film.js':
            js = js.replace("lang=new URLSearchParams(location.search).get('lang')==='en'?'en':'zh'", f"lang='{lang}'")
        page = page.replace(f'<script src="{name}"></script>', '<script>'+js+'</script>')
    for asset in ['party.png', 'party-empty.png', 'bedroom.jpg', 'inside-piano.mp3', 'ballroom-murmur.mp3', 'inside-piano-125.mp3', 'inside-piano-15.mp3', 'inside-piano-2.mp3', 'fonts/cormorant-garamond.ttf']:
        mime = mimetypes.guess_type(asset)[0] or 'application/octet-stream'
        page = page.replace('assets/'+asset, 'data:'+mime+';base64,'+base64.b64encode((ROOT/'assets'/asset).read_bytes()).decode())
    page = page.replace('index.html?lang=zh', 'Inside-Act-I-ZH.html').replace('index.html?lang=en', 'Inside-Act-I-EN.html').replace('href="index.html"', f'href="Inside-Act-I-{lang.upper()}.html"')
    (OUT/f'Inside-Act-I-{lang.upper()}.html').write_text(page)
    cues, clock = [], 0
    for shot in json.loads((ROOT/'timing.json').read_text())['shots']:
        for c in shot['cues']:
            if c['zh']:
                cues.append((clock+c['localStart'], clock+c['localEnd'], c[lang]))
        clock += shot['duration']
    def stamp(t):
        ms = round(t*1000)
        return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
    (OUT/f'Inside-Act-I-{lang.upper()}.srt').write_text('\n\n'.join(f'{i+1}\n{stamp(a)} --> {stamp(b)}\n{text}' for i,(a,b,text) in enumerate(cues))+'\n')
with zipfile.ZipFile(OUT/'Inside-Act-I.zip', 'w', zipfile.ZIP_DEFLATED) as archive:
    archive.write(ROOT/'README.md', 'README.md')
    for p in OUT.iterdir():
        if p.name.startswith('Inside-Act-I-') or p.name.startswith('Revision-17-'):
            archive.write(p, p.name)
print('Bilingual standalone HTML and subtitles built.')
