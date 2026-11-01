# Projet FYC : cours vidéo « Open Code »

Projet de groupe d'Ibrahim, 4e année ESGI (RO DEV), FYC 2026-2027. Deux groupes ont fusionné : le sujet est **Open Code (opencode, de SST), l'alternative open source à Claude Code**. Le groupe n'avait rien rendu aux séances 1 et 2 : on est en rattrapage.

Réponds en français. Ibrahim parle de façon familière ; reste simple et direct.

## Règles du FYC (source : `docs_reference/ESGI_FYC_consignes.pdf`)

- **Vidéos de cours** : 5 à 10 min chacune, total final **1 h 30 à 2 h**. Cumul attendu par séance : 30 min (S2), 1 h (S3, 02/11/2026), 1 h 30 (S4, 04/01/2027).
- **Autres livrables** : vidéo de présentation de l'équipe (3-4 min, on doit voir les membres), cas pratique en 3 parties + **correction en vidéo**, glossaire, rapport de veille, fiche scientifique (S3), poster scientifique A3 (S4), résumé perso de 5 pages (S4), résumé de 30 000 signes, **test final** (ex. 40 QCM). Rendu final le 15/01/2027, soutenance le 03/02/2027.
- **Charte** : police **Roboto** + couleurs de l'ESGI. Sous-titres conseillés.
- **Hébergement** : tout sur Moodle (YouTube, Drive, GitHub interdits).
- **Contenu personnel obligatoire** : la « génération IA automatique » est sanctionnée (conseil de discipline). Le résumé passe sur Compilatio.

## Règles de travail (à respecter absolument)

1. **Ne jamais inventer le contenu du cours.** Le poster, la fiche, les scripts décrivent uniquement ce que le cours fait réellement. Pas de comparaison chiffrée, d'expérience ou de QCM qui n'existe pas encore. En cas de doute, demander.
2. **Sources** : chaque info factuelle va dans `sources.md` avec son lien, où elle est utilisée et son statut (vérifiée / à vérifier). Mettre ce fichier à jour à chaque nouvelle info. Copie aussi dans le projet claude.ai « FYC » (`claude/sources_fyc.md`).
3. **Écriture anti-IA** (scripts, fiche, poster) : langage naturel et simple, phrases de longueurs variées, pas de tirets longs, pas de « crucial », « révolutionner », « en somme », « dans un monde où », pas de triplets d'adjectifs, pas de gras partout. Les scripts doivent pouvoir être lus à voix haute sans sonner récité.
4. **Durées** : mesuré sur la vidéo 1 montée, Ibrahim fait environ **230 mots/min** (1 088 mots pour 4 min 44 ; l'ancienne estimation de 170 était fausse). Plusieurs personnes tournent, donc le débit varie (compter 160 pour quelqu'un de posé). Chaque script a un texte principal et des blocs « [+] Bloc optionnel » : tout le monde enregistre tout, et au montage on garde les blocs [+] un par un tant que la vidéo reste sous 9 min 30. Vérifier les durées avec `python outils/compter_mots.py video*/script.md` : chaque vidéo doit rester entre 5 et 10 min pour 160 comme pour 230 mots/min, et le total au-dessus de 1 h 30 même à 230. Règles détaillées : `plan_tournage.md`.

## Plan des vidéos

| # | Vidéo | Durée visée |
|---|---|---|
| 1 | L'IA incontournable + qu'est-ce qu'un LLM | 7 min |
| 2 | Du LLM classique à l'agent IA | 8 min |
| 3 | Anatomie d'un agent | 8 min |
| 4 | Le contexte, carburant de l'IA | 7 min |
| 5 | MCP et Context7 | 8 min |
| 6 | Claude Code | 6 min |
| 7 | Open Code, coûts et souveraineté | 9 min |
| 8 | Installer et configurer (démo) | 9 min |
| 9 | L'interface et les commandes (démo) | 7 min |
| 10 | Cas pratique : comprendre + ajouter une feature (démo) | 10 min |
| 11 | Cas pratique : bug + refactor (démo) | 8 min |
| 12 | Comparatif, bonnes pratiques, conclusion | 9 min |

