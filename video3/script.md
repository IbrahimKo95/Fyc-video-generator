# Vidéo 3 : LLM classique vs IA agentique

Partie du plan : P2.1 « LLM classique vs IA agentique ».
Bornes : 8:00 – 8:55 (min = quelqu'un de rapide qui lit tout, blocs [+] compris ; max = quelqu'un de posé qui ne lit que le texte principal).
Les lignes en italique décrivent l'écran ou donnent une consigne : elles ne se lisent pas.
Enregistrer tout, y compris les blocs [+]. Au montage, les blocs [+] sont gardés un par un tant que la vidéo reste sous sa borne max.
Sources : voir sources.md (ReAct, SWE-bench).

## 1. Rappel et objectif

*À l'écran : le cerveau dans le bocal de la vidéo 2, puis le titre de la vidéo.*

Dans la vidéo précédente, on a vu ce qu'est un LLM. Une fonction qui prend du texte et qui prédit la suite. Très forte, mais toute seule, elle ne fait rien. Elle ne lance pas de code, elle ne lit pas vos fichiers, elle n'est branchée à rien.

Aujourd'hui, on va voir comment on passe de ce cerveau dans un bocal à un agent, c'est-à-dire un programme qui peut vraiment agir sur votre projet. Et pour bien comprendre ce que ça change, on va d'abord regarder comment on travaille avec un LLM classique, celui qu'on utilise tous les jours dans une fenêtre de chat.

## 2. Le workflow classique

*À l'écran : un schéma en boucle qui se construit : éditeur, copier, chat, réponse, coller, lancer, erreur, retour au chat.*

Prenons une situation que tout le monde connaît. Vous avez un bug, ou une fonction à écrire. Vous ouvrez ChatGPT, ou n'importe quel assistant du même genre.

Vous copiez un morceau de votre code. Vous le collez dans la fenêtre, avec votre question. Le modèle vous répond avec un bout de code. Vous le recopiez dans votre éditeur. Vous lancez. Et là, ça plante.

Alors vous copiez le message d'erreur, vous retournez dans le chat, vous le collez. Le modèle s'excuse, il vous propose une correction. Vous la recopiez. Vous relancez. Et parfois, ça replante, et on repart pour un tour.

Si on regarde bien ce qui se passe, il y a quelque chose d'un peu bizarre. Le modèle écrit le code, mais c'est vous qui faites tout le reste. C'est vous qui exécutez. C'est vous qui regardez le résultat. C'est vous qui ramenez l'erreur au modèle. En fait, dans ce schéma, c'est vous le moteur d'exécution. Le modèle réfléchit, et vous, vous êtes ses mains et ses yeux.

## 3. Les limites de ce fonctionnement

*À l'écran : les cinq limites apparaissent une par une, chacune dans une carte.*

Et ce fonctionnement a des limites assez évidentes.

Première limite : le contexte se perd. À chaque aller-retour, vous ne montrez qu'un bout du problème. Le modèle ne sait pas ce qu'il y a dans le fichier d'à côté, ni comment votre projet est organisé.

Deuxième limite : c'est lent et c'est manuel. Copier, coller, relancer, recopier l'erreur. Sur une petite fonction, ça passe. Sur une vraie tâche, vous y passez l'après-midi.

Troisième limite : le modèle n'a jamais accès au vrai projet. Il ne voit que ce que vous choisissez de lui montrer. S'il vous manque une info, à lui aussi.

Quatrième limite : il ne peut pas vérifier ce qu'il produit. Il vous donne du code qui a l'air correct, mais il ne l'a jamais lancé. Et on a vu dans la vidéo 2 qu'un LLM peut inventer une fonction avec autant d'assurance qu'une vraie.

Et la dernière : ça ne passe pas à l'échelle. Dès qu'une modification touche trois ou quatre fichiers en même temps, le copier-coller devient ingérable.

*[+] Bloc optionnel*

Attention, ça ne veut pas dire que ce mode de travail est inutile. Pour poser une question de cours, comprendre un message d'erreur, ou se faire expliquer un concept, une fenêtre de chat, c'est très bien. Le problème, c'est quand on essaie de l'utiliser pour faire du vrai développement sur un vrai projet. Là, on passe plus de temps à transporter de l'information entre deux fenêtres qu'à réfléchir au problème. Et c'est exactement ce que les agents viennent régler.

*[fin du bloc]*

## 4. Le saut agentique : des outils et une boucle

