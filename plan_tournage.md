# Plan de tournage des vidéos de cours

Objectif du FYC : 1 h 30 à 2 h de vidéos de cours au total, chaque vidéo entre 5 et 10 min.
Scripts : `videoN/script.md`. Durées estimées avec `python outils/compter_mots.py video*/script.md`.

## La règle pour que le total tienne, quel que soit celui qui parle

Le débit change d'une personne à l'autre. Une fois monté (pauses resserrées), Ibrahim parle à environ 230 mots/min ; quelqu'un de plus posé sera autour de 160. Chaque script est donc construit en deux couches :

- le texte principal, toujours gardé ;
- des blocs « [+] Bloc optionnel », qui se suffisent à eux-mêmes.

**Tout le monde enregistre tout, blocs [+] compris.** Au montage, on garde les blocs [+] un par un tant que la vidéo reste sous 9 min 30. Quelqu'un de rapide aura donc tous ses blocs, quelqu'un de lent n'en aura que quelques-uns, et chaque vidéo reste entre 5 et 10 min.

Pour les démos (vidéos 8 à 11), une partie du temps est faite d'écran sans voix (installation, agent qui travaille) et de commentaires improvisés de ce qui s'affiche vraiment. Les passages en italique « Prévoir environ N secondes » le signalent.

Rappel montage : quand on se trompe, on fait une pause et on reprend la phrase depuis le début. La dernière prise complète est gardée.

## Durées estimées après montage

| Vidéo | Sujet | 160 mots/min | 200 mots/min | 230 mots/min |
|---|---|---|---|---|
| 1 | L'IA incontournable + qu'est-ce qu'un LLM (déjà tournée) + complément | 6,2 min (mesurée + complément) | | |
| 2 | Du LLM classique à l'agent | 9,3 | 9,2 | 8,0 |
| 3 | Anatomie d'un agent | 9,4 | 9,2 | 8,0 |
| 4 | Le contexte, carburant de l'IA | 9,4 | 8,5 | 7,4 |
| 5 | MCP et Context7 | 9,2 | 9,1 | 7,9 |
| 6 | Claude Code | 9,2 | 7,4 | 6,4 |
| 7 | Open Code, coûts et souveraineté | 9,7 | 9,1 | 8,3 |
| 8 | Installer et configurer (démo) | 9,7 | 9,3 | 8,6 |
| 9 | L'interface et les commandes (démo) | 9,4 | 8,2 | 7,3 |
| 10 | Cas pratique : comprendre + ajouter une feature (démo) | 9,2 | 8,8 | 8,1 |
| 11 | Cas pratique : bug + refactor (démo) | 9,0 | 8,2 | 7,4 |
| 12 | Comparatif, bonnes pratiques, conclusion | 9,4 | 9,1 | 7,9 |
| **Total** | | **≈ 1 h 49** | **≈ 1 h 42** | **≈ 1 h 32** |

Si une vidéo montée sort plus courte que prévu (moins de 5 min, ou un total qui passe sous 1 h 30), le signaler tout de suite : il faudra réenregistrer un bloc ou en écrire un nouveau.

## Avant de tourner

- Vidéo 1 : la version montée fait 4 min 44, sous le minimum de 5 min. Enregistrer `video1/complement.md` (Ibrahim, même micro), puis remonter.
- Démos 8 à 11 : valider le projet de démo (proposé : une petite API Node.js/Express d'articles avec des tests), le préparer avec un commit avant chaque partie, et tester toutes les demandes la veille.
- Revérifier sur opencode.ai/docs, la veille, chaque commande montrée : Open Code change souvent, et la doc parle de deux versions majeures.
- Une seule personne par vidéo, de préférence, pour garder une voix constante.
