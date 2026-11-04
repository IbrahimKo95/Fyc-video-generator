"""Compte les mots lus de chaque script et vérifie que la vidéo tient dans ses bornes, quel que soit le débit.

Usage : python outils/compter_mots.py video*/script.md

Ne compte pas les titres (#), les lignes en italique (*...*) ni les lignes d'en-tête, qui ne se lisent pas.
Les blocs entre « *[+] Bloc optionnel* » et « *[fin du bloc]* » sont comptés à part.

Chaque script donne ses bornes dans une ligne « Bornes : 6:00 – 6:45 ».
- min = quelqu'un de rapide (230 mots/min) qui lit tout, blocs [+] compris : doit être >= borne min ;
- max = quelqu'un de posé (160 mots/min) qui ne lit que le texte principal : doit être <= borne max.
Règle de montage : on garde les blocs [+] un par un tant que la vidéo reste sous sa borne max.
Les attentes (installation, agent qui travaille) sont coupées ou accélérées au montage : aucune durée fixe n'est comptée.
Débits mesurés après montage : 230 mots/min pour Ibrahim (vidéo 1), 160 pour quelqu'un de posé.
"""
import re
import sys
from pathlib import Path

LENT, RAPIDE = 160, 230
DEBITS = (160, 200, 230)
TOTAL_MIN, TOTAL_MAX = 105, 120           # min : 1 h 45 à 2 h au total
ENTETES = ("Bornes", "Partie du plan", "Enregistrer tout", "Sources", "Les lignes en italique", "Version de référence")


def minutes(txt):
    m, s = txt.split(":")
    return int(m) + int(s) / 60


def mmss(x):
    s = round(x * 60)
    return f"{s // 60}:{s % 60:02d}"


def compter(chemin):
    noyau, blocs, bornes, dans_bloc = 0, [], None, False
    for ligne in Path(chemin).read_text(encoding="utf-8").splitlines():
        s = ligne.strip()
        if s.startswith("Bornes"):
            b = re.findall(r"\d+:\d\d", s)
            bornes = (minutes(b[0]), minutes(b[1]))
        if s.startswith("*[+]"):
            dans_bloc = True
            blocs.append(0)
            continue
        if s.startswith("*[fin du bloc]"):
            dans_bloc = False
            continue
        if not s or s.startswith(("#", "*")) or s.startswith(ENTETES):
            continue
        n = sum(1 for m in s.split() if any(c.isalnum() for c in m))
        if dans_bloc:
            blocs[-1] += n
        else:
            noyau += n
    return noyau, blocs, bornes


def duree_montee(noyau, blocs, debit, limite):
    """Durée après montage : on garde les blocs [+] un par un tant qu'on reste sous la borne max."""
    t = noyau / debit
    for b in blocs:
        if t + b / debit <= limite:
            t += b / debit
    return t


tot_min = tot_max = 0.0
total = {d: 0.0 for d in DEBITS}
print(f"{'script':20} {'noyau':>5} {'[+]':>4}  {'bornes':>11}  {'min':>5} {'max':>5}  "
      + "  ".join(f"{d}m/min" for d in DEBITS) + "  état")
for chemin in sys.argv[1:]:
    noyau, blocs, bornes = compter(chemin)
    option = sum(blocs)
    bmin, bmax = bornes or (5, 10)
    dmin = (noyau + option) / RAPIDE
    dmax = noyau / LENT
    tot_min += dmin
    tot_max += dmax
    durees = [duree_montee(noyau, blocs, d, bmax) for d in DEBITS]
    for d, x in zip(DEBITS, durees):
        total[d] += x
    pb = []
    if dmin < bmin:
        pb.append(f"min trop court (+{round((bmin - dmin) * RAPIDE)} mots en [+])")
    if dmax > bmax:
        pb.append(f"max trop long (-{round((dmax - bmax) * LENT)} mots du texte principal)")
    if bmin < 5 or bmax > 10:
        pb.append("bornes hors 5-10 min")
    print(f"{chemin:20} {noyau:5} {option:4}  {mmss(bmin):>5}-{mmss(bmax):<5}  {mmss(dmin):>5} {mmss(dmax):>5}  "
          + "  ".join(f"{mmss(x):>7}" for x in durees) + "  " + ("OK" if not pb else ", ".join(pb)))
etat = "OK" if tot_min >= TOTAL_MIN and tot_max <= TOTAL_MAX else "hors de 1 h 45 - 2 h"
print(f"{'TOTAL':20} {'':5} {'':4}  {'':11}  {mmss(tot_min):>5} {mmss(tot_max):>5}  "
      + "  ".join(f"{mmss(total[d]):>7}" for d in DEBITS) + "  " + etat)
