(function(){var b=document.querySelector('.burger'),n=document.querySelector('.nav');
if(b)b.addEventListener('click',function(){var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o)});
document.querySelectorAll('.ddbtn').forEach(function(x){x.addEventListener('click',function(){var o=x.parentNode.classList.toggle('open');x.setAttribute('aria-expanded',o)})});
var f=document.getElementById('brief');if(f)f.addEventListener('submit',function(e){e.preventDefault();var d=new FormData(f);
var body='Name: '+d.get('name')+'\nOrganization: '+d.get('org')+'\nReply-to: '+d.get('email')+'\nInterest: '+d.get('sys')+'\n\n'+d.get('msg');
var u='https://github.com/charlesanthonyleone/remote-robotics/issues/new?title='+encodeURIComponent('Briefing request: '+d.get('sys')+' ('+d.get('org')+')')+'&body='+encodeURIComponent(body);
document.getElementById('formnote').innerHTML='Your request is drafted. <a class="link" href="'+u+'" target="_blank" rel="noopener">Review and submit it on GitHub →</a> (GitHub issues are public; do not include sensitive information.)';});
})();
(function(){var d=document.documentElement;d.classList.add('js');
var u=document.getElementById('utc'),s=document.getElementById('scr');
function t(){if(u)u.textContent=new Date().toISOString().substr(11,8)}t();setInterval(t,1000);
function sc(){var h=d.scrollHeight-innerHeight;if(s)s.textContent=String(Math.round(h>0?scrollY/h*100:0)).padStart(3,'0')}addEventListener('scroll',sc,{passive:true});sc();
var els=document.querySelectorAll('main .sec .wrap > *, .status .wrap');
if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{rootMargin:'0px 0px -8% 0px'});
els.forEach(function(e){e.classList.add('fade');io.observe(e)})}
document.querySelectorAll('.hp').forEach(function(h){h.addEventListener('click',function(){var o=h.classList.contains('open');document.querySelectorAll('.hp.open').forEach(function(x){x.classList.remove('open')});if(!o)h.classList.add('open')})});
})();
