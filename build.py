import os

LOGO = 'https://lh3.googleusercontent.com/d/16oZcVd80uLrux2B-jN84sTUlmOqGoPQd'

def head(title, extra_css=''):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0"/>
<meta name="theme-color" content="#1D4ED8"/>
<title>{title} — Pragati Work Exchange</title>
<link rel="stylesheet" href="style.css"/>
</head>
<body>
<div id="loader">
  <div class="ld-icon"><img src="{LOGO}" alt="Pragati" onerror="this.style.display='none'"/></div>
  <div class="ld-brand">Pragati<span>.</span></div>
  <div class="ld-sub">Work Exchange</div>
  <div class="ld-bar"><div class="ld-fill"></div></div>
</div>
<div id="toast"></div>
'''

def foot():
    return '</body>\n</html>\n'

def bnav_petty(active):
    items = [
        ('home.html','🏠','Home','home'),
        ('find.html','🔍','Find Work','find'),
        ('apps.html','📋','My Bids','apps'),
        ('chat.html','💬','Messages','chat'),
    ]
    html = '<nav class="bnav n4">'
    for href,ico,lbl,key in items:
        on = ' on' if key==active else ''
        html += f'<div class="bni{on}" onclick="location.href=\'{href}\'"><div class="ico">{ico}</div><div class="lbl">{lbl}</div></div>'
    return html + '</nav>\n'

def bnav_main(active):
    items = [
        ('main.html','🏠','Home','home'),
        ('post.html','➕','Post Work','post'),
        ('myworks.html','📋','My Works','myworks'),
        ('chat.html','💬','Messages','chat'),
    ]
    html = '<nav class="bnav n4">'
    for href,ico,lbl,key in items:
        on = ' on' if key==active else ''
        html += f'<div class="bni{on}" onclick="location.href=\'{href}\'"><div class="ico">{ico}</div><div class="lbl">{lbl}</div></div>'
    return html + '</nav>\n'

def shared_js():
    return '<script src="shared.js"></script>\n'

def fb_imports():
    return '''<script type="module">
import{initializeApp}from"https://www.gstatic.com/firebasejs/10.12.2/firebase-app.js";
import{getAuth,onAuthStateChanged,signOut,sendPasswordResetEmail}from"https://www.gstatic.com/firebasejs/10.12.2/firebase-auth.js";
import{getFirestore,collection,addDoc,getDocs,getDoc,doc,setDoc,updateDoc,query,where,orderBy,serverTimestamp}from"https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";
const fbApp=initializeApp(FB_CFG);
const auth=getAuth(fbApp);
const db=getFirestore(fbApp);
'''

# ─────────────────────────────────────────
# 1. index.html — Landing + Login + Register
# ─────────────────────────────────────────
pages = {}

pages['index.html'] = f'''{head("Welcome to Pragati")}
<div class="snap-wrap" id="s-auth">

  <!-- HERO -->
  <section class="snap-sec" id="sec-hero" style="background:linear-gradient(160deg,#0F172A 0%,#1E3A5F 55%,#0F172A 100%);display:flex;flex-direction:column;">
    <nav style="padding:52px 18px 0;display:flex;justify-content:space-between;align-items:center;">
      <div style="display:flex;align-items:center;gap:10px;">
        <div style="width:36px;height:36px;border-radius:10px;background:var(--blue2);overflow:hidden;"><img src="{LOGO}" style="width:100%;height:100%;object-fit:contain;" onerror="this.style.display='none'"/></div>
        <div style="font-family:var(--h);font-size:20px;font-weight:800;color:#fff;">Pragati<span style="color:var(--orange3);">.</span></div>
      </div>
      <button class="btn btn-sm" style="background:rgba(255,255,255,.12);color:#fff;border:1px solid rgba(255,255,255,.2);" onclick="document.getElementById('sec-login').scrollIntoView({{behavior:'smooth'}})">Login</button>
    </nav>
    <div style="flex:1;padding:24px 18px 0;">
      <div style="display:flex;justify-content:center;margin-bottom:20px;">
        <svg viewBox="0 0 300 170" width="290" height="165" fill="none">
          <rect width="300" height="145" fill="#0F172A" opacity=".35"/>
          <circle cx="40" cy="18" r="1.5" fill="white" opacity=".5"/><circle cx="120" cy="10" r="1" fill="white" opacity=".6"/><circle cx="200" cy="18" r="1.5" fill="white" opacity=".4"/><circle cx="270" cy="12" r="1" fill="white" opacity=".5"/>
          <rect x="15" y="42" width="48" height="113" rx="3" fill="#1E40AF"/><rect x="15" y="42" width="48" height="7" rx="2" fill="#2563EB"/>
          <rect x="21" y="55" width="10" height="8" rx="1" fill="#93C5FD" opacity=".9"/><rect x="36" y="55" width="10" height="8" rx="1" fill="white" opacity=".8"/>
          <rect x="21" y="70" width="10" height="8" rx="1" fill="white" opacity=".7"/><rect x="36" y="70" width="10" height="8" rx="1" fill="#93C5FD" opacity=".6"/>
          <rect x="21" y="85" width="10" height="8" rx="1" fill="#93C5FD" opacity=".8"/><rect x="36" y="85" width="10" height="8" rx="1" fill="white" opacity=".5"/>
          <rect x="80" y="75" width="80" height="80" rx="3" fill="#334155"/>
          <rect x="76" y="42" width="5" height="113" rx="2" fill="#64748B"/><rect x="159" y="42" width="5" height="113" rx="2" fill="#64748B"/>
          <rect x="76" y="42" width="88" height="5" rx="2" fill="#64748B"/>
          <rect x="76" y="63" width="88" height="2" rx="1" fill="#94A3B8" opacity=".4"/><rect x="76" y="84" width="88" height="2" rx="1" fill="#94A3B8" opacity=".4"/><rect x="76" y="105" width="88" height="2" rx="1" fill="#94A3B8" opacity=".4"/>
          <rect x="88" y="86" width="13" height="11" rx="1" fill="#1E40AF" opacity=".6"/><rect x="108" y="86" width="13" height="11" rx="1" fill="#1E40AF" opacity=".4"/>
          <rect x="222" y="14" width="6" height="141" rx="2" fill="#EA580C"/>
          <rect x="182" y="14" width="78" height="5" rx="2" fill="#F97316"/><rect x="246" y="9" width="17" height="13" rx="3" fill="#DC2626"/>
          <line x1="202" y1="19" x2="202" y2="46" stroke="#94A3B8" stroke-width="1.5"/><rect x="194" y="46" width="16" height="10" rx="3" fill="#F97316"/>
          <rect x="246" y="68" width="40" height="87" rx="3" fill="#1E3A5F"/>
          <circle cx="94" cy="53" r="5" fill="#FBBF24"/><rect x="89" y="58" width="10" height="12" rx="2" fill="#F97316"/><path d="M88 53 Q94 45 100 53" fill="#EA580C"/>
          <circle cx="148" cy="136" r="5" fill="#FCD34D"/><rect x="143" y="141" width="10" height="10" rx="2" fill="#2563EB"/><path d="M142 136 Q148 128 154 136" fill="#F59E0B"/>
          <rect y="150" width="300" height="20" fill="#1E293B"/>
          <text x="150" y="164" text-anchor="middle" font-size="8" font-weight="800" fill="white" opacity=".5" font-family="sans-serif">PRAGATI WORK EXCHANGE</text>
        </svg>
      </div>
      <div style="font-family:var(--h);font-size:32px;font-weight:800;color:#fff;line-height:1.15;margin-bottom:12px;">Find Construction <span style="color:var(--orange3);">Work Faster</span></div>
      <p style="font-size:14px;color:rgba(255,255,255,.65);line-height:1.7;margin-bottom:24px;">India's #1 marketplace for subcontract work. Post requirements or bid for jobs — free forever.</p>
      <div style="display:flex;flex-direction:column;gap:10px;margin-bottom:24px;">
        <button class="btn btn-o btn-bl btn-lg" onclick="document.getElementById('sec-register').scrollIntoView({{behavior:'smooth'}})">Get Started Free →</button>
        <button class="btn btn-bl btn-lg" style="background:rgba(255,255,255,.1);color:#fff;border:1px solid rgba(255,255,255,.2);" onclick="document.getElementById('sec-login').scrollIntoView({{behavior:'smooth'}})">I Have an Account</button>
      </div>
      <div style="display:flex;gap:24px;padding:20px 0;border-top:1px solid rgba(255,255,255,.1);">
        <div><div style="font-family:var(--h);font-size:22px;font-weight:800;color:#fff;">10K+</div><div style="font-size:11px;color:rgba(255,255,255,.5);">Contractors</div></div>
        <div><div style="font-family:var(--h);font-size:22px;font-weight:800;color:#fff;">₹200Cr+</div><div style="font-size:11px;color:rgba(255,255,255,.5);">Work Awarded</div></div>
        <div><div style="font-family:var(--h);font-size:22px;font-weight:800;color:#fff;">28</div><div style="font-size:11px;color:rgba(255,255,255,.5);">States</div></div>
      </div>
    </div>
    <div style="text-align:center;padding:14px 0 20px;color:rgba(255,255,255,.4);font-size:12px;animation:bounce 2s infinite;">↓ Scroll to sign up</div>
  </section>

  <!-- REGISTER -->
  <section class="snap-sec" id="sec-register" style="background:#fff;display:flex;flex-direction:column;">
    <div class="ahero">
      <div class="ld-icon" style="margin:0 auto 12px;"><img src="{LOGO}" style="width:100%;height:100%;object-fit:contain;" onerror="this.style.display='none'"/></div>
      <h2>Create Account</h2>
      <p>Join 10,000+ contractors on Pragati</p>
    </div>
    <div class="abody">
      <p style="font-size:11px;font-weight:700;color:var(--s3);text-transform:uppercase;letter-spacing:.07em;margin-bottom:10px;">I am a…</p>
      <div class="rgrid">
        <div class="rcard sel" id="rc-petty" onclick="selRole('petty')"><div class="ri">👷</div><h4>Petty Contractor</h4><p>Find & apply for work</p></div>
        <div class="rcard" id="rc-main" onclick="selRole('main')"><div class="ri">🏗️</div><h4>Main Contractor</h4><p>Post work & hire</p></div>
      </div>
      <input type="hidden" id="rg-role" value="petty"/>
      <div class="field"><label class="flbl">Full Name *</label><input class="fin" id="rg-name" placeholder="e.g. Rajesh Patil"/></div>
      <div class="g2">
        <div class="field"><label class="flbl">Phone *</label><input class="fin" id="rg-phone" type="tel" placeholder="+91 98765 43210" inputmode="tel"/></div>
        <div class="field"><label class="flbl">City *</label><input class="fin" id="rg-city" placeholder="Pune, MH"/></div>
      </div>
      <div class="field" id="rg-tw"><label class="flbl">Primary Trade</label>
        <select class="fin" id="rg-trade"><option value="">Select…</option><option>Plastering</option><option>Flooring</option><option>Painting</option><option>Electrical</option><option>Plumbing</option><option>Masonry</option><option>Carpentry</option><option>Tiling</option><option>Waterproofing</option><option>Civil Work</option><option>Other</option></select>
      </div>
      <div class="field"><label class="flbl">Email *</label><input class="fin" id="rg-email" type="email" placeholder="you@example.com" inputmode="email"/></div>
      <div class="field"><label class="flbl">Password *</label><input class="fin" id="rg-pass" type="password" placeholder="Min 6 characters"/></div>
      <div class="ferr" id="rg-err">Please fill all required fields correctly.</div>
      <button class="btn btn-p btn-bl btn-lg" id="rg-btn" onclick="doRegister()" style="margin-top:8px;">Create Account →</button>
      <div class="divdr">or</div>
      <p style="text-align:center;font-size:14px;color:var(--s3);">Already registered? <span style="color:var(--blue2);font-weight:600;cursor:pointer;" onclick="document.getElementById('sec-login').scrollIntoView({{behavior:'smooth'}})">Login here</span></p>
    </div>
  </section>

  <!-- LOGIN -->
  <section class="snap-sec" id="sec-login" style="background:#fff;display:flex;flex-direction:column;">
    <div class="ahero">
      <div class="ld-icon" style="margin:0 auto 12px;"><img src="{LOGO}" style="width:100%;height:100%;object-fit:contain;" onerror="this.style.display='none'"/></div>
      <h2>Welcome Back</h2>
      <p>Login to your Pragati account</p>
    </div>
    <div class="abody">
      <div class="field"><label class="flbl">Email Address</label><input class="fin" id="li-email" type="email" placeholder="you@example.com" inputmode="email"/></div>
      <div class="field"><label class="flbl">Password</label><input class="fin" id="li-pass" type="password" placeholder="Your password"/></div>
      <div class="ferr" id="li-err">Invalid email or password.</div>
      <div style="text-align:right;margin-bottom:6px;"><span style="font-size:13px;color:var(--blue2);font-weight:600;cursor:pointer;" onclick="showForgot()">Forgot Password?</span></div>
      <button class="btn btn-p btn-bl btn-lg" id="li-btn" onclick="doLogin()">Login →</button>
      <div class="divdr">or</div>
      <p style="text-align:center;font-size:14px;color:var(--s3);">No account? <span style="color:var(--blue2);font-weight:600;cursor:pointer;" onclick="document.getElementById('sec-register').scrollIntoView({{behavior:'smooth'}})">Register Free</span></p>
    </div>
  </section>
