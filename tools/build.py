import json, os, html
B='/remote-robotics/'
SITE='https://charlesanthonyleone.github.io/remote-robotics/'
CR=json.load(open('credits.json'))
NAV=[('systems/','Systems'),('capabilities/','Capabilities'),('about/','About'),('capability-statement/','Capability Statement'),('contact/','Request a Briefing')]
SYS=[('arachne','ARACHNE','Multi-legged climbing robot for hazardous and vertical terrain'),
     ('destrier','DESTRIER','Quadruped logistics carrier for dismounted teams'),
     ('deeplink','DEEPLINK','Immersive teleoperation station for remote and subsea systems'),
     ('hiveforge','HIVEFORGE','Coordinated aerial construction for expeditionary sites')]
def page(path,title,desc,body,active='',img='renders/v3/arachne-studio.jpg'):
    nav=''
    for p,l in NAV:
        cls=' class="active" aria-current="page"' if active==p else ''
        if p=='systems/':
            dd=''.join(f'<a href="{B}systems/{k}/"{" class=\"active\"" if active==f"systems/{k}/" else ""}>{n.title()}</a>' for k,n,_ in SYS)
            a=' class="active"' if active.startswith('systems') else ''
            nav+=f'<div class="dd"><a href="{B}systems/"{a}>Systems</a><button class="ddbtn" aria-label="Show systems" aria-expanded="false">▾</button><div class="ddmenu"><a href="{B}systems/">All systems</a>{dd}</div></div>'
        else:
            nav+=f'<a href="{B}{p}"{cls}{" class=\"cta\"" if p=="contact/" and not cls else ""}>{l}</a>'
    t=f'{title} | Remote Robotics' if title!='Remote Robotics' else 'Remote Robotics | Human-supervised robotics R&D'
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title><meta name="description" content="{desc}"><link rel="canonical" href="{SITE}{path}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Remote Robotics"><meta property="og:title" content="{t}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{SITE}{path}"><meta property="og:image" content="{SITE}{img}"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="{B}favicon.png"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet"><link rel="stylesheet" href="{B}assets/site.css"></head><body>
<div class="dist"><div class="wrap"><span>Distribution: Unclassified // Public release</span><span class="hide-sm">All systems in development · Concept stage (TRL 1–3)</span></div></div>
<header class="hdr"><div class="wrap"><a class="brand" href="{B}"><span class="mark"></span>REMOTE ROBOTICS</a><button class="burger" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button><nav class="nav">{nav}</nav></div></header>
<main>{body}</main>
<footer class="ftr"><div class="wrap fgrid"><div><a class="brand" href="{B}"><span class="mark"></span>REMOTE ROBOTICS</a><p>Early-stage research and development firm for human-supervised robotic systems. United States.</p></div>
<div><h4>Systems</h4>{''.join(f'<a href="{B}systems/{k}/">{n.title()}</a>' for k,n,_ in SYS)}</div>
<div><h4>Company</h4><a href="{B}capabilities/">Capabilities</a><a href="{B}about/">About</a><a href="{B}capability-statement/">Capability statement</a><a href="{B}contact/">Request a briefing</a><a href="{B}credits/">Image credits</a></div></div>
<div class="wrap legal"><p><strong>Forward-looking statement.</strong> This site describes concept-stage systems under development. Descriptions, capabilities and design targets are goals, not demonstrated performance, and may change. Remote Robotics has no contracts, customers or past performance to date. Images marked “Concept render” are AI-generated illustrations; reference photos show third-party or government systems and are not Remote Robotics products. No government endorsement is stated or implied.</p><p>© 2026 Remote Robotics.</p></div></footer>
<script src="{B}assets/site.js"></script></body></html>'''
def write(path,html_):
    d=path.rstrip('/'); 
    f=(d+'/index.html') if d else 'index.html'
    if path=='404': f='404.html'
    os.makedirs(os.path.dirname(f) or '.',exist_ok=True); open(f,'w').write(html_)
def fig(src,cap,cls=''):
    return f'<figure class="{cls}"><img src="{B}{src}" alt="{html.escape(cap)}" loading="lazy"><figcaption><span class="tag">Concept render</span>{cap}</figcaption></figure>'
def ref(key,cap):
    c=[x for x in CR if x['key']==key][0]
    return f'<figure><img src="{B}{c["file"]}" alt="{html.escape(cap)}" loading="lazy"><figcaption><span class="tag ref">Reference photo</span>{cap} Not a Remote Robotics product. <a href="{B}credits/">Credit</a></figcaption></figure>'
CTA=f'''<section class="ctaband"><div class="wrap"><div><h2>Request a briefing or technical package</h2><p>For program officers, grant reviewers and prospective research partners. Controlled technical detail is shared on request, as appropriate.</p></div><a class="btn" href="{B}contact/">Request a briefing</a></div></section>'''
def ph(eyebrow,h,lead): return f'<section class="phead"><div class="wrap"><p class="eyebrow">{eyebrow}</p><h1>{h}</h1><p class="lead">{lead}</p></div></section>'
D={
'arachne':dict(img='arachne-studio',sum='ARACHNE is a concept for an eight-legged robot that climbs and traverses terrain wheeled and tracked platforms cannot: rock faces, rubble, crevasse walls and steep slopes. It is planned in several sizes around a common control architecture.',
 conops='An operator team deploys ARACHNE from a safe standoff. The robot moves to a point of interest under supervised autonomy, holding footing on its own, while the operator directs inspection and sampling tasks over a remote link. Every task action requires operator approval.',
 caps=['Eight-leg gait concept for vertical and broken terrain','Standoff sensing and inspection in hazardous areas','Modular payload bay for sensors or sampling tools','Scalable family (small, medium, heavy) sharing one control stack'],
 tg=[('Configuration','8 legs, 3 size classes'),('Control','Supervised autonomy, operator-approved tasks'),('Target terrain','Slopes, rubble, ice and rock faces')],
 gal=[('arachne-canyon','Concept: traversing a canyon wall.'),('arachne-glacier','Concept: cold-region variant at a crevasse edge.'),('arachne-lineup','Concept: proposed small, medium and heavy size classes.')]),
'destrier':dict(img='destrier-field',sum='DESTRIER is a concept for a quadruped cargo carrier that moves loads with a dismounted team over terrain where vehicles cannot follow. It draws on a long lineage of legged-mechanism ideas, including the 1893 Rygg “Mechanical Horse” patent.',
 conops='DESTRIER follows a team or travels between waypoints with supplies, batteries and equipment, reducing the load each person carries. Operators can take direct control at any time through a handheld or DEEPLINK station.',
 caps=['Legged mobility for rough, unimproved terrain','Follow-me and waypoint travel under operator supervision','Open cargo deck with standard tie-down points','Remote takeover through DEEPLINK'],
 tg=[('Role','Expeditionary and cold-region logistics'),('Control','Follow / waypoint / direct teleoperation'),('Stage','Concept, TRL 1–2')],
 gal=[('destrier-studio','Concept: DESTRIER with cargo cases.')]),
'deeplink':dict(img='deeplink-station',sum='DEEPLINK is a concept for a teleoperation station that gives a trained operator an intuitive, high-fidelity view and control of a remote robot. It is designed as the common human interface for all Remote Robotics systems, including subsea and space telerobotics.',
 conops='An operator at a ship, shelter or ground station works through a headset and hand controllers. Robots handle low-level stability and safety; the operator makes task decisions. The station logs operator inputs to support review and training.',
 caps=['Immersive vision and hand-tracked manipulation control','Common interface across legged, subsea and aerial systems','Shared control: robot stabilizes, human decides','Session logging for review and operator training'],
 tg=[('Operator','One trained operator per system (target)'),('Domains','Ground, subsea, space telerobotics'),('Stage','Concept, TRL 1–2')],
 gal=[('deeplink-seabed','Concept: work-class ROV controlled through DEEPLINK near a seabed vent.')]),
'hiveforge':dict(img='hiveforge-site',sum='HIVEFORGE is a concept for coordinated drones that place blocks and deposit material to build simple structures, such as berms and barriers, at remote or expeditionary sites without large crews on the ground.',
 conops='A small team defines a structure on a site plan. HIVEFORGE drones are tasked in sequence, while a supervisor monitors progress and approves each build stage. The concept targets force-protection berms and basic site preparation.',
 caps=['Multi-drone task coordination under human supervision','Block placement and material deposition concepts','Stage-by-stage build approval by a supervisor','Reduced crew exposure at remote sites'],
 tg=[('Structures','Berms, barriers, simple shelters'),('Control','Supervised multi-agent tasking'),('Stage','Concept, TRL 1')],
 gal=[('hiveforge-drone','Concept: HIVEFORGE build drone with deposition nozzle and gripper.')]),
}
# home
cards=''.join(f'<a class="card" href="{B}systems/{k}/"><img src="{B}renders/v3/{D[k]["img"]}.jpg" alt="{n} concept render" loading="lazy"><div><span class="tag">Concept render</span><h3>{n}</h3><p>{s}</p><span class="more">View system →</span></div></a>' for k,n,s in SYS)
MA=['Expeditionary logistics','Cold-region / Arctic operations','Hazardous-terrain reconnaissance (EOD-adjacent)','Subsea and seabed operations','Space telerobotics','Expeditionary construction and force-protection berms']
home=f'''<section class="hero"><img src="{B}renders/v3/arachne-canyon.jpg" alt="ARACHNE concept render on a canyon wall"><div class="wrap"><p class="eyebrow">Research &amp; development · Human-supervised robotics</p><h1>Robots for places people should not have to go.</h1><p class="lead">Remote Robotics is an early-stage R&amp;D firm developing legged, subsea and aerial robotic systems operated by trained people from a safe distance.</p><div class="btns"><a class="btn" href="{B}contact/">Request a briefing</a><a class="btn ghost" href="{B}systems/">View systems</a></div><p class="note">Concept render. All systems are in development.</p></div></section>
<section class="sec"><div class="wrap two"><div><p class="eyebrow">Mission</p><h2>Keep people in control, and out of harm’s way.</h2></div><p>We design robots that extend human reach into hazardous, remote and extreme environments. Our systems pair robust mobility with a common teleoperation interface, so a trained operator makes the decisions while the machine takes the risk. We are a new entrant at concept stage (TRL 1–3) and are seeking research partners and funding to mature these designs.</p></div></section>
<section class="sec alt"><div class="wrap"><p class="eyebrow">Systems</p><h2>Four concept systems</h2><div class="cards">{cards}</div></div></section>
<section class="sec"><div class="wrap"><p class="eyebrow">Mission areas</p><ul class="strip">{''.join(f"<li>{m}</li>" for m in MA)}</ul><p><a class="link" href="{B}capabilities/">Capabilities and approach →</a></p></div></section>{CTA}'''
write('',page('','Remote Robotics','Early-stage R&D firm developing human-supervised legged, subsea and aerial robotic systems. Concept stage, TRL 1–3.',home))
# systems overview
rows=''.join(f'<article class="srow"><img src="{B}renders/v3/{D[k]["img"]}.jpg" alt="{n} concept render" loading="lazy"><div><span class="tag">Concept render</span><h2>{n}</h2><p class="sub">{s}</p><p>{D[k]["sum"]}</p><p class="trl">Stage: {D[k]["tg"][-1][1] if "TRL" in D[k]["tg"][-1][1] else "Concept, TRL 1–2"}</p><a class="link" href="{B}systems/{k}/">View {n.title()} →</a></div></article>' for k,n,s in SYS)
write('systems/',page('systems/','Systems','Overview of Remote Robotics concept systems: ARACHNE, DESTRIER, DEEPLINK and HIVEFORGE.',ph('Systems','Concept systems','Four systems sharing one principle: the machine goes into danger, a trained human stays in control. All are concept-stage designs; capabilities shown are design targets.')+f'<section class="sec"><div class="wrap">{rows}</div></section>'+CTA,'systems/'))
for k,n,s in SYS:
    d=D[k]
    b=f'''<section class="shero"><img src="{B}renders/v3/{d["img"]}.jpg" alt="{n} concept render"><div class="wrap"><p class="eyebrow"><a href="{B}systems/">Systems</a> / {n.title()}</p><h1>{n}</h1><p class="lead">{s}</p><p class="note">Concept render. In development.</p></div></section>
