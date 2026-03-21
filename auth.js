// auth.js — include on every app page (not landing/login/register)
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-app.js";
import { getAuth, onAuthStateChanged } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-auth.js";
import { getFirestore, doc, getDoc } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";

const fbApp = initializeApp(FB_CFG);
export const auth = getAuth(fbApp);
export const db = getFirestore(fbApp);

export let CU = null;
export let CD = null;

export function requireAuth(role) {
  return new Promise((resolve) => {
    onAuthStateChanged(auth, async (user) => {
      if (!user) { window.location.href = 'index.html'; return; }
      CU = user;
      try {
        const snap = await getDoc(doc(db, 'users', user.uid));
        if (snap.exists()) CD = snap.data();
      } catch (e) {}
      if (!CD) { window.location.href = 'index.html'; return; }
      // Role check
      if (role && CD.role !== role) {
        window.location.href = CD.role === 'main' ? 'main.html' : 'home.html';
        return;
      }
      document.getElementById('loader')?.classList.add('out');
      resolve({ user: CU, data: CD });
    });
  });
}
