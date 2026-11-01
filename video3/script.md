# Vidéo 3 : Anatomie d'un agent

Durée visée : 8 min. Les lignes en italique décrivent l'écran ou donnent une consigne : elles ne se lisent pas.
Enregistrer tout, y compris les blocs [+]. Au montage, les blocs [+] sont gardés seulement si la vidéo reste sous 9 min 30.

## 1. Intro

*À l'écran : l'équation « LLM + outils + boucle » de la vidéo 2, puis le titre.*

On a vu dans la vidéo précédente qu'un agent, c'est un LLM, des outils et une boucle. Dit comme ça, ça a l'air simple. Mais quand on regarde de plus près, il y a pas mal de pièces qui travaillent ensemble.

Dans cette vidéo, on ouvre la machine. On va suivre un tour de boucle étape par étape, puis passer en revue les six composants d'un agent. Et à la fin, vous saurez ce qui fait la différence entre un agent qui vous fait gagner une heure et un agent qui vous en fait perdre deux.

## 2. Un tour de boucle

*À l'écran : un cercle avec quatre étapes qui s'allument l'une après l'autre : perception, décision, action, observation.*

Commençons par la boucle elle-même. Un tour, ça se passe en quatre temps.

Premier temps, la perception. Le modèle reçoit tout ce qu'il faut pour décider : les instructions de départ de l'outil, ce qu'on appelle le prompt système, votre demande, l'historique de la conversation, et le résultat de tout ce qu'il a déjà fait avant.

Deuxième temps, la décision. À partir de tout ça, le modèle produit soit une réponse finale, quand il estime que c'est terminé, soit un appel d'outil. Un appel d'outil, c'est un petit message structuré qui dit : je veux utiliser tel outil, avec tels paramètres. Par exemple : l'outil de lecture, sur le fichier package.json.

Troisième temps, l'action. Le programme qui entoure le modèle reçoit cette demande et l'exécute vraiment. Il ouvre le fichier, il lance la commande, il fait la recherche.

Quatrième temps, l'observation. Le résultat de l'action est ajouté à la conversation. Le contenu du fichier, la sortie de la commande, le message d'erreur.

Et on recommence. Le modèle relit tout, y compris ce nouveau résultat, et décide de l'étape suivante. La boucle s'arrête quand le modèle dit que c'est fini, quand une limite est atteinte, ou quand vous l'interrompez vous-même.

*À l'écran : le déroulé de l'exemple, une ligne par tour de boucle.*

Pour que ce soit plus parlant, déroulons un exemple. Vous demandez : « le test de connexion échoue, corrige-le ».

Premier tour : le modèle n'a encore rien vu. Il décide de lancer les tests, pour voir l'erreur exacte. L'outil s'exécute, et la sortie revient dans la conversation : un test échoue, avec un message qui parle d'un mot de passe mal comparé.

Deuxième tour : le modèle lit ce message, et décide de chercher dans le projet où se trouve la fonction de connexion. La recherche lui renvoie un nom de fichier.

Troisième tour : il lit ce fichier. Il repère la ligne qui pose problème.

Quatrième tour : il modifie cette ligne.

Cinquième tour : il relance les tests. Cette fois, tout passe. Il vous répond que c'est corrigé, et il vous explique ce qu'il a changé.

Cinq tours de boucle, cinq allers-retours avec le modèle. Et vous, vous n'avez rien eu à copier ni à coller.

## 3. Le modèle, le cerveau

*À l'écran : six cartes vides en grille. La première se remplit : « Le modèle ».*

Passons maintenant aux composants. Il y en a six.

Le premier, c'est le modèle. C'est le cerveau, celui qui décide. Pour un agent, il ne suffit pas que le modèle soit bon en code. Il faut aussi qu'il soit bon à une chose plus précise : produire des appels d'outils propres et fiables. Choisir le bon outil, avec les bons paramètres, au bon moment. Et tous les modèles ne se valent pas là-dessus. Un modèle peut écrire du très bon code dans un chat, et se perdre complètement dès qu'il doit enchaîner vingt actions dans un vrai projet.

C'est un point qu'on retrouvera avec Open Code, où c'est vous qui choisissez le modèle. Le résultat dépend énormément de ce choix.

*[+] Bloc optionnel*

