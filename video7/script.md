# Vidéo 7 : Claude Code, l'agent de développement d'Anthropic

Partie du plan : P4.1 « Claude Code : l'agent de développement d'Anthropic ».
Bornes : 7:00 – 7:50 (min = quelqu'un de rapide qui lit tout, blocs [+] compris ; max = quelqu'un de posé qui ne lit que le texte principal).
Les lignes en italique décrivent l'écran ou donnent une consigne : elles ne se lisent pas.
Enregistrer tout, y compris les blocs [+]. Au montage, les blocs [+] sont gardés un par un tant que la vidéo reste sous sa borne max.
Sources : code.claude.com/docs (pages overview, setup, costs, memory), lues le 01/11/2026. Revérifier la commande d'installation et les offres la veille du tournage.

## 1. Intro

*À l'écran : le titre, puis une frise courte : février 2025, mai 2025.*

On a maintenant toute la théorie : ce qu'est un LLM, ce qu'est un agent, l'importance du contexte, et MCP. Il est temps de regarder les outils. Et on commence par celui contre lequel Open Code se positionne : Claude Code.

Pourquoi le présenter dans un cours sur Open Code ? Parce que c'est la référence. C'est l'outil qui a popularisé l'idée d'un agent de développement qui vit dans le terminal. Et pour comprendre ce qu'Open Code apporte, il faut savoir à quoi on le compare.

## 2. Ce qu'est Claude Code

*À l'écran : une capture du terminal avec Claude Code lancé. Puis quatre icônes : terminal, éditeur, application, navigateur.*

Claude Code, c'est l'agent de développement d'Anthropic, l'entreprise qui fait les modèles Claude. Il a été présenté en avant-première en février 2025, puis ouvert à tout le monde en mai 2025.

À la base, c'est un outil en ligne de commande. Vous vous placez dans le dossier de votre projet, vous tapez « claude », et vous discutez avec un agent qui peut lire votre code, le modifier, et lancer des commandes. Exactement le fonctionnement qu'on a décrit dans les vidéos 3 et 4 : un modèle, des outils, une boucle.

Depuis, il s'est décliné ailleurs. On le trouve en extension pour VS Code et pour les éditeurs JetBrains, en application de bureau, et même sur le web.

## 3. Installation et connexion

*À l'écran : la commande d'installation, puis la commande « claude » dans un dossier de projet.*

L'installation se fait en une commande. Sur macOS et Linux, un script qu'on télécharge et qu'on exécute. Sur Windows, il y a l'équivalent pour PowerShell. Il existe aussi un paquet npm, mais la documentation recommande l'installation native.

Ensuite, il faut se connecter. Et c'est là qu'il y a un point important : Claude Code n'est pas gratuit. Il faut soit un abonnement Claude payant, comme les offres Pro ou Max, soit un compte développeur Anthropic facturé à l'usage. L'offre gratuite de Claude ne donne pas accès à Claude Code. Au premier lancement, l'outil ouvre votre navigateur pour vous connecter, et c'est tout.

## 4. Ce qu'il sait faire

*À l'écran : les fonctionnalités apparaissent une par une, chacune avec une icône.*

Une fois lancé, Claude Code propose tout ce qu'on attend d'un agent de développement moderne. Et vous allez voir que beaucoup de ces idées se retrouvent dans Open Code.

Il a des commandes qui commencent par une barre oblique. Par exemple, la commande init analyse votre projet et génère un fichier de mémoire de départ.

Ce fichier de mémoire, chez Claude Code, s'appelle CLAUDE.md. Il contient les instructions persistantes du projet : comment le lancer, les conventions, ce qu'il faut éviter. Exactement le rôle de AGENTS.md dans Open Code. La documentation conseille d'ailleurs de le garder court, sous les deux cents lignes.

Il a un mode plan, qu'on active avec Majuscule et Tabulation. Dans ce mode, l'agent réfléchit et vous propose un plan avant de toucher au code.

Il gère MCP, donc on peut lui brancher des serveurs comme Context7.

Il a des hooks : des commandes que vous définissez et qui se lancent automatiquement avant ou après certaines actions de l'agent. Par exemple, lancer le formatage du code après chaque modification.

