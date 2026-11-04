# Vidéo 9 : Installer et configurer Open Code (démo)

Partie du plan : P5.1 « Installer et configurer Open Code ».
Bornes : 6:10 – 6:55 (min = quelqu'un de rapide qui lit tout, blocs [+] compris ; max = quelqu'un de posé qui ne lit que le texte principal).
Les lignes en italique décrivent l'écran ou donnent une consigne : elles ne se lisent pas.
Enregistrer tout, y compris les blocs [+]. Au montage, les blocs [+] sont gardés un par un tant que la vidéo reste sous sa borne max.
Sources : opencode.ai/docs (intro, cli, tui, config, providers, mcp-servers, permissions), lues le 01/11/2026.

*Vidéo en capture d'écran, avec la voix par-dessus. Toutes les attentes (téléchargement, installation, agent qui travaille) sont coupées ou accélérées à quelques secondes au montage : la durée de la vidéo, c'est la voix. Les passages qui commentent l'écran sont écrits comme exemple : les adapter à ce qui s'affiche vraiment, en gardant à peu près la même longueur.*

*Avant de tourner :*
*- Ouvrir opencode.ai/docs la veille et revérifier chaque commande. La doc parle d'Open Code 1 et d'Open Code 2, qui utilisent la même commande « opencode » et ne s'installent pas côte à côte. Ce script suit la page d'installation d'Open Code 1. Si vous filmez Open Code 2, adapter les commandes.*
*- Sur Windows, la doc recommande WSL : filmer de préférence sous Linux, macOS ou WSL.*
*- Préparer une clé d'API d'un fournisseur (avec un plafond de dépense réglé), ou Ollama déjà installé avec un modèle téléchargé.*
*- Préparer le projet de démo (le même que pour les vidéos 10 à 14), déjà initialisé avec git.*
*- Ne jamais montrer une vraie clé à l'écran : la flouter au montage, puis la révoquer après le tournage.*

## 1. Intro

*À l'écran : le titre, puis un terminal vide.*

Après toute cette théorie, on passe à la pratique. Dans cette vidéo, on installe Open Code, on le connecte à un modèle, et on le configure proprement pour un projet. À la fin, vous aurez un agent prêt à travailler, avec des règles de sécurité raisonnables, et Context7 branché. Faites les manipulations en même temps que moi, et mettez la vidéo en pause autant que nécessaire.

## 2. Les prérequis

*À l'écran : la section « Prerequisites » de la doc officielle, puis une liste de trois points.*

Avant d'installer, trois choses. D'abord, un terminal récent : l'interface d'Open Code est assez riche, et la documentation recommande des terminaux modernes. Ensuite, si vous êtes sur Windows, la documentation conseille d'utiliser WSL, le sous-système Linux de Windows. Et enfin, il vous faut un modèle : soit une clé d'API chez un fournisseur, soit un modèle local, par exemple avec Ollama.

## 3. L'installation

*À l'écran : on tape la commande d'installation par script ; l'installation défile en accéléré.*

*Commande : curl -fsSL https://opencode.ai/install | bash*

La méthode la plus simple d'après la documentation, c'est le script officiel. On le télécharge avec curl et on l'exécute.

Petite remarque au passage : cette commande télécharge un script et l'exécute directement. C'est pratique, mais c'est exactement le genre de commande dont il faut se méfier en général. Ici, on la prend depuis le site officiel, donc on sait d'où elle vient. Mais retenez le réflexe : on ne lance jamais ce genre de commande depuis une source qu'on ne connaît pas. Et encore moins quand c'est un agent qui vous la propose.

*À l'écran : la variante npm, puis opencode --version et son résultat.*

*Commande : npm install -g opencode-ai*

Si vous préférez npm, le paquet s'appelle opencode tiret ai, et on l'installe en global. Une fois installé, on vérifie que la commande répond, en demandant la version.

*[+] Bloc optionnel*

La documentation liste aussi d'autres méthodes : Homebrew sur macOS et Linux, des gestionnaires de paquets sous Windows, ou une image Docker. Et un point à savoir : elle mentionne deux versions majeures, Open Code 1 et Open Code 2. Elles utilisent la même commande, et on ne peut pas avoir les deux installées en même temps avec leur nom par défaut. L'important, c'est de lire la documentation qui correspond à la version que vous avez. Les principes restent les mêmes, mais certaines commandes peuvent changer.

*[fin du bloc]*