Le modèle ne part pas de rien à chaque tour. Avant même votre demande, l'outil lui envoie un long texte d'instructions : le prompt système. C'est là qu'on lui explique qu'il est un agent de développement, quels outils il a, comment il doit se comporter, quand il doit vous demander confirmation. Vous ne le voyez jamais, mais il est là à chaque appel, et il pèse dans le contexte. Dans un outil fermé, ce texte est caché. Dans un outil open source comme Open Code, on peut aller le lire dans le code. C'est une des raisons pour lesquelles on dit qu'un outil open source est plus transparent.

*[fin du bloc]*

## 4. Les outils

*À l'écran : la deuxième carte se remplit : « Les outils ». À côté, un exemple de description d'outil : nom, description, paramètres.*

Le deuxième composant, ce sont les outils. Techniquement, chaque outil est décrit au modèle avec trois choses : un nom, une description en langage naturel, et la liste de ses paramètres.

Pour un agent de code, on retrouve presque toujours les mêmes. Lire un fichier. Modifier ou écrire un fichier. Lancer une commande dans le terminal. Chercher un texte dans tout le projet. Lister les fichiers qui correspondent à un motif. Récupérer une page web.

Et il y a un détail qui a l'air anodin mais qui compte beaucoup. Le modèle ne connaît un outil que par la description qu'on lui en donne. Il n'a aucun autre moyen de savoir à quoi il sert. Donc si la description est floue, il va mal l'utiliser. Écrire la description d'un outil, c'est en fait écrire un prompt. Et les équipes qui font des agents passent beaucoup de temps à soigner ces textes.

*[+] Bloc optionnel*

L'idée d'apprendre à un modèle à utiliser des outils a d'abord été étudiée en recherche. Un article de 2023, appelé Toolformer, montrait qu'un modèle pouvait apprendre de lui-même quand appeler une calculatrice ou un moteur de recherche, et comment utiliser la réponse. Depuis, les fournisseurs de modèles ont intégré ça directement : on peut décrire des outils au modèle dans un format standard, et il répond avec des appels bien structurés. C'est ce mécanisme, qu'on appelle souvent function calling, qui rend les agents possibles.

*[fin du bloc]*

## 5. Le harness, la boucle d'orchestration

*À l'écran : la troisième carte : « Le harness ». Un schéma montre le modèle à l'extérieur, relié par une flèche « API » au programme qui tourne sur votre machine.*

Le troisième composant, c'est ce qu'on appelle le harness. Le mot anglais veut dire harnais. C'est tout le code qui tient l'ensemble : il envoie le contexte au modèle, il reçoit ses appels d'outils, il les exécute, il renvoie les résultats, et il fait tourner la boucle.

Et c'est un point important pour la suite du cours. Quand on parle de Claude Code ou d'Open Code, on parle de ce harness. Le modèle, lui, est ailleurs. Il tourne sur les serveurs d'un fournisseur et on l'appelle par une API, ou bien il tourne en local sur votre machine. L'outil que vous installez, c'est l'orchestration autour.

Ça veut dire que deux outils qui utilisent exactement le même modèle peuvent donner des résultats très différents. Tout dépend des outils qu'ils proposent, de la façon dont ils les décrivent, et de la façon dont ils gèrent la boucle.

## 6. La mémoire

*À l'écran : la quatrième carte : « La mémoire ». Trois étages : court terme, état de travail, long terme.*

Le quatrième composant, c'est la mémoire. Et on a vu qu'un LLM n'en a pas. Donc c'est l'agent qui doit s'en occuper, à trois niveaux.

Il y a d'abord la mémoire à court terme : c'est la conversation en cours, tout ce qui est dans la fenêtre de contexte.

Il y a ensuite l'état de travail. Pour une grosse tâche, beaucoup d'agents se créent une liste de choses à faire, qu'ils cochent au fur et à mesure. Ça les aide à ne pas perdre le fil.

Et il y a la mémoire à long terme. Ce sont des fichiers qui restent d'une session à l'autre. Dans Open Code, le principal s'appelle AGENTS.md : un fichier texte à la racine du projet, qui décrit comment le projet est organisé, comment on lance les tests, quelles conventions on suit. L'agent le relit à chaque nouvelle session.

Dernier mécanisme : quand la conversation devient trop longue pour la fenêtre de contexte, l'agent peut la résumer, pour faire de la place. On appelle ça la compaction. On garde l'essentiel et on jette les détails.

## 7. La planification

*À l'écran : la cinquième carte : « La planification ». Une grosse tâche se découpe en une liste de quatre étapes.*

