"""Fabrique les sons des vidéos (tout est synthétisé ici : pas de droits à gérer).

Usage :
  python outils/sons.py bruitages                  -> outils/sons/<famille>_<n>.wav
  python outils/sons.py nappe video1/nappe.wav 285 -> nappe musicale de 285 s

Familles de bruitages (plusieurs variantes chacune, le mixage en tire une au hasard) :
  souffle  changement de scène          clic     apparition d'une date, d'un point
  pop      apparition d'une carte       tic      mot, token, barre (très court)
  trait    trait qui se dessine, rature impact   grand titre
  carillon idée importante
"""
import sys
import wave
from pathlib import Path

import numpy as np

SR = 48000
rng = np.random.default_rng(7)
hz = lambda m: 440 * 2 ** ((m - 69) / 12)


def ecrire(chemin, x):
    x = np.clip(x, -1, 1)
    Path(chemin).parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(chemin), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((x * 32767).astype(np.int16).tobytes())


def passe_bas(x, fc):
    """Filtre passe-bas d'ordre 1, fréquence de coupure fixe ou variable (tableau)."""
    fc = np.broadcast_to(np.asarray(fc, dtype=float), x.shape)
    a = 1 - np.exp(-2 * np.pi * fc / SR)
    y = np.empty_like(x)
    acc = 0.0
    for i in range(len(x)):
        acc += a[i] * (x[i] - acc)
        y[i] = acc
    return y


def doux(x, fc, ordre=3):
    """Passe-bas en cascade : coupe vraiment les aigus (un seul étage laisse passer trop de souffle)."""
    for _ in range(ordre):
        x = passe_bas(x, fc)
    return x


def passe_haut(x, fc):
    return x - passe_bas(x, fc)


def reverb(x, duree=0.35, niveau=0.25):
    """Petite queue de réverbération : convolution avec un bruit qui décroît."""
    n = int(duree * SR)
    ir = rng.standard_normal(n) * np.exp(-np.arange(n) / (n / 5))
    ir = doux(ir, 2500, 2)
    y = np.convolve(x, ir) / np.abs(ir).sum() * 8
    out = np.zeros(len(y))
    out[: len(x)] += x
    return out + niveau * y


def norm(x, crete=0.5):
    return crete * x / (np.abs(x).max() + 1e-9)


def t_(d):
    return np.arange(int(d * SR)) / SR


# ---------- bruitages ----------
def souffle(d, f0, f1, sens):
    """Bruit filtré dont la brillance suit une courbe (sens : 'monte', 'descend', 'arche')."""
    t = np.linspace(0, 1, int(d * SR))
    forme = {"monte": t ** 1.5 * (1 - t) ** 0.3, "descend": (1 - t) ** 1.5 * t ** 0.3, "arche": np.sin(np.pi * t) ** 2}[sens]
    forme /= forme.max()
    fc = f0 + (f1 - f0) * forme
    x = doux(rng.standard_normal(len(t)), fc, 4)
    x = passe_haut(x, 150) * forme
    return norm(reverb(x, 0.4, 0.2))


def clic(f, decai):
    t = t_(0.12)
    corps = np.sin(2 * np.pi * f * t) * np.exp(-t / decai) + 0.15 * np.sin(2 * np.pi * f * 2.01 * t) * np.exp(-t / (decai / 2))
    attaque = doux(rng.standard_normal(len(t)), 2000) * np.exp(-t / 0.0018)
    return norm(reverb(corps + 0.5 * attaque, 0.25, 0.15))


def pop(f0, f1):
    t = t_(0.16)
    f = f0 + (f1 - f0) * (1 - np.exp(-t / 0.02))
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.035) * np.minimum(1, t / 0.003)
    return norm(reverb(x, 0.3, 0.2))


def tic(f):
    t = t_(0.04)
    x = np.sin(2 * np.pi * f * t) * np.exp(-t / 0.01) + 0.15 * doux(rng.standard_normal(len(t)), 1800) * np.exp(-t / 0.002)
    return norm(x)


def trait(d, f0, f1):
    t = np.linspace(0, 1, int(d * SR))
    fc = f0 + (f1 - f0) * t
    x = passe_haut(doux(rng.standard_normal(len(t)), fc, 4), 300)
    x *= np.minimum(1, t / 0.15) * (1 - t) ** 1.2
    return norm(x)


def impact(f):
    t = t_(1.6)
    chute = f * (1 + 1.5 * np.exp(-t / 0.05))
    grave = np.sin(2 * np.pi * np.cumsum(chute) / SR) * np.exp(-t / 0.35)
    souffle_ = doux(rng.standard_normal(len(t)), 700) * np.exp(-t / 0.08)
    return norm(reverb(grave + 0.4 * souffle_, 0.9, 0.35))


