const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('on');io.unobserve(e.target)}}),{threshold:.12});
document.querySelectorAll('.rv').forEach(el=>io.observe(el));
const b=document.querySelector('.burger');if(b)b.onclick=()=>document.querySelector('nav ul').classList.toggle('open');
document.querySelectorAll('nav ul a').forEach(a=>a.onclick=()=>document.querySelector('nav ul').classList.remove('open'));
const clk=document.getElementById('clk');if(clk)setInterval(()=>clk.textContent=new Date().toISOString().slice(11,19)+'Z',1000);
document.querySelectorAll('.dive .bg').forEach(bg=>{addEventListener('scroll',()=>{const r=bg.parentElement.getBoundingClientRect();if(r.bottom>0&&r.top<innerHeight)bg.style.transform=`translateY(${r.top*-0.12}px)`},{passive:true})});
const f=document.getElementById('pf');if(f)f.onsubmit=e=>{e.preventDefault();document.getElementById('fmsg').textContent='> TRANSMISSION QUEUED (DEMO). Direct intake channel opens soon. No data was sent.'};