Et il peut lancer des sous-agents, c'est-à-dire plusieurs agents qui travaillent en parallèle sur différentes parties d'une tâche.

*[+] Bloc optionnel*

On peut aussi l'utiliser sans interface, dans un script. Avec une option dédiée, on lui passe une demande directement en ligne de commande, il fait le travail et il rend la main. C'est utile pour l'automatiser, par exemple dans une chaîne d'intégration continue. Open Code propose la même chose, on le verra. Et Claude Code permet aussi de créer ce qu'il appelle des skills : des procédures réutilisables qu'une équipe peut partager, comme une procédure de relecture de code toujours faite de la même façon.

*[fin du bloc]*

## 5. À quoi ressemble une session

*À l'écran : une session type, étape par étape : la demande, une demande d'autorisation, un aperçu des modifications, la réponse finale.*

Concrètement, comment se passe une session ? Vous lancez Claude Code dans votre projet, et vous écrivez votre demande en français, comme dans un chat. Par exemple : « ajoute une route pour supprimer un article, avec un test ».

L'agent commence par explorer. Il cherche les fichiers concernés, il les lit, et il vous affiche au fur et à mesure ce qu'il est en train de faire. Vous voyez passer les fichiers qu'il ouvre et les recherches qu'il lance.

Quand il veut modifier un fichier ou lancer une commande, il vous demande l'autorisation. Vous voyez exactement ce qu'il veut changer, sous forme de différences : les lignes retirées d'un côté, les lignes ajoutées de l'autre. Vous pouvez accepter, refuser, ou lui dire d'accepter automatiquement ce type d'action pour le reste de la session.

Puis il lance les tests. S'ils échouent, il lit l'erreur et il corrige, toujours dans la même boucle. Et à la fin, il vous fait un résumé de ce qu'il a fait.

Si à un moment il part dans une mauvaise direction, vous pouvez l'interrompre, et lui donner une précision. Il reprend en tenant compte de ce que vous avez dit. C'est ce dialogue permanent qui fait la différence avec un simple générateur de code : vous gardez la main, mais vous ne faites plus le travail mécanique.

Un détail sur CLAUDE.md : il peut exister à plusieurs niveaux. Il y a celui du projet, à la racine, qu'on partage avec l'équipe dans le dépôt git. Il y a un fichier personnel, dans votre dossier utilisateur, qui s'applique à tous vos projets : vos préférences à vous. Et il y a une version locale, propre à un projet mais pas partagée. Claude Code charge tout ça au démarrage. La documentation précise d'ailleurs que ces fichiers sont pris comme du contexte, pas comme des règles absolues : l'agent essaie de les suivre, mais rien ne le force à le faire.

## 6. Le modèle : Claude, et seulement Claude

*À l'écran : le logo Claude Code relié à trois cases : Opus, Sonnet, Haiku. Les autres fournisseurs sont grisés.*

Côté modèle, Claude Code utilise les modèles Claude d'Anthropic, et uniquement eux. Il y a plusieurs familles : des modèles très puissants, d'autres plus rapides et moins chers. On peut passer de l'un à l'autre avec une commande.

Et c'est à la fois une force et une limite. Une force, parce que l'outil et les modèles sont faits par la même entreprise. Le harness est réglé finement pour ces modèles précis. Les descriptions d'outils, le prompt système, la gestion du contexte : tout est optimisé pour Claude. C'est une des raisons pour lesquelles Claude Code donne d'aussi bons résultats sans rien configurer.

Mais c'est aussi une limite, parce que vous ne pouvez pas brancher un autre modèle. Pas de modèle d'un autre fournisseur, et pas de modèle qui tourne en local sur votre machine.

*[+] Bloc optionnel*

Même à l'intérieur de la famille Claude, le choix du modèle compte. La documentation de Claude Code le dit clairement : le modèle intermédiaire, Sonnet, gère bien la plupart des tâches de code, et coûte moins cher que le plus puissant, Opus. Et pour des tâches simples, comme les sous-agents qui font des recherches dans le code, elle montre qu'on peut utiliser le plus léger, Haiku. Autrement dit, même avec un seul fournisseur, on retrouve l'idée de choisir le bon modèle pour chaque tâche. On verra qu'Open Code pousse cette idée beaucoup plus loin, puisqu'il permet de mélanger des modèles de fournisseurs différents.

