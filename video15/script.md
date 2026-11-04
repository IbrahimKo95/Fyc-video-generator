# Vidéo 15 : Open Code vs Claude Code

Partie du plan : P7.1 « Open Code vs Claude Code ».
Bornes : 6:00 – 6:45 (min = quelqu'un de rapide qui lit tout, blocs [+] compris ; max = quelqu'un de posé qui ne lit que le texte principal).
Les lignes en italique décrivent l'écran ou donnent une consigne : elles ne se lisent pas.
Enregistrer tout, y compris les blocs [+]. Au montage, les blocs [+] sont gardés un par un tant que la vidéo reste sous sa borne max.
Sources : opencode.ai/docs (intro, providers, agents, rules, cli) et code.claude.com/docs (overview, setup, costs, memory), lues le 01/11/2026.

## 1. Intro

*À l'écran : le titre, puis les deux logos face à face.*

On arrive à la dernière partie du cours. On a vu la théorie, on a présenté les deux outils, et on a utilisé Open Code sur un vrai projet, dans quatre situations différentes. Maintenant, on prend du recul.

Dans cette vidéo, on compare Open Code et Claude Code point par point. Pas pour désigner un gagnant, mais pour savoir lequel choisir, et dans quelle situation. Parce que la bonne réponse change d'un projet à l'autre. Un outil parfait pour un projet personnel peut être interdit chez un client, et l'inverse est vrai aussi.

## 2. Ce qui les rapproche

*À l'écran : une liste de paires qui se répondent : CLAUDE.md et AGENTS.md, mode plan et agent Plan, MCP des deux côtés, sous-agents des deux côtés, claude -p et opencode run.*

Commençons par ce qui les rapproche, parce que c'est beaucoup.

Sur le fond, les deux font la même chose. Un modèle, des outils, une boucle, comme on l'a vu dans la deuxième partie. Ils vivent tous les deux dans le terminal. Ils lisent votre projet, modifient les fichiers, lancent les commandes et les tests.

Et leurs fonctionnalités se répondent presque une à une. Un fichier d'instructions pour le projet : CLAUDE.md d'un côté, AGENTS.md de l'autre. Une façon de réfléchir avant d'agir : le mode plan de Claude Code, l'agent Plan d'Open Code. Le support de MCP, pour brancher des serveurs comme Context7. Des sous-agents, pour déléguer une partie du travail. Et un mode sans interface, pour les utiliser dans un script.

Autrement dit, tout ce que vous avez appris dans les cas pratiques, la méthode en quatre temps, les demandes précises, la relecture, git, marche aussi avec Claude Code. Si vous savez utiliser l'un, vous saurez vite utiliser l'autre.

## 3. Le modèle compte autant que l'outil

*À l'écran : un même outil relié à trois modèles différents, avec trois résultats différents.*

Il y a un point qu'on a vu dès la deuxième partie, et qui change la façon de lire cette comparaison. L'outil, c'est le harness. L'intelligence, c'est le modèle. Quand on compare Claude Code et Open Code, on ne compare donc pas seulement deux outils. Avec Claude Code, l'outil et le modèle viennent ensemble. Avec Open Code, vous choisissez le modèle, et c'est ce choix qui fera l'essentiel de la qualité du résultat.

Donc dire « Open Code donne de moins bons résultats » ou « de meilleurs résultats » n'a pas vraiment de sens sans préciser avec quel modèle. Branché sur un très bon modèle, il peut faire un travail excellent. Branché sur un petit modèle local, il sera beaucoup plus limité.

*[+] Bloc optionnel*

C'est pour ça que l'équipe d'Open Code a pris les devants. Sa documentation propose une liste de modèles qu'elle a testés et validés avec l'outil, pour éviter de tâtonner. Et elle propose aussi son propre abonnement d'accès à des modèles, à petit prix. Ça ne vous oblige à rien, puisque vous pouvez toujours brancher le fournisseur de votre choix. Mais pour démarrer, partir d'un modèle déjà testé avec l'outil évite beaucoup de mauvaises surprises. Vous pourrez toujours en essayer d'autres ensuite, une fois que vous saurez à quoi ressemble un agent qui fonctionne bien.

*[fin du bloc]*

## 4. Ce qui les sépare

*À l'écran : un tableau à deux colonnes qui se remplit ligne par ligne, au rythme de la voix.*

Ce qui les sépare, maintenant.

Le code de l'outil. Claude Code est fermé. Open Code est open source, sous licence MIT, donc lisible, modifiable et vérifiable.

Les modèles. Claude Code utilise uniquement les modèles Claude d'Anthropic. Open Code annonce plus de 75 fournisseurs, et accepte des modèles locaux.

Le coût. Claude Code demande un abonnement Claude payant ou un compte facturé à l'usage. Open Code est gratuit, mais vous payez le modèle : à l'usage avec une clé d'API, par un abonnement, ou rien du tout en local, avec le coût de la machine.

Les données. Avec Claude Code, elles partent chez Anthropic. Avec Open Code, elles partent chez le fournisseur que vous choisissez, ou nulle part si le modèle est local.

Le fichier d'instructions. CLAUDE.md est propre à Claude Code. AGENTS.md est une convention ouverte, que plusieurs outils savent lire.