</div>

<!-- FORGOT PASSWORD SHEET -->
<div class="ovl off" id="forgot-ovl">
  <div class="sheet">
    <div class="shdl"></div>
    <div class="shtit">Reset Password 🔑</div>
    <p style="font-size:14px;color:var(--s4);margin-bottom:16px;line-height:1.6;">Enter your registered email. We will send a password reset link to your inbox.</p>
    <div class="field"><label class="flbl">Email Address</label><input class="fin" id="fp-email" type="email" placeholder="you@example.com" inputmode="email"/></div>
    <div class="ferr" id="fp-err">Please enter a valid email.</div>
    <div id="fp-ok" style="display:none;background:var(--green4);border:1px solid #A7F3D0;border-radius:10px;padding:12px 14px;font-size:13px;color:var(--green);margin-bottom:14px;">✅ Reset link sent! Check your email inbox.</div>
    <button class="btn btn-p btn-bl btn-lg" id="fp-btn" onclick="doReset()">Send Reset Link →</button>
    <button class="btn btn-g btn-bl" style="margin-top:10px;" onclick="document.getElementById('forgot-ovl').classList.add('off')">Cancel</button>
  </div>
</div>

{shared_js()}
{fb_imports()}
// Auto-redirect if already logged in
onAuthStateChanged(auth, async u => {{
  if(u) {{
    const s = await getDoc(doc(db,'users',u.uid));
    const cd = s.exists() ? s.data() : null;
    if(cd) {{ window.location.href = cd.role==='main' ? 'main.html' : 'home.html'; return; }}
  }}
  document.getElementById('loader').classList.add('out');
}});

function selRole(r){{
  document.getElementById('rg-role').value=r;
  document.getElementById('rc-petty').classList.toggle('sel',r==='petty');
  document.getElementById('rc-main').classList.toggle('sel',r==='main');
  document.getElementById('rg-tw').style.display=r==='petty'?'block':'none';
}}

async function doLogin(){{
  const e=document.getElementById('li-email').value.trim(),p=document.getElementById('li-pass').value,err=document.getElementById('li-err'),btn=document.getElementById('li-btn');
  if(!e||!p){{err.classList.add('on');return;}}
  btn.classList.add('btn-ld');btn.textContent='Logging in…';
  try{{
    const uc=await signInWithEmailAndPassword(auth,e,p);
    const s=await getDoc(doc(db,'users',uc.user.uid));
    const cd=s.exists()?s.data():null;
    window.location.href=cd?.role==='main'?'main.html':'home.html';
  }}catch(ex){{
    err.textContent=ex.code==='auth/user-not-found'?'No account with this email.':ex.code==='auth/wrong-password'||ex.code==='auth/invalid-credential'?'Incorrect password.':'Login failed.';
    err.classList.add('on');
  }}
  btn.classList.remove('btn-ld');btn.textContent='Login →';
}}

async function doRegister(){{
  const name=document.getElementById('rg-name').value.trim(),phone=document.getElementById('rg-phone').value.trim(),city=document.getElementById('rg-city').value.trim(),email=document.getElementById('rg-email').value.trim(),pass=document.getElementById('rg-pass').value,role=document.getElementById('rg-role').value,trade=document.getElementById('rg-trade').value,err=document.getElementById('rg-err'),btn=document.getElementById('rg-btn');
  if(!name||!email||!city||pass.length<6){{err.classList.add('on');return;}}
  btn.classList.add('btn-ld');btn.textContent='Creating…';
  try{{
    const uc=await createUserWithEmailAndPassword(auth,email,pass);
    await setDoc(doc(db,'users',uc.user.uid),{{name,email,phone,city,role,trade,exp:'',bio:'',company:role==='main'?name:'',createdAt:serverTimestamp()}});
    window.location.href=role==='main'?'main.html':'home.html';
  }}catch(ex){{
    err.textContent=ex.code==='auth/email-already-in-use'?'Email already registered.':'Error: '+ex.message;
    err.classList.add('on');
  }}
  btn.classList.remove('btn-ld');btn.textContent='Create Account →';
}}

function showForgot(){{
  document.getElementById('fp-email').value=document.getElementById('li-email').value||'';
  document.getElementById('fp-err').classList.remove('on');
  document.getElementById('fp-ok').style.display='none';
  document.getElementById('fp-btn').style.display='';
  document.getElementById('forgot-ovl').classList.remove('off');
}}
async function doReset(){{
  const email=document.getElementById('fp-email').value.trim(),err=document.getElementById('fp-err'),btn=document.getElementById('fp-btn');
  if(!email||!email.includes('@')){{err.textContent='Enter a valid email.';err.classList.add('on');return;}}
  btn.classList.add('btn-ld');btn.textContent='Sending…';
  try{{
    await sendPasswordResetEmail(auth,email);
    document.getElementById('fp-ok').style.display='block';btn.style.display='none';
  }}catch(ex){{
    err.textContent=ex.code==='auth/user-not-found'?'No account with this email.':'Error: '+ex.message;
    err.classList.add('on');btn.classList.remove('btn-ld');btn.textContent='Send Reset Link →';
  }}
}}
import{{createUserWithEmailAndPassword}}from"https://www.gstatic.com/firebasejs/10.12.2/firebase-auth.js";
</script>
{foot()}'''

print("index.html built")

# ─────────────────────────────────────────
# 2. home.html — Petty Contractor Home
# ─────────────────────────────────────────
pages['home.html'] = f'''{head("Home")}
<div style="display:flex;flex-direction:column;min-height:100vh;">
  <div class="hh">
    <div class="hh-top">
      <div><div class="hh-gr">Good day 👋</div><div class="hh-nm" id="hh-nm">—</div></div>
      <div class="hh-av" id="hh-av" onclick="go('profile.html')">RP</div>
    </div>
    <div class="spill" onclick="go('find.html')"><span style="font-size:16px;opacity:.6;">🔍</span><span>Search work by trade, location…</span></div>
  </div>
  <div class="pscr pb90">
    <div class="mets">
      <div class="met"><div class="mn bl" id="st-open">—</div><div class="ml">Open Works</div></div>
      <div class="met"><div class="mn or" id="st-app">0</div><div class="ml">Applied</div></div>
      <div class="met"><div class="mn gr" id="st-awd">0</div><div class="ml">Awarded</div></div>
      <div class="met"><div class="mn pu" id="st-sh">0</div><div class="ml">Shortlisted</div></div>
    </div>
    <div id="home-ntc" style="display:none;" class="ntc">⚡ <span id="home-ntxt"></span></div>
    <div style="padding:12px 16px 0;"><div class="sh"><h3>Browse by Trade</h3></div></div>
    <div class="istrip">
      <div class="icard" onclick="go('find.html','trade=Plastering')"><div class="icico">🧱</div><div class="ictit">Plastering</div><div class="icsub">Wall & ceiling</div></div>
      <div class="icard" onclick="go('find.html','trade=Flooring')"><div class="icico">⬜</div><div class="ictit">Flooring</div><div class="icsub">Tiles & marble</div></div>
      <div class="icard" onclick="go('find.html','trade=Electrical')"><div class="icico">⚡</div><div class="ictit">Electrical</div><div class="icsub">Wiring</div></div>
      <div class="icard" onclick="go('find.html','trade=Painting')"><div class="icico">🎨</div><div class="ictit">Painting</div><div class="icsub">Int. & ext.</div></div>
      <div class="icard" onclick="go('find.html','trade=Plumbing')"><div class="icico">🔧</div><div class="ictit">Plumbing</div><div class="icsub">Sanitary</div></div>
      <div class="icard" onclick="go('find.html','trade=Masonry')"><div class="icico">🏗️</div><div class="ictit">Masonry</div><div class="icsub">Brick & block</div></div>
    </div>
    <div style="padding:0 16px;"><div class="sh"><h3>Latest Works</h3><a onclick="go('find.html')">See all →</a></div></div>
    <div style="padding:0 16px;" id="hw-list"><div class="empty"><div class="spin" style="margin:0 auto;"></div></div></div>
  </div>
  {bnav_petty('home')}
