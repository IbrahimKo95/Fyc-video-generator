# Vidéo 11 : Cas pratique, comprendre un projet (démo)

Partie du plan : P6.1 « Cas pratique : comprendre un projet ».
Bornes : 5:40 – 6:20 (min = quelqu'un de rapide qui lit tout, blocs [+] compris ; max = quelqu'un de posé qui ne lit que le texte principal).
Les lignes en italique décrivent l'écran ou donnent une consigne : elles ne se lisent pas.
Enregistrer tout, y compris les blocs [+]. Au montage, les blocs [+] sont gardés un par un tant que la vidéo reste sous sa borne max.
Sources : opencode.ai/docs (agents, tui), lues le 01/11/2026.

*Vidéo en capture d'écran, avec la voix par-dessus. Les attentes de l'agent sont accélérées à quelques secondes au montage : la durée de la vidéo, c'est la voix.*

*Préparation (à faire avant le tournage) :*
*- Projet de démo proposé, à valider par le groupe : une petite API Node.js/Express qui gère des articles (route GET /articles qui renvoie toute la liste), avec quelques tests automatisés. Taille modeste, que tout le monde comprend. Le même projet sert aux vidéos 9 à 14.*
*- Dépôt git propre, avec un commit avant chaque cas pratique pour pouvoir rejouer la démo.*
*- Tester les demandes la veille avec le modèle choisi. L'agent ne fait jamais exactement deux fois la même chose : garder la meilleure prise.*
*- Les passages qui commentent l'écran sont écrits comme exemple : décrire ce que l'agent fait vraiment, en gardant à peu près la même longueur.*

## 1. Intro

*À l'écran : le dossier du projet de démo dans le terminal, et la liste de ses fichiers.*

On attaque les cas pratiques. Pendant quatre vidéos, on va travailler sur le même projet, une petite API qui gère des articles, et vivre quatre situations que vous rencontrerez forcément en entreprise.

La première, c'est celle de votre premier jour sur un projet. Vous récupérez un code que vous n'avez jamais vu, et on vous demande d'y ajouter une fonctionnalité. Avant de toucher à quoi que ce soit, il faut comprendre comment il marche. Et c'est exactement ce qu'on va demander à l'agent.

## 2. Se mettre en lecture seule

*À l'écran : on lance opencode, on appuie sur Tabulation, l'indicateur passe sur « Plan ».*

On lance Open Code dans le dossier du projet. Et avant d'écrire quoi que ce soit, je passe en mode Plan avec la touche Tabulation. On veut seulement comprendre, donc l'agent n'a aucune raison de modifier un fichier. En mode Plan, il peut lire le projet et réfléchir, mais il ne touche pas aux fichiers. On est tranquille.

On aurait pu rester sur l'agent Build, puisqu'on a réglé les permissions pour qu'il demande avant de modifier un fichier. Mais il aurait fallu surveiller chaque demande. Ici, la règle est simple : on explore, on ne change rien. Choisir le bon agent avant d'écrire, c'est un réflexe à prendre dès le début.

## 3. La demande

*À l'écran : on tape la demande, puis on l'envoie.*

Je lui demande : « Explique-moi l'architecture de ce projet : les dossiers principaux, le chemin d'une requête HTTP depuis son arrivée jusqu'à la réponse, et par où commencer pour ajouter une fonctionnalité. »

Remarquez que je ne lui demande pas juste « explique-moi le projet ». Je lui dis précisément ce que je veux savoir. Trois questions claires, ça donne une réponse structurée. Une question vague, ça donne un résumé vague.

## 4. Regarder l'agent explorer

*À l'écran : l'agent travaille, en accéléré, mais on laisse voir chaque fichier qu'il ouvre.*

Regardez ce qu'il fait. Il ne répond pas tout de suite. Il explore.

*Commentaire d'exemple, à adapter à ce que l'agent fait vraiment :*

