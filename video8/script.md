# Vidéo 8 : Installer et configurer Open Code (démo)

Durée visée : 9 min. Vidéo en capture d'écran avec la voix par-dessus. Les lignes en italique décrivent l'écran ou donnent une consigne : elles ne se lisent pas.
Enregistrer tout, y compris les blocs [+]. Au montage, les blocs [+] sont gardés seulement si la vidéo reste sous 9 min 30.
Sources : opencode.ai/docs (intro, cli, tui, config, providers, mcp-servers, permissions), lues le 01/11/2026.

*Écran sans voix : environ 60 s (installation, /init, réponses de l'agent), accéléré au montage.*

*Avant de tourner :*
*- Ouvrir opencode.ai/docs la veille et revérifier chaque commande. La doc parle d'Open Code 1 et d'Open Code 2, qui utilisent la même commande « opencode » et ne s'installent pas côte à côte. Ce script suit la page d'installation d'Open Code 1. Si vous filmez Open Code 2, adapter les commandes.*
*- Sur Windows, la doc recommande WSL : filmer de préférence sous Linux, macOS ou WSL.*
*- Préparer une clé d'API d'un fournisseur (avec un plafond de dépense réglé), ou Ollama déjà installé avec un modèle téléchargé.*
*- Préparer le projet de démo (le même que pour les vidéos 10 et 11), déjà initialisé avec git.*
*- Ne jamais montrer une vraie clé à l'écran : la flouter au montage, puis la révoquer après le tournage.*

## 1. Intro

*À l'écran : le titre, puis un terminal vide.*

Après toute cette théorie, on passe enfin à la pratique. Dans cette vidéo, on installe Open Code, on le connecte à un modèle, et on le configure proprement pour un projet. À la fin, vous aurez un agent prêt à travailler, avec des règles de sécurité raisonnables, et Context7 branché.

Je vous conseille de faire les manipulations en même temps que moi. Mettez la vidéo en pause autant que nécessaire.

## 2. Les prérequis

*À l'écran : la section « Prerequisites » de la doc officielle, puis une liste de trois points.*

Avant d'installer, trois choses à vérifier.

D'abord, un terminal récent. Open Code a une interface assez riche, avec des couleurs et des panneaux, et la documentation recommande des terminaux modernes, comme WezTerm, Alacritty, Ghostty ou Kitty. Le terminal de base de votre système peut marcher, mais l'affichage sera parfois moins propre.

Ensuite, si vous êtes sur Windows, la documentation recommande d'utiliser WSL, le sous-système Linux de Windows, pour avoir la meilleure expérience. Ça fonctionne aussi directement sous Windows, mais c'est moins confortable.

Et enfin, il vous faut un modèle. Soit une clé d'API chez un fournisseur, soit un modèle local, par exemple avec Ollama. On verra les deux.

## 3. L'installation

*À l'écran : on tape la commande d'installation par script, puis l'installation défile. Couper ou accélérer l'attente au montage.*

Pour installer, la méthode la plus simple d'après la documentation, c'est le script officiel. On le télécharge avec curl et on l'exécute.

*Commande : curl -fsSL https://opencode.ai/install | bash*

Petite remarque au passage : cette commande télécharge un script et l'exécute directement. C'est pratique, mais c'est exactement le genre de commande dont il faut se méfier en général. Ici, on la prend depuis le site officiel, donc on sait d'où elle vient. Mais retenez le réflexe : on ne lance jamais ce genre de commande depuis une source qu'on ne connaît pas. Et encore moins quand c'est un agent qui vous la propose.

*À l'écran : la variante npm.*

Si vous préférez passer par npm, c'est possible aussi. Le paquet s'appelle opencode tiret ai, et on l'installe en global.

*Commande : npm install -g opencode-ai*

La documentation liste aussi d'autres méthodes : Homebrew sur macOS et Linux, des gestionnaires de paquets sous Windows, ou une image Docker. Choisissez celle qui correspond à votre système.

*À l'écran : opencode --version, puis le résultat.*

Une fois installé, on vérifie que la commande répond, en demandant la version.

*[+] Bloc optionnel*

Un point à savoir : la documentation mentionne deux versions majeures, Open Code 1 et Open Code 2. Elles utilisent la même commande, opencode, et on ne peut pas avoir les deux installées en même temps avec leur nom par défaut. Selon la méthode d'installation, vous n'aurez pas forcément la même version. Pour suivre ce cours, l'important, c'est de regarder la documentation qui correspond à la version que vous avez installée. Les grands principes restent les mêmes, mais certaines commandes peuvent changer.

*[fin du bloc]*

## 4. Premier lancement

*À l'écran : cd dans le projet de démo, puis « opencode ». L'interface s'ouvre.*

Maintenant, on se place dans le dossier d'un projet. Open Code travaille toujours sur le dossier dans lequel on le lance. Et on tape simplement : opencode.

*À l'écran : l'interface vide, avec la zone de saisie en bas.*

Et voilà l'interface. On la détaillera dans la prochaine vidéo. Pour l'instant, il manque l'essentiel : un modèle. Sans modèle, l'agent n'a pas de cerveau.

## 5. Connecter un fournisseur

*À l'écran : on tape /connect, la liste des fournisseurs s'affiche, on en choisit un, on colle la clé (floutée).*

Pour connecter un fournisseur, on utilise la commande connect, directement dans l'interface. On tape barre oblique connect. Open Code affiche la liste des fournisseurs disponibles. On choisit le sien, et on colle la clé d'API.

*À l'écran : un second terminal, la commande opencode auth login.*

On peut aussi faire la même chose depuis le terminal, sans ouvrir l'interface, avec la commande opencode auth login. Et opencode auth list affiche les fournisseurs déjà connectés.

*À l'écran : le chemin du fichier où sont rangées les clés.*

Les clés sont rangées dans un fichier de votre dossier utilisateur, en dehors du projet. Et c'est voulu. Une clé d'API, c'est de l'argent. Quelqu'un qui la récupère peut consommer sur votre compte. Donc elle ne doit jamais se retrouver dans le dépôt git du projet, ni dans une capture d'écran, ni dans un message à un collègue.

Open Code peut aussi lire les clés depuis les variables d'environnement, ou depuis un fichier .env dans le projet. Si vous faites ça, vérifiez bien que ce fichier .env est dans votre .gitignore.

*[+] Bloc optionnel*

Et pendant qu'on parle de clés, un réflexe à prendre dès maintenant : allez dans le tableau de bord de votre fournisseur et fixez une limite de dépense. La plupart des fournisseurs le proposent. Comme ça, si un agent part en boucle, ou si votre clé fuite malgré tout, la facture ne peut pas dépasser un montant que vous avez choisi. Ça prend deux minutes, et ça peut vous éviter une très mauvaise surprise.

*[fin du bloc]*

## 6. Choisir un modèle

*À l'écran : /models, la liste des modèles, on en sélectionne un. Le nom du modèle apparaît dans la barre d'état.*

Une fois le fournisseur connecté, on choisit le modèle avec la commande models. La liste affiche tous les modèles disponibles chez les fournisseurs connectés. On en sélectionne un, et c'est lui qui sera utilisé pour la suite.

On peut en changer à tout moment, même au milieu d'une session. C'est pratique pour utiliser un modèle léger pour explorer, et un modèle plus costaud pour coder.

## 7. Le fichier de configuration

*À l'écran : on crée opencode.json à la racine du projet, et on le remplit au fur et à mesure qu'on en parle.*

Maintenant, on va configurer le projet. Ça se passe dans un fichier opencode.json, à la racine.

*À l'écran : la ligne $schema.*

On commence par une ligne qui indique le schéma officiel. Elle ne change rien au fonctionnement, mais elle permet à votre éditeur de proposer l'autocomplétion et de signaler les erreurs dans le fichier.

*À l'écran : la clé « model », au format fournisseur/modèle.*

On peut fixer le modèle par défaut pour ce projet, avec le nom du fournisseur, une barre oblique, et le nom du modèle. La commande opencode models, dans le terminal, liste les noms exacts.

*À l'écran : le bloc « permission » avec bash et edit sur « ask ».*

Ensuite, et c'est le plus important, les permissions. On l'a dit dans la vidéo précédente : par défaut, Open Code autorise la plupart des actions sans rien demander, y compris lancer des commandes. Pour un premier projet, je vous conseille de passer les commandes et les modifications de fichiers en mode « ask ». L'agent devra vous demander avant chaque commande et chaque modification. C'est un peu plus lent, mais vous voyez tout ce qu'il fait, et vous apprenez comment il travaille.

Une fois que vous serez à l'aise, vous pourrez assouplir. La documentation montre par exemple comment autoriser automatiquement les commandes git ou npm, tout en refusant les commandes de suppression.

*À l'écran : le bloc « mcp » avec context7, type remote, et son adresse.*

Et enfin, on branche Context7, le serveur MCP qu'on a vu dans la vidéo 5. Un bloc mcp, avec un nom, le type « remote » parce que le serveur est distant, et son adresse. C'est tout. À partir de maintenant, quand vous ajouterez « use context7 » dans une demande, l'agent pourra aller chercher une documentation à jour.

*À l'écran : on relance opencode pour prendre en compte la configuration.*

On enregistre, et on relance Open Code pour qu'il prenne en compte la configuration.

*[+] Bloc optionnel*

*À l'écran : le chemin du fichier de configuration global, dans le dossier utilisateur.*

Ce fichier opencode.json est propre au projet. Mais il existe aussi un fichier de configuration global, dans votre dossier utilisateur, qui s'applique à tous vos projets. Les deux se combinent : le fichier du projet complète le fichier global, et prend le dessus en cas de conflit. En pratique, on met dans le global ce qui nous concerne nous, comme notre modèle préféré ou nos permissions habituelles. Et dans le projet, ce qui concerne toute l'équipe, comme les serveurs MCP utiles au projet. Et ce fichier de projet, on peut le partager dans git, puisqu'il ne contient aucune clé.

*[fin du bloc]*

## 8. Le fichier AGENTS.md avec /init

*À l'écran : on tape /init. L'agent explore le projet. Accélérer au montage. Puis on ouvre le fichier AGENTS.md généré.*

Dernière étape : on va donner à l'agent sa mémoire de projet. On tape barre oblique init.

*Pendant que l'agent travaille, commenter ce qu'on voit réellement passer à l'écran : les fichiers qu'il lit, les recherches qu'il fait. Prévoir environ 20 secondes.*

L'agent analyse le projet et crée un fichier AGENTS.md à la racine. Regardons ce qu'il a écrit. On y trouve en général une description du projet, les commandes pour l'installer et lancer les tests, et les conventions qu'il a repérées dans le code.

Ce fichier, relisez-le. L'agent a pu se tromper, ou rater une information importante. Corrigez ce qui ne va pas, et ajoutez ce que lui ne pouvait pas deviner : les pièges du projet, ce qu'il ne faut jamais toucher. Puis, comme le conseille la documentation, ajoutez-le au dépôt git, pour que toute l'équipe en profite.

## 9. Un premier test

*À l'écran : on passe en mode Plan avec Tabulation, puis on tape la demande. Montrer la réponse réelle de l'agent, accélérée si elle est longue.*

Avant d'aller plus loin, on vérifie que tout fonctionne avec une demande simple et sans risque. Je passe en mode Plan avec la touche Tabulation, pour que l'agent ne modifie rien. Et je lui demande : « en trois phrases, à quoi sert ce projet, et comment on lance les tests ? »

*Commenter brièvement la réponse réelle : est-ce qu'elle est juste ? Est-ce qu'elle reprend des informations du fichier AGENTS.md ? Prévoir environ 15 secondes.*

Si l'agent répond correctement, c'est que tout est en place : le fournisseur est connecté, le modèle répond, et l'agent arrive à lire le projet. Si vous avez une erreur à ce stade, c'est presque toujours un problème de clé ou de nom de modèle. Revérifiez la connexion avec opencode auth list, et le nom exact du modèle avec opencode models.

Et pour tester Context7, on peut lui poser une question sur une bibliothèque du projet, en ajoutant « use context7 » à la fin. Si tout est bien branché, vous verrez passer un appel vers Context7 dans le fil de la conversation, avant la réponse.

## 10. Variante : un modèle local avec Ollama

*À l'écran : un bloc « provider » pour Ollama dans opencode.json, avec l'adresse locale. Vérifier l'exemple exact dans la doc, page Providers, section Ollama.*

Si vous préférez ne rien envoyer à l'extérieur, vous pouvez utiliser un modèle local. Avec Ollama installé et un modèle téléchargé, on ajoute dans la configuration un fournisseur qui pointe vers l'adresse locale d'Ollama. Open Code lui parle comme à n'importe quel autre fournisseur.

Gardez en tête ce qu'on a dit dans la vidéo précédente : un modèle local est souvent moins à l'aise pour enchaîner des actions qu'un gros modèle dans le cloud. La documentation précise d'ailleurs que si les appels d'outils échouent avec Ollama, il faut augmenter la taille de contexte du modèle.

*[+] Bloc optionnel*

Et pour savoir si votre machine peut suivre, testez sur une petite tâche avant de vous lancer sur un vrai projet. Demandez par exemple à l'agent d'expliquer un seul fichier, puis de faire une petite modification. Si chaque réponse prend plusieurs minutes, ou si l'agent n'arrive pas à utiliser ses outils correctement, il vaut mieux passer par un fournisseur dans le cloud pour les tâches lourdes, et garder le modèle local pour les questions simples.

*[fin du bloc]*

## 11. Conclusion et transition

*À l'écran : le projet avec ses deux nouveaux fichiers : opencode.json et AGENTS.md.*

Récapitulons. On a installé Open Code, connecté un fournisseur, choisi un modèle, et créé une configuration de projet avec des permissions plus prudentes et Context7 branché. Et on a généré un fichier AGENTS.md, qu'on a relu et ajouté au dépôt.

Notre agent est prêt. Dans la prochaine vidéo, on fait le tour de l'interface : comment écrire une demande, désigner des fichiers, passer en mode plan, gérer ses sessions et revenir en arrière quand l'agent s'est trompé.