</div>
{shared_js()}
{fb_imports()}
onAuthStateChanged(auth,async u=>{{
  if(!u){{location.href='index.html';return;}}
  const s=await getDoc(doc(db,'users',u.uid));
  const cd=s.exists()?s.data():null;
  if(!cd){{location.href='index.html';return;}}
  if(cd.role==='main'){{location.href='main.html';return;}}
  document.getElementById('loader').classList.add('out');
  const n=cd.name||'Contractor';
  document.getElementById('hh-nm').textContent=n.split(' ')[0];
  document.getElementById('hh-av').textContent=initials(n);
  // Load works
  let works=[];
  try{{const ws=await getDocs(query(collection(db,'works'),orderBy('createdAt','desc')));works=ws.docs.map(d=>({{id:d.id,...d.data()}}));}}
  catch(e){{works=DEMO_WORKS;}}
  document.getElementById('st-open').textContent=works.length;
  document.getElementById('hw-list').innerHTML=works.slice(0,4).map(w=>mkCard(w)).join('')||emptyHTML('🏗️','No works yet','Check back soon');
  if(works.length){{document.getElementById('home-ntc').style.display='flex';document.getElementById('home-ntxt').textContent=works.length+' open works available near you!';}}
  // App stats
  try{{
    let snap;
    try{{snap=await getDocs(query(collection(db,'applications'),where('applicantId','==',u.uid),orderBy('createdAt','desc')));}}
    catch(e2){{snap=await getDocs(query(collection(db,'applications'),where('applicantId','==',u.uid)));}}
    const apps=snap.docs.map(d=>d.data());
    document.getElementById('st-app').textContent=apps.length;
    document.getElementById('st-awd').textContent=apps.filter(a=>a.status==='awarded').length;
    document.getElementById('st-sh').textContent=apps.filter(a=>a.status==='review'||a.status==='shortlisted').length;
  }}catch(e){{}}
}});
</script>
{foot()}'''

# ─────────────────────────────────────────
# 3. main.html — Main Contractor Home
# ─────────────────────────────────────────
pages['main.html'] = f'''{head("Dashboard")}
<div style="display:flex;flex-direction:column;min-height:100vh;">
  <div class="hh" style="background:linear-gradient(135deg,#065F46,#059669);">
    <div class="hh-top">
      <div><div class="hh-gr">Main Contractor 🏗️</div><div class="hh-nm" id="mh-nm">—</div></div>
      <div class="hh-av" id="mh-av" onclick="go('profile.html')" style="background:rgba(255,255,255,.2);">MC</div>
    </div>
  </div>
  <div class="pscr pb90">
    <div class="mets">
      <div class="met"><div class="mn bl" id="mm-post">0</div><div class="ml">Works Posted</div></div>
      <div class="met"><div class="mn or" id="mm-bids">0</div><div class="ml">Bids Received</div></div>
      <div class="met"><div class="mn gr" id="mm-awd">0</div><div class="ml">Awarded</div></div>
      <div class="met"><div class="mn pu" id="mm-act">0</div><div class="ml">Active Works</div></div>
    </div>
    <div style="padding:0 16px 0;"><div class="sh" style="margin-top:4px;"><h3>My Recent Works</h3><a onclick="go('myworks.html')">View all →</a></div></div>
    <div style="padding:0 16px;" id="mw-list"><div class="empty"><div class="spin" style="margin:0 auto;"></div></div></div>
    <div style="padding:10px 16px 4px;"><button class="btn btn-o btn-bl btn-lg" onclick="go('post.html')">+ Post New Work Requirement</button></div>
  </div>
  {bnav_main('home')}
</div>
{shared_js()}
{fb_imports()}
onAuthStateChanged(auth,async u=>{{
  if(!u){{location.href='index.html';return;}}
  const s=await getDoc(doc(db,'users',u.uid));
  const cd=s.exists()?s.data():null;
  if(!cd){{location.href='index.html';return;}}
  if(cd.role!=='main'){{location.href='home.html';return;}}
  document.getElementById('loader').classList.add('out');
  const n=cd.name||'Company';
  document.getElementById('mh-nm').textContent=n;
  document.getElementById('mh-av').textContent=initials(n);
  let works=[];
  try{{const ws=await getDocs(query(collection(db,'works'),where('postedBy','==',u.uid)));works=ws.docs.map(d=>({{id:d.id,...d.data()}}));}}
  catch(e){{works=DEMO_WORKS.slice(0,3);}}
  document.getElementById('mm-post').textContent=works.length;
  document.getElementById('mm-bids').textContent=works.reduce((s,w)=>s+(w.bids||0),0);
  document.getElementById('mm-awd').textContent=works.filter(w=>w.status==='awarded').length;
  document.getElementById('mm-act').textContent=works.filter(w=>!w.status||w.status==='open').length;
  document.getElementById('mw-list').innerHTML=works.slice(0,3).map(w=>`<div class="arow" onclick="go('bids.html','id=${{w.id}}')">
    <div class="tags" style="margin-bottom:7px;"><span class="tag t-bl">${{w.trade||'—'}}</span><span class="tag ${{tagColor(w.urgency)}}">${{w.urgency||'Normal'}}</span></div>
    <div class="art">${{w.title}}</div><div class="ars">📍 ${{w.location||'—'}} · ${{w.bids||0}} bids received</div>
    <div class="arf"><span class="sts ${{w.status==='awarded'?'awd':'open'}}">${{w.status==='awarded'?'Awarded ✓':'Accepting Bids'}}</span><span style="font-size:13px;font-weight:700;color:var(--green2);">${{fmtBudget(w)}}</span></div>
  </div>`).join('')||emptyHTML('🏗️','No works posted yet','Post your first work requirement');
}});
</script>
{foot()}'''

# ─────────────────────────────────────────
# 4. find.html — Find Work
# ─────────────────────────────────────────
pages['find.html'] = f'''{head("Find Work")}
<div style="display:flex;flex-direction:column;min-height:100vh;">
  <div class="tbar"><h2>Find Work</h2><span id="find-cnt" class="tag t-bl" style="flex-shrink:0;">0 Open</span></div>
  <div style="padding:12px 16px 0;flex-shrink:0;"><div class="sbar-wrap"><input class="sbar" id="s-inp" placeholder="Trade, company, city…" oninput="filterWorks()"/></div></div>
  <div class="chips" style="padding:10px 16px 0;flex-shrink:0;">
    <div class="chip on" onclick="setChip(this,'')">All</div>
    <div class="chip" onclick="setChip(this,'Plastering')">Plastering</div>
    <div class="chip" onclick="setChip(this,'Flooring')">Flooring</div>
    <div class="chip" onclick="setChip(this,'Electrical')">Electrical</div>
    <div class="chip" onclick="setChip(this,'Painting')">Painting</div>
    <div class="chip" onclick="setChip(this,'Plumbing')">Plumbing</div>
    <div class="chip" onclick="setChip(this,'Masonry')">Masonry</div>
    <div class="chip" onclick="setChip(this,'Carpentry')">Carpentry</div>
  </div>
  <div class="pscr pb90" style="padding:10px 16px 0;" id="find-list"><div class="empty"><div class="spin" style="margin:0 auto;"></div></div></div>
  {bnav_petty('find')}
</div>
{shared_js()}
{fb_imports()}
let allWorks=[],filterTV='';
onAuthStateChanged(auth,async u=>{{
  if(!u){{location.href='index.html';return;}}
  document.getElementById('loader').classList.add('out');
  try{{const ws=await getDocs(query(collection(db,'works'),orderBy('createdAt','desc')));allWorks=ws.docs.map(d=>({{id:d.id,...d.data()}}));}}
  catch(e){{allWorks=DEMO_WORKS;}}
  // Check URL param
  const t=getParam('trade');
  if(t){{filterTV=t;document.querySelectorAll('.chip').forEach(c=>c.classList.toggle('on',c.textContent.trim()===t));}}
  renderFind();
}});
function renderFind(){{
  const q=document.getElementById('s-inp').value.toLowerCase();
  let arr=allWorks.filter(w=>(w.title+''+w.location+''+w.trade+''+w.company+''+w.postedByName).toLowerCase().includes(q));
  if(filterTV)arr=arr.filter(w=>w.trade===filterTV);
  document.getElementById('find-cnt').textContent=arr.length+' Open';
  document.getElementById('find-list').innerHTML=arr.length?arr.map(w=>mkCard(w)).join(''):emptyHTML('🔍','No results','Try different filters');
}}
function filterWorks(){{renderFind();}}
function setChip(el,t){{document.querySelectorAll('.chip').forEach(c=>c.classList.remove('on'));el.classList.add('on');filterTV=t;renderFind();}}
</script>
{foot()}'''

# ─────────────────────────────────────────
# 5. detail.html — Work Detail
# ─────────────────────────────────────────
pages['detail.html'] = f'''{head("Work Details")}
<div style="display:flex;flex-direction:column;min-height:100vh;">
  <div class="dh" id="det-hero">
    <div style="display:flex;align-items:center;gap:10px;margin-bottom:14px;">
      <button class="tbk" onclick="history.back()" style="background:rgba(255,255,255,.2);color:#fff;">←</button>
      <div style="flex:1;"></div>
      <button class="tbk" id="save-btn" style="background:rgba(255,255,255,.2);" onclick="toggleSave()">🔖</button>
    </div>
    <div class="tags" id="det-tags"></div>
    <h1 id="det-title">Loading…</h1>
    <div class="dco" id="det-co"></div>
    <div class="dprog"><div class="dpf" id="det-pf" style="width:50%;"></div></div>
    <div style="display:flex;justify-content:space-between;margin-top:6px;font-size:11px;opacity:.75;"><span id="det-bt"></span><span id="det-dl"></span></div>
  </div>
  <div class="pscr" style="padding-bottom:0;">
    <div class="dsec"><h4>Work Details</h4>
      <div class="irow"><span class="ik">Budget</span><span class="iv" style="color:var(--green2);" id="det-bud">—</span></div>
      <div class="irow"><span class="ik">Location</span><span class="iv" id="det-loc">—</span></div>
      <div class="irow"><span class="ik">Duration</span><span class="iv" id="det-dur">—</span></div>
      <div class="irow"><span class="ik">Start Date</span><span class="iv" id="det-std">—</span></div>
      <div class="irow"><span class="ik">Experience</span><span class="iv" id="det-exp">—</span></div>
      <div class="irow"><span class="ik">Labour</span><span class="iv" id="det-lab">—</span></div>
    </div>
    <div class="dsec"><h4>Scope of Work</h4><div id="det-scope"></div></div>
    <div class="dsec" id="det-applied-box" style="display:none;text-align:center;padding:16px;">
      <div style="font-size:32px;margin-bottom:8px;">✅</div>
      <div style="font-family:var(--h);font-size:15px;font-weight:700;color:var(--green2);">Already Applied!</div>
      <div style="font-size:12px;color:var(--s4);margin-top:4px;">You'll be notified when status changes.</div>
    </div>
    <div style="height:100px;"></div>
  </div>
  <div class="scta" id="det-cta">
    <button class="btn btn-g" style="width:46px;font-size:20px;padding:0;" onclick="go('chat.html')">💬</button>
    <button class="btn btn-p" style="flex:1;" id="apply-btn">Submit Quotation →</button>
  </div>
