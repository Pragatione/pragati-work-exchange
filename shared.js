// ── PRAGATI SHARED CONFIG ──
const FB_CFG = {
  apiKey: "AIzaSyBT465A_V0oe-8wkeWk8hee7NXUBSLZcyA",
  authDomain: "pragati-work-exchange.firebaseapp.com",
  projectId: "pragati-work-exchange",
  storageBucket: "pragati-work-exchange.firebasestorage.app",
  messagingSenderId: "422215240765",
  appId: "1:422215240765:web:eefb239420262c9d822e54"
};

// ── NAVIGATION ──
function go(page, params) {
  params = params || {};
  var q = new URLSearchParams(params).toString();
  window.location.href = page + (q ? '?' + q : '');
}

function getParam(key) {
  return new URLSearchParams(window.location.search).get(key);
}

// ── LOCAL STORAGE HELPERS ──
function saveLS(k, v) { try { localStorage.setItem('pg_' + k, JSON.stringify(v)); } catch(e) {} }
function getLS(k) { try { return JSON.parse(localStorage.getItem('pg_' + k)); } catch(e) { return null; } }
function clearLS(k) { localStorage.removeItem('pg_' + k); }

// Aliases used by older pages
var saveState = saveLS;
var getState = getLS;
var clearState = clearLS;

// ── FORMAT HELPERS ──
function fmtBudget(w) {
  var f = function(n) { return n >= 100000 ? '₹' + (n/100000).toFixed(1).replace('.0','') + 'L' : '₹' + n.toLocaleString('en-IN'); };
  return (w.minBudget && w.maxBudget) ? f(w.minBudget) + '–' + f(w.maxBudget) : w.minBudget ? f(w.minBudget) : 'TBD';
}
var fmtBud = fmtBudget;

