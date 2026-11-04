# Vidéo 4 : Les composants d'un agent IA

Partie du plan : P2.2 « Les composants d'un agent IA ».
Bornes : 5:30 – 6:10 (min = quelqu'un de rapide qui lit tout, blocs [+] compris ; max = quelqu'un de posé qui ne lit que le texte principal).
Les lignes en italique décrivent l'écran ou donnent une consigne : elles ne se lisent pas.
Enregistrer tout, y compris les blocs [+]. Au montage, les blocs [+] sont gardés un par un tant que la vidéo reste sous sa borne max.
Sources : voir sources.md (Toolformer ; Open Code : AGENTS.md, agents Build et Plan, permissions, doom_loop).

## 1. Intro

*À l'écran : l'équation « modèle + outils + boucle = agent » de la vidéo 3, puis le titre.*

On a vu dans la vidéo précédente qu'un agent, c'est un modèle, des outils et une boucle. Dit comme ça, ça a l'air simple. Mais quand on regarde de plus près, il y a plusieurs pièces qui travaillent ensemble.

Dans cette vidéo, on ouvre la machine. On suit d'abord un tour de boucle, puis on passe en revue les six composants d'un agent.

## 2. Un tour de boucle

*À l'écran : un cercle avec quatre étapes qui s'allument l'une après l'autre : perception, décision, action, observation.*

Un tour de boucle se passe en quatre temps.

La perception : le modèle reçoit tout ce qu'il faut pour décider. Les instructions de départ de l'outil, ce qu'on appelle le prompt système, votre demande, l'historique, et le résultat de ce qu'il a déjà fait.

La décision : il produit soit une réponse finale, soit un appel d'outil. Un appel d'outil, c'est un petit message structuré qui dit : je veux tel outil, avec tels paramètres. Par exemple, lire le fichier package.json.

L'action : le programme qui entoure le modèle exécute vraiment cette demande.

L'observation : le résultat est ajouté à la conversation. Et on recommence, jusqu'à ce que le modèle dise que c'est fini, qu'une limite soit atteinte, ou que vous l'interrompiez.

*À l'écran : le déroulé de l'exemple, une ligne par tour de boucle.*

Un exemple. Vous demandez : « le test de connexion échoue, corrige-le ». Premier tour, l'agent lance les tests pour voir l'erreur. Deuxième tour, il cherche où se trouve la fonction de connexion. Troisième tour, il lit ce fichier et repère la ligne en cause. Quatrième tour, il la modifie. Cinquième tour, il relance les tests, et tout passe. Cinq allers-retours avec le modèle, et vous n'avez rien copié ni collé.

## 3. Le modèle et les outils

*À l'écran : six cartes vides en grille. Les deux premières se remplissent : « Le modèle », « Les outils ».*

Passons aux six composants.

Le premier, c'est le modèle, le cerveau qui décide. Pour un agent, il ne suffit pas qu'il soit bon en code. Il doit surtout savoir produire des appels d'outils fiables : le bon outil, avec les bons paramètres, au bon moment. Un modèle peut être excellent dans un chat, et se perdre dès qu'il doit enchaîner vingt actions dans un vrai projet.

Le deuxième, ce sont les outils. Chacun est décrit au modèle par un nom, une description et des paramètres. Pour un agent de code, on retrouve toujours les mêmes : lire un fichier, le modifier, lancer une commande, chercher dans le projet, récupérer une page web. Et le modèle ne connaît un outil que par sa description. Si elle est floue, il l'utilise mal. Écrire la description d'un outil, c'est en fait écrire un prompt.

*[+] Bloc optionnel*

L'idée d'apprendre à un modèle à se servir d'outils a d'abord été étudiée en recherche. Un article de 2023, appelé Toolformer, montrait qu'un modèle pouvait apprendre de lui-même quand appeler une calculatrice ou un moteur de recherche, et comment utiliser la réponse. Depuis, les fournisseurs l'ont intégré directement : on décrit des outils au modèle dans un format standard, et il répond avec des appels bien structurés. C'est ce mécanisme, qu'on appelle souvent function calling, qui rend les agents possibles.

*[fin du bloc]*

## 4. Le harness

*À l'écran : la troisième carte : « Le harness ». Le modèle à l'extérieur, relié par une flèche « API » au programme qui tourne sur votre machine.*

Le troisième composant, c'est le harness, le harnais en anglais. C'est tout le code qui tient l'ensemble : il envoie le contexte au modèle, reçoit ses appels d'outils, les exécute, renvoie les résultats, et fait tourner la boucle.

Et c'est un point important pour la suite. Quand on parle de Claude Code ou d'Open Code, on parle de ce harness. Le modèle, lui, tourne ailleurs, chez un fournisseur ou sur votre machine. Deux outils qui utilisent exactement le même modèle peuvent donc donner des résultats très différents.

*[+] Bloc optionnel*