</div>
{shared_js()}
{fb_imports()}
let CU=null;
onAuthStateChanged(auth,async u=>{{
  if(!u){{location.href='index.html';return;}}
  CU=u;
  document.getElementById('loader').classList.add('out');
  const id=getParam('id');
  if(!id){{history.back();return;}}
  let w=null;
  try{{const s=await getDoc(doc(db,'works',id));if(s.exists())w={{id:s.id,...s.data()}};}}
  catch(e){{}}
  if(!w)w=DEMO_WORKS.find(x=>x.id===id);
  if(!w){{history.back();return;}}
  saveState('currentWork',w);
  document.getElementById('det-tags').innerHTML=`<span class="tag" style="background:rgba(255,255,255,.2);color:#fff;">${{w.trade||''}}</span>${{w.urgency&&w.urgency!=='Normal'?`<span class="tag t-or">${{w.urgency.toUpperCase()}}</span>`:''}}`;
  document.getElementById('det-title').textContent=w.title;
  document.getElementById('det-co').textContent='🏢 '+(w.company||w.postedByName||'')+' · 📍 '+(w.location||'');
  document.getElementById('det-bud').textContent=fmtBudget(w);
  document.getElementById('det-loc').textContent=w.location||'—';
  document.getElementById('det-dur').textContent=w.duration?w.duration+' Days':'—';
  document.getElementById('det-std').textContent=w.startDate||'—';
  document.getElementById('det-exp').textContent=w.experience||'—';
  document.getElementById('det-lab').textContent=w.labour||'—';
  document.getElementById('det-bt').textContent=(w.bids||0)+' bids received';
  document.getElementById('det-dl').textContent=w.startDate?'Start: '+w.startDate:'';
  document.getElementById('det-pf').style.width=Math.min(100,((w.bids||0)/12)*100)+'%';
  document.getElementById('det-scope').innerHTML=w.scope?w.scope.split(/\\n/).filter(s=>s.trim()).map(s=>`<div class="blit"><div class="bdo"></div>${{s.trim()}}</div>`).join(''):'<p style="color:var(--s4);font-size:13px;">No scope details.</p>';
  document.getElementById('apply-btn').onclick=()=>go('quote.html',{{id:id}});
  // Check applied
  try{{
    let snap;
    try{{snap=await getDocs(query(collection(db,'applications'),where('workId','==',id),where('applicantId','==',u.uid)));}}
    catch(e2){{snap=await getDocs(query(collection(db,'applications'),where('workId','==',id)));}}
    const applied=!snap.empty&&snap.docs.some(d=>d.data().applicantId===u.uid);
    document.getElementById('det-applied-box').style.display=applied?'block':'none';
    document.getElementById('det-cta').style.display=applied?'none':'flex';
  }}catch(e){{}}
}});
function toggleSave(){{const b=document.getElementById('save-btn');b.textContent=b.textContent==='🔖'?'🔖✓':'🔖';toast('Saved to bookmarks','ok');}}
</script>
{foot()}'''

# ─────────────────────────────────────────
# 6. quote.html — Submit Quotation
# ─────────────────────────────────────────
pages['quote.html'] = f'''{head("Submit Quotation")}
<div style="display:flex;flex-direction:column;min-height:100vh;">
  <div class="tbar"><button class="tbk" onclick="history.back()">←</button><h2>Submit Quotation</h2></div>
  <div class="pscr" style="padding:14px 16px 100px;">
    <div id="work-ref" style="background:var(--blue5);border:1px solid #BFDBFE;border-radius:13px;padding:13px;margin-bottom:18px;">
      <div style="font-family:var(--h);font-size:13px;font-weight:700;color:var(--blue2);margin-bottom:5px;" id="q-wt">Loading work…</div>
      <div style="display:flex;gap:12px;font-size:12px;color:var(--s3);flex-wrap:wrap;"><span id="q-wco">—</span><span id="q-wloc">—</span><span id="q-wbud" style="color:var(--green2);font-weight:700;">—</span></div>
    </div>
    <div class="slbl"><div class="snm">1</div>Your Price</div>
    <div class="g2">
      <div class="field"><label class="flbl">Quote Amount (₹) *</label><input class="fin" id="q-amt" type="number" placeholder="275000" inputmode="numeric"/></div>
      <div class="field"><label class="flbl">Timeline (Days) *</label><input class="fin" id="q-days" type="number" placeholder="40" inputmode="numeric"/></div>
    </div>
    <div class="field"><label class="flbl">Labour Count</label><input class="fin" id="q-lab" type="number" placeholder="9" inputmode="numeric"/></div>
    <div class="slbl"><div class="snm">2</div>Your Pitch</div>
    <div class="field"><label class="flbl">Why choose you? *</label><textarea class="fin" id="q-pitch" rows="4" placeholder="Describe your experience, past projects, quality standards…"></textarea></div>
    <div class="slbl"><div class="snm">3</div>Payment Terms</div>
    <div class="field"><label class="flbl">Terms</label><select class="fin" id="q-terms"><option>30% advance · 40% mid · 30% completion</option><option>50% advance · 50% completion</option><option>100% on completion</option><option>Custom terms</option></select></div>
    <div class="slbl"><div class="snm">4</div>Attachments (Optional)</div>
    <div class="field">
      <label class="attach-zone" onclick="document.getElementById('q-files').click()">
        <span style="font-size:28px;">📎</span>
        <span id="attach-lbl" style="font-size:13px;font-weight:600;color:var(--s3);">Tap to upload files</span>
        <span style="font-size:11px;color:var(--s5);">PDF, JPG, PNG · Max 10MB each</span>
      </label>
      <input type="file" id="q-files" multiple accept=".pdf,.jpg,.jpeg,.png" style="display:none;" onchange="showFiles(this)"/>
      <div id="attach-list" style="margin-top:8px;display:flex;flex-direction:column;gap:6px;"></div>
    </div>
    <div class="ferr" id="q-err">Please fill all required fields.</div>
    <button class="btn btn-p btn-bl btn-lg" id="q-btn" onclick="submitQuote()" style="margin-top:8px;">Submit Quotation →</button>
  </div>
</div>
{shared_js()}
{fb_imports()}
let CU=null,CD=null,CW=null;
onAuthStateChanged(auth,async u=>{{
  if(!u){{location.href='index.html';return;}}
  CU=u;
  const s=await getDoc(doc(db,'users',u.uid));
  CD=s.exists()?s.data():null;
  document.getElementById('loader').classList.add('out');
  const id=getParam('id');
  CW=getState('currentWork');
  if(!CW&&id){{
    try{{const ws=await getDoc(doc(db,'works',id));if(ws.exists())CW={{id:ws.id,...ws.data()}};}}
    catch(e){{CW=DEMO_WORKS.find(x=>x.id===id);}}
  }}
  if(CW){{
    document.getElementById('q-wt').textContent=CW.title;
    document.getElementById('q-wco').textContent='🏢 '+(CW.company||CW.postedByName||'');
    document.getElementById('q-wloc').textContent='📍 '+(CW.location||'');
    document.getElementById('q-wbud').textContent=fmtBudget(CW);
  }}
}});
async function submitQuote(){{
  const amt=document.getElementById('q-amt').value,days=document.getElementById('q-days').value,pitch=document.getElementById('q-pitch').value.trim(),err=document.getElementById('q-err'),btn=document.getElementById('q-btn');
  if(!amt||!days||!pitch){{err.classList.add('on');return;}}err.classList.remove('on');
  btn.classList.add('btn-ld');btn.textContent='Submitting…';
  try{{
    await addDoc(collection(db,'applications'),{{
      workId:CW.id,workTitle:CW.title,workCompany:CW.company||CW.postedByName||'',workLocation:CW.location||'',
      applicantId:CU.uid,applicantName:CD?.name||'',applicantPhone:CD?.phone||'',
      amount:Number(amt),days:Number(days),labour:document.getElementById('q-lab').value||'',
      pitch,terms:document.getElementById('q-terms').value,status:'pending',createdAt:serverTimestamp()
    }});
    try{{await updateDoc(doc(db,'works',CW.id),{{bids:(CW.bids||0)+1}});}}catch(e){{}}
    toast('Quotation submitted! 🎉','ok');
    setTimeout(()=>location.href='apps.html',1200);
  }}catch(e){{toast('Error: '+e.message,'err');}}
  btn.classList.remove('btn-ld');btn.textContent='Submit Quotation →';
}}
function showFiles(input){{
  const list=document.getElementById('attach-list');list.innerHTML='';
  Array.from(input.files).forEach(f=>{{
    const div=document.createElement('div');div.className='attach-file';
    const ico=f.type.includes('pdf')?'📄':'🖼️';
    div.innerHTML=`<span style="font-size:18px;">${{ico}}</span><div style="flex:1;"><div style="font-weight:600;">${{f.name}}</div><div style="font-size:11px;color:var(--s4);">${{(f.size/1024).toFixed(0)}}KB</div></div><span style="color:var(--green2);">✓</span>`;
    list.appendChild(div);
  }});
  if(input.files.length){{document.getElementById('attach-lbl').textContent=input.files.length+' file(s) selected';}}
}}
</script>
{foot()}'''

# ─────────────────────────────────────────
# 7. apps.html — My Applications
# ─────────────────────────────────────────
pages['apps.html'] = f'''{head("My Applications")}
<div style="display:flex;flex-direction:column;min-height:100vh;">
  <div class="tbar"><h2>My Applications</h2><button class="btn btn-p btn-sm" onclick="go('find.html')">Find Work</button></div>
  <div class="chips" style="padding:12px 16px 0;flex-shrink:0;">
    <div class="chip on" onclick="setChip(this,'all')">All</div>
    <div class="chip" onclick="setChip(this,'pending')">Pending</div>
    <div class="chip" onclick="setChip(this,'rev')">Shortlisted</div>
    <div class="chip" onclick="setChip(this,'awarded')">Awarded</div>
    <div class="chip" onclick="setChip(this,'rejected')">Rejected</div>
  </div>
  <div class="pscr pb90" style="padding:10px 16px 0;" id="apps-list"><div class="empty"><div class="spin" style="margin:0 auto;"></div></div></div>
  {bnav_petty('apps')}
