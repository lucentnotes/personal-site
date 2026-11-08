"""Render an original, restrained piano sketch using the installed General MIDI piano."""
import ctypes as C,ctypes.util,wave,pathlib,numpy as np
lib=C.CDLL(ctypes.util.find_library('fluidsynth'))
def bind(name,args,result):
 f=getattr(lib,name);f.argtypes=args;f.restype=result;return f
ptr=C.c_void_p;I=C.c_int;D=C.c_double;S=C.c_char_p
settings=bind('new_fluid_settings',[],ptr)()
bind('fluid_settings_setnum',[ptr,S,D],I)(settings,b'synth.sample-rate',22050.)
bind('fluid_settings_setnum',[ptr,S,D],I)(settings,b'synth.gain',.52)
bind('fluid_settings_setnum',[ptr,S,D],I)(settings,b'synth.reverb.room-size',.65)
bind('fluid_settings_setnum',[ptr,S,D],I)(settings,b'synth.reverb.level',.22)
synth=bind('new_fluid_synth',[ptr],ptr)(settings)
bind('fluid_synth_sfload',[ptr,S,I],I)(synth,b'/usr/share/sounds/sf2/TimGM6mb.sf2',1)
bind('fluid_synth_program_change',[ptr,I,I],I)(synth,0,0)
on=bind('fluid_synth_noteon',[ptr,I,I,I],I);off=bind('fluid_synth_noteoff',[ptr,I,I],I)
write=bind('fluid_synth_write_float',[ptr,I,ptr,I,I,ptr,I,I],I)
# 54 bpm; open, sparse D-minor / B-flat / F / suspended-A voicings.
beat=60/54;bar=beat*4;events=[]
chords=[(38,57,62,65),(34,53,58,62),(41,57,60,65),(33,55,60,64)]
melodies=[[69,65,64,62],[65,62,60,62],[69,67,65,64],[64,62,60,57],[62,64,65,69],[65,64,62,60],[60,62,65,64],[64,62,61,62]]
def note(at,key,vel,length):events.extend([(at,1,key,vel),(at+length,0,key,0)])
for n in range(16):
 at=n*bar;chord=chords[(n//2)%4]
 note(at+.05,chord[0],39,bar*1.7)
 for j,key in enumerate(chord[1:]):note(at+.18+j*.17,key,30+j*2,bar*.95)
 if n%2==0:
  m=melodies[(n//2)%len(melodies)]
  for j,key in enumerate(m):note(at+.48+j*beat*1.65,key,47-(j%3)*3,beat*1.8)
 else:
  note(at+beat*2.5,chord[-1]+12,32,beat*2)
sr=22050;cycle=16*bar;length=cycle+12;out=np.zeros((int(sr*length),2),np.float32);events.sort();cursor=0
for at,kind,key,velocity in events+[(length,0,0,0)]:
 end=min(len(out),int(at*sr));count=end-cursor
 if count>0:
  l=np.empty(count,np.float32);r=np.empty(count,np.float32);write(synth,count,l.ctypes.data,0,1,r.ctypes.data,0,1);out[cursor:end,0]=l;out[cursor:end,1]=r;cursor=end
 if key:
  (on(synth,0,key,velocity) if kind else off(synth,0,key))
# Fold decaying piano tails into the start so the waveform can repeat without a silent ending.
period=round(cycle*sr);tail=out[period:].copy();out=out[:period].copy();out[:len(tail)]+=tail
peak=np.max(np.abs(out));out*=.79/max(peak,.001)
p=pathlib.Path('/workspace/work/inside-piano.wav')
with wave.open(str(p),'wb')as w:w.setnchannels(2);w.setsampwidth(2);w.setframerate(sr);w.writeframes((np.clip(out,-1,1)*32767).astype('<i2').tobytes())
print('Loopable piano sketch rendered:',cycle,'seconds; peak',float(np.max(np.abs(out))))
