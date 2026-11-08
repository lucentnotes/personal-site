from pathlib import Path
import numpy as np,subprocess,wave,json,hashlib,sys,tempfile,shutil
r=Path(__file__).resolve().parents[1];out=r/'licensed-score';out.mkdir(exist_ok=True);sr=22050
inputdir=Path(sys.argv[1]);work=Path(tempfile.mkdtemp(prefix='licensed-score-'))
tracks={}
for name in ['reverie','moonlight']:
 p=inputdir/(name+'.mp3');tracks[name]=np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',str(p),'-f','f32le','-ac','2','-ar',str(sr),'-']),dtype='<f4').reshape(-1,2)
def ease(x):x=np.clip(x,0,1);return x*x*(3-2*x)
# The new 1x clock is 1.25 times the old animation clock; music remains at its recorded tempo.
seconds=191/1.25;edit=np.zeros((round(seconds*sr),2),np.float32)
def place(name,start,source,duration,fadein,fadeout,gain):
 n=round(duration*sr);a=round(start*sr);v=tracks[name][round(source*sr):round(source*sr)+n].copy();tt=np.arange(len(v))/sr
 e=ease(tt/fadein) if fadein else np.ones(len(v));e*=1-ease((tt-(duration-fadeout))/fadeout)
 edit[a:a+len(v)]+=v*e[:,None]*gain
place('reverie',0,0,121.5/1.25,3/1.25,(121.5-114.2)/1.25,.72)
place('moonlight',145.45/1.25,1.8,seconds-145.45/1.25,.08,2,.88)
for name,audio in [('edit',edit)]:
 wav=work/(name+'.wav')
 with wave.open(str(wav),'wb')as w:w.setnchannels(2);w.setsampwidth(2);w.setframerate(sr);w.writeframes((np.clip(audio,-1,1)*32767).astype('<i2').tobytes())
 if name=='hold':
  subprocess.run(['ffmpeg','-y','-v','error','-i',str(wav),'-b:a','128k',str(out/'hold.mp3')],check=True);continue
 for ui,suffix in [(.8,'original-clock'),(1,'125'),(1.25,'15625'),(1.5,'1875'),(2,'25')]:
  cmd=['ffmpeg','-y','-v','error','-i',str(wav)]
  if ui!=1:cmd+=['-af',f'atempo={ui}']
  subprocess.run(cmd+['-b:a','128k',str(out/f'score-{suffix}.mp3')],check=True)
d={'previewOnly':True,'author':'Scott Buckley','license':'CC-BY-4.0','licenseURL':'https://creativecommons.org/licenses/by/4.0/','checkedDate':'2026-11-08','permittedUseEvidence':'Both individual track pages explicitly allow adaptation and project use, including commercial, with attribution.','authorUsageURL':'https://www.scottbuckley.com.au/library/using-this-music/','credits':[],'edits':'Excerpts, gain reduction, fades, pause for shop/phone/ballroom, and pitch-preserving speed variants. New 1x preserves recorded tempo. Cue timing unchanged; musical attack belongs to the new piece, not the old first chord.','cueSheet':[{'track':'Reverie','sourceSeconds':[0,97.2],'logicalTimeline':[0,121.5],'purpose':'Everyday distance; continuous musical phrasing, no repeated loop'},{'track':'Moonlight','sourceSeconds':[1.8,38.24],'logicalTimeline':[145.45,191],'purpose':'Memory returns at neck-touch; a contrasting recorded piano/string cue'}]}
for name,title in [('reverie','Reverie'),('moonlight','Moonlight')]:
 d['credits'].append({'title':title,'attribution':f"'{title}' by Scott Buckley – released under CC-BY 4.0. www.scottbuckley.com.au",'officialSource':f'https://www.scottbuckley.com.au/library/{name}/','downloadMirror':f'https://raw.githubusercontent.com/shuangboxu/alpenruhe/9b0c29f82764159630ce875537f9fa70e3d538ab/public/assets/audio/music/sb_{name}.mp3','sourceFileSHA256':hashlib.sha256((inputdir/(name+'.mp3')).read_bytes()).hexdigest()})
(out/'sources.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');print('Two-cue licensed film edit rendered')

shutil.rmtree(work)