</div>
{shared_js()}
{fb_imports()}
let allApps=[],filterA='all';
onAuthStateChanged(auth,async u=>{{
  if(!u){{location.href='index.html';return;}}
  document.getElementById('loader').classList.add('out');
  try{{
    let snap;
    try{{snap=await getDocs(query(collection(db,'applications'),where('applicantId','==',u.uid),orderBy('createdAt','desc')));}}
    catch(e2){{snap=await getDocs(query(collection(db,'applications'),where('applicantId','==',u.uid)));}}
    allApps=snap.docs.map(d=>({{id:d.id,...d.data()}}));
    allApps.sort((a,b)=>(b.createdAt?.toMillis?.()||b.createdAt||0)-(a.createdAt?.toMillis?.()||a.createdAt||0));
  }}catch(e){{allApps=[];}}
  renderApps();
}});
const SL={{pending:'Under Review',review:'Shortlisted ✓',shortlisted:'Shortlisted ✓',awarded:'Awarded 🎉',rejected:'Not Selected'}};
const SM={{pending:'pend',review:'rev',shortlisted:'rev',awarded:'awd',rejected:'rej'}};
function renderApps(){{
  const el=document.getElementById('apps-list');
  let arr=filterA==='all'?allApps:allApps.filter(a=>{{
    if(filterA==='rev')return a.status==='review'||a.status==='shortlisted';
    return a.status===filterA;
  }});
  if(!arr.length){{
    el.innerHTML=emptyHTML('📋','No applications yet','Browse works and submit your first quotation!')+`<div style="padding:0 0 10px;"><button class="btn btn-p btn-bl" onclick="go('find.html')">Browse Works →</button></div>`;
    return;
  }}
  el.innerHTML=arr.map(a=>`<div class="arow">
    <div class="art">${{a.workTitle}}</div>
    <div class="ars">${{a.workCompany||'—'}} · ${{a.workLocation||'—'}}</div>
    <div style="font-size:12px;color:var(--s4);margin-bottom:9px;">Quoted ₹${{Number(a.amount).toLocaleString('en-IN')}} · ${{a.days}} days</div>
    <div class="arf">
      <span class="sts ${{SM[a.status||'pending']||'pend'}}">${{SL[a.status||'pending']||'Under Review'}}</span>
      <div style="display:flex;gap:6px;">
        ${{a.status==='awarded'?`<button class="btn btn-sm" style="background:var(--green4);color:var(--green);border:none;" onclick="toast('Rating feature coming soon!','ok')">Rate ⭐</button>`:''}}<button class="btn btn-g btn-sm" onclick="go('chat.html')">💬</button>
      </div>
    </div>
  </div>`).join('');
}}
function setChip(el,f){{document.querySelectorAll('.chip').forEach(c=>c.classList.remove('on'));el.classList.add('on');filterA=f;renderApps();}}
</script>
{foot()}'''

# ─────────────────────────────────────────
# 8. post.html — Post New Work
# ─────────────────────────────────────────
pages['post.html'] = f'''{head("Post New Work")}
<div style="display:flex;flex-direction:column;min-height:100vh;">
  <div class="tbar"><button class="tbk" onclick="history.back()">←</button><h2>Post New Work</h2></div>
  <div class="pscr" style="padding:14px 16px 100px;">
    <div style="background:linear-gradient(135deg,var(--blue5),#fff);border:1px solid #BFDBFE;border-radius:14px;padding:16px;margin-bottom:18px;text-align:center;">
      <svg viewBox="0 0 240 80" width="100%" height="70" fill="none">
        <rect x="10" y="20" width="35" height="55" rx="2" fill="#1E40AF"/><rect x="16" y="28" width="8" height="7" rx="1" fill="#93C5FD" opacity=".9"/><rect x="30" y="28" width="8" height="7" rx="1" fill="white" opacity=".8"/>
        <rect x="60" y="35" width="55" height="40" rx="2" fill="#334155"/><rect x="57" y="18" width="3" height="57" rx="1" fill="#64748B"/><rect x="112" y="18" width="3" height="57" rx="1" fill="#64748B"/><rect x="57" y="18" width="58" height="3" rx="1" fill="#64748B"/>
        <rect x="170" y="5" width="4" height="70" rx="2" fill="#EA580C"/><rect x="148" y="5" width="50" height="4" rx="2" fill="#F97316"/><rect x="188" y="1" width="14" height="11" rx="2" fill="#DC2626"/>
        <line x1="160" y1="9" x2="160" y2="28" stroke="#94A3B8" stroke-width="1.5"/><rect x="153" y="28" width="14" height="9" rx="2" fill="#F97316"/>
        <circle cx="130" cy="52" r="5" fill="#FBBF24"/><rect x="125" y="57" width="10" height="11" rx="2" fill="#2563EB"/><path d="M124 52 Q130 44 136 52" fill="#EA580C"/>
      </svg>
      <div style="font-family:var(--h);font-size:12px;font-weight:700;color:var(--blue2);margin-top:6px;">Post Work → Get Quotations → Award Best Contractor</div>
    </div>
    <div class="slbl"><div class="snm">1</div>Basic Details</div>
    <div class="field"><label class="flbl">Work Title *</label><input class="fin" id="pw-tit" placeholder="e.g. Interior Plastering – Block A"/></div>
    <div class="g2">
      <div class="field"><label class="flbl">Trade Type *</label>
        <select class="fin" id="pw-tr" onchange="toggleOther()">
          <option value="">Select…</option><option>Plastering</option><option>Flooring</option><option>Painting</option><option>Electrical</option><option>Plumbing</option><option>Masonry</option><option>Carpentry</option><option>Tiling</option><option>Waterproofing</option><option>Civil Work</option><option value="Other">Other (specify below)</option>
        </select>
      </div>
      <div class="field"><label class="flbl">Urgency</label><select class="fin" id="pw-urg"><option value="Normal">Normal</option><option value="Urgent">Urgent</option><option value="Critical">Critical</option></select></div>
    </div>
    <div class="field" id="pw-other-wrap" style="display:none;"><label class="flbl">Specify Trade *</label><input class="fin" id="pw-other" placeholder="e.g. Guniting, Grouting, Scaffolding…"/></div>
    <div class="field"><label class="flbl">Project Location *</label><input class="fin" id="pw-loc" placeholder="e.g. Hinjewadi, Pune"/></div>
    <div class="slbl"><div class="snm">2</div>Budget & Timeline</div>
    <div class="g2">
      <div class="field"><label class="flbl">Min Budget (₹) *</label><input class="fin" id="pw-min" type="number" placeholder="250000" inputmode="numeric"/></div>
      <div class="field"><label class="flbl">Max Budget (₹) *</label><input class="fin" id="pw-max" type="number" placeholder="300000" inputmode="numeric"/></div>
    </div>
    <div class="g2">
      <div class="field"><label class="flbl">Start Date</label><input class="fin" id="pw-std" type="date"/></div>
      <div class="field"><label class="flbl">Duration (Days)</label><input class="fin" id="pw-dur" type="number" placeholder="45" inputmode="numeric"/></div>
    </div>
    <div class="slbl"><div class="snm">3</div>Requirements</div>
    <div class="g2">
      <div class="field"><label class="flbl">Min Experience</label><input class="fin" id="pw-exp" placeholder="5 years"/></div>
      <div class="field"><label class="flbl">Labour Count</label><input class="fin" id="pw-lab" placeholder="8–10"/></div>
    </div>
    <div class="field"><label class="flbl">Scope of Work *</label><textarea class="fin" id="pw-scope" rows="5" placeholder="Full scope, quality standards, materials expected…"></textarea></div>
    <div class="slbl"><div class="snm">4</div>Attachments (Optional)</div>
    <div class="field">
      <label class="attach-zone" onclick="document.getElementById('pw-files').click()">
        <span style="font-size:28px;">📎</span>
        <span id="pw-attach-lbl" style="font-size:13px;font-weight:600;color:var(--s3);">Tap to upload BOQ / Drawings / Photos</span>
        <span style="font-size:11px;color:var(--s5);">PDF, JPG, PNG, DWG · Max 10MB each</span>
      </label>
      <input type="file" id="pw-files" multiple accept=".pdf,.jpg,.jpeg,.png,.dwg" style="display:none;" onchange="showFiles(this,'pw-attach-lbl','pw-attach-list')"/>
      <div id="pw-attach-list" style="margin-top:8px;display:flex;flex-direction:column;gap:6px;"></div>
    </div>
    <div class="ferr" id="pw-err">Please fill all required fields.</div>
    <button class="btn btn-o btn-bl btn-lg" id="pw-btn" onclick="postWork()" style="margin-top:8px;">Post Work →</button>
  </div>