Le harness envoie aussi au modèle, avant même votre demande, un long texte d'instructions : le prompt système. C'est là qu'on lui explique qu'il est un agent de développement, quels outils il a, et quand il doit vous demander confirmation. Vous ne le voyez jamais, mais il est là à chaque appel. Dans un outil fermé, ce texte est caché. Dans un outil open source comme Open Code, on peut aller le lire dans le code.

*[fin du bloc]*

## 5. Mémoire, planification et garde-fous

*À l'écran : les trois dernières cartes se remplissent l'une après l'autre.*

Le quatrième composant, c'est la mémoire. Un LLM n'en a pas, donc c'est l'agent qui s'en occupe. À court terme, c'est la conversation en cours. Pour une grosse tâche, beaucoup d'agents tiennent aussi une liste de choses à faire, qu'ils cochent au fur et à mesure. Et à long terme, il y a des fichiers qui restent d'une session à l'autre. Dans Open Code, le principal s'appelle AGENTS.md : il décrit le projet, comment lancer les tests, les conventions à suivre. Quand la conversation devient trop longue, l'agent peut aussi la résumer pour faire de la place. C'est ce qu'on appelle la compaction.

Le cinquième, c'est la planification. Face à une grosse tâche, un bon agent la découpe en étapes. Certains outils vous montrent ce plan avant de toucher au code, pour que vous puissiez le corriger. C'est le cas d'Open Code, avec un agent dédié qu'on verra en démo. Planifier, c'est aussi savoir se corriger : comprendre que son hypothèse était fausse, et changer d'approche.

*[+] Bloc optionnel*

Certains agents délèguent aussi une partie du travail à des sous-agents. Par exemple : « va chercher dans tout le projet où on utilise cette fonction, et rapporte-moi seulement la liste ». Le sous-agent fait toute l'exploration de son côté, avec sa propre conversation, et ne renvoie que le résultat. L'agent principal garde ainsi un contexte propre. Claude Code et Open Code proposent tous les deux ce mécanisme.

*[fin du bloc]*

Et le sixième, ce sont les garde-fous. L'agent agit sur votre machine, il faut pouvoir l'encadrer. Il y a les permissions, pour qu'il demande avant certaines actions. L'isolement, pour limiter ce qu'il peut toucher. Et vous, l'humain dans la boucle, qui validez.

*À l'écran : une fenêtre de permission : « L'agent veut lancer : npm install. Autoriser ? »*

Concrètement, une permission ressemble à ça. L'agent veut lancer une commande, par exemple installer les dépendances du projet. Au lieu de le faire directement, l'outil vous affiche la commande exacte et attend votre réponse. Vous lisez, et vous acceptez ou vous refusez. C'est simple, mais c'est souvent la dernière barrière avant une erreur.

Attention, ces garde-fous ne sont pas toujours actifs par défaut. Dans Open Code, la plupart des actions sont autorisées d'office, et c'est à vous de resserrer les règles.

*[+] Bloc optionnel*

Un détail montre bien le problème. Open Code prévoit une protection contre ce que sa documentation appelle une « doom loop », une boucle infernale : l'agent qui répète la même action sans avancer. Par défaut, quand ça arrive, il doit vous demander s'il peut continuer. Si les développeurs ont prévu ce cas, c'est qu'il arrive vraiment.

*[fin du bloc]*

## 6. Bon agent ou agent qui boucle ?

*À l'écran : deux colonnes : à gauche, un agent qui tourne en rond ; à droite, cinq qualités qui apparaissent une par une.*

Avec tout ça, qu'est-ce qui distingue un bon agent d'un agent qui tourne en rond ?

D'abord, de bons outils, bien décrits. Ensuite, savoir s'arrêter : un agent qui ne sait pas dire « c'est fini », ou « je n'y arrive pas », continue à consommer des tokens pour rien. Il faut aussi une bonne gestion du contexte, pour ne pas se noyer dans des informations inutiles. Puis la capacité à se relever après une erreur, au lieu de retenter la même chose. Et enfin, tout en bas, la qualité du modèle lui-même.

Remarquez que sur ces cinq points, quatre dépendent du harness, pas du modèle. C'est pour ça que le choix de l'outil compte autant que le choix du modèle.

*[+] Bloc optionnel*

Et vous avez votre part là-dedans. Un agent qui reçoit une demande floue, sans contexte, sans moyen de vérifier son travail, va se comporter comme un mauvais agent, même s'il est excellent. À l'inverse, une demande précise, un fichier AGENTS.md à jour et une suite de tests qui tourne mettent n'importe quel agent dans les meilleures conditions. Une bonne partie de ce cours, c'est justement apprendre à lui donner ces conditions.

*[fin du bloc]*

## 7. Conclusion et transition

*À l'écran : les six cartes réunies, puis le mot « contexte » qui grossit au centre.*

On résume. Une boucle en quatre temps : percevoir, décider, agir, observer. Et six composants : le modèle, les outils, le harness, la mémoire, la planification et les garde-fous.

Et un mot est revenu sans arrêt : le contexte, ce que le modèle reçoit à chaque tour. C'est lui qui fait en grande partie la qualité du résultat. C'est le sujet de la prochaine partie.
