# Plan de tournage des vidéos de cours

Objectif : **1 h 45 à 2 h** de vidéos de cours au total (le FYC demande 1 h 30 à 2 h, on vise plus haut pour garder de la marge), chaque vidéo entre 5 et 10 min.
Plan suivi : celui du Word des collègues (`docs_reference/plan_open_code_collegues.docx`, version en 7 parties), une vidéo par sous-partie.
Scripts : `videoN/script.md`. Vérifier les durées avec `python outils/compter_mots.py video{1..16}/script.md`.

## La règle pour que le total tienne, quel que soit celui qui parle

Le débit change d'une personne à l'autre. Une fois monté (pauses resserrées), Ibrahim parle à environ 230 mots/min ; quelqu'un de plus posé sera autour de 160. Chaque script est donc construit en deux couches :

- le texte principal, toujours gardé ;
- des blocs « [+] Bloc optionnel », qui se suffisent à eux-mêmes.

Chaque vidéo a deux bornes, écrites en tête du script (« Bornes : 6:00 – 6:45 ») :

- **min** : quelqu'un de rapide (230 mots/min) qui lit tout, blocs [+] compris ;
- **max** : quelqu'un de posé (160 mots/min) qui ne lit que le texte principal.

**Tout le monde enregistre tout, blocs [+] compris.** Au montage, on garde les blocs [+] un par un, dans l'ordre, **tant que la vidéo reste sous sa borne max**. Quelqu'un de rapide garde tous ses blocs, quelqu'un de posé n'en garde que quelques-uns, et la vidéo reste toujours entre ses deux bornes.

**Aucun temps d'attente n'est compté.** Dans les démos (vidéos 9 à 14), les installations, les chargements et l'agent qui travaille sont coupés ou accélérés à quelques secondes au montage, avec la voix par-dessus. La durée d'une vidéo, c'est sa voix. Les passages qui commentent l'écran sont écrits dans le script comme exemple (« Commentaire d'exemple, à adapter… ») : on les adapte à ce que l'agent fait vraiment, en gardant à peu près la même longueur.

Rappel montage : quand on se trompe, on fait une pause et on reprend la phrase depuis le début. La dernière prise complète est gardée.

## Les 16 vidéos

| # | Partie du plan | Vidéo | Min | Max |
|---|---|---|---|---|
| 1 | P1.1 | L'IA est devenue incontournable | 6:00 | 6:45 |
| 2 | P1.2 | Qu'est-ce qu'un LLM ? | 6:45 | 7:30 |
| 3 | P2.1 | LLM classique vs IA agentique | 8:00 | 8:55 |
| 4 | P2.2 | Les composants d'un agent IA | 5:30 | 6:10 |
| 5 | P3.1 | Le contexte : le carburant de l'IA | 7:30 | 8:20 |
| 6 | P3.2 | Context7 (MCP expliqué en premier) | 6:45 | 7:30 |
| 7 | P4.1 | Claude Code | 7:00 | 7:50 |
| 8 | P4.2 | Open Code : une alternative open source | 8:00 | 8:55 |
| 9 | P5.1 | Installer et configurer Open Code (démo) | 6:10 | 6:55 |
| 10 | P5.2 | Découvrir l'interface et les fonctionnalités (démo) | 6:10 | 6:55 |
| 11 | P6.1 | Cas pratique : comprendre un projet (démo) | 5:40 | 6:20 |
| 12 | P6.2 | Cas pratique : développer une fonctionnalité (démo) | 6:30 | 7:15 |
| 13 | P6.3 | Cas pratique : corriger un bug (démo) | 6:10 | 6:50 |
| 14 | P6.4 | Cas pratique : améliorer un code existant (démo) | 6:10 | 6:50 |
| 15 | P7.1 | Open Code vs Claude Code | 6:00 | 6:45 |
| 16 | P7.2 + Conclusion | Bonnes pratiques et conclusion du cours | 8:00 | 8:55 |
| | | **Total des bornes** | **1 h 46** | **1 h 59** |

Mesure des scripts actuels (04/11/2026) : **1 h 48 au minimum** (tout le monde rapide) et **1 h 55 au maximum** (tout le monde posé). Après montage avec la règle des blocs [+] : environ 1 h 55 à 160 mots/min, 1 h 56 à 200, 1 h 48 à 230.

Si une vidéo montée sort sous sa borne min, ou au-dessus de sa borne max, le signaler tout de suite : il faudra réenregistrer un bloc, ou en retirer un.

## Qui tourne quoi

Quatre blocs de quatre vidéos qui se suivent : chacun garde un thème cohérent et une voix constante sur toute sa partie. Remplacer « Membre 2/3/4 » par les prénoms.

| Personne | Vidéos | Thème | Durée (min – max) |
|---|---|---|---|
| Ibrahim | 1 à 4 | Bases : l'IA, les LLM, les agents | 25:45 – 28:50 |
| Membre 2 | 5 à 8 | Contexte, Context7, Claude Code, Open Code | 29:15 – 32:35 |
| Membre 3 | 9 à 12 | Démos : installation, interface, comprendre un projet, ajouter une fonctionnalité | 24:30 – 27:25 |
| Membre 4 | 13 à 16 | Démos bug et refactoring, comparatif, bonnes pratiques et conclusion | 26:20 – 29:30 |

Pourquoi ce découpage :
- Ibrahim a déjà enregistré une partie des vidéos 1 et 2 : il garde le début, et sa voix reste la même sur toutes les bases théoriques.
- Membre 3 prépare le projet de démo et l'environnement (Open Code installé, clé d'API, permissions). Membre 4 reprend le même dépôt git pour les vidéos 13 et 14, à partir du commit de la pagination : se mettre d'accord avant de tourner sur le modèle utilisé et le thème de l'interface, pour que les écrans se ressemblent.
- Membre 2 a le bloc le plus long, mais il n'a aucune démo à préparer.

## Avant de tourner

- Vidéos 1 et 2 : une partie du texte a déjà été enregistrée par Ibrahim (ancienne vidéo 1). Le script de chaque vidéo dit quelles parties sont reprises mot pour mot, et lesquelles restent à enregistrer.
- Démos 9 à 14 : valider le projet de démo (proposé : une petite API Node.js/Express d'articles avec des tests), le préparer avec un commit avant chaque cas pratique, et tester toutes les demandes la veille.
- Revérifier sur opencode.ai/docs, la veille, chaque commande montrée : Open Code change souvent, et la doc parle de deux versions majeures.
- Une seule personne par vidéo, de préférence, pour garder une voix constante.
- Les scripts sont une base : chacun relit et reformule avec ses mots avant de tourner (contenu personnel exigé par le FYC).