</div>
{shared_js()}
{fb_imports()}
let CU=null,CD=null;
onAuthStateChanged(auth,async u=>{{
  if(!u){{location.href='index.html';return;}}
  CU=u;
  const s=await getDoc(doc(db,'users',u.uid));
  CD=s.exists()?s.data():null;
  if(CD?.role!=='main'){{location.href='home.html';return;}}
  document.getElementById('loader').classList.add('out');
}});
function toggleOther(){{document.getElementById('pw-other-wrap').style.display=document.getElementById('pw-tr').value==='Other'?'block':'none';}}
async function postWork(){{
  const rawTrade=document.getElementById('pw-tr').value,trade=rawTrade==='Other'?(document.getElementById('pw-other').value.trim()||'Other'):rawTrade;
  const title=document.getElementById('pw-tit').value.trim(),loc=document.getElementById('pw-loc').value.trim(),minB=document.getElementById('pw-min').value,maxB=document.getElementById('pw-max').value,scope=document.getElementById('pw-scope').value.trim(),err=document.getElementById('pw-err'),btn=document.getElementById('pw-btn');
  if(!title||!trade||!loc||!minB||!maxB||!scope){{err.classList.add('on');return;}}err.classList.remove('on');
  btn.classList.add('btn-ld');btn.textContent='Posting…';
  try{{
    await addDoc(collection(db,'works'),{{
      title,trade,location:loc,company:CD?.name||'Main Contractor',postedByName:CD?.name||'',postedBy:CU.uid,
      minBudget:Number(minB),maxBudget:Number(maxB),duration:document.getElementById('pw-dur').value||'',
      startDate:document.getElementById('pw-std').value||'',experience:document.getElementById('pw-exp').value||'',
      labour:document.getElementById('pw-lab').value||'',urgency:document.getElementById('pw-urg').value,
      scope,bids:0,status:'open',createdAt:serverTimestamp()
    }});
    toast('Work posted! 🎉','ok');
    setTimeout(()=>location.href='myworks.html',1200);
  }}catch(e){{toast('Error: '+e.message,'err');}}
  btn.classList.remove('btn-ld');btn.textContent='Post Work →';
}}
function showFiles(input,lblId,listId){{
  const list=document.getElementById(listId);list.innerHTML='';
  Array.from(input.files).forEach(f=>{{
    const div=document.createElement('div');div.className='attach-file';
    const ico=f.type.includes('pdf')?'📄':'🖼️';
    div.innerHTML=`<span style="font-size:18px;">${{ico}}</span><div style="flex:1;"><div style="font-weight:600;">${{f.name}}</div><div style="font-size:11px;color:var(--s4);">${{(f.size/1024).toFixed(0)}}KB</div></div><span style="color:var(--green2);">✓</span>`;
    list.appendChild(div);
  }});
  if(input.files.length)document.getElementById(lblId).textContent=input.files.length+' file(s) selected';
}}
</script>
{foot()}'''

# ─────────────────────────────────────────
# 9. myworks.html — My Posted Works
# ─────────────────────────────────────────
pages['myworks.html'] = f'''{head("My Works")}
<div style="display:flex;flex-direction:column;min-height:100vh;">
  <div class="tbar"><button class="tbk" onclick="history.back()">←</button><h2>My Works</h2><button class="btn btn-o btn-sm" onclick="go('post.html')">+ Post</button></div>
  <div class="pscr pb90" style="padding:12px 16px 0;" id="myw-list"><div class="empty"><div class="spin" style="margin:0 auto;"></div></div></div>
  {bnav_main('myworks')}
</div>
{shared_js()}
{fb_imports()}
onAuthStateChanged(auth,async u=>{{
  if(!u){{location.href='index.html';return;}}
  document.getElementById('loader').classList.add('out');
  let works=[];
  try{{const ws=await getDocs(query(collection(db,'works'),where('postedBy','==',u.uid)));works=ws.docs.map(d=>({{id:d.id,...d.data()}}));}}
  catch(e){{works=DEMO_WORKS.slice(0,3);}}
  const el=document.getElementById('myw-list');
  if(!works.length){{el.innerHTML=emptyHTML('🏗️','No works posted yet','Post your first work')+`<div style="padding:0 0 10px;"><button class="btn btn-o btn-bl btn-lg" onclick="go('post.html')">Post Now →</button></div>`;return;}}
  el.innerHTML=works.map(w=>`<div class="arow" onclick="go('bids.html',{{id:'${{w.id}}'}})">
    <div class="tags" style="margin-bottom:7px;"><span class="tag t-bl">${{w.trade||'—'}}</span><span class="tag ${{tagColor(w.urgency)}}">${{w.urgency||'Normal'}}</span></div>
    <div class="art">${{w.title}}</div>
    <div class="ars">📍 ${{w.location||'—'}} · ${{fmtBudget(w)}}</div>
    <div class="arf"><span class="sts ${{w.status==='awarded'?'awd':'open'}}">${{w.status==='awarded'?'Awarded ✓':'Accepting Bids'}}</span><span style="font-size:12px;font-weight:700;color:var(--blue2);">${{w.bids||0}} bids →</span></div>
  </div>`).join('');
}});
</script>
{foot()}'''

# ─────────────────────────────────────────
# 10. bids.html — Bid Management
# ─────────────────────────────────────────
pages['bids.html'] = f'''{head("Bid Management")}
<div style="display:flex;flex-direction:column;min-height:100vh;">
  <div class="tbar"><button class="tbk" onclick="history.back()">←</button><h2>Bid Management</h2><span id="bids-cnt" class="tag t-bl" style="flex-shrink:0;">0</span></div>
  <div style="background:var(--blue5);border-bottom:1px solid var(--s7);padding:10px 16px;flex-shrink:0;">
    <div style="font-family:var(--h);font-size:13px;font-weight:700;color:var(--blue2);" id="bw-tit">—</div>
    <div style="font-size:11px;color:var(--s4);" id="bw-meta">—</div>
  </div>
  <div class="pscr pb90" style="padding:12px 16px 0;" id="bids-list"><div class="empty"><div class="spin" style="margin:0 auto;"></div></div></div>
</div>

<!-- AWARD SHEET -->
<div class="ovl off" id="award-ovl">
  <div class="sheet">
    <div class="shdl"></div>
    <div class="shtit">Award This Work 🏆</div>
    <p style="font-size:14px;color:var(--s3);margin-bottom:20px;line-height:1.6;" id="award-txt">—</p>
    <button class="btn btn-o btn-bl btn-lg" onclick="confirmAward()">Yes, Award Work →</button>
    <button class="btn btn-g btn-bl" style="margin-top:10px;" onclick="document.getElementById('award-ovl').classList.add('off')">Cancel</button>
  </div>
</div>
{shared_js()}
{fb_imports()}
let pendingAward=null;
onAuthStateChanged(auth,async u=>{{
  if(!u){{location.href='index.html';return;}}
  document.getElementById('loader').classList.add('out');
  const id=getParam('id');if(!id){{history.back();return;}}
  let w=null;
  try{{const s=await getDoc(doc(db,'works',id));if(s.exists())w={{id:s.id,...s.data()}};}}catch(e){{}}
  if(!w)w=DEMO_WORKS.find(x=>x.id===id);
  if(!w){{history.back();return;}}
  document.getElementById('bw-tit').textContent=w.title;
  document.getElementById('bw-meta').textContent=`📍 ${{w.location||''}} · ${{fmtBudget(w)}} · ${{w.bids||0}} quotations received`;
  let apps=[];
  try{{const as=await getDocs(query(collection(db,'applications'),where('workId','==',id)));apps=as.docs.map(d=>({{id:d.id,...d.data()}}));}}catch(e){{}}
  if(!apps.length&&id.startsWith('d'))apps=[
    {{id:'b1',applicantName:'Mohan Kumar',amount:265000,days:40,pitch:'15 years plastering experience across Pune and Mumbai. 12 major residential projects.',rating:4.8,projects:12,status:'pending'}},
    {{id:'b2',applicantName:'Rajesh Patil',amount:275000,days:38,pitch:'Expert plasterer with 8 years. High-end residential specialist. Full team safety-certified.',rating:4.7,projects:15,status:'pending'}},
    {{id:'b3',applicantName:'Suresh More',amount:280000,days:45,pitch:'Quality work with 1 year warranty. References from Lodha and Godrej available.',rating:4.5,projects:8,status:'pending'}},
    {{id:'b4',applicantName:'Vijay Deshmukh',amount:290000,days:48,pitch:'Honest contractor, dedicated team, fully committed to quality.',rating:4.2,projects:5,status:'pending'}},
  ];
  document.getElementById('bids-cnt').textContent=apps.length;
  const cols=['#1D4ED8','#059669','#7C3AED','#EA580C','#DC2626'];
  const el=document.getElementById('bids-list');
  if(!apps.length){{el.innerHTML=emptyHTML('📬','No bids yet','Share your work to attract contractors');return;}}
  el.innerHTML=apps.map((a,i)=>`<div class="bcard ${{i===0?'top':''}}">
    ${{i===0?'<div class="bbadge">BEST MATCH</div>':''}}
    <div style="display:flex;gap:11px;align-items:center;margin-bottom:10px;">
      <div class="bav" style="background:${{cols[i%5]}};">${{initials(a.applicantName||'C')}}</div>
      <div style="flex:1;"><div class="bnm">${{a.applicantName||'Contractor'}}</div><div class="bsb">${{a.rating?'⭐ '+a.rating+' · ':''}}${{a.projects||0}} projects</div></div>
      <div style="text-align:right;"><div class="bpr">₹${{Number(a.amount).toLocaleString('en-IN')}}</div><div style="font-size:10px;color:var(--s4);">${{a.days}} days</div></div>
    </div>
    <div class="bpit">"${{a.pitch||'No pitch provided'}}"</div>
    <div style="display:flex;gap:8px;">
      ${{a.status==='awarded'?'<span class="sts awd" style="padding:8px 14px;">Awarded ✓</span>':`<button class="btn btn-g btn-sm" style="flex:1;" onclick="go('chat.html')">💬 Chat</button><button class="btn btn-o btn-sm" onclick="showAward('${{a.id}}','${{a.applicantName}}')">Award →</button>`}}
    </div>
  </div>`).join('');
}});
function showAward(id,name){{pendingAward=id;document.getElementById('award-txt').textContent=`Award this work to ${{name}}? They will be notified immediately.`;document.getElementById('award-ovl').classList.remove('off');}}
async function confirmAward(){{
  if(!pendingAward)return;
  try{{await updateDoc(doc(db,'applications',pendingAward),{{status:'awarded'}});toast('Work awarded! 🏆','ok');setTimeout(()=>location.href='myworks.html',1200);}}
  catch(e){{toast('Error: '+e.message,'err');}}
  document.getElementById('award-ovl').classList.add('off');
}}
</script>
{foot()}'''

# ─────────────────────────────────────────
# 11. profile.html — Profile
# ─────────────────────────────────────────
pages['profile.html'] = f'''{head("My Profile")}
<div style="display:flex;flex-direction:column;min-height:100vh;">
  <div class="pscr pb90">
    <div class="ph">
      <div style="display:flex;justify-content:flex-end;margin-bottom:10px;"><button class="tbk" style="background:rgba(255,255,255,.2);color:#fff;" onclick="document.getElementById('edit-ovl').classList.remove('off')">✏️ Edit</button></div>
      <div class="pav" id="pf-av">RP<div class="pav-ver">✓</div></div>
      <div class="pnm" id="pf-nm">—</div>
      <div class="prl" id="pf-rl">—</div>
      <div class="pst">★★★★★</div>
      <div class="skts" id="pf-sk"></div>
    </div>
    <div class="psts">
      <div class="psi"><div class="psn" id="ps-proj">0</div><div class="psl">Projects</div></div>
      <div class="psi"><div class="psn" id="ps-exp">—</div><div class="psl">Yrs Exp</div></div>
      <div class="psi"><div class="psn">4.8</div><div class="psl">Rating</div></div>
    </div>
    <div class="psec">
      <div class="prow"><div class="pro-ico">📞</div><div style="flex:1;"><div class="pro-txt" id="pf-ph">—</div><div style="font-size:11px;color:var(--s4);">Phone</div></div></div>
      <div class="prow"><div class="pro-ico">📍</div><div style="flex:1;"><div class="pro-txt" id="pf-ct">—</div><div style="font-size:11px;color:var(--s4);">Location</div></div></div>
      <div class="prow"><div class="pro-ico">📧</div><div style="flex:1;"><div class="pro-txt" id="pf-em">—</div><div style="font-size:11px;color:var(--s4);">Email</div></div></div>
    </div>
    <div class="psec" style="margin-top:0;">
      <div class="prow"><div class="pro-ico">🪪</div><div class="pro-txt">Aadhaar Verified</div><div class="pro-badge">Verified</div></div>
      <div class="prow"><div class="pro-ico">🏦</div><div class="pro-txt">Bank Account</div><div class="pro-badge">Linked</div></div>
    </div>
    <div class="psec" style="margin-top:0;">
      <div class="prow" onclick="go('notifications.html')"><div class="pro-ico">🔔</div><div class="pro-txt">Notifications</div><div class="pro-arr">›</div></div>
      <div class="prow" onclick="document.getElementById('help-ovl').classList.remove('off')"><div class="pro-ico">❓</div><div class="pro-txt">Help & Support</div><div class="pro-arr">›</div></div>
      <div class="prow" onclick="document.getElementById('about-ovl').classList.remove('off')"><div class="pro-ico">ℹ️</div><div class="pro-txt">About Pragati</div><div class="pro-arr">›</div></div>
      <div class="prow" onclick="doLogout()"><div class="pro-ico">🚪</div><div class="pro-txt" style="color:var(--red2);">Logout</div><div class="pro-arr" style="color:var(--red2);">›</div></div>
    </div>
    <div style="height:16px;"></div>
  </div>
  <div class="bnav n4" id="pf-bnav"></div>