## 4. Premier lancement et connexion d'un fournisseur

*À l'écran : cd dans le projet de démo, puis « opencode ». L'interface s'ouvre.*

On se place dans le dossier d'un projet, parce qu'Open Code travaille toujours sur le dossier dans lequel on le lance. Et on tape simplement : opencode. Voilà l'interface. On la détaillera dans la prochaine vidéo. Pour l'instant, il manque l'essentiel : un modèle.

*À l'écran : on tape /connect, la liste des fournisseurs s'affiche, on en choisit un, on colle la clé (floutée).*

Pour connecter un fournisseur, on tape barre oblique connect. Open Code affiche la liste des fournisseurs. On choisit le sien, et on colle la clé d'API. On peut faire la même chose depuis le terminal avec opencode auth login, et opencode auth list affiche les fournisseurs déjà connectés.

*À l'écran : le chemin du fichier où sont rangées les clés.*

Les clés sont rangées dans un fichier de votre dossier utilisateur, en dehors du projet. Et c'est voulu. Une clé d'API, c'est de l'argent : quelqu'un qui la récupère consomme sur votre compte. Elle ne doit jamais se retrouver dans le dépôt git, ni dans une capture d'écran. Open Code sait aussi lire les clés depuis les variables d'environnement, ou depuis un fichier .env dans le projet. Si vous faites ça, vérifiez bien que ce fichier .env est dans votre .gitignore. Sinon, votre clé partira avec le prochain commit.

*[+] Bloc optionnel*

Et un réflexe à prendre dès maintenant : allez dans le tableau de bord de votre fournisseur et fixez une limite de dépense. La plupart des fournisseurs le proposent. Si un agent part en boucle, ou si votre clé fuite malgré tout, la facture ne pourra pas dépasser un montant que vous avez choisi. Ça prend deux minutes.

*[fin du bloc]*

## 5. Choisir un modèle

*À l'écran : /models, la liste des modèles, on en sélectionne un. Son nom apparaît dans la barre d'état.*

Une fois le fournisseur connecté, on choisit le modèle avec barre oblique models. La liste affiche tous les modèles disponibles chez les fournisseurs connectés. On en sélectionne un, et on peut en changer à tout moment, même au milieu d'une session.

## 6. Le fichier de configuration

*À l'écran : on crée opencode.json à la racine du projet, et on le remplit au fur et à mesure.*

Maintenant, on configure le projet, dans un fichier opencode.json, à la racine.

*À l'écran : la ligne $schema, puis la clé « model ».*

On commence par une ligne qui indique le schéma officiel. Elle permet à votre éditeur de proposer l'autocomplétion et de signaler les erreurs. On peut ensuite fixer le modèle par défaut du projet, avec le nom du fournisseur, une barre oblique, et le nom du modèle. La commande opencode models, dans le terminal, liste les noms exacts.

*À l'écran : le bloc « permission » avec bash et edit sur « ask ».*

Ensuite, le plus important : les permissions. Par défaut, Open Code autorise la plupart des actions sans rien demander, y compris lancer des commandes. Pour un premier projet, je vous conseille de passer les commandes et les modifications de fichiers en mode « ask ». L'agent devra vous demander avant chaque commande et chaque modification. C'est un peu plus lent, mais vous voyez tout ce qu'il fait. Et c'est la meilleure façon d'apprendre comment il travaille : quelles commandes il lance, dans quel ordre, et pourquoi. Au bout de quelques sessions, vous saurez ce qui est normal, et donc repérer ce qui ne l'est pas. Une fois à l'aise, vous pourrez assouplir, par exemple en autorisant les commandes git tout en refusant les suppressions.

*À l'écran : le bloc « mcp » avec context7, type remote, et son adresse.*

Et enfin, on branche Context7, le serveur MCP de la vidéo 6. Un bloc mcp, avec un nom, le type « remote » parce que le serveur est distant, et son adresse. On enregistre, et on relance Open Code pour qu'il prenne en compte la configuration.

*[+] Bloc optionnel*

*À l'écran : le chemin du fichier de configuration global, dans le dossier utilisateur.*

Ce fichier est propre au projet. Mais il existe aussi un fichier global, dans votre dossier utilisateur, qui s'applique à tous vos projets. Les deux se combinent, et celui du projet l'emporte en cas de conflit. En pratique, on met dans le global ce qui nous concerne nous, comme notre modèle préféré. Et dans le projet, ce qui concerne toute l'équipe, comme les serveurs MCP utiles. Ce fichier de projet peut être partagé dans git, puisqu'il ne contient aucune clé.

