from pathlib import Path
import subprocess,ctypes as C,ctypes.util,wave,json,numpy as np,shutil,tempfile
root=Path(__file__).resolve().parents[1];out=root/'music-study';out.mkdir(exist_ok=True)
work=Path(tempfile.mkdtemp(prefix='inside-music-study-'))
# Reuse the existing, locally authored note scheduler and documented instrument.
source=(root/'tools/render_score.py').read_text();prefix=source[:source.index('for n in range(16):')];exec(prefix)
# New accompaniment: selected notes from the same voicings, without the repeating melody.
for at,key,vel,length in [(85,38,29,5),(90,57,24,3),(95,34,27,6),(99,62,25,4),(112.5,41,28,7),(114.8,60,25,6),(117,65,24,4),(176.5,38,27,7),(180,57,23,6),(183,62,22,6)]:note(at,key,vel,length)
sr=22050;length=201;arr=np.zeros((int(sr*length),2),np.float32);events.sort();cursor=0
for at,kind,key,velocity in events+[(length,0,0,0)]:
 end=min(len(arr),int(at*sr));count=end-cursor
 if count>0:
  l=np.empty(count,np.float32);r=np.empty(count,np.float32);write(synth,count,l.ctypes.data,0,1,r.ctypes.data,0,1);arr[cursor:end,0]=l;arr[cursor:end,1]=r;cursor=end
 if key:(on(synth,0,key,velocity) if kind else off(synth,0,key))
# Match sparse notes below the original recording's peaks; no per-section amplification.
arr*=.65/max(np.max(np.abs(arr)),.001)
raw=subprocess.check_output(['ffmpeg','-v','error','-i',str(root/'assets/inside-piano.mp3'),'-f','f32le','-ac','2','-ar',str(sr),'-'])
original=np.frombuffer(raw,dtype='<f4').reshape(-1,2)
track=arr[:int(191*sr)].copy()
def smooth(x):x=np.clip(x,0,1);return x*x*(3-2*x)
def add_original(start,seconds,fadein,fadeout,gain=1):
 n=int(seconds*sr);x=np.arange(n)/sr;env=smooth(x/fadein) if fadein else np.ones(n)
 if fadeout:env*=1-smooth((x-(seconds-fadeout))/fadeout)
 track[int(start*sr):int(start*sr)+n]+=original[:n]*env[:,None]*gain
add_original(0,34,3,7)
# User-approved cue uses the actual original opening, not a recreated or louder accent.
add_original(145.45,14.55,0,4)
# Clear station, typing, phone, and recognition passages. Shop exits only finish fading at 121.5.
for a,b in [(34,84.5),(103.5,112.5),(121.5,145.45),(160,176.5),(189,191)]:track[int(a*sr):int(b*sr)]=0
x=np.arange(len(track))/sr
shop=1-smooth((x-119.25)/2.25);track[(x>=119.25)&(x<121.5)]*=shop[(x>=119.25)&(x<121.5),None]
for end in [103.5,189]:
 mask=(x>=end-.7)&(x<end);track[mask]*=(1-smooth((x[mask]-end+.7)/.7))[:,None]
# Small roll-offs for newly introduced sparse sections.
for a in [84.5,93.5,112.5,176.5]:
 mask=(x>=a)&(x<a+.35);track[mask]*=smooth((x[mask]-a)/.35)[:,None]
with wave.open(str(work/'arranged.wav'),'wb') as w:w.setnchannels(2);w.setsampwidth(2);w.setframerate(sr);w.writeframes((np.clip(track,-1,1)*32767).astype('<i2').tobytes())
for rate,suffix in [(1,'original-clock'),(1.25,'125'),(1.5625,'15625'),(1.875,'1875'),(2.5,'25')]:
 subprocess.run(['ffmpeg','-y','-v','error','-i',str(work/'arranged.wav'),'-af',f'atempo={rate}','-b:a','128k',str(out/f'score-{suffix}.mp3')],check=True)
shutil.copy('/usr/share/doc/timgm6mb-soundfont/copyright',out/'instrument-source-license.txt');shutil.copy('/usr/share/common-licenses/GPL-2',out/'GPL-2.txt')
manifest={'status':'audition_only_not_main_film','baseSpeed':1.25,'durationSecondsAtNew1x':191/1.25,'composition':'Project-authored note sequences in tools/render_score.py; no external song used','instrument':'TimGM6mb.sf2','instrumentLicense':'GPL-2, documented sample provenance; see instrument-source-license.txt','source':'https://github.com/musescore/musescore-old/commit/90c33ef9d87b3f5ff92efd3b07d89eb455fb1fef','arrangement':[['0–34','Original opening, fade in then leave'],['34–84.5','No score: rice/room/platform/bus foley'],['84.5–103.5','Sparse bass and isolated upper notes'],['103.5–112.5','No score: typing'],['112.5–121.5','Light voicing, exit fade ends outside shop'],['121.5–145.45','No score: phone and ballroom crowd'],['145.45–160','Exact original track opening at neck touch; no accent boost'],['160–176.5','No score: mistaken recognition'],['176.5–189','Sparse classroom voicing; gesture wait separately loops quietly']],'arrangementTimes':'original logical timeline; divide by 1.25 for default viewing time'}
(out/'sources.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Rendered full audition arrangement, 152.8 sec at new 1x')

shutil.rmtree(work)