*À l'écran : l'équation « modèle + outils + boucle = agent » qui se construit terme par terme.*

Alors, qu'est-ce qui change avec un agent ? En réalité, on ajoute seulement deux choses au modèle.

La première, ce sont des outils. Un outil, c'est une action que le modèle a le droit de demander. Lire un fichier. Écrire dans un fichier. Lancer une commande dans le terminal. Chercher un mot dans tout le projet. Aller lire une page web. Le modèle ne fait pas ces actions lui-même, il ne peut toujours produire que du texte. Mais ce texte, maintenant, peut être une demande du genre : « je veux lire le fichier server.js ». Et un programme autour du modèle exécute cette demande pour lui.

La deuxième chose, c'est une boucle. Le modèle décide d'une action. Le programme l'exécute. Le résultat est renvoyé au modèle. Le modèle lit ce résultat et décide de l'action suivante. Et ainsi de suite, jusqu'à ce que la tâche soit terminée.

*À l'écran : la boucle tourne : décide, exécute, résultat, décide.*

*[+] Bloc optionnel*

Petite précision sur l'endroit où vivent ces agents. Certains sont intégrés directement dans un éditeur de code : c'est le cas de Cursor en mode agent, par exemple, ou des extensions d'agent dans VS Code. D'autres vivent dans le terminal, comme Claude Code et Open Code. Le principe est le même, un modèle, des outils, une boucle. Ce qui change, c'est l'interface. Les agents en terminal ont un avantage : ils ne dépendent d'aucun éditeur. Vous pouvez les utiliser avec l'éditeur que vous voulez, sur un serveur distant, ou même dans un script automatisé.

*[fin du bloc]*

Et ces deux ajouts changent tout. Maintenant, le modèle peut explorer votre base de code tout seul. Il peut lancer les tests, lire les erreurs, corriger, relancer. Le rôle que vous teniez dans le workflow classique, celui de moteur d'exécution, c'est l'agent qui le prend.

*[+] Bloc optionnel*

Cette idée n'est pas sortie de nulle part. En 2022, des chercheurs ont proposé une approche appelée ReAct, pour « raisonner et agir ». Le principe : au lieu de demander au modèle une réponse directe, on le fait alterner entre une étape de réflexion, une action, puis l'observation du résultat. Et ils ont montré que les modèles font moins d'erreurs quand ils peuvent vérifier ce qu'ils avancent. Les agents qu'on utilise aujourd'hui reposent sur cette logique, en beaucoup plus abouti.

*[fin du bloc]*

## 5. Un exemple concret : ajouter la pagination

*À l'écran : deux colonnes « Classique » et « Agent », les étapes s'affichent en parallèle.*

Prenons un exemple pour rendre ça concret. Vous avez une API, avec une route qui renvoie la liste des articles. Et on vous demande d'ajouter de la pagination : pouvoir demander la page 2, avec dix articles par page.

En mode classique, vous décrivez la route au modèle. Vous collez le code du contrôleur. Il vous renvoie un extrait. Vous l'intégrez à la main, vous vous rendez compte qu'il faut aussi toucher à la couche qui lit la base de données, vous retournez lui demander. Vous lancez, il y a une erreur, vous la recopiez. Au final, plusieurs allers-retours, et c'est vous qui avez fait tout l'assemblage.

En mode agent, vous écrivez une seule demande : « ajoute la pagination sur la route des articles ». L'agent cherche lui-même où est définie cette route. Il lit le fichier, puis ceux qui sont autour. Il modifie le contrôleur et la couche de données, de façon cohérente. Il lance les tests. S'il y en a un qui échoue, il lit l'erreur et il corrige. Et à la fin, il vous présente l'ensemble des modifications.

Et vous, qu'est-ce que vous faites pendant ce temps ? Vous relisez. Votre travail ne disparaît pas, il change de nature. Vous passez de celui qui tape à celui qui vérifie. On aura l'occasion de faire exactement cet exemple en démonstration, dans le cas pratique de la vidéo 12.

## 6. Le prix de l'autonomie

*À l'écran : trois cartes avec une icône d'alerte : imprévisible, il exécute, il consomme.*

Évidemment, cette autonomie a un prix. Et il faut le connaître dès maintenant, parce qu'on va le retrouver tout au long du cours.

D'abord, un agent est imprévisible. Il peut partir dans une mauvaise direction. Mal comprendre la demande, modifier un fichier qui n'avait rien à voir, ou tourner en rond en essayant toujours la même correction. Plus la tâche est vague, plus ce risque est grand.

