// API utilisée par outils/rendre_video.py : show/seek/lens pour l'image, sfx pour les bruitages.
const scenes = [...document.querySelectorAll('.scene')];
function lens() { return scenes.map(s => parseFloat(getComputedStyle(s).getPropertyValue('--len'))); }
// barre de progression de la vidéo entière, ajoutée en bas de chaque scène
(() => {
  const L = lens(), total = L.reduce((a, b) => a + b, 0);
  let t = 0;
  scenes.forEach((s, i) => {
    const p = document.createElement('div');
    p.className = 'progression';
    p.style.cssText = `--p0:${t / total};--p1:${(t + L[i]) / total}`;
    p.innerHTML = '<i></i>';
    s.appendChild(p);
    t += L[i];
  });
})();
function show(i) { scenes.forEach((s, k) => s.classList.toggle('on', k === i)); }
function seek(i, t) {
  scenes[i].getAnimations({ subtree: true }).forEach(a => { a.pause(); a.currentTime = t * 1000; });
  return new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
}
// éléments marqués data-sfx="clic" (ou pop, tic, trait, impact, carillon...) : le son part au même --d que l'animation
function sfx(i) {
  return [...scenes[i].querySelectorAll('[data-sfx]')].map(e => ({
    t: parseFloat(getComputedStyle(e).getPropertyValue('--d')) || 0, s: e.dataset.sfx }));
}
window.API = { show, seek, lens, sfx, n: scenes.length, lead: parseFloat(document.body.dataset.lead || 0) };
