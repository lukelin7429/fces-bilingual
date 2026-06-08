/* FengChou Festival English — always show a "Back to FengChou" bar at the top.
   (Self-contained under fces.taiwan-bilingual.org; links back to the school home.) */
(function(){
  function inject(){
    if(document.querySelector('.schoolbar'))return;
    var css=document.createElement('style');
    css.textContent='.schoolbar{background:#1F3A5F;color:#fff;padding:11px 22px;'+
      "font-family:'Lato','PingFang TC','Apple LiGothic Medium','Microsoft JhengHei',sans-serif;"+
      'font-size:16px;letter-spacing:.3px;display:flex;align-items:center;justify-content:center;gap:10px;'+
      'box-shadow:inset 0 -3px 0 #13283F;line-height:1.4;text-align:center;}'+
      '.schoolbar a{color:#fff;text-decoration:none;font-weight:700;border-bottom:1px solid rgba(255,255,255,.45);padding-bottom:1px;}'+
      '.schoolbar a:hover{border-bottom-color:#fff;}'+
      '.schoolbar .arr{font-size:18px;}'+
      '@media(min-width:720px){.schoolbar{font-size:18px;padding:13px 24px;}}';
    document.head.appendChild(css);
    var bar=document.createElement('div');
    bar.className='schoolbar';
    bar.innerHTML='<a href="/"><span class="arr">←</span> Back to FengChou Elementary · 回豐洲國小首頁</a>';
    document.body.insertAdjacentElement('afterbegin',bar);
  }
  if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',inject);}else{inject();}
})();