Il commence par le package.json. C'est logique : c'est là qu'il trouve les dépendances, donc le framework utilisé, et les commandes pour lancer le projet et les tests. Ensuite, il cherche le point d'entrée, le fichier qui démarre le serveur. Il l'ouvre, il voit quelles routes sont branchées, et il suit les imports, d'un fichier à l'autre. Là, il fait une recherche dans tout le projet pour trouver où les articles sont lus. Il ne lit pas tout. Il va droit vers ce qui répond à mes questions.

C'est exactement la démarche qu'aurait un développeur expérimenté le premier jour : regarder les dépendances, trouver le point d'entrée, suivre le chemin du code. Sauf qu'ici, ça prend une minute. Et c'est aussi le context engineering de la vidéo 5 en action : une récupération ciblée, plutôt que de tout charger.

*[+] Bloc optionnel*

Sur un projet plus gros, l'agent peut aussi confier cette exploration à un sous-agent. Open Code en fournit un qui s'appelle explore : un agent rapide, en lecture seule, fait pour fouiller le code. On peut l'appeler soi-même avec l'arobase suivie de son nom, et l'agent principal peut aussi le lancer de lui-même. L'intérêt : le sous-agent parcourt des dizaines de fichiers de son côté, et ne renvoie que ce qu'il a trouvé. La conversation principale reste propre, et l'agent principal ne se noie pas dans des fichiers qui ne servent pas à répondre à votre question.

*[fin du bloc]*

## 5. Lire la réponse, et la vérifier

*À l'écran : la réponse de l'agent. Faire défiler lentement.*

Voici sa réponse.

*Commentaire d'exemple, à adapter à la réponse réelle :*

Il décrit trois dossiers : les routes, les contrôleurs, et la couche qui accède aux données. Il explique qu'une requête arrive sur le serveur, passe par le fichier des routes, qui appelle le bon contrôleur, qui lui-même demande les articles à la couche de données. Et pour ajouter une fonctionnalité, il conseille de commencer par le contrôleur des articles.

C'est clair, et c'est un très bon point de départ. Mais attention. On a vu dans la vidéo 2 qu'un LLM produit du texte qui a l'air juste, pas du texte vérifié. Une explication de projet, c'est pareil. L'agent peut décrire avec assurance un fonctionnement qui n'est pas tout à fait celui du code.

*À l'écran : on ouvre dans l'éditeur un des fichiers cités par l'agent.*

Donc on vérifie. Je prends une de ses affirmations, et j'ouvre le fichier qu'il cite.

*Dire ce qu'on constate réellement. Si l'agent s'est trompé, c'est un excellent moment à garder : le montrer clairement.*

Prenez cette habitude : ouvrir un ou deux fichiers cités pour contrôler. Ça prend trente secondes, et ça évite de construire sur une base fausse.

Et méfiez-vous en particulier de certains signes. Une explication très générale, qui pourrait s'appliquer à n'importe quel projet Express, sans citer de vrais noms de fichiers. Un fichier cité qui n'existe pas. Ou une fonctionnalité décrite que vous ne retrouvez nulle part. Dans ces cas-là, demandez à l'agent de citer précisément le fichier et la fonction concernés. S'il n'y arrive pas, c'est probablement qu'il a comblé un trou en devinant.

## 6. Creuser avec des questions ciblées

*À l'écran : deux questions de suivi, l'une après l'autre, avec leurs réponses.*

Une fois la vue d'ensemble obtenue, on peut creuser. Par exemple : « où sont lus les articles depuis la base de données ? » Ou : « comment sont organisés les tests, et comment on les lance ? »

L'agent garde le contexte de la conversation, donc il repart de ce qu'il a déjà exploré. Il n'a pas besoin de tout relire, et ses réponses arrivent plus vite.

