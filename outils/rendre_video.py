import sys, subprocess, os, pathlib, json
from playwright.sync_api import sync_playwright

# usage : python outils/rendre_video.py <page.html> <preview|render|sfx> [scènes ex: 0,2]
PAGE = pathlib.Path(sys.argv[1]).resolve()
HERE = PAGE.parent
URL = PAGE.as_uri()
FPS = 30
mode = sys.argv[2]          # "preview" or "render"
which = [int(x) for x in sys.argv[3].split(",")] if len(sys.argv) > 3 else None

with sync_playwright() as p:
    b = p.chromium.launch()
    def fresh():
        pg = b.new_page(viewport={"width": 1920, "height": 1080})
        pg.goto(URL)
        pg.evaluate("document.fonts.ready")
        return pg
    pg = fresh()
    lens = pg.evaluate("API.lens()")
    if mode == "sfx":
        # bruitages : un souffle à chaque changement de scène + les éléments marqués data-sfx
        ev, t0 = [], 0.0
        for i, L in enumerate(lens):
            if i:
                ev.append({"t": round(t0 - 0.45, 3), "s": "souffle"})
            for e in pg.evaluate(f"API.sfx({i})"):
                ev.append({"t": round(t0 + e["t"], 3), "s": e["s"]})
            t0 += L
        out = HERE / "sfx.json"
        out.write_text(json.dumps({"lead": pg.evaluate("API.lead"), "events": ev}, indent=1), encoding="utf-8")
        print(f"OK : {out} ({len(ev)} bruitages, {t0:.2f} s)")
        sys.exit()
    pg.close()
    idx = which if which is not None else range(len(lens))
    for i in idx:
        pg = fresh()
        pg.evaluate(f"API.show({i})")
        pg.wait_for_timeout(50)
        if mode == "preview":
            L = lens[i]
            for t in (L * 0.55, L - 0.6):
                pg.evaluate(f"API.seek({i},{t})")
                pg.screenshot(path=str(HERE / f"prev_s{i+1}_{t:.1f}.jpg"), type="jpeg", quality=80)
            pg.close()
            continue
        n = round(lens[i] * FPS)
        tmp = HERE / f"scene{i+1}.part.mp4"
        ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS),
                               "-c:v", "mjpeg", "-i", "-", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
                               "-pix_fmt", "yuv420p", "-r", str(FPS), "-f", "mp4", str(tmp)], stdin=subprocess.PIPE)
        for f in range(n):
            pg.evaluate(f"API.seek({i},{f / FPS})")
            ff.stdin.write(pg.screenshot(type="jpeg", quality=92))
        ff.stdin.close()
        if ff.wait() == 0:
            os.replace(tmp, HERE / f"scene{i+1}.mp4")
        pg.close()
        print("scene", i + 1, "done", flush=True)
    b.close()
