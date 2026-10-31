const chapterLinks = [...document.querySelectorAll('aside nav a')];
const chapters = [...document.querySelectorAll('.chapter')];
let scheduled = false;
function updateReading() {
 const distance = document.documentElement.scrollHeight - innerHeight;
 document.querySelector('.progress').style.width = `${distance > 0 ? Math.min(100, Math.max(0, scrollY / distance * 100)) : 0}%`;
 const current = chapters.filter(section => section.getBoundingClientRect().top < innerHeight * .42).at(-1);
 chapterLinks.forEach(link => { const active = link.hash === `#${current?.id}`; link.classList.toggle('active', active); if(active) link.setAttribute('aria-current','location'); else link.removeAttribute('aria-current'); });
 scheduled = false;
}
addEventListener('scroll',()=>{if(!scheduled){scheduled=true;requestAnimationFrame(updateReading);}}, {passive:true});
addEventListener('resize',updateReading);updateReading();
const screenPair=document.querySelector('.ui-pair');
document.querySelectorAll('[data-screen-switch]').forEach(button=>button.addEventListener('click',()=>{
 screenPair.dataset.activeScreen=button.dataset.screenSwitch;
 document.querySelectorAll('[data-screen-switch]').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));
}));
const pathSteps=[
 {title:'成长中心',kind:'原界面',image:'growth-home.webp',alt:'成长中心完整界面',explanation:'从成长中心进入灵玛乐园。'},
 {title:'动画内容',kind:'原界面',image:'growth-library.webp',alt:'灵玛乐园完整内容界面',explanation:'在动画内容中选择好习惯养成系列。'},
 {title:'动画详情',kind:'原界面',image:'growth-detail.webp',alt:'动画系列详情完整界面',explanation:'从系列详情选择具体剧集。'},
 {title:'播放动画',kind:'原动画素材',video:true,explanation:'以刷牙主题动画说明内容与后续任务的承接。'},
 {title:'设置成长目标',kind:'方案示意',image:'goal-settings.webp',alt:'补画示意：设置成长目标完整界面',explanation:'动画后的目标承接方案：确认目标，按需调整重复日期与提醒时间。'},
 {title:'查看目标',kind:'方案示意',image:'goal-added.webp',alt:'补画示意：已添加成长目标完整界面',explanation:'查看已添加的目标。后续提醒、实际行动与家长核验仍是执行链的一部分。'}
];
const pathButtons=[...document.querySelectorAll('[data-path-step]')];
const video=document.querySelector('#path-video');
const pathImage=document.querySelector('#path-image');
const expand=document.querySelector('#path-expand');
let pathIndex=0;
function selectPath(index){
 if(index<0||index>=pathSteps.length)return;
 pathIndex=index;video.pause();const step=pathSteps[index];
 pathButtons.forEach((button,i)=>button.setAttribute('aria-pressed',String(i===index)));
 document.querySelector('#path-title').textContent=step.title;
 document.querySelector('#path-kind').textContent=step.kind;
 document.querySelector('#path-explanation').textContent=step.explanation;
 expand.hidden=Boolean(step.video);video.hidden=!step.video;
 if(!step.video){const src=`./assets/${step.image}?v=story6`;pathImage.src=src;pathImage.alt=step.alt;expand.dataset.image=src;expand.dataset.caption=`${step.title} · ${step.kind}`;}
 document.querySelector('#path-prev').disabled=index===0;
 document.querySelector('#path-next').disabled=index===pathSteps.length-1;
 requestAnimationFrame(updateReading);
}
pathButtons.forEach((button,index)=>{
 button.addEventListener('click',()=>selectPath(index));
 button.addEventListener('keydown',event=>{
  let next;
  if(event.key==='ArrowDown'||event.key==='ArrowRight')next=Math.min(pathSteps.length-1,index+1);
  if(event.key==='ArrowUp'||event.key==='ArrowLeft')next=Math.max(0,index-1);
  if(event.key==='Home')next=0;if(event.key==='End')next=pathSteps.length-1;
  if(next!==undefined){event.preventDefault();selectPath(next);pathButtons[next].focus();}
 });
});
document.querySelector('#path-prev').addEventListener('click',()=>selectPath(pathIndex-1));
document.querySelector('#path-next').addEventListener('click',()=>selectPath(pathIndex+1));
const dialog=document.querySelector('.image-dialog');const expanded=document.querySelector('#expanded-image');let imageTrigger;
document.addEventListener('click',event=>{
 const button=event.target.closest('[data-image]');if(!button)return;
 imageTrigger=button;expanded.src=button.dataset.image;expanded.alt=button.querySelector('img').alt;
 document.querySelector('#image-caption').textContent=button.dataset.caption;dialog.showModal();dialog.scrollTop=0;document.body.classList.add('no-scroll');
});
document.querySelector('#image-close').addEventListener('click',()=>dialog.close());
dialog.addEventListener('click',event=>{if(event.target===dialog){const r=dialog.getBoundingClientRect();if(event.clientX<r.left||event.clientX>r.right||event.clientY<r.top||event.clientY>r.bottom)dialog.close();}});
dialog.addEventListener('close',()=>{document.body.classList.remove('no-scroll');imageTrigger?.focus();});
document.querySelectorAll('details').forEach(details=>details.addEventListener('toggle',()=>requestAnimationFrame(updateReading)));
