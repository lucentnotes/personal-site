from pathlib import Path
import subprocess,json,re,time
source=Path('/workspace/work/video-export/capture.mkv');raw=source.with_name('zh.webm')
if raw.exists() and (not source.exists() or raw.stat().st_mtime>source.stat().st_mtime):
 subprocess.run(['ffmpeg','-y','-v','error','-i',str(raw),'-c','copy',str(source)],check=True)
dest=Path('/workspace/inside-web/artworks/inside/exports');last=0
for _ in range(100):
 if source.exists() and source.stat().st_size>1000000 and time.time()-source.stat().st_mtime>3:break
 time.sleep(3)
else:raise SystemExit('No complete recording')
probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(source)]));assert float(probe['format']['duration'])>160;assert any(s['codec_type']=='audio' for s in probe['streams'])
print('Recording received:',source.stat().st_size,probe['format']['duration'],flush=True)
analysis=subprocess.run(['ffmpeg','-hide_banner','-i',str(source),'-vn','-af','loudnorm=I=-20:TP=-1.5:LRA=11:print_format=json','-f','null','-'],capture_output=True,text=True,check=True)
m=json.JSONDecoder().raw_decode(analysis.stderr[analysis.stderr.rfind('{'):])[0];flt='loudnorm=I=-20:TP=-1.5:LRA=11:measured_I='+m['input_i']+':measured_TP='+m['input_tp']+':measured_LRA='+m['input_lra']+':measured_thresh='+m['input_thresh']+':offset='+m['target_offset']+':linear=true:print_format=summary'
mp4=dest/'Inside-Act-I-ZH-1080p.mp4'
subprocess.run(['ffmpeg','-y','-hide_banner','-loglevel','error','-i',str(source),'-c:v','libx264','-preset','fast','-crf','22','-pix_fmt','yuv420p','-vf','fade=t=out:st='+str(float(probe['format']['duration'])-1.5)+':d=1.5','-r','30','-af',flt,'-c:a','aac','-b:a','192k','-ar','48000','-movflags','+faststart','-metadata','title=里面有人 · 第一幕：空出来的位置','-metadata','artist=借我800到火星',str(mp4)],check=True)
subprocess.run(['ffmpeg','-y','-v','error','-ss','2','-i',str(mp4),'-frames:v','1',str(dest/'cover.jpg')],check=True)
result=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(mp4)]));(dest/'video-info.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
(dest/'render-notes.json').write_text(json.dumps({'language':'zh','author':'借我800到火星','export':'1920x1080, H264, AAC, 30fps','nativeAnimationClockSpeed':1.25,'linearAdaptation':'3.5 sec title, automatic 2.6 sec notebook gesture, 12 sec ending/credits; website UI removed','audio':'Live Web Audio master with score, foley, ambience and local crowd recording; two-pass loudness adjustment to -20 LUFS / -1.5 dBTP','source':'Current Act I with corrected notebook demonstration drawing','sourceWebmSeconds':probe['format']['duration'],'outputBytes':mp4.stat().st_size,'loudnessInput':m},ensure_ascii=False,indent=2))
print('MP4 ready:',mp4,mp4.stat().st_size,flush=True)