Ensuite, il exécute des commandes. Et ça, c'est à la fois ce qui le rend puissant et ce qui le rend dangereux. Une commande qui supprime des fichiers, qui installe un paquet douteux, qui touche à une base de données : l'agent peut la lancer. C'est pour ça que les bons outils ont un système de permissions, où il doit vous demander avant de faire certaines actions. On verra comment le régler dans Open Code.

Et enfin, il consomme beaucoup. Rappelez-vous, tout se compte en tokens. Or à chaque tour de boucle, l'agent renvoie au modèle tout le contexte : votre demande, les fichiers qu'il a lus, les résultats des commandes. Une tâche qui demande vingt tours de boucle, c'est vingt fois ce contexte qui repart. Ça se paie, en temps et en argent.

*[+] Bloc optionnel*

Ce dernier point surprend souvent les gens qui découvrent les agents. Avec un chat, on paie à la question. Avec un agent, on paie à la tâche, et une tâche peut demander des dizaines d'échanges avec le modèle sans que vous ne voyiez rien passer. C'est pour ça que les outils comme Open Code affichent ce que la session a consommé. On y reviendra en détail dans la vidéo 8, quand on parlera du coût réel d'un agent.

*[fin du bloc]*

## 7. Ce qu'on peut confier à un agent

*À l'écran : cinq cartes : nouvelle fonctionnalité, bug, refactoring, tests, documentation.*

Malgré ces limites, la liste de ce qu'on peut confier à un agent est déjà longue. Et c'est pour ça qu'il est devenu un outil de tous les jours pour beaucoup de développeurs.

On peut lui demander d'ajouter une fonctionnalité, comme notre pagination. Il cherche où intervenir, il modifie les bons fichiers, il vérifie que rien n'est cassé.

On peut lui demander de corriger un bug. Là, il est particulièrement à l'aise si vous lui donnez un moyen de reproduire le problème, par exemple un test qui échoue. Il lance le test, il lit l'erreur, il formule une hypothèse, il corrige, il relance.

On peut lui demander de refactorer, c'est-à-dire de réécrire un code pour le rendre plus propre sans changer ce qu'il fait. Renommer, découper une grosse fonction, supprimer des doublons. C'est un travail mécanique, et il le fait bien, à condition de vérifier derrière.

On peut aussi lui faire écrire des tests, ou de la documentation. Un README, des commentaires, la description d'une API. Ce sont des tâches qu'on a souvent tendance à repousser, et qu'un agent fait en quelques minutes.

Et enfin, il y a une utilisation qu'on oublie souvent : lui faire expliquer un projet. Vous arrivez sur un code que vous ne connaissez pas, vous lui demandez comment il est organisé, et il va le lire pour vous. C'est d'ailleurs par là qu'on commencera nos cas pratiques.

*[+] Bloc optionnel*

Pour mesurer ce que valent vraiment ces agents, des chercheurs ont créé en 2024 un banc d'essai appelé SWE-bench. L'idée est simple : on prend de vrais tickets, ouverts sur de vrais projets open source sur GitHub. On donne le ticket et le code à l'agent, et on regarde s'il arrive à produire une correction qui fait passer les tests du projet. C'est devenu une référence pour comparer les agents entre eux. Et c'est intéressant parce que ça ne mesure pas si le modèle sait parler de code, mais s'il sait vraiment modifier un projet existant pour résoudre un problème réel. Exactement ce qu'on attend de lui au quotidien. Autrement dit, on ne juge pas le code d'un agent en le lisant : on le juge en lançant les tests, et en regardant s'ils passent.

*[fin du bloc]*

## 8. Conclusion et transition

*À l'écran : le schéma « LLM + outils + boucle » se transforme en deux logos : Claude Code et Open Code.*

Si on résume : un agent, c'est un LLM, plus des outils, plus une boucle. Le modèle réfléchit et décide. Les outils lui donnent des mains. La boucle lui permet de vérifier son travail et de recommencer.

Et c'est exactement ce que sont Claude Code et Open Code. Ce ne sont pas des modèles d'IA en eux-mêmes. Ce sont des programmes qui tiennent cette boucle autour d'un modèle, avec un jeu d'outils bien choisis.

Dans la prochaine vidéo, on va ouvrir cette boucle et regarder chaque pièce de près : comment le modèle appelle un outil, comment l'agent garde la mémoire de ce qu'il fait, et ce qui fait la différence entre un bon agent et un agent qui tourne en rond.
