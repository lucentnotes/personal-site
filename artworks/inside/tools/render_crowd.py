"""Generate a wordless, speech-like crowd bed; no dialogue or external recording."""
import numpy as np,soundfile as sf
import subprocess,tempfile
from pathlib import Path
rng=np.random.default_rng(77);sr=24000;seconds=10;n=int(sr*seconds);out=np.zeros(n)
vowels=[(470,1350,2600),(530,1700,2650),(320,2150,2900),(430,900,2450),(310,950,2300)]
for voice in range(7):
 pos=rng.uniform(0,.45);base=rng.uniform(115,230)
 while pos<seconds:
  duration=rng.uniform(.13,.34);count=int(duration*sr);tt=np.arange(count)/sr;pitch=base*(1+.065*np.sin(tt*rng.uniform(7,14)+rng.uniform(0,6)))
  phase=2*np.pi*np.cumsum(pitch)/sr;v=np.zeros(count);f1,f2,f3=vowels[rng.integers(len(vowels))]
  for k in range(1,27):
   freq=base*k;weight=(.65*np.exp(-((freq-f1)/190)**2)+.30*np.exp(-((freq-f2)/260)**2)+.10*np.exp(-((freq-f3)/360)**2))/(k**.4)
   v+=weight*np.sin(k*phase+rng.uniform(-.1,.1))
  v+=rng.normal(0,.025,count);envelope=np.sin(np.linspace(0,np.pi,count))**.65;v*=envelope*rng.uniform(.1,.24)
  begin=int(pos*sr);length=min(count,n-begin)
  if length>0:out[begin:begin+length]+=v[:length]
  pos+=duration+rng.uniform(.045,.22)
for delay,gain in [(0.073,.13),(.139,.10),(.211,.065)]:
 shift=int(delay*sr);out[shift:]+=out[:-shift]*gain
# Remove rumble and high-frequency hiss, then make a soft loop boundary.
f=np.fft.rfftfreq(n,1/sr);spectrum=np.fft.rfft(out);spectrum*=1/(1+(160/np.maximum(f,1))**6)*1/(1+(f/2300)**6);out=np.fft.irfft(spectrum,n)
fade=int(.05*sr);out[:fade]*=np.linspace(0,1,fade);out[-fade:]*=np.linspace(1,0,fade);out*=.78/np.max(np.abs(out))
root=Path(__file__).resolve().parents[1]
with tempfile.TemporaryDirectory() as tmp:
 p=Path(tmp)/'murmur.wav';sf.write(p,out,sr,subtype='PCM_16')
 subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-i',str(p),'-codec:a','libmp3lame','-b:a','96k',str(root/'assets/ballroom-murmur.mp3')],check=True)
print('Synthesized wordless crowd bed',seconds,'seconds')
