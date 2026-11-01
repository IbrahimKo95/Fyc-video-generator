# Vidéo 10 : Cas pratique 1, comprendre un projet et ajouter une fonctionnalité (démo)

Durée visée : 10 min (dont environ 1 min 30 d'écran où l'agent travaille, accéléré au montage). Les lignes en italique décrivent l'écran ou donnent une consigne : elles ne se lisent pas.
Enregistrer tout, y compris les blocs [+]. Au montage, les blocs [+] sont gardés seulement si la vidéo reste sous 9 min 30 de voix.

*Écran sans voix : environ 60 s (agent qui travaille, accéléré au montage).*

*Préparation (à faire avant le tournage) :*
*- Projet de démo proposé, à valider par le groupe : une petite API Node.js/Express qui gère des articles (route GET /articles qui renvoie toute la liste), avec quelques tests automatisés. Taille modeste, que tout le monde comprend.*
*- Le même projet sert aux vidéos 8, 9 et 11. Dépôt git propre, avec un commit avant chaque partie pour pouvoir rejouer la démo.*
*- Tester les demandes la veille avec le modèle choisi. L'agent ne fait jamais exactement deux fois la même chose : garder la meilleure prise.*
*- Pendant le tournage, ne pas lire mot pour mot les passages qui commentent l'écran : décrire ce que l'agent fait vraiment. Les passages en italique « Commenter… » indiquent où et combien de temps.*

## 1. Intro

*À l'écran : le dossier du projet de démo dans le terminal.*

On passe au premier cas pratique. Le scénario est simple, et vous le vivrez forcément en entreprise : vous arrivez sur un projet que vous ne connaissez pas, et on vous demande d'y ajouter une fonctionnalité.

On va le faire en deux temps. D'abord, on va demander à l'agent de nous expliquer le projet, sans rien toucher. Ensuite, on lui fera ajouter la fonctionnalité, en commençant par un plan qu'on validera avant qu'il écrive la moindre ligne.

Le projet, c'est une petite API qui gère des articles. Et la fonctionnalité qu'on va ajouter, c'est celle dont on parlait dans la vidéo 2 : la pagination sur la liste des articles.

## 2. Partie 1 : comprendre le projet

*À l'écran : on lance opencode, on passe en mode Plan avec Tabulation, l'indicateur change.*

On lance Open Code dans le dossier du projet. Et avant d'écrire quoi que ce soit, je passe en mode Plan avec la touche Tabulation. On veut seulement comprendre, donc l'agent n'a aucune raison de modifier un fichier. En mode Plan, on est tranquille.

*À l'écran : on tape la demande, puis on l'envoie.*

Je lui demande : « Explique-moi l'architecture de ce projet : les dossiers principaux, le chemin d'une requête HTTP depuis son arrivée jusqu'à la réponse, et par où commencer pour ajouter une fonctionnalité. »

*À l'écran : l'agent travaille. Accélérer au montage, mais laisser voir les fichiers qu'il ouvre.*

Regardez ce qu'il fait pendant qu'il travaille. Il ne répond pas tout de suite. Il explore.

*Commenter ce que l'agent fait réellement : quels fichiers il ouvre en premier (souvent le package.json, puis le point d'entrée), s'il fait des recherches dans le code, s'il suit les imports. Prévoir environ 30 secondes.*

C'est exactement la démarche qu'aurait un développeur expérimenté le premier jour sur un projet : regarder les dépendances, trouver le point d'entrée, suivre le chemin du code. Sauf qu'ici, ça prend une minute.

## 3. Lire la réponse, et la vérifier

*À l'écran : la réponse de l'agent. Faire défiler lentement.*

Voici sa réponse.

*Commenter la réponse réelle : les dossiers qu'il décrit, le chemin d'une requête. Prévoir environ 30 secondes.*

C'est clair, et c'est un très bon point de départ. Mais attention, on a dit dans la vidéo 1 qu'un LLM produit du texte qui a l'air juste, pas du texte vérifié. Une explication de projet, c'est pareil. L'agent peut décrire avec assurance un fonctionnement qui n'est pas tout à fait celui du code.

*À l'écran : on ouvre dans l'éditeur un des fichiers cités par l'agent, et on vérifie une de ses affirmations.*

Donc on vérifie. Je prends une de ses affirmations, et j'ouvre le fichier qu'il cite pour voir si c'est vrai.

*Dire ce qu'on constate réellement : l'affirmation est juste, ou il y a une approximation. Si l'agent s'est trompé, c'est un excellent moment à garder : le montrer clairement.*

Prenez cette habitude : ouvrir un ou deux fichiers cités pour contrôler. Ça prend trente secondes, et ça vous évite de construire sur une base fausse.

*À l'écran : une question de suivi.*

On peut ensuite poser des questions plus ciblées. Par exemple : « où sont lus les articles depuis la base de données ? » L'agent garde le contexte de la conversation, donc il repart de ce qu'il a déjà exploré.

*[+] Bloc optionnel*

Remarquez qu'à aucun moment on n'a modifié quoi que ce soit. Rien à annuler, rien à valider. Cette première étape d'exploration est sans risque, et elle est très rentable. Même quand vous comptez faire la modification vous-même à la main, demander d'abord à l'agent de vous expliquer le code est souvent un gain de temps énorme. C'est d'ailleurs une des utilisations les plus sous-estimées des agents : pas pour écrire du code, mais pour comprendre celui des autres.

*[fin du bloc]*

## 4. Partie 2 : ajouter la pagination, d'abord un plan

*À l'écran : on reste en mode Plan. On tape la demande.*

Passons à la fonctionnalité. Et on reste en mode Plan pour l'instant. Je lui demande :

