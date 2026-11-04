# Vidéo 12 : Cas pratique, développer une fonctionnalité (démo)

Partie du plan : P6.2 « Cas pratique : développer une fonctionnalité ».
Bornes : 6:30 – 7:15 (min = quelqu'un de rapide qui lit tout, blocs [+] compris ; max = quelqu'un de posé qui ne lit que le texte principal).
Les lignes en italique décrivent l'écran ou donnent une consigne : elles ne se lisent pas.
Enregistrer tout, y compris les blocs [+]. Au montage, les blocs [+] sont gardés un par un tant que la vidéo reste sous sa borne max.
Sources : opencode.ai/docs (agents, permissions, tui, cli), lues le 01/11/2026.

*Vidéo en capture d'écran, avec la voix par-dessus. Les attentes de l'agent sont accélérées à quelques secondes au montage : la durée de la vidéo, c'est la voix.*

*Préparation : même projet que la vidéo 11, dépôt propre, avec un commit juste avant. Permissions de commandes et de modifications sur « ask » (vidéo 9). Tester la demande la veille. Les passages qui commentent l'écran sont écrits comme exemple : décrire ce que l'agent fait vraiment, en gardant à peu près la même longueur.*

## 1. Intro

*À l'écran : le projet de démo, et un appel à GET /articles qui renvoie une très longue liste.*

Dans la vidéo précédente, on a compris comment fonctionne notre petite API d'articles. Maintenant, on va y ajouter une fonctionnalité. Et c'est celle dont on parlait dans la vidéo 3 : la pagination.

Aujourd'hui, la route qui liste les articles les renvoie tous d'un coup. Avec dix articles, ça va. Avec dix mille, c'est un problème. On veut pouvoir demander une page précise, avec un nombre d'articles par page. C'est une petite fonctionnalité, mais elle a tout d'une vraie : elle touche plusieurs fichiers, la route, l'accès aux données et les tests, et elle cache quelques cas pièges. C'est exactement le genre de tâche qu'on confie à un agent au quotidien.

On va suivre une méthode en quatre temps : planifier, corriger le plan, construire, puis relire.

## 2. D'abord, un plan

*À l'écran : l'indicateur est sur « Plan ». On tape la demande.*

On reste en mode Plan pour l'instant. Je lui demande :

« Planifie l'ajout de la pagination sur la route GET /articles, avec deux paramètres dans l'URL : page et limit. Indique les fichiers à modifier et les tests à ajouter. Ne code rien pour l'instant. »

La demande est précise. La route concernée, les noms des paramètres, et ce que j'attends : un plan, avec les fichiers et les tests. C'est ce qu'on a vu dans la vidéo 5 : plus la demande est précise, moins l'agent doit deviner.

Et pourquoi ne pas demander directement à l'agent Build de coder la pagination ? Parce qu'il prendrait une série de décisions tout seul, sans me les montrer : où lire les paramètres, que faire des valeurs absurdes, quoi tester. Je ne les découvrirais qu'en relisant le code, et chaque désaccord voudrait dire refaire une partie du travail. Le plan rend ces décisions visibles avant qu'elles coûtent quelque chose.

*À l'écran : l'agent explore puis présente son plan, en accéléré.*

*Commentaire d'exemple, à adapter au plan réel :*

Il propose de lire les deux paramètres dans le contrôleur des articles, de calculer à partir d'eux la position du premier article à renvoyer, puis de ne demander à la couche de données que les articles de cette page. Côté tests, il prévoit de vérifier qu'on obtient bien la première page, la deuxième, et une page vide quand on demande trop loin.

## 3. Corriger le plan avant le code

*À l'écran : on écrit une correction au plan. L'agent met son plan à jour.*

Et c'est maintenant qu'on a le plus de pouvoir. Le plan, c'est le moment le moins cher pour corriger le tir. Aucune ligne de code n'a été écrite, donc changer d'avis ne coûte rien.

*Choisir une vraie correction selon le plan obtenu. Exemples possibles : une valeur par défaut pour limit, une limite maximale, le nombre total d'articles dans la réponse, le refus des valeurs négatives.*