*[fin du bloc]*

## 7. Le coût

*À l'écran : deux colonnes : « Abonnement » et « À l'usage ». Puis le chiffre officiel.*

Parlons argent. Il y a deux façons de payer Claude Code. Soit votre abonnement Claude inclut l'utilisation, dans certaines limites. Soit vous utilisez un compte développeur, et vous payez chaque token consommé.

Pour se faire une idée, la documentation officielle donne un ordre de grandeur pour les entreprises : en moyenne, environ 13 dollars par développeur et par jour d'utilisation. Et pour 90 % des utilisateurs, ça reste sous les 30 dollars par jour. Ce sont des chiffres d'Anthropic, mesurés sur des déploiements en entreprise, donc à prendre comme un ordre de grandeur. Mais ça montre bien qu'un agent, ça consomme.

*[+] Bloc optionnel*

Et on sait maintenant pourquoi. Dans la vidéo 3, on a vu qu'à chaque tour de boucle, tout le contexte repart vers le modèle : la demande, l'historique, les fichiers lus, la sortie des commandes. Une seule tâche peut demander des dizaines de tours. Donc une journée de travail avec un agent représente une quantité de tokens sans commune mesure avec quelques questions posées dans un chat. Ce n'est pas propre à Claude Code : c'est le fonctionnement de tous les agents, et on retrouvera exactement la même question avec Open Code.

*[fin du bloc]*

## 8. Forces et limites

*À l'écran : deux colonnes « Forces » et « Limites » qui se remplissent en alternance.*

Si on résume, Claude Code a de vraies forces. Il est très bien fini. L'intégration avec les modèles est très serrée, donc les résultats sont bons dès le départ, sans configuration. Les réglages par défaut sont soignés. Et il est maintenu activement, avec des nouveautés régulières.

Mais il a aussi des limites. Vous êtes lié à Anthropic : un seul fournisseur de modèles. Le code de l'outil n'est pas ouvert, donc on ne peut pas vérifier exactement ce qu'il fait ni l'héberger soi-même. Il faut un abonnement ou un compte payant. Et votre code, vos demandes, le contenu des fichiers que l'agent lit, tout ça passe par les serveurs d'Anthropic.

*[+] Bloc optionnel*

Pour beaucoup de développeurs, ces limites ne posent aucun problème. Mais pour certains projets, elles sont bloquantes. Une entreprise qui travaille sur du code confidentiel peut ne pas avoir le droit d'envoyer ce code à un service extérieur. Une équipe qui veut maîtriser son budget peut vouloir choisir un modèle moins cher pour les tâches simples. Et un développeur qui travaille souvent sans connexion ne peut tout simplement pas l'utiliser. C'est exactement pour ces cas-là qu'on s'intéresse à une alternative.

*[fin du bloc]*

*[+] Bloc optionnel*

*À l'écran : quatre paires de cartes qui se répondent : CLAUDE.md et AGENTS.md, mode plan et agent Plan, MCP et MCP, claude -p et opencode run.*

Gardez en tête ces fonctionnalités, parce que vous allez les retrouver presque toutes dans Open Code, sous un autre nom. Le fichier CLAUDE.md a son équivalent, AGENTS.md. Le mode plan existe aussi, sous la forme d'un agent dédié. MCP fonctionne de la même façon. Les sous-agents aussi. Et le mode sans interface a son équivalent en ligne de commande. Autrement dit, si vous savez utiliser l'un, vous saurez vite utiliser l'autre. Ce qui change vraiment, ce n'est pas la façon de travailler, c'est tout ce qu'il y a autour : le code ouvert ou fermé, le choix du modèle, le prix et vos données.

*[fin du bloc]*

## 9. Conclusion et transition

*À l'écran : le logo Claude Code glisse sur le côté, le logo Open Code arrive.*

Claude Code, c'est donc la référence : un agent très abouti, mais fermé, payant, et attaché aux modèles d'une seule entreprise.

Et c'est justement là qu'Open Code entre en jeu. Un outil qui reprend la même idée, mais en open source, et qui vous laisse choisir votre modèle. Dans la prochaine vidéo, on va voir ce qu'il est, comment il fonctionne, et ce que ça change pour vos coûts et pour vos données.