def carillon(m):
    t = t_(2.2)
    f = hz(m)
    x = sum(a * np.sin(2 * np.pi * f * r * t) * np.exp(-t / dec)
            for r, a, dec in ((1, 1, 1.0), (2.0, 0.35, 0.6), (2.76, 0.12, 0.3)))
    x *= np.minimum(1, t / 0.004)
    return norm(reverb(x, 0.8, 0.3))


def bruitages(ici):
    sons = {
        "souffle": [souffle(0.9, 300, 2900, "arche"), souffle(0.75, 250, 2800, "monte"), souffle(1.0, 400, 2400, "descend"), souffle(0.7, 400, 2600, "arche")],
        "clic": [clic(hz(m), dec) for m, dec in ((69, .03), (72, .026), (67, .032), (64, .034), (71, .028))],
        "pop": [pop(240, 560), pop(280, 640), pop(200, 480), pop(320, 700)],
        "tic": [tic(f) for f in (880, 990, 1050, 830, 940)],
        "trait": [trait(0.28, 800, 3000), trait(0.35, 600, 2600), trait(0.25, 900, 3200)],
        "impact": [impact(52), impact(46)],
        "carillon": [carillon(m) for m in (69, 64, 72)],
    }
    for famille, variantes in sons.items():
        for i, x in enumerate(variantes, 1):
            ecrire(ici / f"{famille}_{i}.wav", x)
    print("OK :", ", ".join(f"{k} x{len(v)}" for k, v in sons.items()))


# ---------- nappe ----------
def note(f, d, attaque, relache, brillance=1.6):
    t = t_(d)
    env = np.minimum(1, t / attaque) * np.minimum(1, (d - t) / relache).clip(0)
    x = sum(np.sin(2 * np.pi * f * k * t) / k ** brillance for k in (1, 2, 3))
    x += sum(np.sin(2 * np.pi * f * (1 + e) * t) for e in (-0.003, 0.003)) * 0.5
    return x * env


def nappe(duree):
    """Deux suites d'accords en la mineur qui alternent, une basse douce, des arpèges jamais identiques."""
    suites = [[(57, 60, 64), (53, 57, 60), (48, 55, 60), (55, 59, 62)],     # Am F C G
              [(53, 57, 60), (55, 59, 62), (52, 55, 59), (57, 60, 64)]]     # F G Em Am
    mesure, croche = 8.0, 0.5                    # ~60 bpm, un accord toutes les 8 s
    n = int((duree + 4) * SR)
    x = np.zeros(n)

    def ajoute(s, a):
        b = int(a * SR)
        if b < n:
            x[b:b + len(s)] += s[: n - b]

    k = 0
    while k * mesure < duree + 2:
        a0 = k * mesure
        accord = suites[(k // 4) % 2][k % 4]
        for m in accord:                                      # nappe
            ajoute(note(hz(m), mesure + 3, 2.5, 3) * 0.13, a0)
        basse = hz(accord[0] - 12)
        for b in (0, 4):                                      # basse sur les temps 1 et 3
            ajoute(note(basse, 3.5, 0.02, 3.0, 2.5) * 0.16, a0 + b)
        # densité qui varie lentement : quelques notes au début, plus au milieu
        densite = 0.35 + 0.35 * np.sin(np.pi * min(1, a0 / max(duree, 1)))
        tons = [m + 12 for m in accord] + [accord[0] + 24]
        prec = None
        for j in range(int(mesure / croche)):
            if rng.random() < densite:
                m = rng.choice([u for u in tons if u != prec])
                prec = m
                vel = 0.035 + 0.02 * rng.random()
                ajoute(note(hz(m), 1.6, 0.008, 1.5, 2.2) * vel, a0 + j * croche + rng.normal(0, 0.008))
        k += 1
    x = passe_bas(x, 2400)
    x = x[: int(duree * SR)]
    t = np.arange(len(x)) / SR
    x *= np.minimum(1, t / 3) * np.minimum(1, (duree - t) / 4).clip(0)
    return norm(x)


if __name__ == "__main__":
    ici = Path(__file__).parent / "sons"
    if sys.argv[1] == "bruitages":
        for f in ici.glob("*.wav"):
            f.unlink()
        bruitages(ici)
    elif sys.argv[1] == "nappe":
        ecrire(sys.argv[2], nappe(float(sys.argv[3])))
        print("OK :", sys.argv[2])