Et posez aussi les questions que vous n'oseriez pas poser à un collègue le premier jour. Pourquoi ce fichier existe ? À quoi sert cette dépendance ? L'agent ne vous jugera pas, et il ne s'impatiente jamais.

Profitez-en aussi pour comparer ce que vous apprenez avec le fichier AGENTS.md du projet. S'il manque une information importante, comme une commande ou une convention, notez-la. On l'ajoutera au fichier, pour que l'agent la connaisse dès la prochaine session.

*[+] Bloc optionnel*

Remarquez qu'à aucun moment on n'a modifié quoi que ce soit. Rien à annuler, rien à valider. Cette étape est sans risque, et elle est très rentable. Même quand vous comptez faire la modification vous-même à la main, demander d'abord à l'agent de vous expliquer le code fait gagner beaucoup de temps. C'est une des utilisations les plus sous-estimées des agents : pas pour écrire du code, mais pour comprendre celui des autres.

*[fin du bloc]*

*[+] Bloc optionnel*

*À l'écran : un schéma en texte, avec des flèches, produit par l'agent.*

Une demande que j'aime bien, pour finir : « fais-moi un schéma en texte du chemin d'une requête GET /articles, avec les noms des fichiers ». L'agent répond avec un petit dessin fait de flèches, qu'on peut lire d'un coup d'œil. C'est souvent plus parlant qu'un long paragraphe. Et comme chaque case porte un vrai nom de fichier, c'est aussi très facile à vérifier.

*[fin du bloc]*

*[+] Bloc optionnel*

*À l'écran : on tape /export.*

Et si cette explication vous a été utile, gardez-la. La commande export enregistre la conversation au format Markdown. Vous pouvez la relire plus tard, la partager avec un autre développeur qui arrive sur le projet, ou vous en servir pour compléter le fichier AGENTS.md avec ce que vous avez appris.

*[fin du bloc]*

## 7. Vérifier que le projet tourne

*À l'écran : on tape « !npm test » ; la sortie des tests s'affiche dans la conversation, tout est vert.*

Dernière étape avant de toucher au code : s'assurer que le projet fonctionne tel qu'il est. L'agent nous a dit comment lancer les tests. Plutôt que de le croire sur parole, je les lance moi-même, directement dans Open Code, avec le point d'exclamation qu'on a vu dans la vidéo précédente.

*Commentaire d'exemple, à adapter à la sortie réelle :*

Tous les tests passent. Parfait.

Ça a l'air d'un détail, mais c'est une étape très importante. Si un test échouait déjà avant qu'on commence, on risquerait plus tard d'accuser l'agent d'une erreur qu'il n'a pas faite, ou au contraire de laisser passer une vraie régression au milieu d'échecs qu'on croit normaux. Maintenant, on a un point de départ propre. Et comme le résultat de la commande est entré dans la conversation, l'agent le sait aussi.

*[+] Bloc optionnel*

Et si un test échoue dès le départ ? Ne foncez pas. Notez-le, et demandez d'abord à l'agent, toujours en mode Plan, de vous expliquer pourquoi. Soit c'est un vrai bug, et ce sera votre prochaine tâche. Soit c'est un problème d'installation ou de configuration sur votre machine, et il faut le régler avant tout le reste. Dans les deux cas, mieux vaut le savoir maintenant que le découvrir au milieu d'une fonctionnalité.

*[fin du bloc]*

## 8. Conclusion et transition

*À l'écran : récapitulatif en trois étapes : mode Plan, demande précise, vérifier.*

Ce qu'on retient de ce premier cas : pour comprendre un projet, on reste en mode Plan, on pose des questions précises, et on vérifie une ou deux affirmations dans le code. On n'a rien modifié, mais on sait maintenant où intervenir.

Et justement, dans la prochaine vidéo, on va intervenir. On va ajouter une vraie fonctionnalité à ce projet : la pagination sur la liste des articles, en commençant par un plan qu'on corrigera avant que l'agent écrive la moindre ligne.