Ici, il me manque deux choses. Que se passe-t-il si on appelle la route sans paramètre ? Et si quelqu'un demande la page moins trois ? Je lui écris : « Ajoute une valeur par défaut, dix articles par page, et une limite maximale de cent. Refuse les valeurs négatives ou qui ne sont pas des nombres, avec une erreur claire. Et ajoute des tests pour ces cas. »

*À l'écran : le plan mis à jour, les nouveaux points surlignés.*

Il met son plan à jour. Imaginez la même correction après coup, une fois le code écrit : il aurait fallu tout reprendre. Ce va-et-vient sur le plan, c'est là que votre expérience de développeur compte le plus. L'agent pense rarement tout seul aux cas tordus. Vous, vous savez qu'un utilisateur finira toujours par envoyer n'importe quoi.

*[+] Bloc optionnel*

Et si le plan proposé est complètement à côté ? Par exemple, s'il veut réécrire toute la couche de données pour une simple pagination. Dans ce cas, ne passez pas dix messages à le corriger morceau par morceau. Le contexte se remplirait de tentatives abandonnées. Ouvrez plutôt une nouvelle session, et refaites une demande plus précise, qui dit clairement ce que vous ne voulez pas. Repartir de zéro coûte souvent moins cher que de raccommoder un mauvais départ.

*[fin du bloc]*

*[+] Bloc optionnel*

Si votre fonctionnalité utilise une bibliothèque, c'est aussi le bon moment pour faire intervenir Context7. Par exemple, si on voulait valider les paramètres avec une bibliothèque de validation, on ajouterait « use context7 » à la demande de plan. L'agent irait chercher la documentation de la version installée dans le projet, et son plan s'appuierait sur la bonne façon de faire, pas sur un souvenir d'entraînement. Ici, on n'en a pas besoin : on reste sur du code simple, sans nouvelle dépendance. Et c'est une bonne règle en général : moins l'agent ajoute de dépendances, moins vous aurez de choses à vérifier, à mettre à jour, et à surveiller plus tard.

*[fin du bloc]*

## 4. Passer en mode Build

*À l'écran : on appuie sur Tabulation pour passer en Build, et on demande d'appliquer le plan. Les demandes d'autorisation apparaissent ; on les lit et on accepte.*

Le plan me convient. Je repasse sur l'agent Build avec Tabulation, et je lui dis simplement : « applique ce plan ». Il garde toute la conversation, donc il sait exactement ce qui a été décidé.

Comme on a réglé les permissions sur « demander », il me montre chaque modification avant de la faire. Je les lis au fur et à mesure.

*Commentaire d'exemple, à adapter à ce que l'agent fait vraiment :*

Il commence par le contrôleur, où il ajoute la lecture des deux paramètres et leur vérification. Je lis le changement proposé, il correspond au plan, j'accepte. Il passe ensuite à la couche de données. Puis il ajoute les tests, et il me demande l'autorisation de les lancer. Un test échoue : celui de la limite maximale. Il lit l'erreur, il s'aperçoit qu'il a oublié d'appliquer cette limite, il corrige, et il relance. Cette fois, tout passe.

Vous voyez la boucle de la vidéo 4 en action : il lance, il lit l'erreur, il corrige, il relance. Sans que j'aie eu à copier le moindre message d'erreur.

Et lire les demandes d'autorisation, ce n'est pas juste cliquer sur « oui ». Si l'agent me demandait d'installer une nouvelle bibliothèque pour gérer la pagination, je refuserais. Ce n'était pas dans le plan, et on n'en a pas besoin pour quelques lignes de calcul. Je lui dirais pourquoi, et il continuerait sans. Une demande d'autorisation, c'est le moment où vous pouvez encore dire non, avant que le changement soit fait.

## 5. Relire le résultat

*À l'écran : dans un terminal à côté, git diff ; on fait défiler les changements.*

L'agent a terminé. Mais nous, on n'a pas terminé. Maintenant, on relit. Et pour ça, rien de mieux que git : la commande git diff me montre toutes les lignes qui ont changé dans le projet.

*Relire réellement le diff, en survolant : ce qui a été ajouté dans la route, dans l'accès aux données, dans les tests.*

