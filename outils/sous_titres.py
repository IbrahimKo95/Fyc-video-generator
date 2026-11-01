"""Fabrique les sous-titres .srt d'une vidéo à partir de la transcription du montage.

Usage : python outils/sous_titres.py audio/voix_montee_video1.transcript.json video1/corrections.json video1/final.srt [décalage]

- décalage : secondes ajoutées à tous les temps (la voix démarre 0,5 s après l'image).
- corrections.json : liste de [mal entendu, correct], appliquée au texte de chaque sous-titre
  (Whisper écrit « Cloud Code » pour « Claude Code », etc.). Relire le .srt après coup.
Règles : 2 lignes de 42 caractères au plus, 6 s au plus, coupe aux fins de phrase et aux pauses.
"""
import json
import sys
from pathlib import Path

MAX_CAR, MAX_DUREE, PAUSE = 84, 6.0, 0.5

data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
corr = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
dec = float(sys.argv[4]) if len(sys.argv) > 4 else 0.0
mots = [w for s in data for w in s["words"]]


def colle(ws):
    t = ""
    for w in ws:
        m = w["w"]
        # Whisper découpe « l'outil » en « l » + « 'outil » : on recolle sans espace
        t += m if (m.startswith("'") or m.startswith("-") or not t) else " " + m
    return t


# 1) groupes = phrases (ponctuation finale ou pause nette)
groupes, cur = [], []
for i, w in enumerate(mots):
    cur.append(w)
    suiv = mots[i + 1] if i + 1 < len(mots) else None
    if suiv is None or w["w"].endswith((".", "?", "!")) or suiv["s"] - w["e"] > PAUSE:
        if suiv is None or not suiv["w"].startswith(("'", "-")):
            groupes.append(cur)
            cur = []


def instant(ws, frac):
    """Temps correspondant à une position (0..1) dans le texte du groupe."""
    pos, total = [], len(colle(ws))
    for k in range(len(ws)):
        pos.append((len(colle(ws[:k + 1])) / total, ws[k]))
    for f, w in pos:
        if f >= frac - 1e-6:
            return w["e"]
    return ws[-1]["e"]


def morceaux(t, n):
    """Coupe t en n morceaux de longueur proche, de préférence après une virgule."""
    if n <= 1:
        return [t]
    cible = len(t) / n
    espaces = [i for i, c in enumerate(t) if c == " "]
    i = min(espaces, key=lambda k: abs(k - cible) - (12 if t[k - 1] in ",:" else 0))
    return [t[:i]] + morceaux(t[i + 1:], n - 1)


# 2) chaque groupe corrigé puis découpé si trop long
cues = []
for g in groupes:
    t = colle(g)
    for a, b in corr:
        t = t.replace(a, b)
    duree = g[-1]["e"] - g[0]["s"]
    n = max(1, -(-len(t) // MAX_CAR), int(-(-duree // MAX_DUREE)))
    parts, fait = morceaux(t, n), 0
    for k, part in enumerate(parts):
        d = g[0]["s"] if k == 0 else instant(g, fait / len(t))
        fait += len(part) + 1
        f = g[-1]["e"] if k == len(parts) - 1 else instant(g, fait / len(t))
        cues.append((d, f, part))


def deux_lignes(t):
    if len(t) <= 42:
        return t
    milieu = len(t) // 2
    # jamais juste après « ni juste avant » ? : ; de préférence après une virgule
    coupes = [i for i, c in enumerate(t) if c == " " and t[i - 1] != "«" and t[i + 1] not in "»?:;!"]
    i = min(coupes, key=lambda k: abs(k - milieu) - (8 if t[k - 1] == "," else 0))
    return t[:i] + "\n" + t[i + 1:]


def hms(x):
    ms = round(x * 1000)
    return f"{ms // 3600000:02}:{ms // 60000 % 60:02}:{ms // 1000 % 60:02},{ms % 1000:03}"


out = []
for k, (d, f, t) in enumerate(cues):
    d, f = d + dec, max(f, d + 1.0) + dec
    if k + 1 < len(cues):
        f = min(f + 0.3, cues[k + 1][0] + dec - 0.05)
    out.append(f"{k + 1}\n{hms(d)} --> {hms(f)}\n{deux_lignes(t)}\n")
Path(sys.argv[3]).write_text("\n".join(out), encoding="utf-8")
print(f"OK : {sys.argv[3]} ({len(cues)} sous-titres)")
