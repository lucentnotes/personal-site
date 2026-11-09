const viewer=document.querySelector('#viewer');
document.querySelectorAll('[data-image]').forEach(b=>b.addEventListener('click',()=>{const img=viewer.querySelector('img');img.src=b.dataset.image;img.alt=b.querySelector('img').alt;viewer.showModal()}));
document.querySelector('#close').addEventListener('click',()=>viewer.close());
viewer.addEventListener('click',e=>{if(e.target===viewer)viewer.close()});
function updateSectionNavigation(){
 const sections=[...document.querySelectorAll('.body>section')];
 const nav=document.querySelector('.case-nav');
 const threshold=(nav?.getBoundingClientRect().height||0)+25;
 let current=sections[0];
 for(const section of sections){if(section.getBoundingClientRect().top<=threshold)current=section;else break;}
 document.querySelectorAll('.case-nav a').forEach(link=>link.classList.toggle('active',link.hash==='#'+current.id));
}
let navFrame=false;
function scheduleSectionNavigation(){if(navFrame)return;navFrame=true;requestAnimationFrame(()=>{navFrame=false;updateSectionNavigation()})}
window.addEventListener('scroll',scheduleSectionNavigation,{passive:true});
window.addEventListener('resize',scheduleSectionNavigation);
document.addEventListener('toggle',scheduleSectionNavigation,true);
document.fonts.ready.then(scheduleSectionNavigation);
scheduleSectionNavigation();

// Keep both languages on the same page, including headings, captions and controls.
const textRecords=[];
const walker=document.createTreeWalker(document.documentElement,NodeFilter.SHOW_TEXT);
while(walker.nextNode()){
 const node=walker.currentNode;
 if(['SCRIPT','STYLE'].includes(node.parentElement.tagName))continue;
 if(Object.hasOwn(translations,node.nodeValue))textRecords.push({node,zh:node.nodeValue,en:translations[node.nodeValue]});
}
const altEnglish=[
 'Game scene: a student checking assessment criteria',
 'Historical prototype for adjusting and confirming assessment weights',
 'Earlier results preview showing percentage growth',
 'Later results preview showing the selected metric as a checked card',
 'A prototype screen from the handoff guide',
 'Branching flowchart from the mechanism document',
 'Original written mechanism explanation',
 'Team review record showing an issue screen and proposed changes'
];
const imageAltByFile={"cinematic.png": "Game scene: a student checking assessment criteria", "weights-editor.png": "Historical prototype for adjusting and confirming assessment weights", "before.png": "Earlier results preview showing percentage growth", "after.png": "Later results preview showing the selected metric as a checked card", "document-131.jpeg": "A prototype screen from the handoff guide", "document-129.jpeg": "Branching flowchart from the mechanism document", "document-130.jpeg": "Original written mechanism explanation", "document-142.jpeg": "Team review record showing an issue screen and proposed changes"};
const altRecords=[...document.querySelectorAll("main img, #record-viewer img")].map(node=>({node,zh:node.alt,en:node.dataset.altEn||imageAltByFile[node.getAttribute("src").split("/").pop()]||node.alt}));
const attrRecords=[
 {node:document.querySelector('#record-viewer'),key:'aria-label',zh:'补充材料',en:'Supporting material'},
 {node:document.querySelector('.skip'),key:'aria-label',zh:'跳到正文',en:'Skip to content'},
 {node:document.querySelector('nav'),key:'aria-label',zh:'案例目录',en:'Case study contents'},
 {node:viewer,key:'aria-label',zh:'图片放大预览',en:'Enlarged image preview'},
 {node:document.querySelector('meta[name="description"]'),key:'content',zh:document.querySelector('meta[name="description"]').content,en:'Gaming the System: a team course project exploring assessment through game mechanics, prototyping and iteration.'}
];
function setLanguage(lang){
 lang=lang==='en'?'en':'zh';
 document.documentElement.lang=lang==='en'?'en':'zh-CN';
 scheduleSectionNavigation();
 for(const r of textRecords)r.node.nodeValue=r[lang];
 for(const r of altRecords)r.node.alt=r[lang];
 for(const r of attrRecords)r.node.setAttribute(r.key,r[lang]);
 document.querySelectorAll('[data-lang]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.lang===lang)));
 try{localStorage.setItem('gts-case-language',lang)}catch{}
}
document.querySelectorAll('[data-lang]').forEach(b=>b.addEventListener('click',()=>setLanguage(b.dataset.lang)));
const initialLanguage = new URLSearchParams(location.search).get('lang') === 'zh' ? 'zh' : 'en';
setLanguage(initialLanguage);

const recordViewer=document.querySelector('#record-viewer');
document.querySelectorAll('[data-record]').forEach(button=>button.addEventListener('click',()=>{
 document.querySelectorAll('[data-record-sheet]').forEach(sheet=>sheet.hidden=sheet.dataset.recordSheet!==button.dataset.record);
 recordViewer.showModal();recordViewer.scrollTop=0;
}));
document.querySelector('#close-record').addEventListener('click',()=>recordViewer.close());
recordViewer.addEventListener('click',event=>{if(event.target===recordViewer)recordViewer.close()});
