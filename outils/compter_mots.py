"""Compte les mots lus de chaque script et estime la durée de la vidéo selon le débit.

Usage : python outils/compter_mots.py video*/script.md

Ne compte pas les titres (#) ni les lignes en italique (*...*), qui ne se lisent pas.
Les blocs entre « *[+] Bloc optionnel* » et « *[fin du bloc]* » sont comptés à part ;
au montage, on les garde un par un tant que la vidéo reste sous LIMITE.
Débits mesurés après montage : 230 mots/min pour Ibrahim (vidéo 1), 160 pour quelqu'un de posé.
Démos : on ajoute un temps fixe, lu dans les lignes en italique : « Prévoir environ 30 secondes »
(commentaire improvisé de l'écran) et « Écran sans voix : environ 60 s » (installation, agent qui travaille).
"""
import re
import sys
from pathlib import Path

DEBITS = (160, 200, 230)
LIMITE = 9.5                     # min : au-delà, on retire les blocs [+] au montage


def compter(chemin):
    noyau = 0
    blocs = []                   # nombre de mots de chaque bloc [+]
    fixe = 0.0                   # secondes qui ne dépendent pas du débit
    dans_bloc = False
    for ligne in Path(chemin).read_text(encoding="utf-8").splitlines():
        s = ligne.strip()
        if s.startswith("*[+]"):
            dans_bloc = True
            blocs.append(0)
            continue
        if s.startswith("*[fin du bloc]"):
            dans_bloc = False
            continue
        if s.startswith("*"):
            fixe += sum(int(x) for x in re.findall(r"[Pp]révoir environ (\d+) secondes", s))
            fixe += sum(int(x) for x in re.findall(r"Écran sans voix : environ (\d+) s", s))
        if not s or s.startswith("#") or s.startswith("*") or s.startswith(("Durée visée", "Enregistrer tout", "Sources")):
            continue
        n = sum(1 for m in s.split() if any(c.isalnum() for c in m))
        if dans_bloc:
            blocs[-1] += n
        else:
            noyau += n
    return noyau, blocs, fixe / 60


def duree_montee(noyau, blocs, fixe, debit):
    """Durée après montage : on garde les blocs [+] un par un tant qu'on reste sous la limite."""
    t = noyau / debit + fixe
    for b in blocs:
        if t + b / debit <= LIMITE:
            t += b / debit
    return t


total = {d: 0.0 for d in DEBITS}
print(f"{'script':28} {'noyau':>6} {'[+]':>5} {'fixe':>5}  " + "  ".join(f"{d} m/min" for d in DEBITS))
for chemin in sys.argv[1:]:
    noyau, blocs, fixe = compter(chemin)
    option = sum(blocs)
    durees = [duree_montee(noyau, blocs, fixe, d) for d in DEBITS]
    for d, x in zip(DEBITS, durees):
        total[d] += x
    print(f"{chemin:28} {noyau:6} {option:5} {fixe:4.1f}m  " + "  ".join(f"{x:6.1f} min" for x in durees))
print(f"{'TOTAL':28} {'':6} {'':5} {'':5}  " + "  ".join(f"{total[d]:6.1f} min" for d in DEBITS))