*[fin du bloc]*

## 7. Le fichier AGENTS.md avec /init

*À l'écran : on tape /init. L'agent explore le projet, en accéléré. Puis on ouvre le fichier AGENTS.md généré.*

Dernière étape : la mémoire du projet. On tape barre oblique init.

*Commentaire d'exemple, à adapter à ce que l'agent fait vraiment :*

Vous le voyez parcourir le projet : il ouvre le package.json pour trouver les commandes, il regarde comment les dossiers sont organisés, il jette un œil aux tests.

L'agent crée un fichier AGENTS.md à la racine. On y trouve en général une description du projet, les commandes pour l'installer et lancer les tests, et les conventions qu'il a repérées. Ce fichier, relisez-le. L'agent a pu se tromper ou rater une information. Corrigez, et ajoutez ce qu'il ne pouvait pas deviner : les pièges du projet, ce qu'il ne faut jamais toucher. Puis, comme le conseille la documentation, ajoutez-le au dépôt git.

*[+] Bloc optionnel*

Un bon AGENTS.md n'a pas besoin d'être long. Quelques lignes suffisent : comment installer le projet, comment lancer les tests, les conventions de nommage, l'organisation des dossiers, et les pièges connus. Par exemple : « ne jamais modifier le dossier des migrations à la main ». En gros, tout ce que vous diriez à un nouveau développeur le premier jour. Comme ce fichier est relu à chaque session, l'agent part toujours avec ces informations.

*[fin du bloc]*

## 8. Un premier test

*À l'écran : on passe en mode Plan avec Tabulation, puis on tape la demande. La réponse s'affiche.*

On vérifie que tout fonctionne avec une demande sans risque. Je passe en mode Plan avec la touche Tabulation, pour que l'agent ne modifie rien, et je demande : « en trois phrases, à quoi sert ce projet, et comment on lance les tests ? »

*Commentaire d'exemple, à adapter à la réponse réelle :*

La réponse est juste, et on reconnaît la commande de test qu'il a notée dans AGENTS.md. Le fournisseur est connecté, le modèle répond, et l'agent arrive à lire le projet.

Si vous avez une erreur à ce stade, c'est presque toujours un problème de clé ou de nom de modèle. Revérifiez avec opencode auth list et opencode models.

*[+] Bloc optionnel*

Pour tester Context7, posez une question sur une bibliothèque du projet, en ajoutant « use context7 » à la fin. Si tout est bien branché, vous verrez passer un appel vers Context7 dans le fil de la conversation, avant la réponse.

*[fin du bloc]*

## 9. Variante : un modèle local avec Ollama

*À l'écran : un bloc « provider » pour Ollama dans opencode.json, avec l'adresse locale. Vérifier l'exemple exact dans la doc, page Providers, section Ollama.*

Si vous préférez ne rien envoyer à l'extérieur, vous pouvez utiliser un modèle local. Avec Ollama installé et un modèle téléchargé, on ajoute dans la configuration un fournisseur qui pointe vers l'adresse locale d'Ollama. Gardez en tête qu'un modèle local est souvent moins à l'aise pour enchaîner des actions. La documentation précise d'ailleurs que si les appels d'outils échouent avec Ollama, il faut augmenter la taille de contexte du modèle.

*[+] Bloc optionnel*

Pour savoir si votre machine peut suivre, testez sur une petite tâche avant de vous lancer sur un vrai projet. Demandez par exemple à l'agent d'expliquer un seul fichier, puis de faire une petite modification. Si chaque réponse prend plusieurs minutes, ou si l'agent n'arrive pas à utiliser ses outils correctement, passez par un fournisseur dans le cloud pour les tâches lourdes, et gardez le modèle local pour les questions simples.

*[fin du bloc]*

## 10. Conclusion et transition

*À l'écran : le projet avec ses deux nouveaux fichiers : opencode.json et AGENTS.md.*

Récapitulons. On a installé Open Code, connecté un fournisseur, choisi un modèle, et créé une configuration de projet avec des permissions prudentes et Context7 branché. Et on a généré un fichier AGENTS.md, qu'on a relu et ajouté au dépôt.

Dans la prochaine vidéo, on fait le tour de l'interface : écrire une demande, désigner des fichiers, passer en mode plan, gérer ses sessions, et revenir en arrière quand l'agent s'est trompé.