</div>

<!-- EDIT PROFILE -->
<div class="ovl off" id="edit-ovl">
  <div class="sheet">
    <div class="shdl"></div>
    <div class="shtit">Edit Profile</div>
    <div class="field"><label class="flbl">Full Name</label><input class="fin" id="ep-nm"/></div>
    <div class="g2">
      <div class="field"><label class="flbl">Phone</label><input class="fin" id="ep-ph" type="tel" inputmode="tel"/></div>
      <div class="field"><label class="flbl">City</label><input class="fin" id="ep-ct"/></div>
    </div>
    <div class="field" id="ep-tw"><label class="flbl">Primary Trade</label><select class="fin" id="ep-tr"><option value="">—</option><option>Plastering</option><option>Flooring</option><option>Painting</option><option>Electrical</option><option>Plumbing</option><option>Masonry</option><option>Carpentry</option><option>Tiling</option><option>Waterproofing</option><option>Civil Work</option><option>Other</option></select></div>
    <div class="g2">
      <div class="field"><label class="flbl">Years Exp.</label><input class="fin" id="ep-exp" type="number" inputmode="numeric"/></div>
      <div class="field"><label class="flbl">Company/Firm</label><input class="fin" id="ep-co"/></div>
    </div>
    <div class="field"><label class="flbl">Bio / About You</label><textarea class="fin" id="ep-bio" rows="3"></textarea></div>
    <button class="btn btn-p btn-bl btn-lg" onclick="saveProfile()">Save Profile</button>
    <button class="btn btn-g btn-bl" style="margin-top:10px;" onclick="document.getElementById('edit-ovl').classList.add('off')">Cancel</button>
  </div>
</div>

<!-- HELP -->
<div class="ovl off" id="help-ovl">
  <div class="sheet">
    <div class="shdl"></div>
    <div class="shtit">Help & Support</div>
    <div class="psec" style="margin:0 0 12px;">
      <div class="prow"><div class="pro-ico">📞</div><div class="pro-txt">Call: +91 800-PRAGATI</div></div>
      <div class="prow"><div class="pro-ico">📧</div><div class="pro-txt">support@pragati.in</div></div>
      <div class="prow"><div class="pro-ico">💬</div><div class="pro-txt">WhatsApp Support</div></div>
    </div>
    <div style="background:var(--s8);border-radius:12px;padding:14px;font-size:13px;color:var(--s3);line-height:1.7;margin-bottom:12px;">
      <strong>How to apply:</strong> Find Work → Open work → Submit Quotation<br/>
      <strong>How to post work:</strong> Dashboard → Post New Work<br/>
      <strong>How to award:</strong> My Works → View Bids → Award
    </div>
    <button class="btn btn-g btn-bl" onclick="document.getElementById('help-ovl').classList.add('off')">Close</button>
  </div>
</div>

<!-- ABOUT -->
<div class="ovl off" id="about-ovl">
  <div class="sheet">
    <div class="shdl"></div>
    <div style="text-align:center;margin-bottom:16px;">
      <div class="ld-icon" style="margin:0 auto 12px;"><img src="{LOGO}" style="width:100%;height:100%;object-fit:contain;" onerror="this.style.display='none'"/></div>
      <div style="font-family:var(--h);font-size:20px;font-weight:800;">Pragati Work Exchange</div>
      <div style="font-size:13px;color:var(--s4);margin-top:4px;">Version 1.0.0 · PragatiOne Platform</div>
    </div>
    <div style="font-size:13px;color:var(--s3);line-height:1.7;margin-bottom:16px;">India's leading marketplace for construction subcontract work. Connecting Main Contractors with verified Petty Contractors across 28 states.</div>
    <button class="btn btn-g btn-bl" onclick="document.getElementById('about-ovl').classList.add('off')">Close</button>
  </div>
</div>

{shared_js()}
{fb_imports()}
let CU=null,CD=null;
onAuthStateChanged(auth,async u=>{{
  if(!u){{location.href='index.html';return;}}
  CU=u;
  const s=await getDoc(doc(db,'users',u.uid));
  CD=s.exists()?s.data():null;
  if(!CD){{location.href='index.html';return;}}
  document.getElementById('loader').classList.add('out');
  // Build bottom nav based on role
  const nav=document.getElementById('pf-bnav');
  const isMain=CD.role==='main';
  nav.innerHTML=`
    <div class="bni" onclick="location.href='${{isMain?'main.html':'home.html'}}'"><div class="ico">🏠</div><div class="lbl">Home</div></div>
    <div class="bni" onclick="location.href='${{isMain?'post.html':'find.html'}}'"><div class="ico">${{isMain?'➕':'🔍'}}</div><div class="lbl">${{isMain?'Post Work':'Find Work'}}</div></div>
    <div class="bni" onclick="location.href='${{isMain?'myworks.html':'apps.html'}}'"><div class="ico">📋</div><div class="lbl">${{isMain?'My Works':'My Bids'}}</div></div>
    <div class="bni on"><div class="ico">👤</div><div class="lbl">Profile</div></div>`;
  // Fill profile
  const n=CD.name||'User';
  document.getElementById('pf-av').innerHTML=initials(n)+'<div class="pav-ver">✓</div>';
  document.getElementById('pf-nm').textContent=n;
  document.getElementById('pf-rl').textContent=(CD.trade||CD.role==='main'?'Main Contractor':'Petty Contractor')+(CD.city?' · '+CD.city:'');
  document.getElementById('pf-ph').textContent=CD.phone||'—';
  document.getElementById('pf-ct').textContent=CD.city||'—';
  document.getElementById('pf-em').textContent=CD.email||'—';
  document.getElementById('ps-exp').textContent=CD.exp||'—';
  document.getElementById('pf-sk').innerHTML=CD.trade?`<span class="skt">${{CD.trade}}</span>`:'';
  // Pre-fill edit form
  document.getElementById('ep-nm').value=CD.name||'';
  document.getElementById('ep-ph').value=CD.phone||'';
  document.getElementById('ep-ct').value=CD.city||'';
  document.getElementById('ep-tr').value=CD.trade||'';
  document.getElementById('ep-exp').value=CD.exp||'';
  document.getElementById('ep-co').value=CD.company||'';
  document.getElementById('ep-bio').value=CD.bio||'';
  if(isMain)document.getElementById('ep-tw').style.display='none';
}});
async function saveProfile(){{
  const u={{name:document.getElementById('ep-nm').value.trim()||CD.name,phone:document.getElementById('ep-ph').value.trim(),city:document.getElementById('ep-ct').value.trim(),trade:document.getElementById('ep-tr').value,exp:document.getElementById('ep-exp').value,company:document.getElementById('ep-co').value.trim(),bio:document.getElementById('ep-bio').value.trim()}};
  try{{await updateDoc(doc(db,'users',CU.uid),u);CD={{...CD,...u}};toast('Profile saved ✓','ok');document.getElementById('edit-ovl').classList.add('off');location.reload();}}
  catch(e){{toast('Error: '+e.message,'err');}}
}}
async function doLogout(){{await signOut(auth);location.href='index.html';}}
</script>
{foot()}'''

# ─────────────────────────────────────────
# 12. chat.html — Messages
# ─────────────────────────────────────────
pages['chat.html'] = f'''{head("Messages")}
<div style="display:flex;flex-direction:column;min-height:100vh;">
  <div id="chat-list-view" style="display:flex;flex-direction:column;flex:1;">
    <div class="tbar"><button class="tbk" onclick="history.back()">←</button><h2>Messages</h2></div>
    <div style="flex:1;overflow-y:auto;background:#fff;" id="chat-list">
      <div class="cli" onclick="openChat('KP','Kalpataru Projects','rgba(37,99,235,.12)','var(--blue2)')"><div class="cav" style="background:rgba(37,99,235,.12);color:var(--blue2);">KP</div><div class="cinfo"><div class="cnm">Kalpataru Projects</div><div class="cpv">Please share availability for site visit</div></div><div style="display:flex;flex-direction:column;align-items:flex-end;gap:4px;"><div style="font-size:10px;color:var(--s5);">2:30 PM</div><div class="cund">2</div></div></div>
      <div class="cli" onclick="openChat('GP','Godrej Properties','rgba(16,185,129,.12)','var(--green2)')"><div class="cav" style="background:rgba(16,185,129,.12);color:var(--green2);">GP</div><div class="cinfo"><div class="cnm">Godrej Properties</div><div class="cpv">Your quotation looks good, let's discuss</div></div><div style="display:flex;flex-direction:column;align-items:flex-end;gap:4px;"><div style="font-size:10px;color:var(--s5);">11:15</div><div class="cund">1</div></div></div>
      <div class="cli" onclick="openChat('SP','Shapoorji Pallonji','rgba(249,115,22,.12)','var(--orange2)')"><div class="cav" style="background:rgba(249,115,22,.12);color:var(--orange2);">SP</div><div class="cinfo"><div class="cnm">Shapoorji Pallonji</div><div class="cpv">Congratulations! Work awarded to you 🎉</div></div><div style="display:flex;flex-direction:column;align-items:flex-end;gap:4px;"><div style="font-size:10px;color:var(--s5);">Yesterday</div></div></div>
      <div class="cli" onclick="openChat('LG','Lodha Group','rgba(124,58,237,.12)','#7C3AED')"><div class="cav" style="background:rgba(124,58,237,.12);color:#7C3AED;">LG</div><div class="cinfo"><div class="cnm">Lodha Group</div><div class="cpv">Please share your GST certificate</div></div><div style="display:flex;flex-direction:column;align-items:flex-end;gap:4px;"><div style="font-size:10px;color:var(--s5);">Mon</div></div></div>
      <div class="cli" onclick="openChat('TR','Tata Realty','rgba(220,38,38,.1)','var(--red2)')"><div class="cav" style="background:rgba(220,38,38,.1);color:var(--red2);">TR</div><div class="cinfo"><div class="cnm">Tata Realty</div><div class="cpv">Site visit scheduled for Saturday 10 AM</div></div><div style="display:flex;flex-direction:column;align-items:flex-end;gap:4px;"><div style="font-size:10px;color:var(--s5);">Sun</div></div></div>
    </div>
    <div class="bnav n4" id="chat-bnav"></div>
  </div>
  <div id="chat-win" style="display:none;flex-direction:column;height:100vh;position:fixed;inset:0;background:#fff;z-index:100;">
    <div style="background:#fff;padding:14px 14px;border-bottom:1px solid var(--s7);display:flex;align-items:center;gap:10px;padding-top:52px;">
      <button class="tbk" onclick="closeChat()">←</button>
      <div class="cav" id="cw-av" style="width:36px;height:36px;border-radius:11px;font-size:13px;flex-shrink:0;">KP</div>
      <div style="flex:1;"><div style="font-family:var(--h);font-size:14px;font-weight:700;" id="cw-nm">—</div><div style="font-size:11px;color:var(--green2);">● Online</div></div>
      <button class="tbk">📞</button>
    </div>
    <div class="mwrap" id="msg-wrap">
      <div class="mtime">Today</div>
      <div class="msg them">Hello! We reviewed your quotation for the plastering work.</div>
      <div class="msg them">Your price looks competitive. Can you visit the site this week?</div>
      <div class="msg me">Thank you! I'm available Saturday 10 AM or Sunday anytime.</div>
      <div class="msg them">Saturday 10 AM works. Hinjewadi Phase 2, ask for Mr. Sharma at gate.</div>
      <div class="msg me">Confirmed! Should I bring any documents?</div>
      <div class="msg them">Please bring Aadhaar copy and photos of past work if any.</div>
    </div>
    <div class="cbar">
      <input class="cin" id="cin" placeholder="Type a message…"/>
      <button class="csnd" onclick="sendMsg()"><svg width="16" height="16" viewBox="0 0 24 24" fill="none"><path d="M22 2L11 13M22 2L15 22L11 13L2 9L22 2Z" stroke="white" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
    </div>
  </div>