La qualité des résultats. Claude Code est réglé finement pour les modèles Claude, et donne de très bons résultats sans configuration. Avec Open Code, la qualité dépend beaucoup du modèle que vous branchez.

La finition. Claude Code est très abouti. Open Code est plus jeune, il évolue vite, et ses commandes changent parfois d'une version à l'autre.

Les réglages par défaut. Claude Code demande votre accord avant de modifier un fichier ou de lancer une commande. Open Code, lui, autorise la plupart des actions d'office : on l'a vu, c'est à vous de resserrer les permissions.

Et le travail sans connexion. Impossible avec Claude Code. Possible avec Open Code et un modèle local.

*[+] Bloc optionnel*

Petite précision sur ce dernier point. « Possible » ne veut pas dire « aussi bien ». Un modèle local qui tourne sur un ordinateur portable n'a pas la puissance des gros modèles dans le cloud. Pour une question simple ou un petit changement, il peut suffire. Pour une fonctionnalité qui touche plusieurs fichiers, il risque de se perdre en route. Le travail hors ligne est un vrai avantage d'Open Code, mais il a un prix en qualité, et il faut le savoir avant de compter dessus.

*[fin du bloc]*

## 5. Lequel choisir ?

*À l'écran : deux profils, chacun avec ses critères.*

Alors, lequel choisir ? Ça dépend de votre situation.

Claude Code est un bon choix si vous voulez les meilleurs résultats tout de suite, sans passer de temps à configurer. Si vous utilisez déjà les modèles d'Anthropic. Et si envoyer votre code chez Anthropic ne pose aucun problème à votre entreprise ou à votre client.

Open Code est un bon choix si vous voulez choisir votre modèle, ou en changer selon la tâche. Si vos données ne doivent pas sortir, ou seulement chez un fournisseur précis. Si vous voulez pouvoir vérifier ce que fait l'outil. Si vous voulez maîtriser vos coûts au plus près. Ou simplement si vous préférez l'open source.

Et ce n'est pas l'un ou l'autre. Beaucoup de développeurs gardent les deux et choisissent selon le projet : le client, la confidentialité du code, le budget.

Et pour vous, en tant qu'étudiants ? Open Code a un avantage simple : vous pouvez commencer avec un modèle peu cher, ou un modèle local si votre machine le permet, et voir exactement ce que vous consommez. Et comme son code est ouvert, vous pouvez aller voir comment un agent fonctionne vraiment, avec son prompt système et ses outils. Pour apprendre, c'est précieux.

*[+] Bloc optionnel*

Passer de l'un à l'autre est d'ailleurs assez facile. Open Code sait lire un fichier CLAUDE.md quand le projet n'a pas de AGENTS.md. Donc si votre équipe utilise déjà Claude Code, vous pouvez essayer Open Code sur le même projet sans rien réécrire. Et dans l'autre sens, un AGENTS.md bien écrit reste lisible par n'importe qui, humain compris. Le vrai travail, ce n'est pas la migration de l'outil. C'est d'apprendre les réglages d'Open Code, à commencer par les permissions.

*[fin du bloc]*

## 6. Les questions à se poser pour son projet

*À l'écran : quatre questions, une par carte.*

Si vous devez trancher pour un vrai projet, posez-vous quatre questions, dans cet ordre.

Un : est-ce que le code a le droit de sortir ? Si la réponse est non, la question est réglée. Il vous faut un modèle local, donc Open Code.

Deux : est-ce que vous avez déjà un fournisseur imposé ? Si votre entreprise a un contrat avec un fournisseur autre qu'Anthropic, Open Code vous permet de l'utiliser. Si c'est Anthropic, les deux restent possibles.

Trois : combien de temps voulez-vous passer à configurer ? Claude Code marche bien dès le départ. Open Code demande de choisir un modèle, de régler les permissions, et parfois de tester plusieurs modèles avant de trouver le bon.

Et quatre : comment voulez-vous payer ? Un abonnement fixe et prévisible, ou une facture à l'usage, plus transparente, mais qui peut grimper si on ne fait pas attention.

*[+] Bloc optionnel*

Et si vous hésitez encore, le plus simple est d'essayer les deux sur un même petit projet, avec la même tâche. Une fonctionnalité simple, un bug à corriger. Regardez le temps passé, la qualité du résultat, le nombre de corrections que vous avez dû faire, et ce que ça a coûté. Avec Open Code, essayez aussi deux ou trois modèles différents. Vous verrez vite si l'écart vient plutôt de l'outil ou plutôt du modèle. C'est le meilleur moyen de vous faire votre propre avis, plutôt que de vous fier à ce qu'on lit en ligne.

*[fin du bloc]*

## 7. Conclusion et transition

*À l'écran : une balance : d'un côté « résultats immédiats », de l'autre « contrôle et liberté ».*

On résume. Les deux outils font la même chose, de la même façon. Claude Code mise sur les résultats immédiats et la finition. Open Code mise sur la liberté : le choix du modèle, le code ouvert, la maîtrise des coûts et des données. En échange, il demande un peu plus de configuration.

Mais quel que soit l'outil, un agent reste un outil puissant, qui agit sur votre machine. Dans la dernière vidéo, on rassemble toutes les bonnes pratiques du cours, avec un accent particulier sur la sécurité, et on conclut.
