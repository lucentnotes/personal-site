const viewer=document.querySelector('#viewer');
document.querySelectorAll('[data-image]').forEach(b=>b.addEventListener('click',()=>{const img=viewer.querySelector('img');img.src=b.dataset.image;img.alt=b.querySelector('img').alt;viewer.showModal()}));
document.querySelector('#close').addEventListener('click',()=>viewer.close());
viewer.addEventListener('click',e=>{if(e.target===viewer)viewer.close()});
const observer=new IntersectionObserver(entries=>{for(const e of entries)if(e.isIntersecting){document.querySelectorAll('nav a').forEach(a=>a.classList.toggle('active',a.hash==='#'+e.target.id))}},{rootMargin:'-10% 0px -65% 0px'});
document.querySelectorAll('.body>section').forEach(s=>observer.observe(s));

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
const altRecords=[...document.querySelectorAll("main img")].map(node=>({node,zh:node.alt,en:node.dataset.altEn||imageAltByFile[node.getAttribute("src").split("/").pop()]||node.alt}));
const attrRecords=[
 {node:document.querySelector('.skip'),key:'aria-label',zh:'跳到正文',en:'Skip to content'},
 {node:document.querySelector('nav'),key:'aria-label',zh:'案例目录',en:'Case study contents'},
 {node:viewer,key:'aria-label',zh:'图片放大预览',en:'Enlarged image preview'},
 {node:document.querySelector('meta[name="description"]'),key:'content',zh:document.querySelector('meta[name="description"]').content,en:'Gaming the System: a team course project exploring assessment through game mechanics, prototyping and iteration.'}
];
function setLanguage(lang){
 lang=lang==='en'?'en':'zh';
 document.documentElement.lang=lang==='en'?'en':'zh-CN';
 for(const r of textRecords)r.node.nodeValue=r[lang];
 for(const r of altRecords)r.node.alt=r[lang];
 for(const r of attrRecords)r.node.setAttribute(r.key,r[lang]);
 document.querySelectorAll('[data-lang]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.lang===lang)));
 try{localStorage.setItem('gts-case-language',lang)}catch{}
}
document.querySelectorAll('[data-lang]').forEach(b=>b.addEventListener('click',()=>setLanguage(b.dataset.lang)));
let initialLanguage='zh';try{initialLanguage=localStorage.getItem('gts-case-language')||'zh'}catch{}
setLanguage(initialLanguage);
