"""Generate the three pitch-preserving score variants. Requires FFmpeg."""
from pathlib import Path
import subprocess
ROOT = Path(__file__).resolve().parents[1]
for rate, suffix in [(1.25, '125'), (1.5, '15'), (2, '2')]:
    subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y',
                    '-i', str(ROOT/'assets/inside-piano.mp3'), '-af', f'atempo={rate}',
                    '-codec:a', 'libmp3lame', '-b:a', '96k',
                    str(ROOT/f'assets/inside-piano-{suffix}.mp3')], check=True)