*Commentaire d'exemple, à adapter au diff réel :*

Dans le contrôleur, on voit la lecture de page et de limit, avec leurs valeurs par défaut, et le renvoi d'une erreur si elles ne sont pas valides. Dans la couche de données, une fonction qui ne renvoie plus que les articles de la page demandée. Et dans les tests, les cas qu'on avait listés dans le plan, y compris les valeurs négatives. Rien d'autre n'a bougé.

Relire le code de l'agent, ce n'est pas une option. C'est votre travail. Vous êtes responsable de ce code, exactement comme si vous l'aviez écrit. Il y a d'ailleurs un piège connu : on a tendance à relire le code généré plus vite qu'un code écrit par un collègue, parce qu'il a l'air propre. Restez discipliné.

*À l'écran : on lance les tests soi-même, puis on fait un vrai appel à l'API avec page=2 et limit=5.*

Je relance les tests moi-même, et je fais un vrai appel à l'API, en demandant la deuxième page avec cinq articles. J'obtiens bien les articles six à dix. Et si je demande la page moins trois, j'ai mon erreur claire.

*[+] Bloc optionnel*

*À l'écran : on demande à l'agent de mettre à jour le README ; la nouvelle section s'affiche.*

Une fonctionnalité n'est pas finie tant qu'elle n'est pas documentée. Et c'est une tâche qu'on a tous tendance à repousser. Je demande donc à l'agent : « mets à jour le README pour décrire les paramètres page et limit, avec leurs valeurs par défaut et un exemple d'appel ». En quelques secondes, il ajoute une section. Je la relis, comme le code. Une documentation fausse est pire que pas de documentation du tout.

*[fin du bloc]*

*[+] Bloc optionnel*

Pendant la relecture, posez-vous toujours les mêmes questions. Est-ce que le code fait ce que j'ai demandé, ni plus ni moins ? Est-ce qu'il a modifié un fichier qui n'avait rien à voir ? Est-ce qu'il a ajouté une dépendance ? Et est-ce que les tests vérifient vraiment quelque chose ? Un agent peut écrire des tests qui ont l'air sérieux mais qui passent quoi qu'il arrive. Si un test ne vous semble pas solide, demandez-lui de le renforcer.

*[fin du bloc]*

## 6. Valider avec un commit

*À l'écran : git add, git commit avec un message clair.*

Dernière étape : on valide avec un commit, avec un message clair. Comme ça, on a un point de retour propre avant la suite. Le message doit dire ce qui a changé, pas qui l'a fait : « ajoute la pagination sur la liste des articles », par exemple. Pour la personne qui lira l'historique dans six mois, peu importe que ce soit l'agent ou vous qui ayez tapé le code. Ce qui compte, c'est que quelqu'un l'a relu et l'assume.

Et si on regarde ce qu'on a fait, à chaque étape, on a gardé la main. Le mode Plan pour réfléchir. La correction du plan pour les cas limites. Les autorisations pour voir chaque action. La relecture et les tests pour valider. L'agent a fait le travail mécanique, et nous, les décisions.

*[+] Bloc optionnel*

*À l'écran : dans un terminal, opencode stats.*

Par curiosité, regardons ce que cette fonctionnalité a consommé. La commande opencode stats affiche des statistiques sur l'utilisation.

*Commenter les chiffres réels affichés, sans les arrondir de façon trompeuse.*

C'est une bonne habitude au début : regarder ce que coûte chaque tâche. Vous verrez vite que l'exploration et les allers-retours sur le plan pèsent lourd. Et que les demandes précises coûtent moins cher que les vagues, parce que l'agent fait moins de tours de boucle.

*[fin du bloc]*

## 7. Conclusion et transition

*À l'écran : récapitulatif en quatre étapes : planifier, corriger, construire, relire.*

Retenez cette méthode : planifier en mode Plan, corriger le plan, construire en mode Build, puis relire et valider avec git. Elle marche pour presque toutes les tâches.

Mais même avec une bonne méthode, il reste des bugs. Dans la prochaine vidéo, on en corrige un, sur ce même projet. Et on verra à quel point la façon de le décrire à l'agent change tout.
