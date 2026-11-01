"""Mixe la voix montée, la nappe musicale et les bruitages d'une vidéo.

Usage : python outils/mixer_son.py video1

Lit dans le dossier de la vidéo :
- voix_montee.wav : la voix validée (sortie de monter_audio.py)
- nappe.wav       : la nappe musicale (outils/sons.py nappe ...)
- sfx.json        : {"lead": 0.5, "events": [{"t": 12.3, "s": "clic"}, ...]}
                    écrit par `rendre_video.py <page> sfx` (temps absolus dans la vidéo)
Écrit mix.wav. La voix est décalée de `lead` secondes (le titre s'affiche avant qu'on parle),
la nappe baisse toute seule quand la voix parle (ducking).
"""
import json
import subprocess
import sys
import wave
from pathlib import Path

import numpy as np

SR = 48000
SONS = Path(__file__).parent / "sons"
# volume de chaque famille de bruitages (outils/sons.py), avant limiteur
GAIN = {"souffle": 0.4, "clic": 0.3, "pop": 0.32, "tic": 0.16, "trait": 0.24, "impact": 0.5, "carillon": 0.26}
NAPPE_DB = -30                          # niveau RMS de la nappe dans les silences
DUCK_DB = -10                           # baisse de la nappe pendant que la voix parle


def lire(chemin):
    with wave.open(str(chemin)) as w:
        assert w.getframerate() == SR and w.getnchannels() == 1, chemin
        return np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(float) / 32768


def lisse(x, monte, descend, dt):
    """Suivi d'enveloppe à attaque et relâche différentes (en secondes)."""
    y = np.empty_like(x)
    acc = x[0]
    for i, v in enumerate(x):
        tau = monte if v > acc else descend
        acc += (v - acc) * (1 - np.exp(-dt / tau))
        y[i] = acc
    return y


dossier = Path(sys.argv[1])
cfg = json.loads((dossier / "sfx.json").read_text(encoding="utf-8"))
lead = cfg["lead"]
voix = lire(dossier / "voix_montee.wav")
nappe = lire(dossier / "nappe.wav")
n = max(len(nappe), int(lead * SR) + len(voix))

piste_voix = np.zeros(n)
a = int(lead * SR)
piste_voix[a:a + len(voix)] = voix

# ducking calculé à 100 Hz puis interpolé
pas = SR // 100
rms = np.sqrt(np.convolve(piste_voix ** 2, np.ones(pas * 3) / (pas * 3), "same")[::pas])
parle = (20 * np.log10(rms + 1e-9) > -42).astype(float)
g = lisse(parle, 0.08, 0.7, 0.01)
gain_db = DUCK_DB * g
gain = 10 ** (np.interp(np.arange(n) / pas, np.arange(len(gain_db)), gain_db) / 20)

piste_nappe = np.zeros(n)
piste_nappe[: len(nappe)] = nappe
cible = 10 ** (NAPPE_DB / 20)
piste_nappe *= cible / (np.sqrt(np.mean(nappe[nappe != 0] ** 2)) + 1e-9) * gain

# chaque bruitage tire une variante de sa famille (jamais deux fois la même de suite)
# et un volume légèrement différent, pour que ça ne sonne pas en boucle
rng = np.random.default_rng(1)
variantes = {f: [lire(p) for p in sorted(SONS.glob(f"{f}_*.wav"))] for f in GAIN}
derniere = {}
piste_sfx = np.zeros(n)
for ev in cfg["events"]:
    choix = [k for k in range(len(variantes[ev["s"]])) if k != derniere.get(ev["s"])] or [0]
    k = int(rng.choice(choix))
    derniere[ev["s"]] = k
    s = variantes[ev["s"]][k] * GAIN[ev["s"]] * ev.get("g", 1) * rng.uniform(0.85, 1.1)
    d = int(ev["t"] * SR)
    if 0 <= d < n:
        piste_sfx[d:d + len(s)] += s[: n - d]

mix = piste_voix + piste_nappe + piste_sfx
tmp = dossier / "mix.brut.wav"
with wave.open(str(tmp), "wb") as w:
    w.setnchannels(1)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes((np.clip(mix * 0.8, -1, 1) * 32767).astype(np.int16).tobytes())
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(tmp),
                "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-ar", str(SR), str(dossier / "mix.wav")], check=True)
tmp.unlink()
print(f"OK : {dossier / 'mix.wav'} ({n / SR:.1f} s, {len(cfg['events'])} bruitages)")