« Planifie l'ajout de la pagination sur la route GET /articles, avec deux paramètres dans l'URL : page et limit. Indique les fichiers à modifier et les tests à ajouter. Ne code rien pour l'instant. »

Vous remarquez que la demande est précise. Les noms des paramètres, la route concernée, et ce que j'attends : un plan, avec les fichiers et les tests. C'est ce qu'on a vu dans la vidéo 4 : plus la demande est précise, moins l'agent doit deviner.

*À l'écran : l'agent explore puis présente son plan. Accélérer l'attente.*

*Lire ou résumer le plan réel de l'agent. Prévoir environ 30 secondes.*

## 5. Corriger le plan avant le code

*À l'écran : on écrit une correction au plan, par exemple sur le format de réponse ou les valeurs par défaut.*

Et c'est maintenant qu'on a le plus de pouvoir. Le plan, c'est le moment le moins cher pour corriger le tir. Aucune ligne de code n'a été écrite, donc changer d'avis ne coûte rien.

*Choisir une vraie correction selon le plan obtenu. Exemples possibles : demander une valeur par défaut pour limit, ou une limite maximale, ou que la réponse contienne aussi le nombre total d'articles, ou que la page 0 et les valeurs négatives soient refusées.*

Par exemple ici, je lui demande d'ajouter une valeur par défaut, et de refuser les valeurs absurdes, comme une page négative. Il met son plan à jour.

Imaginez la même correction après coup, une fois le code écrit : il aurait fallu tout reprendre. Prenez l'habitude de ce va-et-vient sur le plan. C'est là que votre expérience de développeur compte le plus.

## 6. Passer en mode Build

*À l'écran : on appuie sur Tabulation pour passer en Build, et on demande d'appliquer le plan. Les demandes d'autorisation apparaissent ; on les lit et on accepte.*

Le plan me convient. Je repasse sur l'agent Build avec Tabulation, et je lui dis simplement : « applique ce plan ».

*À l'écran : l'agent modifie les fichiers et lance les tests. Accélérer, mais montrer chaque demande d'autorisation.*

Comme on a réglé les permissions sur « demander », il me montre chaque modification avant de la faire. Je les lis au fur et à mesure.

*Commenter ce que l'agent fait réellement : quels fichiers il modifie, s'il lance les tests, si un test échoue et qu'il corrige. Prévoir environ 30 secondes.*

Et s'il y a un test qui échoue, vous voyez la boucle de la vidéo 3 en action : il lit l'erreur, il corrige, il relance.

## 7. Relire le résultat

*À l'écran : dans un terminal à côté, git diff ; on fait défiler les changements.*

L'agent a terminé. Mais nous, on n'a pas terminé. Maintenant, on relit. Et pour ça, rien de mieux que git : la commande git diff me montre toutes les lignes qui ont changé dans le projet.

*Relire réellement le diff à voix haute, en survolant : ce qui a été ajouté dans la route, dans l'accès aux données, dans les tests.*

Relire le code de l'agent, ce n'est pas une option. C'est votre travail. Vous êtes responsable de ce code, exactement comme si vous l'aviez écrit. Il y a d'ailleurs un piège connu : on a tendance à relire le code généré plus vite et moins attentivement que celui d'un collègue, parce qu'il a l'air propre. Restez discipliné.

*À l'écran : on lance les tests soi-même, puis on fait un appel à l'API avec page=2.*

Je relance les tests moi-même, et je fais un vrai appel à l'API pour voir le résultat. Tout est bon.

*[+] Bloc optionnel*

Pendant cette relecture, posez-vous toujours les mêmes questions. Est-ce que le code fait vraiment ce que j'ai demandé, ni plus ni moins ? Est-ce qu'il a modifié un fichier qui n'avait rien à voir ? Est-ce qu'il a ajouté une dépendance au projet ? Est-ce que les tests vérifient vraiment quelque chose, ou est-ce qu'ils passent quoi qu'il arrive ? Un agent peut écrire des tests qui ont l'air sérieux mais qui ne testent pas grand-chose. Si un test ne vous semble pas solide, demandez-lui de le renforcer.

*[fin du bloc]*

## 8. Valider avec un commit

*À l'écran : git add, git commit avec un message clair.*

Dernière étape : on valide avec un commit, avec un message clair. Comme ça, on a un point de retour propre avant la suite.

Et si on regarde ce qu'on a fait : on a compris un projet inconnu, puis ajouté une fonctionnalité avec ses tests. Mais surtout, à chaque étape, on a gardé la main. Le mode Plan pour comprendre et pour réfléchir. Les autorisations pour voir chaque action. La relecture pour valider. L'agent a fait le travail mécanique, et nous, les décisions.

*[+] Bloc optionnel*

*À l'écran : dans un terminal, opencode stats.*

Et par curiosité, regardons ce que cette fonctionnalité a coûté. La commande opencode stats affiche des statistiques sur l'utilisation.

*Commenter les chiffres réels affichés, sans les arrondir de façon trompeuse. Prévoir environ 15 secondes.*

C'est une bonne habitude à prendre au début : regarder ce que coûte chaque tâche. Vous allez vite voir que l'exploration du projet et les allers-retours sur le plan comptent pour une bonne part. Et que les demandes précises coûtent moins cher que les demandes vagues, parce que l'agent fait moins de tours de boucle.

*[fin du bloc]*

## 9. Conclusion et transition

*À l'écran : récapitulatif en quatre étapes : comprendre, planifier, construire, relire.*

Retenez cette méthode en quatre étapes : comprendre en mode Plan, planifier en mode Plan, construire en mode Build, puis relire et valider avec git. Elle marche pour presque toutes les tâches.

Dans la prochaine vidéo, on continue sur le même projet avec deux autres situations courantes : corriger un bug, et améliorer un code existant sans casser ce qui marche.
