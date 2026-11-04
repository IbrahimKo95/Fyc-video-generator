# Vidéo 1 : L'IA est devenue incontournable

Partie du plan : P1.1 « Introduction : l'IA est devenue incontournable ».
Bornes : 6:00 – 6:45 (min = quelqu'un de rapide qui lit tout, blocs [+] compris ; max = quelqu'un de posé qui ne lit que le texte principal).
Les lignes en italique décrivent l'écran ou donnent une consigne : elles ne se lisent pas.
Enregistrer tout, y compris les blocs [+]. Au montage, les blocs [+] sont gardés un par un tant que la vidéo reste sous sa borne max.
Sources : voir sources.md (Copilot et Codex, ChatGPT, Claude Code, licence d'Open Code).

*Les parties 1 à 4 reprennent mot pour mot le texte déjà enregistré par Ibrahim (ancienne vidéo 1) : ces prises peuvent être réutilisées au montage. À enregistrer : les parties 5 à 8 et les blocs [+].*

## 1. Intro

*À l'écran : titre « Open Code », le terminal qui tape `opencode`.*

Salut à tous, et bienvenue dans ce cours sur Open Code, l'alternative open source à Claude Code.

Avant de mettre les mains dans l'outil, on va prendre un peu de recul. Parce que pour bien utiliser un agent IA, il faut comprendre ce qu'il y a dedans et d'où ça vient. Donc on part de la théorie, et petit à petit on va aller vers la pratique, jusqu'à utiliser Open Code sur un vrai projet.

## 2. Accroche

*À l'écran : la première question apparaît puis se fait barrer, la seconde arrive.*

Aujourd'hui, coder avec l'IA, ce n'est plus un truc de curieux. Dans beaucoup d'entreprises, c'est devenu la façon normale de travailler.

Du coup, la vraie question, ce n'est plus « est-ce qu'on utilise l'IA pour coder ? ». Ça, c'est réglé. La vraie question, c'est : « est-ce qu'on l'utilise bien ? »

Et c'est tout l'objectif de ce cours : qu'à la fin, vous sachiez faire tourner un agent sur un vrai projet, mais surtout que vous sachiez où sont les pièges.

## 3. Comment on en est arrivés là

*À l'écran : la frise se construit, une date à la fois.*

Alors, comment on en est arrivés là ? Faisons un petit retour en arrière.

Avant 2021, on avait surtout de l'autocomplétion un peu améliorée, avec des outils comme Tabnine ou Kite. Ça vous complétait la fin de la ligne. Pratique, mais ça s'arrêtait là.

En 2021, GitHub Copilot arrive, et là, c'est la première fois qu'un modèle de langage vous propose des fonctions entières, directement dans l'éditeur. Mais ça reste de la suggestion : l'outil propose, et c'est vous qui acceptez ou pas.

*[+] Bloc optionnel*

Derrière les débuts de Copilot, il y avait un modèle appelé Codex, présenté la même année par OpenAI dans un article de recherche. L'idée était de prendre un grand modèle de langage et de l'entraîner en plus sur une énorme quantité de code public. Et les chercheurs ont mesuré ses résultats d'une façon très concrète : on lui donne la description d'une fonction, il écrit le code, et on lance des tests pour voir si ça marche vraiment. Cette façon d'évaluer, en exécutant le code plutôt qu'en le lisant, on la retrouvera plus tard avec les agents.

*[fin du bloc]*

Fin 2022, ChatGPT sort, et on découvre le format conversation. On décrit son problème en français, on a une réponse. Par contre, il faut tout faire à la main : copier son code dans la fenêtre, recopier la réponse dans l'éditeur, et recommencer à la moindre erreur.

En 2023 et 2024, apparaissent les premiers agents. L'idée, c'est de donner au modèle des outils et une boucle. Il peut lire des fichiers, lancer des commandes, voir ce qui se passe, et réessayer.

Et en 2025, ces agents deviennent grand public, avec Claude Code, Cursor en mode agent, et des alternatives open source comme Open Code.

## 4. De l'assistant à l'agent

*À l'écran : la carte « suggère » s'éteint, la flèche, puis la carte « agit ».*

Si on devait résumer tout ça en une phrase : on est passés d'un assistant qui suggère à un agent qui agit.

Avant, l'outil vous proposait du code, et c'était à vous de le copier, de le lancer, de le tester. Maintenant, l'agent lit votre projet, modifie les fichiers, lance les commandes, et vérifie lui-même si ça marche.

Et forcément, ça change notre métier. Ce qui compte de plus en plus, ce n'est plus de taper vite. C'est de savoir bien cadrer un problème, donner le bon contexte à l'IA, et surtout relire du code qu'on n'a pas écrit soi-même.

*[+] Bloc optionnel*

Attention, ça ne veut pas dire que savoir coder ne sert plus à rien. C'est même l'inverse. Pour relire le code d'un agent, il faut être capable de juger s'il est bon. Pour lui donner une demande claire, il faut avoir compris le problème. Et pour voir qu'il part dans une mauvaise direction, il faut savoir où on veut aller. Un agent entre les mains de quelqu'un qui ne sait pas coder, c'est un peu comme une voiture puissante entre les mains de quelqu'un qui n'a pas le permis. Ça avance vite, mais on ne sait pas trop où.

*[fin du bloc]*

## 5. Ce que l'agent fait, et ce qui reste à vous

*À l'écran : deux colonnes. À gauche « L'agent » : explorer, écrire, lancer, corriger. À droite « Vous » : décider, cadrer, relire, assumer.*

Concrètement, qu'est-ce qu'on confie à un agent aujourd'hui ? Beaucoup de choses. Explorer un projet qu'on ne connaît pas et nous l'expliquer. Écrire une nouvelle fonctionnalité avec ses tests. Chercher l'origine d'un bug, le corriger, et vérifier que la correction tient. Remettre au propre un vieux code que personne n'ose toucher.

Et qu'est-ce qui reste à vous ? Tout ce qui demande du jugement. Choisir ce qu'on construit, et comment. Découper le travail en tâches claires. Décider si une solution est acceptable. Et surtout, assumer le résultat. Le jour où un bug arrive en production, personne ne va accepter « c'est l'agent qui l'a écrit » comme explication. Le code que vous gardez, c'est votre code.

C'est cette répartition qu'on va apprendre à maîtriser tout au long du cours.

## 6. Pourquoi un cours sur Open Code ?

*À l'écran : deux logos côte à côte : Claude Code et Open Code. Sous Claude Code : « fermé », « un seul fournisseur ». Sous Open Code : « open source », « le modèle de votre choix ».*

Alors pourquoi un cours sur Open Code en particulier ?

Parmi tous ces agents, celui qui a fait le plus parler de lui pour travailler dans le terminal, c'est Claude Code, l'outil d'Anthropic. Il marche très bien. Mais il a trois contraintes. Son code n'est pas ouvert. Il faut un abonnement ou un compte payant. Et il ne fonctionne qu'avec les modèles d'une seule entreprise.

Open Code reprend la même idée : un agent de développement qui vit dans votre terminal. Mais il est open source, sous licence MIT. Tout son code est public. Et surtout, c'est vous qui choisissez le modèle qui travaille derrière. Un modèle chez un grand fournisseur, un autre chez un concurrent, ou même un modèle qui tourne sur votre propre machine, sans que rien ne sorte de chez vous.

Pour une entreprise qui veut garder la main sur ses coûts ou sur ses données, ça change beaucoup de choses. Et pour nous, c'est aussi un outil idéal pour apprendre. Comme son code est ouvert, on peut regarder comment un agent fonctionne vraiment, au lieu de le traiter comme une boîte noire.

*[+] Bloc optionnel*

Open Code est un projet récent. Son dépôt de code a été créé fin avril 2025, par l'équipe derrière SST, un outil open source connu des développeurs web. Et il a beaucoup évolué depuis, très vite. C'est une bonne nouvelle, parce que le projet est vivant. Mais ça veut aussi dire qu'un tutoriel d'il y a quelques mois peut déjà être en partie dépassé. Dans ce cours, chaque commande a été vérifiée dans la documentation officielle. Et c'est un réflexe que je vous conseille de garder : avec un outil qui bouge autant, la documentation officielle passe avant tout le reste.

*[fin du bloc]*

## 7. Le programme du cours

*À l'écran : sept cases qui s'allument l'une après l'autre, une par partie.*

Voici comment on va avancer.

Dans la première partie, celle-ci, on pose les bases : d'où vient l'IA qu'on utilise pour coder, et ce qu'est vraiment un modèle de langage.

Dans la deuxième, on voit comment on passe d'un simple modèle à un agent, et de quoi un agent est fait.

La troisième partie est consacrée au contexte, c'est-à-dire tout ce qu'on donne à lire au modèle. Vous allez voir que c'est souvent là que tout se joue. On y verra aussi Context7, un outil qui donne à l'agent une documentation à jour.

Dans la quatrième, on présente les deux outils : Claude Code, puis Open Code.

La cinquième partie, c'est la prise en main : on installe Open Code, on le configure, et on fait le tour de l'interface.

La sixième, c'est la pratique. Quatre cas sur un vrai projet : comprendre un code qu'on ne connaît pas, ajouter une fonctionnalité, corriger un bug, et améliorer un code existant.

Et dans la dernière partie, on compare les deux outils, et on fait le point sur les bonnes pratiques, notamment de sécurité.

*[+] Bloc optionnel*

Un mot sur la façon de suivre ce cours. On suppose que vous savez déjà programmer, que vous êtes à l'aise avec un terminal, et que vous connaissez les bases de git. Pour les vidéos de démonstration, je vous conseille vivement de refaire les manipulations en même temps, en mettant la vidéo en pause. Un agent, ça s'apprend surtout en le voyant se tromper, et en apprenant à le remettre sur les rails. Ça, aucune vidéo ne peut le faire à votre place.

*[fin du bloc]*

## 8. Conclusion et transition

*À l'écran : la frise complète, puis un point d'interrogation sur le mot « LLM ».*

Ce qu'on retient de cette introduction : en quelques années, on est passés de l'autocomplétion à des agents capables de modifier un projet entier. Et le travail du développeur s'est déplacé : moins de frappe, plus de cadrage et plus de relecture.

Mais tous ces outils reposent sur la même brique de base : un grand modèle de langage, ce qu'on appelle un LLM. Avant d'aller plus loin, il faut comprendre ce que c'est, et surtout ce que ça n'est pas. C'est le sujet de la prochaine vidéo.