<section class="sec"><div class="wrap two"><div><p class="eyebrow">Summary</p><h2>Mission</h2></div><div><p>{d["sum"]}</p><h3>Concept of operations</h3><p>{d["conops"]}</p></div></div></section>
<section class="sec alt"><div class="wrap two"><div><p class="eyebrow">Capabilities</p><h2>Key capabilities</h2><ul class="ticks">{"".join(f"<li>{c}</li>" for c in d["caps"])}</ul></div><div><p class="eyebrow">Design targets</p><h2>Headline targets</h2><dl class="targets">{"".join(f"<div><dt>{a}</dt><dd>{v}</dd></div>" for a,v in d["tg"])}</dl><p class="small">Design targets only; not demonstrated performance. Detailed technical information is available on request.</p></div></div></section>
<section class="sec"><div class="wrap"><p class="eyebrow">Gallery</p><div class="gal">{"".join(fig("renders/v3/"+g+".jpg",c) for g,c in d["gal"])}</div></div></section>{CTA}'''
    write(f'systems/{k}/',page(f'systems/{k}/',n.title(),f'{n}: {s}. Concept-stage system in development by Remote Robotics.',b,f'systems/{k}/',f'renders/v3/{d["img"]}.jpg'))
# capabilities
MAD=[('Expeditionary logistics','Moving supplies with dismounted teams over terrain vehicles cannot cross.','DESTRIER, DEEPLINK','ls3-field','Legged Squad Support System, a DARPA/U.S. Marine Corps program, shown as reference for the mission area.'),
('Cold-region / Arctic operations','Survey, sampling and transport on ice, snow and crevassed ground.','ARACHNE, DESTRIER','crevasse','Glacier crevasse terrain.'),
('Hazardous-terrain reconnaissance','Standoff inspection of unstable or hazardous areas, adjacent to EOD support tasks. Our systems are inspection tools and carry no weapons.','ARACHNE, DEEPLINK','gorge','Steep canyon terrain.'),
('Subsea and seabed operations','Inspection and manipulation at depth through an intuitive operator interface.','DEEPLINK','rov-arm','NOAA remotely operated vehicle manipulator arm.'),
('Space telerobotics','Applying the same human-in-the-loop interface to robotic work in orbit or on planetary surfaces.','DEEPLINK','robonaut','NASA Robonaut 2.'),
('Expeditionary construction and force protection','Building berms, barriers and simple structures with reduced crew exposure.','HIVEFORGE','construction','Construction site reference.')]
ma=''.join(f'<article class="ma">{ref(r,c)}<div><h3>{t}</h3><p>{x}</p><p class="small">Relevant systems: {s}</p></div></article>' for t,x,s,r,c in MAD)
cap=ph('Capabilities','Mission areas and approach','Where our concept systems are intended to operate, and how people stay in control of them.')+f'''<section class="sec"><div class="wrap"><div class="magrid">{ma}</div></div></section>
<section class="sec alt"><div class="wrap two"><div><p class="eyebrow">Approach</p><h2>Human in the loop</h2></div><div><p>Every Remote Robotics system is designed around a trained operator. Robots handle low-level stability, footing and collision avoidance; people choose objectives and approve task actions. This keeps accountability with humans and keeps operators at a safe distance from hazards.</p><p>Our systems are not weapons and are not designed to carry them. We nonetheless align our design approach with the principles of <a class="link" href="https://www.esd.whs.mil/portals/54/documents/dd/issuances/dodd/300009p.pdf" rel="noopener">DoD Directive 3000.09, “Autonomy in Weapon Systems”</a> (updated January 25, 2023), which calls for “appropriate levels of human judgment over the use of force.” We cite it as a design reference, not as a claim of compliance, review or endorsement.</p></div></div></section>{CTA}'''
write('capabilities/',page('capabilities/','Capabilities','Mission areas for Remote Robotics concept systems and our human-in-the-loop design approach.',cap,'capabilities/'))
# about
ab=ph('About','Company','Remote Robotics is a new, early-stage research and development firm focused on human-supervised robotic systems for hazardous and remote environments.')+f'''<section class="sec"><div class="wrap two"><div><p class="eyebrow">Mission</p><h2>Extend human reach, not human risk.</h2></div><div><p>We develop robotic platforms and a common teleoperation interface that let trained people work in places that are dangerous, remote or unreachable. Our work is at concept stage: we are defining requirements, building analyses and early models, and seeking partners and research funding.</p><p><strong>Past performance:</strong> none yet. Remote Robotics is a new entrant with no contracts or customers to date.</p></div></div></section>
<section class="sec alt"><div class="wrap"><p class="eyebrow">Development path</p><h2>Three steps</h2><ol class="path"><li><span>01</span><h3>Concept and analysis</h3><p>Requirements, mission analysis and design studies. TRL 1–2. Current stage.</p></li><li><span>02</span><h3>Component prototypes</h3><p>Bench and lab validation of key subsystems and the DEEPLINK interface. Target TRL 3.</p></li><li><span>03</span><h3>Integrated demonstrators</h3><p>Partner-supported field demonstrations in relevant environments.</p></li></ol></div></section>
<section class="sec"><div class="wrap two"><div><p class="eyebrow">Heritage</p><h2>An old idea, new tools</h2><p>Legged machines have a long history. In 1893 Lewis A. Rygg of St. Paul, Minnesota was granted U.S. Patent 491,927 for a “Mechanical Horse”, a pedal-driven mechanism that walked on four legs. DESTRIER revisits the idea with modern actuation and control.</p></div>{ref("rygg","Patent case file cover, U.S. Patent 491,927 (Rygg, 1893). National Archives.")}</div></section>{CTA}'''
write('about/',page('about/','About','About Remote Robotics: mission, stage and development path.',ab,'about/'))
# capability statement
cs=f'''<section class="phead"><div class="wrap"><p class="eyebrow">Capability statement</p><h1>Remote Robotics</h1><p class="lead">Human-supervised robotics research and development. Public release.</p><p><a class="btn" href="{B}capability-statement/remote-robotics-capability-statement.pdf" download>Download PDF</a> <button class="btn ghost" onclick="window.print()">Print</button></p></div></section>
<section class="sec"><div class="wrap"><div class="onepager">
<div class="op-h"><div><strong>REMOTE ROBOTICS</strong><br><span class="small">Capability Statement · Distribution: Unclassified // Public release</span></div><div class="small">Rev. Oct 2026</div></div>
<div class="op-g"><div><h3>Company overview</h3><p>Early-stage R&amp;D firm developing legged, subsea and aerial robotic systems operated by trained people through a common teleoperation interface. All systems are at concept stage (TRL 1–3).</p>
<h3>Core competencies</h3><ul><li>Legged mobility concepts for extreme terrain (ARACHNE, DESTRIER)</li><li>Immersive teleoperation and shared control (DEEPLINK)</li><li>Coordinated aerial construction concepts (HIVEFORGE)</li><li>Human-in-the-loop system design</li></ul>
<h3>Mission areas</h3><p>Expeditionary logistics · Cold-region / Arctic · Hazardous-terrain reconnaissance · Subsea and seabed · Space telerobotics · Expeditionary construction</p></div>
<div><h3>Differentiators</h3><ul><li>One operator interface across ground, subsea and aerial systems</li><li>Operator-approved task actions by design</li><li>Unarmed systems; inspection, logistics and construction roles</li></ul>
<h3>Company data</h3><dl class="cd"><dt>UEI</dt><dd>Pending registration</dd><dt>CAGE</dt><dd>Pending registration</dd><dt>Past performance</dt><dd>None yet (new entrant)</dd><dt>Stage</dt><dd>Concept, TRL 1–3</dd></dl>
<h3>NAICS codes</h3><dl class="cd"><dt>541715</dt><dd>R&amp;D in the Physical, Engineering, and Life Sciences (except Nanotechnology and Biotechnology)</dd><dt>541330</dt><dd>Engineering Services</dd><dt>333924</dt><dd>Industrial Truck, Tractor, Trailer, and Stacker Machinery Manufacturing</dd><dt>333120</dt><dd>Construction Machinery Manufacturing</dd></dl>
<h3>Contact</h3><p>Request a briefing: charlesanthonyleone.github.io/remote-robotics/contact/</p></div></div>
<p class="small">Forward-looking statement: describes concept-stage systems; capabilities are design targets, not demonstrated performance. No government endorsement implied.</p></div></div></section>{CTA}'''
write('capability-statement/',page('capability-statement/','Capability Statement','Remote Robotics capability statement: overview, core competencies, NAICS codes, UEI/CAGE pending.',cs,'capability-statement/'))
# contact
ct=ph('Contact','Request a briefing or technical package','For program officers, grant reviewers and prospective research partners. Submitting opens a pre-filled message in your own email app; nothing is stored on this site.')+f'''<section class="sec"><div class="wrap two"><form class="form" id="brief"><label>Name<input name="name" required></label><label>Organization<input name="org" required></label><label>Your email<input type="email" name="email" required></label><label>Interest<select name="sys"><option>General briefing</option>{"".join(f"<option>{n}</option>" for _,n,_ in SYS)}<option>Capability statement / partnering</option></select></label><label>Message<textarea name="msg" rows="5"></textarea></label><button class="btn" type="submit">Prepare request</button><p class="small" id="formnote"></p></form>
<div><h3>What to expect</h3><p>Briefings cover concept status, mission fit and development path. Additional technical information is shared case by case, as appropriate.</p><p>Remote Robotics does not yet publish a public email address. Requests are prepared through GitHub: <a class="link" href="https://github.com/charlesanthonyleone/remote-robotics/issues/new" rel="noopener">open a contact request on GitHub</a>, or use the form to draft one.</p></div></div></section>'''
write('contact/',page('contact/','Request a Briefing','Request a briefing or technical package from Remote Robotics.',ct,'contact/'))
# credits
rows=''.join(f'<tr><td><img src="{B}{c["file"]}" alt="" loading="lazy"></td><td><a href="{c["page"]}" rel="noopener">{html.escape(c["title"])}</a><br><span class="small">{html.escape(c["artist"] or "")}</span></td><td>{f"<a href=\"{c["licurl"]}\" rel=\"noopener\">{c["license"]}</a>" if c["licurl"] else c["license"]}</td></tr>' for c in CR)
rr=''.join(f'<li><a href="{B}renders/v3/{f}">{f}</a></li>' for f in sorted(os.listdir('renders/v3')))
cr=ph('Credits','Image credits','Reference photos are from Wikimedia Commons, downloaded and served from this site. They show third-party or government systems and places and are not Remote Robotics products.')+f'''<section class="sec"><div class="wrap"><div class="tw"><table class="ct"><thead><tr><th>Image</th><th>Source</th><th>License</th></tr></thead><tbody>{rows}</tbody></table></div>
<h2>Concept renders</h2><p>All images labeled “Concept render” are AI-generated illustrations created for Remote Robotics. They depict design concepts, not built hardware, and do not show demonstrated performance.</p><ul class="small">{rr}</ul></div></section>'''
write('credits/',page('credits/','Image Credits','Sources and licenses for images used on the Remote Robotics site.',cr))
nf=ph('404','Page not found','The page you requested does not exist or has moved.')+f'<section class="sec"><div class="wrap"><a class="btn" href="{B}">Return home</a> <a class="btn ghost" href="{B}systems/">View systems</a></div></section>'
write('404',page('404.html','Page not found','Page not found.',nf))
urls=['','systems/']+[f'systems/{k}/' for k,_,_ in SYS]+['capabilities/','about/','capability-statement/','contact/','credits/']
open('sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'<url><loc>{SITE}{u}</loc><lastmod>2026-10-28</lastmod></url>\n' for u in urls)+'</urlset>\n')
open('robots.txt','w').write(f'User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n')