Contenu détaillé de chaque partie : `docs_reference/plan_open_code_collegues.docx` (le script de cours des collègues, fait avec ChatGPT : s'en servir comme base de contenu, jamais le recopier).

## Montage d'une vidéo (voix enregistrée d'une traite)

Ibrahim enregistre sans couper : quand il se trompe, il fait une pause puis **reprend la phrase depuis le début**. Règle : **la dernière prise complète d'une phrase est la bonne.**

Installation (Arch Linux, une seule fois) :
```bash
sudo pacman -S --needed ffmpeg python
python -m venv .venv && source .venv/bin/activate
pip install faster-whisper "av<16" playwright   # av 16+ casse faster-whisper 1.2
python -m playwright install chromium
```

Étapes :
1. Mettre l'enregistrement dans `audio/` (ex. `audio/voix_video1.wav`).
2. Transcrire : `python outils/transcrire.py audio/voix_video1.wav` → `.transcript.json` (mots horodatés) et `.transcript.txt`.
3. Aligner la transcription sur `video1/script.md` : pour chaque phrase du script, retrouver la **dernière** prise complète et propre (sans bégaiement ni mot raté). Couper juste avant le premier mot et juste après le dernier (+ ~0,08 s de marge). Écrire `video1/edl.json` (format décrit en tête de `outils/monter_audio.py`). Mettre une pause de 0,35 s entre phrases et ~0,8 s aux changements de scène. Signaler à Ibrahim les phrases introuvables ou ratées dans toutes les prises.
4. Monter : `python outils/monter_audio.py video1/edl.json` → `video1/voix_montee.wav` + `.timeline.json` (correspondance brut → montage, pour caler les animations).
5. Ibrahim écoute `voix_montee.wav` et valide avant de faire le visuel.
   Astuce : caler les coupes sur les silences (`ffmpeg ... -af silencedetect=n=-40dB:d=0.25`) plutôt que sur les seuls temps Whisper, qui dérivent après les longues pauses ; puis retranscrire le montage pour vérifier qu'il ne reste ni reprise ni « je recommence ». Exemple : `video1/prises.py`.
6. Visuel : une page HTML par vidéo sur le gabarit commun `outils/gabarit_video.css` + `outils/gabarit_video.js` (modèle : `video1/visuel.html`). Une `<section class="scene">` par scène, durée = durée réelle de la voix (bornes au milieu des pauses de 0,8 s, arrondies à l'image, voix décalée de 0,5 s au début et 1,5 s de fin). Chaque apparition est calée (`--d`) sur le mot prononcé : transcrire `voix_montee.wav` elle-même pour avoir les temps directement dans le montage. Rendu : `python outils/rendre_video.py videoN/visuel.html preview` (vérifier les captures), puis `render`.
7. Son : `python outils/sons.py bruitages` (une fois), `python outils/sons.py nappe videoN/nappe.wav <durée>`, puis `python outils/rendre_video.py videoN/visuel.html sfx` (un souffle à chaque changement de scène + un clic sur chaque élément marqué `data-sfx="clic"`) et `python outils/mixer_son.py videoN` → `mix.wav` (nappe baissée sous la voix, -16 LUFS). Réglages des volumes en tête de `mixer_son.py`. Tous les sons sont synthétisés : pas de droits à gérer.
8. Assembler : concaténer les scènes (`ffmpeg -f concat -safe 0 -i list.txt -c copy video.mp4`), puis ajouter le son mixé (`ffmpeg -i video.mp4 -i videoN/mix.wav -c:v copy -c:a aac -b:a 192k -shortest videoN/final.mp4`).
9. Sous-titres : `python outils/sous_titres.py audio/voix_montee_videoN.transcript.json videoN/corrections.json videoN/final.srt 0.5` (les corrections remplacent ce que Whisper entend mal, ex. « Cloud Code » → « Claude Code »), puis relire le `.srt`.

### Direction visuelle des vidéos

Ibrahim a essayé une version sobre (fond clair uni, une seule couleur) et préfère le style de `video1/visuel_test.mp4` : la version sobre faisait « vide ». Le style retenu (01/11/2026) est donc celui du test, repris dans le gabarit commun `outils/gabarit_video.css` : fond sombre, **grille de fond qui dérive**, halos discrets, barre de progression, plusieurs couleurs (cyan, orange, vert, rouge) **mais toujours dans des cadres** (cartes, puces, bordures). Garder des écrans remplis (cartes, icônes, schémas qui se construisent quand on en parle), Roboto, textes courts. Même gabarit pour toutes les vidéos.

Son : une palette variée de bruitages synthétisés (`outils/sons.py`, 7 familles et plusieurs variantes chacune), pas 2 ou 3 sons qui reviennent en boucle. Mais rester cohérent : des timbres graves et feutrés (rien au-dessus d'environ 1 kHz de centre spectral, pas de sons aigus), et pas de son sur les détails (chaque mot ou token qui défile, chaque case d'un schéma). Le carillon est réservé à 2 ou 3 moments clés par vidéo. Une barre qui « charge » doit être découpée en segments calés sur chaque point, jamais une seule animation linéaire. Chaque élément animé choisit sa famille via `data-sfx` (`pop` pour une carte, `clic` pour un point de liste, `tic` pour un mot ou un token, `trait` pour un trait ou une rature, `impact` pour un grand titre, `carillon` pour une idée clé). Le son part au `--d` de l'élément lui-même : sur un élément sans `--d` propre (une rature avec `--b`, par exemple), ajouter `--d`, sinon il hérite de celui du parent.

## Fichiers

- `video1/script.md` : script de la vidéo 1 (version de référence : doc claude.ai https://claude.ai/artifact/SLXLp7tnRpm7prKEMAYKzx). `video1/complement.md` : deux passages à enregistrer pour passer la vidéo 1 au-dessus de 5 min.
- `video2/` à `video12/script.md` : scripts des autres vidéos (écrits le 01/11/2026 à partir du plan des collègues et des docs officielles, à relire par le groupe).
- `plan_tournage.md` : règles de tournage pour le groupe et durées estimées.
- `fiche/` : fiche scientifique (LaTeX, `xelatex fiche_scientifique.tex` deux fois ; polices Roboto dans `fiche/fonts/`).
- `poster/poster.dc.html` : poster A3 (l'original modifiable est l'artifact Design https://claude.ai/artifact/Y1Tavudm2Kw7UCPgVW9Tzy). Problématique retenue : « OpenCode est-il une alternative crédible à Claude Code, et comment l'utiliser efficacement et en sécurité sur un vrai projet ? »
- `sources.md` : sources de chaque info.
- `docs_reference/` : consignes officielles, exemples de fiche et de poster fournis par l'école, plan des collègues.

## À faire

- [ ] Vidéo 1 : monter la voix enregistrée, refaire le visuel en version sobre, sous-titres
- [ ] Vidéo 1 : enregistrer `video1/complement.md` et remonter (la version actuelle fait 4 min 44, sous le minimum de 5 min)
- [ ] Pitch de 2 min pour la séance 3
- [ ] Vidéo de présentation de l'équipe (3-4 min)
- [ ] Faire relire les scripts des vidéos 2 à 12 par le groupe, puis répartir qui tourne quoi
- [ ] Valider et préparer le projet de démo des vidéos 8 à 11 (proposé : petite API Node.js/Express d'articles avec tests)
- [ ] Cas pratique (3 parties + corrections vidéo), glossaire, rapport de veille
- [ ] Test final (QCM)
- [ ] Remplacer noms, mentor, logos et couleurs ESGI dans la fiche et le poster
- [ ] Vérifier les sources marquées « à vérifier », en particulier opencode.ai/docs avant les démos