</div>
{shared_js()}
{fb_imports()}
let currentChatName='',CU=null,CD=null;
onAuthStateChanged(auth,async u=>{{
  if(!u){{location.href='index.html';return;}}
  CU=u;
  const s=await getDoc(doc(db,'users',u.uid));
  CD=s.exists()?s.data():null;
  document.getElementById('loader').classList.add('out');
  const isMain=CD?.role==='main';
  const nav=document.getElementById('chat-bnav');
  nav.innerHTML=`
    <div class="bni" onclick="location.href='${{isMain?'main.html':'home.html'}}'"><div class="ico">🏠</div><div class="lbl">Home</div></div>
    <div class="bni" onclick="location.href='${{isMain?'post.html':'find.html'}}'"><div class="ico">${{isMain?'➕':'🔍'}}</div><div class="lbl">${{isMain?'Post Work':'Find Work'}}</div></div>
    <div class="bni" onclick="location.href='${{isMain?'myworks.html':'apps.html'}}'"><div class="ico">📋</div><div class="lbl">${{isMain?'My Works':'My Bids'}}</div></div>
    <div class="bni on"><div class="ico">💬</div><div class="lbl">Messages</div></div>`;
}});
function openChat(code,name,bg,color){{
  currentChatName=name;
  document.getElementById('chat-list-view').style.display='none';
  const cw=document.getElementById('chat-win');cw.style.display='flex';cw.style.flexDirection='column';
  const av=document.getElementById('cw-av');av.textContent=code;av.style.background=bg;av.style.color=color;
  document.getElementById('cw-nm').textContent=name;
  document.querySelectorAll('.cli').forEach(c=>{{if(c.querySelector('.cnm')?.textContent===name){{const u=c.querySelector('.cund');if(u)u.remove();}}}});
}}
function closeChat(){{document.getElementById('chat-list-view').style.display='flex';document.getElementById('chat-win').style.display='none';}}
function sendMsg(){{
  const inp=document.getElementById('cin'),txt=inp.value.trim();if(!txt)return;
  const mw=document.getElementById('msg-wrap');
  const m=document.createElement('div');m.className='msg me';m.textContent=txt;mw.appendChild(m);inp.value='';mw.scrollTop=mw.scrollHeight;
  setTimeout(()=>{{
    const replies=['Got it, thanks!','Sure, will check and get back to you.','Please confirm the site visit time.','Yes that works.','Can you share your experience certificate?','We will review and let you know.'];
    const r=document.createElement('div');r.className='msg them';r.textContent=replies[Math.floor(Math.random()*replies.length)];mw.appendChild(r);mw.scrollTop=mw.scrollHeight;
  }},1500);
}}
document.addEventListener('DOMContentLoaded',()=>{{
  const ci=document.getElementById('cin');
  if(ci)ci.addEventListener('keydown',e=>{{if(e.key==='Enter'&&!e.shiftKey){{e.preventDefault();sendMsg();}}}});
}});
</script>
{foot()}'''

# ─────────────────────────────────────────
# 13. notifications.html
# ─────────────────────────────────────────
pages['notifications.html'] = f'''{head("Notifications")}
<div style="display:flex;flex-direction:column;min-height:100vh;">
  <div class="tbar"><button class="tbk" onclick="history.back()">←</button><h2>Notifications</h2><button class="btn btn-g btn-sm" onclick="markAllRead()">Mark all read</button></div>
  <div class="pscr pb90" style="padding:12px 16px 0;" id="notif-list"><div class="empty"><div class="spin" style="margin:0 auto;"></div></div></div>
  <div class="bnav n4" id="notif-bnav"></div>
</div>
{shared_js()}
{fb_imports()}
onAuthStateChanged(auth,async u=>{{
  if(!u){{location.href='index.html';return;}}
  const s=await getDoc(doc(db,'users',u.uid));
  const cd=s.exists()?s.data():null;
  document.getElementById('loader').classList.add('out');
  const isMain=cd?.role==='main';
  document.getElementById('notif-bnav').innerHTML=`
    <div class="bni" onclick="location.href='${{isMain?'main.html':'home.html'}}'"><div class="ico">🏠</div><div class="lbl">Home</div></div>
    <div class="bni" onclick="location.href='${{isMain?'post.html':'find.html'}}'"><div class="ico">${{isMain?'➕':'🔍'}}</div><div class="lbl">${{isMain?'Post Work':'Find Work'}}</div></div>
    <div class="bni" onclick="location.href='${{isMain?'myworks.html':'apps.html'}}'"><div class="ico">📋</div><div class="lbl">${{isMain?'My Works':'My Bids'}}</div></div>
    <div class="bni" onclick="location.href='profile.html'"><div class="ico">👤</div><div class="lbl">Profile</div></div>`;
  const notifs=[
    {{ico:'🎉',bg:'var(--green4)',title:'Work Awarded!',sub:'Congratulations! Shapoorji Pallonji awarded you the External Painting work.',time:'2 hours ago',unread:true}},
    {{ico:'👁️',bg:'var(--blue4)',title:'Shortlisted',sub:'Kalpataru Constructions shortlisted your bid for Interior Plastering.',time:'5 hours ago',unread:true}},
    {{ico:'💬',bg:'var(--blue4)',title:'New Message',sub:'Godrej Properties: "Your quotation looks good, can we discuss?"',time:'Yesterday',unread:true}},
    {{ico:'📋',bg:'var(--s8)',title:'New Works Near You',sub:'6 new works posted near Pune today matching your trade.',time:'Yesterday',unread:false}},
    {{ico:'⭐',bg:'var(--yellow4)',title:'Rating Received',sub:'Tata Realty rated you 4.8 stars for the recent Masonry work.',time:'2 days ago',unread:false}},
    {{ico:'🔔',bg:'var(--s8)',title:'Bid Deadline',sub:'Your application for Marble Flooring – Mumbai closes in 2 days.',time:'3 days ago',unread:false}},
  ];
  document.getElementById('notif-list').innerHTML=notifs.map(n=>`<div class="notif-item ${{n.unread?'unread':''}}">
    <div class="ntico" style="background:${{n.bg}};">${{n.ico}}</div>
    <div style="flex:1;"><div style="font-size:13px;font-weight:600;margin-bottom:2px;">${{n.title}}</div><div style="font-size:12px;color:var(--s4);line-height:1.4;">${{n.sub}}</div><div style="font-size:10px;color:var(--s5);margin-top:4px;">${{n.time}}</div></div>
  </div>`).join('');
}});
function markAllRead(){{document.querySelectorAll('.notif-item.unread').forEach(el=>el.classList.remove('unread'));toast('All marked as read','ok');}}
</script>
{foot()}'''

# Write all files
for filename, content in pages.items():
    filepath = f'/home/claude/pragati-split/{filename}'
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"✅ {filename} ({len(content)} chars)")

print(f"\n✅ All {len(pages)} pages built!")
