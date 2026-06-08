/* FengChou bilingual site — scroll reveal + Word of the Day audio/video */
(function(){
  /* ---- scroll reveal ---- */
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(!reduce){
    document.documentElement.classList.add('reveal-on');
    var sel='.pillar,.life-card,.pband,.ncard,.vc,.commit,.curriculum-card,.trophy,.station,.about-text,.lineage,.principal-card,.gallery figure';
    var els=[].slice.call(document.querySelectorAll(sel));
    els.forEach(function(el){el.classList.add('reveal');});
    var show=function(el){el.classList.add('in');};
    if('IntersectionObserver' in window){
      var io=new IntersectionObserver(function(en){en.forEach(function(e){
        if(!e.isIntersecting)return;
        var sibs=[].slice.call(e.target.parentNode.children).filter(function(n){return n.classList.contains('reveal');});
        e.target.style.transitionDelay=(Math.max(0,sibs.indexOf(e.target))*70)+'ms';
        show(e.target); io.unobserve(e.target);
      });},{threshold:0.12,rootMargin:'0px 0px -6% 0px'});
      els.forEach(function(el){io.observe(el);});
      /* safety net: never leave content hidden */
      setTimeout(function(){els.forEach(show);},3000);
    } else { els.forEach(show); }
  }

  /* ---- Word of the Day: speak (Web Speech) + play video INLINE ---- */
  function speak(text){
    if(!('speechSynthesis' in window)){return;}
    try{
      window.speechSynthesis.cancel();
      var u=new SpeechSynthesisUtterance(text);
      u.lang='en-US'; u.rate=0.9;
      window.speechSynthesis.speak(u);
    }catch(e){}
  }
  document.addEventListener('click',function(ev){
    var b=ev.target.closest('[data-speak]');
    if(b){ speak(b.getAttribute('data-speak')); return; }

    /* Play the video INLINE inside the card — never pop out to YouTube */
    var v=ev.target.closest('[data-vid]');
    if(v){
      ev.preventDefault();
      var card=v.closest('.vc');
      var box=card && card.querySelector('.vc__embed');
      if(box && !box.dataset.loaded){
        var id=v.getAttribute('data-vid');
        box.innerHTML='<iframe src="https://www.youtube-nocookie.com/embed/'+id+'?autoplay=1&rel=0&playsinline=1" title="Word of the Day video" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>';
        box.dataset.loaded='1';
        box.classList.add('on');
        v.textContent='▶ Playing below';
        v.classList.add('is-playing');
      } else if(box){
        box.scrollIntoView({behavior:'smooth',block:'nearest'});
      }
    }
  });
})();
