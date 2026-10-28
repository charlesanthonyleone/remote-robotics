(function(){var b=document.querySelector('.burger'),n=document.querySelector('.nav');
if(b)b.addEventListener('click',function(){var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o)});
document.querySelectorAll('.ddbtn').forEach(function(x){x.addEventListener('click',function(){var o=x.parentNode.classList.toggle('open');x.setAttribute('aria-expanded',o)})});
var f=document.getElementById('brief');if(f)f.addEventListener('submit',function(e){e.preventDefault();var d=new FormData(f);
var body='Name: '+d.get('name')+'\nOrganization: '+d.get('org')+'\nReply-to: '+d.get('email')+'\nInterest: '+d.get('sys')+'\n\n'+d.get('msg');
var u='https://github.com/charlesanthonyleone/remote-robotics/issues/new?title='+encodeURIComponent('Briefing request: '+d.get('sys')+' ('+d.get('org')+')')+'&body='+encodeURIComponent(body);
document.getElementById('formnote').innerHTML='Your request is drafted. <a class="link" href="'+u+'" target="_blank" rel="noopener">Review and submit it on GitHub →</a> (GitHub issues are public; do not include sensitive information.)';});
})();
