"""Monte la voix à partir d'une liste de passages à garder (EDL).

Usage : python outils/monter_audio.py video1/edl.json

Format de edl.json :
{
  "source": "audio/voix_video1.wav",
  "out": "video1/voix_montee.wav",
  "pause": 0.35,                       # silence inséré entre deux passages (s)
  "keep": [[12.40, 18.92], [25.10, 31.05], ...],   # [début, fin] dans l'enregistrement brut
  "pauses": {"5": 0.8}                 # optionnel : pause plus longue après le passage n°5 (changement de scène)
}

Sorties :
- le fichier audio monté (48 kHz mono, volume normalisé à -16 LUFS)
- <out>.timeline.json : pour chaque passage, sa position dans le brut et dans le montage.
  Sert à caler les animations : temps_montage = out[0] + (temps_brut - src[0]).
"""
import json
import subprocess
import sys
from pathlib import Path

edl = json.loads(Path(sys.argv[1]).read_text())
src, out = edl["source"], edl.get("out", "voix_montee.wav")
pause_def = edl.get("pause", 0.35)
pauses = {int(k): v for k, v in edl.get("pauses", {}).items()}
keep = edl["keep"]

fc, parts, timeline, t = [], [], [], 0.0
for i, (s, e) in enumerate(keep):
    d = e - s
    fc.append(
        f"[0:a]atrim={s}:{e},asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=mono,"
        f"afade=t=in:d=0.012,afade=t=out:st={max(d - 0.012, 0):.3f}:d=0.012[a{i}]"
    )
    parts.append(f"[a{i}]")
    timeline.append({"n": i, "src": [s, e], "out": [round(t, 3), round(t + d, 3)]})
    t += d
    if i < len(keep) - 1:
        p = pauses.get(i, pause_def)
        fc.append(f"anullsrc=r=48000:cl=mono,atrim=0:{p}[g{i}]")
        parts.append(f"[g{i}]")
        t += p

fc.append(f"{''.join(parts)}concat=n={len(parts)}:v=0:a=1,afftdn=nf=-25,loudnorm=I=-16:TP=-1.5:LRA=11[out]")
cmd = ["ffmpeg", "-y", "-loglevel", "error", "-i", src, "-filter_complex", ";".join(fc),
       "-map", "[out]", "-ar", "48000", "-ac", "1", out]
subprocess.run(cmd, check=True)
Path(f"{out}.timeline.json").write_text(json.dumps(timeline, indent=1))
print(f"OK : {out} ({t:.1f} s, {len(keep)} passages)")