function esc(s) { return String(s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
function initials(name) { return (name||'U').split(' ').map(function(x){return x[0];}).join('').toUpperCase().slice(0,2); }
function tagClr(u) { return u==='Urgent'?'t-or':u==='Critical'?'t-re':'t-gr'; }
var tagColor = tagClr;

// ── TOAST ──
function toast(msg, type) {
  type = type || '';
  var el = document.getElementById('toast');
  if (!el) { el = document.createElement('div'); el.id = 'toast'; document.body.appendChild(el); }
  el.textContent = msg;
  el.className = type ? 'on ' + type : 'on';
  clearTimeout(el._t);
  el._t = setTimeout(function() { el.className = ''; }, 3200);
}

// ── EMPTY STATE ──
function emptyHTML(icon, title, sub) {
  return '<div class="empty"><div class="ei">'+icon+'</div><h3>'+title+'</h3><p>'+sub+'</p></div>';
}

// ── WORK CARD HTML ──
function mkCard(w) {
  var onclick = "location.href='detail.html?id=" + esc(w.id) + "'";
  return '<div class="wcard" onclick="'+onclick+'">' +
    '<div class="wh"><div class="tags"><span class="tag t-bl">'+esc(w.trade||'General')+'</span>' +
    '<span class="tag '+tagClr(w.urgency)+'">'+esc(w.urgency||'Normal')+'</span></div>' +
    '<div class="wt">'+esc(w.title||'')+'</div>' +
    '<div class="wco">🏢 '+esc(w.company||w.postedByName||'Main Contractor')+'</div></div>' +
    '<div class="wb"><div class="wmeta"><span>📍 '+esc(w.location||'—')+'</span>' +
    '<span>⏱ '+esc(w.startDate||'TBD')+'</span>' +
    '<span>👷 '+esc(w.experience||'—')+'</span></div></div>' +
    '<div class="wf"><span class="wbud">'+fmtBudget(w)+'</span>' +
    '<span class="wbids">'+(w.bids||0)+' bids</span></div></div>';
}

// ── NOTIFICATION HELPERS ──
async function createNotification(db, FS, toUid, type, title, body, linkUrl) {
  try {
    await db.collection('notifications').add({
      toUid: toUid,
      type: type,           // 'awarded','shortlisted','rejected','hire_request','new_bid'
      title: title,
      body: body,
      link: linkUrl || '',
      read: false,
      createdAt: FS.FieldValue.serverTimestamp()
    });
  } catch(e) { /* silent */ }
}

async function getUnreadNotifCount(db, uid, callback) {
  try {
    var snap = await db.collection('notifications')
      .where('toUid','==',uid)
      .where('read','==',false)
      .get();
    callback(snap.size);
  } catch(e) { callback(0); }
}

// ── BOTTOM NAV BUILDER ──
function buildBnav(isMain, activeKey) {
  var petty = [
    {h:'home.html',    i:icoHome,    l:'Home',      k:'home'},
    {h:'find.html',    i:icoSearch,  l:'Find Work', k:'find'},
    {h:'apps.html',    i:icoApps,    l:'My Bids',   k:'apps'},
    {h:'chat.html',    i:icoChat,    l:'Messages',  k:'chat'},
  ];
  var main = [
    {h:'main.html',    i:icoHome,    l:'Home',      k:'home'},
    {h:'post.html',    i:icoPlus,    l:'Post Work', k:'post'},
    {h:'myworks.html', i:icoBrief,   l:'My Works',  k:'myworks'},
    {h:'chat.html',    i:icoChat,    l:'Messages',  k:'chat'},
  ];
  var items = isMain ? main : petty;
  var html = '<nav class="bnav">';
  items.forEach(function(it) {
    var on = it.k === activeKey ? ' on' : '';
    html += '<div class="bni'+on+'" onclick="location.href=\''+it.h+'\'"><div class="ico">'+it.i+'</div><div class="lbl">'+it.l+'</div></div>';
  });
  html += '</nav>';
  return html;
}
// Keep legacy aliases
var buildBnavHTML = buildBnav;
var buildDynBnav = buildBnav;

// ── ICON STRINGS ──
var icoHome = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>';
var icoSearch = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>';
var icoApps = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="8" height="4" x="8" y="2" rx="1" ry="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><path d="M12 11h4"/><path d="M12 16h4"/><path d="M8 11h.01"/><path d="M8 16h.01"/></svg>';
var icoChat = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/><path d="M8 10h.01"/><path d="M12 10h.01"/><path d="M16 10h.01"/></svg>';
var icoPlus = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 8v8"/><path d="M8 12h8"/></svg>';
var icoBrief = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="14" x="2" y="7" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>';

// ── DEMO CONTRACTORS ──
var DEMO_CONTRACTORS = [
  {uid:'demo_mk',name:'Mohan Kumar',trade:'Plastering',city:'Hinjewadi, Pune',expYears:15,labour:'9–12',rating:4.8,reviews:23,projects:42,dailyRate:6500,available:true,verified:true,hireDirect:true,
   bio:'Specialist in interior and exterior plastering for large residential projects. Worked with Lodha, Kalpataru and Godrej over 15 years. Full team safety-certified. ISO quality standards. 1-year workmanship warranty on all projects.',
   skills:['Cement Plastering','POP Punning','Gypsum Plaster','Chicken Mesh Work','Texture Finish','Damp Proofing'],
   experience:[{company:'Lodha Group, Thane',role:'Plastering Contractor',duration:'2021–2024'},{company:'Kalpataru Constructions, Pune',role:'Senior Plastering Supervisor',duration:'2017–2021'}],
   certifications:['Safety Training Certificate 2023','POP Certified Applicator','ISO 9001 Compliance Training'],
   reviewsList:[{reviewer:'Kalpataru Constructions',rating:5,text:'Exceptional quality and on-time delivery for all 120 flats. Highly recommended.'},{reviewer:'Lodha Group',rating:5,text:'Very professional team. Maintained quality throughout the 90-day project.'}]},
  {uid:'demo_rp',name:'Rajesh Patil',trade:'Flooring',city:'Andheri, Mumbai',expYears:11,labour:'12–15',rating:4.7,reviews:18,projects:31,dailyRate:8000,available:true,verified:true,hireDirect:true,
   bio:'Expert in high-end Italian marble, vitrified tile and granite flooring. 11 years serving premium residential builders in Mumbai. Full polishing and grouting team included. References from Godrej and Prestige Group available.',
   skills:['Italian Marble','Vitrified Tiles','Granite Flooring','Epoxy Flooring','Carpet Flooring','Stone Polishing'],
   experience:[{company:'Godrej Properties, Andheri',role:'Flooring Contractor',duration:'2020–2024'},{company:'Prestige Group, Koramangala',role:'Marble & Tile Specialist',duration:'2016–2020'}],
   certifications:['Kajaria Certified Applicator','Stone Polishing Expert Certificate'],
   reviewsList:[{reviewer:'Godrej Properties',rating:5,text:'Pristine marble finish. Work completed ahead of schedule.'},{reviewer:'Prestige Group',rating:4,text:'Good team, quality was consistent across all 80 apartments.'}]},
  {uid:'demo_vs',name:'Vijay Shinde',trade:'Electrical',city:'Thane, Mumbai',expYears:13,labour:'15–20',rating:4.6,reviews:14,projects:28,dailyRate:9000,available:false,verified:true,hireDirect:true,
   bio:'Complete electrical solutions for residential and commercial projects. Expert in conduit wiring, DB boards, MCB fitting and commissioning. All work ISI certified. 13+ years with top-tier builders across MMR.',
   skills:['Wiring & Conduit','DB Board Fitting','MCB Installation','Earthing','CCTV Installation','Solar Panels'],
   experience:[{company:'Lodha Group, Thane',role:'Electrical Contractor – Tower 2 & 3',duration:'2022–2024'},{company:'Rustomjee, Mumbai',role:'Electrical Supervisor',duration:'2018–2022'}],
   certifications:['Licensed Electrical Contractor (Govt. of Maharashtra)','Fire Safety Compliance 2023'],
   reviewsList:[{reviewer:'Lodha Group',rating:5,text:'Completed 200 units in 90 days. Testing and commissioning was impeccable.'},{reviewer:'Rustomjee Developers',rating:4,text:'Reliable team, good safety practices.'}]},
  {uid:'demo_sd',name:'Suresh Deshpande',trade:'Painting',city:'Nagpur, MH',expYears:8,labour:'10–12',rating:4.5,reviews:11,projects:19,dailyRate:5500,available:true,hireDirect:true,
   bio:'Interior and exterior painting specialist. Expert in Asian Paints, Nerolac and Dulux application. Full scaffolding team. Safety-equipped for high-rise work. 8 years with Shapoorji and Tata Realty.',
   skills:['Interior Painting','Exterior Painting','Texture Painting','PU Coating','Waterproof Coating','Anti-Rust Painting'],
   experience:[{company:'Shapoorji Pallonji, Nagpur',role:'Painting Contractor',duration:'2021–2024'},{company:'Tata Realty, Pune',role:'Exterior Paint Supervisor',duration:'2018–2021'}],
   certifications:['Asian Paints Authorized Applicator','Safety at Height Certificate'],
   reviewsList:[{reviewer:'Shapoorji Pallonji',rating:5,text:'Excellent finish. Full 4 towers completed in 30 days as promised.'}]},
  {uid:'demo_ap',name:'Arvind Pawar',trade:'Plumbing',city:'Koramangala, Bangalore',expYears:9,labour:'6–8',rating:4.7,reviews:16,projects:22,dailyRate:7000,available:true,verified:true,hireDirect:true,
   bio:'Complete sanitary and plumbing solutions. Certified Jaquar applicator with 9 years experience in premium residential projects. HDPE, CPVC and Pex piping specialist. Pressure testing and commissioning included.',
   skills:['HDPE Piping','Sanitary Fitting','Water Heater','Jaquar CP Fittings','Sewage System','Pressure Testing'],
   experience:[{company:'Prestige Group, Bangalore',role:'Plumbing Contractor',duration:'2021–2024'},{company:'Brigade Group, Whitefield',role:'Sanitary Supervisor',duration:'2019–2021'}],
   certifications:['Jaquar Certified Plumber','ISI Mark Quality Compliance'],
   reviewsList:[{reviewer:'Prestige Group',rating:5,text:'Flawless plumbing for 60 units. No leakage issues post-handover.'},{reviewer:'Brigade Group',rating:4,text:'Professional and punctual. Highly recommend for luxury projects.'}]},
  {uid:'demo_rm',name:'Ramesh More',trade:'Masonry',city:'Wakad, Pune',expYears:18,labour:'20–25',rating:4.4,reviews:9,projects:35,dailyRate:7500,available:true,hireDirect:true,
   bio:'Brick masonry, RCC work, shuttering and centering for large-scale residential and commercial projects. 18 years across Pune and Mumbai. Large labour force with safety training.',
   skills:['Brickwork','RCC Work','Shuttering','Centering','Block Work','Sand-faced Plaster'],
   experience:[{company:'Tata Realty, Wakad',role:'Masonry Contractor',duration:'2022–2024'},{company:'Kolte-Patil Developers',role:'Civil Contractor',duration:'2018–2022'}],
   certifications:['Safety Supervisor Certificate','Civil Work Quality Standard 2022'],
   reviewsList:[{reviewer:'Tata Realty',rating:4,text:'Dependable team. Block D completed within timeline and budget.'}]},
  {uid:'demo_pk',name:'Pravin Kulkarni',trade:'Waterproofing',city:'Koregaon Park, Pune',expYears:12,labour:'3–6',rating:4.9,reviews:20,projects:48,dailyRate:8500,available:true,verified:true,hireDirect:true,
   bio:'Waterproofing specialist with 12 years expertise in terrace, bathroom, basement and podium waterproofing. Torch-applied membrane, crystalline coatings, APP membrane. All work includes 10-year written warranty.',
   skills:['Terrace Waterproofing','Bathroom Waterproofing','Crystalline Coating','APP Membrane','Epoxy Injection','Damp Proofing'],
   experience:[{company:'Puravankara Ltd, Pune',role:'Waterproofing Contractor',duration:'2020–2024'},{company:'Piramal Realty, Mumbai',role:'Waterproofing Supervisor',duration:'2016–2020'}],
   certifications:['BASF Certified Waterproofing Applicator','Dr. Fixit Authorized Contractor'],
   reviewsList:[{reviewer:'Puravankara',rating:5,text:'Best waterproofing contractor we\'ve worked with. Zero complaints in 3 years.'},{reviewer:'Piramal Realty',rating:5,text:'Ponding tests passed on first attempt for all terraces.'}]},
  {uid:'demo_nj',name:'Nitin Jadhav',trade:'Carpentry',city:'Whitefield, Bangalore',expYears:10,labour:'4–6',rating:4.6,reviews:13,projects:26,dailyRate:6000,available:false,hireDirect:true,
   bio:'False ceiling, modular furniture, doors & windows, wooden partitions and wood polish. Expert in gypsum, PVC and GI grid systems. Interior finishing specialist for luxury residential and hospitality projects.',
   skills:['False Ceiling','Modular Furniture','Doors & Windows','Partition','Wood Polish','Cove Lighting'],
   experience:[{company:'Brigade Group, Whitefield',role:'Carpentry & Interior Contractor',duration:'2021–2024'},{company:'ITC Hotels, Bangalore',role:'Woodwork Supervisor',duration:'2018–2021'}],
   certifications:['Interior Design Execution Certificate','Fire Retardant Material Compliance'],
   reviewsList:[{reviewer:'Brigade Group',rating:5,text:'Stunning false ceiling work for 5000 sqft club house. Delivered 5 days early.'}]},
];

// ── DEMO WORKS ──
var DEMO_WORKS = [
  {id:'d1',title:'Interior Plastering Work – Phase 2',company:'Kalpataru Constructions',trade:'Plastering',location:'Hinjewadi, Pune',minBudget:250000,maxBudget:300000,duration:45,startDate:'2025-06-15',experience:'5 years',labour:'8–10 workers',urgency:'Urgent',scope:'Internal plastering for 120 flats (3 BHK)\nCement mortar ratio 1:4 throughout\nChicken mesh on all joints mandatory\nPOP punning over plaster for smooth finish\nMaterial supplied by Main Contractor',bids:8,postedBy:'m1',postedByName:'Kalpataru Constructions'},
  {id:'d2',title:'Marble Flooring – Block C Tower',company:'Godrej Properties',trade:'Flooring',location:'Andheri, Mumbai',minBudget:500000,maxBudget:700000,duration:60,startDate:'2025-06-22',experience:'3 years',labour:'12–15 workers',urgency:'Normal',scope:'Italian marble flooring for 80 apartments\nGrouting with white cement only\nPolishing and final sealing included\nQuality inspection after each floor',bids:14,postedBy:'m2',postedByName:'Godrej Properties'},
  {id:'d3',title:'Full Electrical Wiring – Tower 2',company:'Lodha Group',trade:'Electrical',location:'Thane, Mumbai',minBudget:800000,maxBudget:1000000,duration:90,startDate:'2025-07-01',experience:'7 years',labour:'15–20 workers',urgency:'Normal',scope:'Complete electrical wiring for 200 residential units\nISI certified conduit wiring throughout\nDB boards and MCB fitting included\nFull testing and commissioning at end',bids:6,postedBy:'m3',postedByName:'Lodha Group'},
  {id:'d4',title:'External Painting – Phase 2',company:'Shapoorji Pallonji',trade:'Painting',location:'Nagpur, MH',minBudget:400000,maxBudget:600000,duration:30,startDate:'2025-07-05',experience:'2 years',labour:'10–12 workers',urgency:'Normal',scope:'External texture painting for 4 residential towers\nAsian Paints Apex Weather Proof two coats\nScaffolding and safety equipment by contractor\nFinal inspection before payment',bids:3,postedBy:'m4',postedByName:'Shapoorji Pallonji'},
  {id:'d5',title:'Sanitary & Plumbing – Phase 3',company:'Prestige Group',trade:'Plumbing',location:'Koramangala, Bangalore',minBudget:350000,maxBudget:500000,duration:45,startDate:'2025-07-10',experience:'4 years',labour:'6–8 workers',urgency:'Urgent',scope:'Complete sanitary and plumbing for 60 units\nCP fittings by Jaquar brand only\nHDPE piping for all drainage\nWater pressure testing on completion',bids:5,postedBy:'m5',postedByName:'Prestige Group'},
  {id:'d6',title:'Masonry & Brickwork – Block D',company:'Tata Realty',trade:'Masonry',location:'Wakad, Pune',minBudget:600000,maxBudget:800000,duration:70,startDate:'2025-07-20',experience:'6 years',labour:'20–25 workers',urgency:'Normal',scope:'Brick masonry for Block D all floors\nM20 grade concrete for columns and beams\nSand-faced plaster on all external walls\nQuality inspections at DPC and lintel levels',bids:4,postedBy:'m6',postedByName:'Tata Realty'},
  {id:'d7',title:'False Ceiling – Club House',company:'Brigade Group',trade:'Carpentry',location:'Whitefield, Bangalore',minBudget:180000,maxBudget:250000,duration:25,startDate:'2025-07-28',experience:'3 years',labour:'4–6 workers',urgency:'Urgent',scope:'Gypsum false ceiling for 5000 sqft club house\nCove lighting provision in all areas\nElectrical conduits embedded before boarding\nSmooth finish with two coats of putty',bids:7,postedBy:'m7',postedByName:'Brigade Group'},
  {id:'d8',title:'Waterproofing – Terrace & Bathrooms',company:'Puravankara Ltd',trade:'Waterproofing',location:'Koregaon Park, Pune',minBudget:120000,maxBudget:180000,duration:20,startDate:'2025-08-05',experience:'4 years',labour:'3–5 workers',urgency:'Normal',scope:'Terrace waterproofing using torch applied membrane\nBathroom waterproofing with polymer-modified mortar\nAll work with 10-year warranty certificate\nPonding test before handover',bids:2,postedBy:'m8',postedByName:'Puravankara Ltd'},
];
