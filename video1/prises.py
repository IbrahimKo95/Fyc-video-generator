# Liste des bonnes prises de video1 (temps bruts) -> video1/edl.json, coupes calées sur les silences.
# Usage : ffmpeg -i audio/voix_video1.wav -af silencedetect=n=-40dB:d=0.25 -f null - (-> silences.txt), puis
#         python video1/prises.py silences.txt video1/edl.json
import json,sys
sil=[tuple(map(float,l.split())) for l in open(sys.argv[1])]
# (début, fin) approximatifs tirés des mots, "|" = changement de scène après
R="""4.74 8.88
9.18 15.30
16.50 21.80 |
40.18 42.52
42.88 45.20
46.24 52.74
54.06 60.38 |
63.48 66.70
67.02 72.22
72.88 75.36
76.88 84.44
84.98 89.22
89.78 96.12
97.10 104.08
114.54 117.24
117.96 120.34
120.92 123.98
142.00 148.34 |
153.56 157.90
167.35 171.46
172.44 177.00
193.04 194.46
194.92 202.00 |
207.48 215.54
219.80 221.22
221.80 226.18
230.96 231.76
232.30 234.22
234.80 245.28
260.60 268.96 |
273.44 278.04
278.46 281.96
283.10 286.64
292.04 300.06
300.66 304.82 |
308.06 311.22
325.70 326.76
327.38 341.96
359.66 367.52
368.66 371.46
387.55 397.04 |
400.48 405.30
416.10 421.16
437.26 446.86
448.22 456.76
458.52 462.40
464.05 465.76
466.88 469.84 |
472.52 474.32
474.96 477.76
478.82 481.02
481.84 490.58"""
def snap_start(a):
    for s,e in sil:
        if s<=a<=e: return e-0.08,"dans silence"
    c=[e for s,e in sil if a-0.7<=e<=a+0.15]
    return (max(c)-0.08,"calé") if c else (a,"exact")
def snap_end(b):
    for s,e in sil:
        if s<=b<=e: return s+0.12,"dans silence"
    c=[s for s,e in sil if b-0.15<=s<=b+0.6]
    return (min(c)+0.12,"calé") if c else (b+0.08,"!! pas de silence")
keep,pauses=[],{}
for l in R.splitlines():
    p=l.split(); a,b=float(p[0]),float(p[1])
    s,ms=snap_start(a); e,me=snap_end(b)
    # coupe les longues pauses internes (> 0,7 s)
    pts=[s]
    for x,y in sil:
        if s<x and y<e and y-x>0.7: pts+=[x+0.12,y-0.08]
    pts.append(e)
    for i in range(0,len(pts),2): keep.append([round(pts[i],3),round(pts[i+1],3)])
    if len(pts)>2: print(f"  coupé en {len(pts)//2}: {a}-{b}")
    if ms[0] in "!e" or me[0]=="!": print(f"{a}-{b}: début {ms}, fin {me}")
    if len(p)>2: pauses[str(len(keep)-1)]=0.8
json.dump({"source":"audio/voix_video1.wav","out":"video1/voix_montee.wav","pause":0.35,"keep":keep,"pauses":pauses},open(sys.argv[2],"w"),indent=1)
print(len(keep),"passages, durée parole",round(sum(e-s for s,e in keep),1))
