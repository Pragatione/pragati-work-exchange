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
function go(page, params = {}) {
  const q = new URLSearchParams(params).toString();
  window.location.href = page + (q ? '?' + q : '');
}

function getParam(key) {
  return new URLSearchParams(window.location.search).get(key);
}

// ── LOCAL STORAGE HELPERS ──
function saveState(key, val) { try { localStorage.setItem('pg_' + key, JSON.stringify(val)); } catch(e) {} }
function getState(key) { try { return JSON.parse(localStorage.getItem('pg_' + key)); } catch(e) { return null; } }
function clearState(key) { localStorage.removeItem('pg_' + key); }

// ── FORMAT BUDGET ──
function fmtBudget(w) {
  const f = n => n >= 100000 ? '₹' + (n / 100000).toFixed(1).replace('.0', '') + 'L' : '₹' + n.toLocaleString('en-IN');
  return (w.minBudget && w.maxBudget) ? f(w.minBudget) + '–' + f(w.maxBudget) : w.minBudget ? f(w.minBudget) : 'TBD';
}

// ── INITIALS ──
function initials(name) { return (name || 'U').split(' ').map(x => x[0]).join('').toUpperCase().slice(0, 2); }

// ── TAG COLOR ──
function tagColor(u) { return u === 'Urgent' ? 't-or' : u === 'Critical' ? 't-re' : 't-gr'; }

// ── TOAST ──
function toast(msg, type = '') {
  let el = document.getElementById('toast');
  if (!el) { el = document.createElement('div'); el.id = 'toast'; document.body.appendChild(el); }
  el.textContent = msg;
  el.className = type ? 'on ' + type : 'on';
  setTimeout(() => { el.className = ''; }, 3200);
}

// ── EMPTY STATE ──
function emptyHTML(icon, title, sub) {
  return `<div class="empty"><div class="ei">${icon}</div><h3>${title}</h3><p>${sub}</p></div>`;
}

// ── WORK CARD HTML ──
function mkCard(w, onclick) {
  return `<div class="wcard" onclick="${onclick || `go('detail.html',{id:'${w.id}'})` }">
    <div class="wh"><div class="tags"><span class="tag t-bl">${w.trade || 'General'}</span><span class="tag ${tagColor(w.urgency)}">${w.urgency || 'Normal'}</span></div>
    <div class="wt">${w.title}</div><div class="wco">🏢 ${w.company || w.postedByName || 'Main Contractor'}</div></div>
    <div class="wb"><div class="wmeta"><span>📍 ${w.location || '—'}</span><span>⏱ ${w.startDate || 'TBD'}</span><span>👷 ${w.experience || '—'}</span></div></div>
    <div class="wf"><span class="wbud">${fmtBudget(w)}</span><span class="wbids">${w.bids || 0} bids</span></div>
  </div>`;
}

// ── DEMO WORKS ──
const DEMO_WORKS = [
  {id:'d1',title:'Interior Plastering Work – Phase 2',company:'Kalpataru Constructions',trade:'Plastering',location:'Hinjewadi, Pune',minBudget:250000,maxBudget:300000,duration:45,startDate:'2025-01-15',experience:'5 years',labour:'8–10 workers',urgency:'Urgent',scope:'Internal plastering for 120 flats (3 BHK)\nCement mortar ratio 1:4 throughout\nChicken mesh on all joints mandatory\nPOP punning over plaster for smooth finish\nMaterial supplied by Main Contractor',bids:8,postedBy:'m1',postedByName:'Kalpataru Constructions'},
  {id:'d2',title:'Marble Flooring – Block C Tower',company:'Godrej Properties',trade:'Flooring',location:'Andheri, Mumbai',minBudget:500000,maxBudget:700000,duration:60,startDate:'2025-01-22',experience:'3 years',labour:'12–15 workers',urgency:'Normal',scope:'Italian marble flooring for 80 apartments\nGrouting with white cement only\nPolishing and final sealing included\nQuality inspection after each floor',bids:14,postedBy:'m2',postedByName:'Godrej Properties'},
  {id:'d3',title:'Full Electrical Wiring – Tower 2',company:'Lodha Group',trade:'Electrical',location:'Thane, Mumbai',minBudget:800000,maxBudget:1000000,duration:90,startDate:'2025-01-30',experience:'7 years',labour:'15–20 workers',urgency:'Normal',scope:'Complete electrical wiring for 200 residential units\nISI certified conduit wiring throughout\nDB boards and MCB fitting included\nFull testing and commissioning at end',bids:6,postedBy:'m3',postedByName:'Lodha Group'},
  {id:'d4',title:'External Painting – Phase 2',company:'Shapoorji Pallonji',trade:'Painting',location:'Nagpur, MH',minBudget:400000,maxBudget:600000,duration:30,startDate:'2025-02-05',experience:'2 years',labour:'10–12 workers',urgency:'Normal',scope:'External texture painting for 4 residential towers\nAsian Paints Apex Weather Proof two coats\nScaffolding and safety equipment by contractor\nFinal inspection before payment',bids:3,postedBy:'m4',postedByName:'Shapoorji Pallonji'},
  {id:'d5',title:'Sanitary & Plumbing – Phase 3',company:'Prestige Group',trade:'Plumbing',location:'Koramangala, Bangalore',minBudget:350000,maxBudget:500000,duration:45,startDate:'2025-02-10',experience:'4 years',labour:'6–8 workers',urgency:'Urgent',scope:'Complete sanitary and plumbing for 60 units\nCP fittings by Jaquar brand only\nHDPE piping for all drainage\nWater pressure testing on completion',bids:5,postedBy:'m5',postedByName:'Prestige Group'},
  {id:'d6',title:'Masonry & Brickwork – Block D',company:'Tata Realty',trade:'Masonry',location:'Wakad, Pune',minBudget:600000,maxBudget:800000,duration:70,startDate:'2025-02-20',experience:'6 years',labour:'20–25 workers',urgency:'Normal',scope:'Brick masonry for Block D all floors\nM20 grade concrete for columns and beams\nSand-faced plaster on all external walls\nQuality inspections at DPC and lintel levels',bids:4,postedBy:'m6',postedByName:'Tata Realty'},
  {id:'d7',title:'False Ceiling – Club House',company:'Brigade Group',trade:'Carpentry',location:'Whitefield, Bangalore',minBudget:180000,maxBudget:250000,duration:25,startDate:'2025-02-28',experience:'3 years',labour:'4–6 workers',urgency:'Urgent',scope:'Gypsum false ceiling for 5000 sqft club house\nCove lighting provision in all areas\nElectrical conduits embedded before boarding\nSmooth finish with two coats of putty',bids:7,postedBy:'m7',postedByName:'Brigade Group'},
  {id:'d8',title:'Waterproofing – Terrace & Bathrooms',company:'Puravankara Ltd',trade:'Waterproofing',location:'Koregaon Park, Pune',minBudget:120000,maxBudget:180000,duration:20,startDate:'2025-03-05',experience:'4 years',labour:'3–5 workers',urgency:'Normal',scope:'Terrace waterproofing using torch applied membrane\nBathroom waterproofing with polymer-modified mortar\nAll work with 10-year warranty certificate\nPonding test before handover',bids:2,postedBy:'m8',postedByName:'Puravankara Ltd'},
];