Le cinquième composant, c'est la planification. Face à une tâche un peu grosse, un bon agent ne fonce pas tête baissée. Il la découpe en étapes. Certains outils vous montrent même ce plan avant de toucher au code, pour que vous puissiez le corriger. C'est le cas d'Open Code, avec un mode dédié qu'on verra en démo.

*[+] Bloc optionnel*

Certains agents vont plus loin, avec ce qu'on appelle des sous-agents. L'agent principal, face à une grosse tâche, délègue une partie du travail à un autre agent, avec sa propre conversation. Par exemple : « va chercher dans tout le projet où on utilise cette fonction, et rapporte-moi seulement la liste ». Le sous-agent fait toute l'exploration de son côté, et ne renvoie que le résultat. L'intérêt, c'est que l'agent principal garde un contexte propre, sans les dizaines de fichiers parcourus. Claude Code et Open Code proposent tous les deux ce mécanisme.

*[fin du bloc]*

La planification, c'est aussi la capacité à se corriger. Lire une erreur, comprendre que son hypothèse était fausse, et changer d'approche au lieu de réessayer la même chose.

## 8. Les garde-fous

*À l'écran : la sixième carte : « Les garde-fous ». Une fenêtre de permission : « L'agent veut lancer : npm install. Autoriser ? »*

Et le sixième composant, ce sont les garde-fous. Puisque l'agent peut agir sur votre machine, il faut pouvoir l'encadrer.

Il y a les permissions : l'agent doit vous demander avant certaines actions, comme lancer une commande ou modifier un fichier. Il y a l'isolement, ce qu'on appelle le sandboxing : limiter ce que l'agent peut toucher, par exemple un seul dossier. Et il y a vous, l'humain dans la boucle, qui validez les étapes importantes.

Attention, ces garde-fous ne sont pas toujours actifs par défaut. On verra que dans Open Code, par exemple, la plupart des actions sont autorisées d'office, et que c'est à vous de resserrer les règles.

*[+] Bloc optionnel*

Il y a un garde-fou particulier qui montre bien le problème. Open Code prévoit une protection contre ce que sa documentation appelle une « doom loop », une boucle infernale. C'est le cas où l'agent répète la même action en boucle sans avancer. Par défaut, quand ça arrive, il doit vous demander la permission de continuer. Que les développeurs aient jugé utile de prévoir ce cas en dit long : un agent qui tourne en rond, ce n'est pas un scénario théorique, ça arrive vraiment.

*[fin du bloc]*

## 9. Bon agent ou agent qui boucle ?

*À l'écran : deux colonnes : à gauche, un agent qui tourne en rond ; à droite, cinq qualités qui apparaissent une par une.*

Alors, avec tout ça, qu'est-ce qui distingue un bon agent d'un agent qui tourne en rond ?

D'abord, de bons outils, bien décrits. Ensuite, savoir s'arrêter : un agent qui ne sait pas dire « c'est fini » ou « je n'y arrive pas » va consommer des tokens pour rien. Il faut aussi une bonne gestion du contexte, pour ne pas se noyer dans des informations qui ne servent à rien. Puis la capacité à se relever après une erreur. Et enfin, tout en bas, la qualité du modèle lui-même.

Remarquez que sur ces cinq points, quatre dépendent du harness, pas du modèle. C'est pour ça que le choix de l'outil compte autant que le choix du modèle.

*[+] Bloc optionnel*

Et vous avez votre part là-dedans. Un agent qui reçoit une demande floue, sans contexte, sans moyen de vérifier son travail, va se comporter comme un mauvais agent, même s'il est excellent. À l'inverse, une demande précise, un fichier AGENTS.md à jour et une suite de tests qui tourne, ça met n'importe quel agent dans les meilleures conditions. Une bonne partie de ce cours, c'est justement apprendre à lui donner ces conditions.

*[fin du bloc]*

## 10. Conclusion et transition

*À l'écran : les six cartes réunies, puis le mot « contexte » qui grossit au centre.*

On résume. Un agent, c'est une boucle en quatre temps : percevoir, décider, agir, observer. Et six composants : le modèle, les outils, le harness, la mémoire, la planification et les garde-fous.

Vous avez peut-être remarqué qu'un mot est revenu sans arrêt : le contexte. Ce que le modèle reçoit à chaque tour. C'est lui qui détermine en grande partie la qualité du résultat. Et c'est le sujet de la prochaine vidéo.
