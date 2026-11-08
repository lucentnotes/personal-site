'use strict';
const actDirectory=document.getElementById('actDirectory'),actMenu=document.getElementById('actsMenu'),directoryShade=document.getElementById('directoryShade');
const isEnglish=document.documentElement.lang==='en';

if(isEnglish){document.querySelector('.menu-caption').textContent='Act I';document.getElementById('directoryTitle').textContent='Eight acts / Contents';document.getElementById('closeDirectory').textContent='Close ×';document.querySelector('.directory-intro').textContent='From an empty place to somewhere else.';document.querySelectorAll('.act-title').forEach(e=>e.textContent=e.dataset.en);document.querySelectorAll('.act-state').forEach((e,i)=>e.textContent=i?'To come':'Available ↗');document.querySelector('.reading-marker span:last-child').textContent='A Place Left Empty';}
let resumeAfterDirectory=false;
function showDirectory(open){if(open){resumeAfterDirectory=filmInspection.state.playing;if(resumeAfterDirectory)document.getElementById('play').click();}else if(resumeAfterDirectory&&!filmInspection.state.playing&&document.getElementById('cover').style.display==='none'){document.getElementById('play').click();}actDirectory.hidden=!open;directoryShade.hidden=!open;actMenu.setAttribute('aria-expanded',String(open));document.body.classList.toggle('directory-open',open);document.body.classList.remove('is-idle');if(open){document.getElementById('closeDirectory').focus();}else actMenu.focus();}
actMenu.addEventListener('click',()=>showDirectory(actDirectory.hidden));document.getElementById('closeDirectory').addEventListener('click',()=>showDirectory(false));directoryShade.addEventListener('click',()=>showDirectory(false));document.addEventListener('keydown',e=>{if(e.key==='Escape'&&!actDirectory.hidden){showDirectory(false);e.stopPropagation();}});
document.querySelector('[data-act="0"]').addEventListener('click',()=>{document.getElementById('start').click();showDirectory(false);});
document.querySelectorAll('.chapters button').forEach(e=>e.addEventListener('click',()=>showDirectory(false)));
let idleTimer;function awaken(){document.body.classList.remove('is-idle');clearTimeout(idleTimer);idleTimer=setTimeout(()=>{if(document.body.classList.contains('has-started')&&actDirectory.hidden&&speedOptions.hidden)document.body.classList.add('is-idle');},3500);}
['pointermove','pointerdown','keydown'].forEach(type=>document.addEventListener(type,awaken,{passive:true}));
setInterval(()=>{const state=window.filmInspection.state;document.body.classList.toggle('has-started',state.t>0||state.playing||document.getElementById('cover').style.display==='none');document.getElementById('pauseWord').textContent=isEnglish?(state.playing?'Pause':'Continue'):(state.playing?'暂停':'继续');},150);
window.addEventListener('pageshow',e=>{if(e.persisted){showDirectory(false);document.body.classList.remove('has-started','is-idle');}});

document.addEventListener('keydown',event=>{if(event.key!=='Tab'||actDirectory.hidden)return;const items=[...actDirectory.querySelectorAll('button:not(:disabled),summary')].filter(e=>e.getClientRects().length);const first=items[0],last=items[items.length-1];if(event.shiftKey&&document.activeElement===first){event.preventDefault();last.focus();}else if(!event.shiftKey&&document.activeElement===last){event.preventDefault();first.focus();}});

const speedToggle=document.getElementById('speedToggle'),speedOptions=document.getElementById('speedOptions');
if(isEnglish){speedToggle.firstChild.textContent='Speed ';speedOptions.ariaLabel='Playback speed';speedOptions.querySelectorAll('button').forEach(b=>b.title='Select again to return to 1x');}
function closeSpeed(){speedOptions.hidden=true;speedToggle.setAttribute('aria-expanded','false');document.body.classList.remove('speed-open');}
speedToggle.addEventListener('click',()=>{const open=speedOptions.hidden;speedOptions.hidden=!open;speedToggle.setAttribute('aria-expanded',String(open));document.body.classList.toggle('speed-open',open);});
speedOptions.querySelectorAll('button').forEach(button=>button.addEventListener('click',()=>{const rate=Number(button.dataset.rate);filmInspection.setPlaybackRate(filmInspection.state.playbackRate===rate?1:rate);closeSpeed();speedToggle.focus();}));
window.addEventListener('filmratechange',event=>{const rate=event.detail;document.getElementById('speedValue').textContent=rate+'x';speedOptions.querySelectorAll('button').forEach(b=>b.setAttribute('aria-pressed',String(Number(b.dataset.rate)===rate)));});
document.addEventListener('pointerdown',event=>{if(!event.target.closest('.speed-control'))closeSpeed();});
document.addEventListener('keydown',event=>{if(event.key==='Escape'&&!speedOptions.hidden){closeSpeed();speedToggle.focus();}});
window.addEventListener('pageshow',event=>{if(event.persisted)closeSpeed();});

if(isEnglish){document.querySelector('#ending .ending-act').textContent='ACT II';document.querySelector('#ending .ending-name').textContent='A Room on Paper';document.getElementById('replay').innerHTML='Watch again'+document.getElementById('replay').querySelector('svg').outerHTML;document.getElementById('nextAct').textContent='To be continued';document.getElementById('nextAct').ariaLabel='Act II is not available yet';}
setInterval(()=>document.body.classList.toggle('is-ending',filmInspection.state.finished),100);
