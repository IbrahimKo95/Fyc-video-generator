"""Transcrit un enregistrement avec l'horodatage de chaque mot.

Usage : python outils/transcrire.py audio/voix_video1.wav [modele]
Sortie : audio/<nom>.transcript.json  et  audio/<nom>.transcript.txt
Modèle par défaut : medium (plus précis que small, plus lent).
"""
import json
import sys
from pathlib import Path

from faster_whisper import WhisperModel

audio = Path(sys.argv[1])
modele = sys.argv[2] if len(sys.argv) > 2 else "medium"

model = WhisperModel(modele, device="cpu", compute_type="int8")
# condition_on_previous_text=False : évite que Whisper "lisse" les reprises et répétitions,
# qu'on a justement besoin de voir pour choisir la bonne prise.
segments, _ = model.transcribe(
    str(audio),
    language="fr",
    word_timestamps=True,
    condition_on_previous_text=False,
    vad_filter=False,
)

data, lignes = [], []
for s in segments:
    mots = [{"w": w.word.strip(), "s": round(w.start, 3), "e": round(w.end, 3), "p": round(w.probability, 2)} for w in s.words]
    data.append({"start": round(s.start, 3), "end": round(s.end, 3), "text": s.text.strip(), "words": mots})
    ligne = f"[{s.start:8.2f} -> {s.end:8.2f}] {s.text.strip()}"
    lignes.append(ligne)
    print(ligne, flush=True)

base = audio.with_suffix("")
Path(f"{base}.transcript.json").write_text(json.dumps(data, ensure_ascii=False, indent=1))
Path(f"{base}.transcript.txt").write_text("\n".join(lignes) + "\n")
print(f"\nOK : {base}.transcript.json")
