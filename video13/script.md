# Vidéo 13 : Cas pratique, corriger un bug (démo)

Partie du plan : P6.3 « Cas pratique : corriger un bug ».
Bornes : 6:10 – 6:50 (min = quelqu'un de rapide qui lit tout, blocs [+] compris ; max = quelqu'un de posé qui ne lit que le texte principal).
Les lignes en italique décrivent l'écran ou donnent une consigne : elles ne se lisent pas.
Enregistrer tout, y compris les blocs [+]. Au montage, les blocs [+] sont gardés un par un tant que la vidéo reste sous sa borne max.
Sources : opencode.ai/docs (tui : /undo, /new ; permissions : doom_loop), lues le 01/11/2026.

*Vidéo en capture d'écran, avec la voix par-dessus. Les attentes de l'agent sont accélérées à quelques secondes au montage : la durée de la vidéo, c'est la voix.*

*Préparation (à faire avant le tournage) :*
*- Même projet que la vidéo 12, à partir du commit de la pagination.*
*- Introduire volontairement un bug dans le calcul de la pagination, par exemple un décalage d'un élément dans le calcul de la position de départ, et un test qui le met en évidence. Committer cet état « avec bug ».*
*- Tester les deux demandes (précise et vague) la veille, et garder les meilleures prises. Les passages qui commentent l'écran sont écrits comme exemple : décrire ce que l'agent fait vraiment, en gardant à peu près la même longueur.*

## 1. Intro

*À l'écran : le projet, et l'historique git avec le commit de la pagination.*

On reprend notre projet avec sa toute nouvelle pagination. Et dans cette vidéo, on s'attaque à la tâche la plus courante du métier : corriger un bug.

Pour la démo, on a glissé volontairement une erreur dans le calcul de la pagination. On va voir comment la faire corriger proprement par l'agent. Puis on fera l'inverse : on décrira le même bug de façon vague, pour voir ce que ça change.

## 2. Un test qui échoue

*À l'écran : on lance les tests ; un test échoue avec son message d'erreur.*

On commence par lancer les tests. Et l'un d'eux échoue : celui qui vérifie qu'on récupère bien la deuxième page d'articles.

*Commentaire d'exemple, à adapter au message réel :*

Le test attendait les articles six à dix, et il a reçu les articles cinq à neuf. Il y a un décalage d'un article.

C'est la situation idéale pour un agent. Pourquoi ? Parce qu'on a un moyen objectif de savoir si le bug est corrigé : le test doit passer. Rappelez-vous la vidéo 3 : un agent qui peut lancer les tests et lire le résultat se corrige tout seul. Sans moyen de vérifier, il devine.

*[+] Bloc optionnel*

*À l'écran : l'indicateur passe sur « Plan », on tape la demande d'explication.*

Avant de demander la correction, on peut aussi demander une explication. En mode Plan : « explique-moi pourquoi ce test échoue, sans rien corriger ». L'agent mène l'enquête, et il vous présente la cause. Si vous êtes en train d'apprendre, ou si le code est critique, c'est une très bonne façon de faire. Vous comprenez le bug avant de le voir disparaître, et vous pouvez juger si la correction qu'il proposera ensuite est la bonne.

*[fin du bloc]*

## 3. Une demande précise

*À l'écran : Open Code sur l'agent Build. On tape la demande avec le nom exact du test.*

J'écris une demande précise, avec le nom exact du test : « Le test » suivi de son nom « échoue. Trouve la cause et corrige-la, sans modifier le test. »

Le « sans modifier le test » est important. Sinon, un agent peut être tenté de faire passer le test en le changeant, au lieu de corriger le code. Le test passerait, mais le bug serait toujours là. C'est un comportement qu'on voit vraiment, surtout quand la correction n'est pas évidente.

*À l'écran : l'agent lance le test, lit l'erreur, ouvre les fichiers, corrige, relance. En accéléré, mais on laisse voir chaque étape et chaque demande d'autorisation.*

*Commentaire d'exemple, à adapter à ce que l'agent fait vraiment :*

Il commence par lancer le test, pour voir l'erreur lui-même. Il lit le message, et il en déduit que le problème vient du calcul de la position de départ. Il ouvre le fichier de la pagination, il trouve la ligne qui fait ce calcul. Il m'explique son hypothèse : on retire un de trop. Il propose la correction, je la lis, j'accepte. Et il relance le test. Cette fois, il passe.

Vous voyez la boucle en action. Lancer, lire l'erreur, chercher, comprendre, corriger, relancer. Exactement ce qu'on a décrit en théorie, dans la deuxième partie du cours.

Et pendant tout ce temps, je lis les demandes d'autorisation. Quand il veut lancer une commande, je vérifie que c'est bien la commande de test du projet, et pas autre chose. Quand il veut modifier un fichier, je regarde lequel. Ici, il ne touche qu'au fichier de la pagination. C'est cohérent avec son hypothèse, donc j'accepte.

## 4. Vérifier la correction

*À l'écran : git diff sur la correction ; puis on relance tous les tests.*

Le test passe. Mais comme toujours, on regarde ce qui a changé. La commande git diff me montre la correction.

*Lire la ligne corrigée et expliquer en une phrase pourquoi c'était faux.*

La correction est petite, et elle est logique. Je relance toute la suite de tests, pas seulement celui qui échouait, pour m'assurer que rien n'est cassé ailleurs. Tout est vert, on peut faire un commit.

*À l'écran : un appel à l'API avec page=2 et limit=5 ; la réponse contient les articles six à dix.*

Et je vérifie aussi à la main, avec un vrai appel à l'API. Deuxième page, cinq articles par page : j'obtiens bien les articles six à dix. Le test et l'appel réel disent la même chose.

Remarquez la taille du changement. Une seule ligne. C'est souvent bon signe. Un agent qui modifie six fichiers pour corriger un décalage d'un élément, ça doit vous alerter : soit il n'a pas trouvé la vraie cause, soit il en profite pour changer des choses qu'on ne lui a pas demandées.

Une dernière question à se poser avant de passer à autre chose : est-ce que la même erreur existe ailleurs ? Un calcul faux a souvent été copié. Je demande donc à l'agent : « cherche dans le projet si ce même calcul de position est fait ailleurs, et dis-moi où, sans rien modifier ».

*Commentaire d'exemple, à adapter à la réponse réelle :*

Il fait une recherche dans tout le projet, et il me répond que ce calcul n'existe qu'à un seul endroit. Très bien, le bug est vraiment réglé. Sur un vrai projet, c'est souvent là qu'on découvre un deuxième bug, caché derrière le premier.

## 5. Le contre-exemple : une demande vague

*À l'écran : on revient au commit avec le bug, on tape /new, puis une demande vague : « la pagination bugue parfois, corrige ».*

Maintenant, je veux vous montrer ce qui se passe avec une mauvaise demande. Je reviens à l'état avec le bug, j'ouvre une nouvelle session pour que l'agent ne se souvienne pas de la solution, et j'écris simplement : « la pagination bugue parfois, corrige ».

*Commentaire à adapter au résultat réel, en restant honnête. Deux versions possibles :*

*Si l'agent cherche longtemps ou corrige à côté :*

On le voit, il tâtonne. Il ne sait pas ce que « bugue parfois » veut dire. Alors il lit plusieurs fichiers, il fait des suppositions, et il propose de modifier la validation des paramètres, qui n'avait rien à voir. Il consomme des tokens, et il ne trouve pas.

*Si l'agent trouve quand même :*

Cette fois, il a trouvé. Mais regardez le nombre d'étapes et le temps qu'il lui a fallu, par rapport à tout à l'heure. Et sur un projet plus gros, avec des dizaines de fichiers, il aurait eu beaucoup moins de chances.

Dans les deux cas, la leçon est la même : la précision de votre demande fait la différence. Un nom de test, un message d'erreur, un fichier : chaque indice que vous donnez, c'est de l'exploration en moins pour l'agent.

*[+] Bloc optionnel*

Et si vous n'avez pas de test qui reproduit le bug ? Commencez par là. Demandez à l'agent d'écrire d'abord un test qui met le bug en évidence. Vérifiez que ce test échoue, et pour la bonne raison. Et seulement ensuite, demandez la correction. C'est un peu plus long, mais vous obtenez deux choses : une correction vérifiée, et un test qui empêchera le bug de revenir plus tard. C'est une très bonne habitude, avec ou sans agent.

*[fin du bloc]*

*[+] Bloc optionnel*

Une bonne description de bug, pour un agent, c'est la même que pour un collègue. Ce que vous avez fait. Ce que vous attendiez. Ce que vous avez obtenu à la place. Et si possible, le message d'erreur complet, copié tel quel. Par exemple : « j'appelle la liste des articles avec page égale deux et limit égale cinq, j'attends les articles six à dix, j'obtiens les articles cinq à neuf ». Avec ces trois phrases, l'agent sait déjà presque où chercher.

*[fin du bloc]*

## 6. Quand l'agent n'y arrive pas

*À l'écran : un rappel des réflexes : Échap, /undo, /new, une demande plus précise.*

Et si l'agent tourne en rond ? Ça arrive, même avec une bonne demande. Il essaie une correction, elle échoue, il en essaie une autre, puis revient à la première. Ou il commence à modifier des fichiers qui n'ont rien à voir.

Dans ce cas, n'attendez pas qu'il finisse par trouver. Chaque tour de boucle vous coûte du temps et des tokens. Appuyez sur Échap pour l'arrêter. Annulez ce qu'il a modifié avec la commande undo. Et repartez d'une nouvelle session, avec une demande enrichie de ce que vous avez appris : le fichier en cause, la piste qui ne marche pas, celle qui vous semble la bonne.

Et parfois, la bonne réponse, c'est de reprendre la main. Si vous avez compris le problème en regardant l'agent chercher, corrigez-le vous-même. Un agent est un outil, pas une obligation. Savoir quand l'arrêter fait partie de savoir s'en servir.

*[+] Bloc optionnel*

Méfiez-vous aussi d'un agent qui annonce « c'est corrigé » trop vite. Parfois, il modifie le code, il explique très bien pourquoi ça devrait marcher, mais il n'a pas relancé les tests. Ou il les a relancés, mais pas tous. Avant de le croire, regardez dans le fil de la conversation : est-ce que la sortie des tests est là, et est-ce qu'elle est verte ? Sinon, demandez-lui de les lancer, ou lancez-les vous-même avec le point d'exclamation.

*[fin du bloc]*

*[+] Bloc optionnel*

Et quand le bug vient de la production, sans test pour le reproduire ? Donnez à l'agent ce que vous avez : le message d'erreur complet, la trace de la pile, les lignes de journal autour de l'erreur. Vous pouvez les coller dans la demande, ou les afficher avec une commande précédée du point d'exclamation. Puis demandez-lui d'abord d'écrire un test qui reproduit le problème. On retombe alors sur la situation idéale : un test qui échoue, et une correction qu'on peut vérifier.

*[fin du bloc]*

*[+] Bloc optionnel*

Open Code a d'ailleurs prévu ce cas. Quand l'agent répète la même action en boucle, ce que la documentation appelle une « doom loop », il doit par défaut vous demander s'il peut continuer. Si vous voyez apparaître cette question, c'est un signal clair. Ne répondez pas oui par réflexe : c'est probablement le moment d'arrêter, et de reformuler.

*[fin du bloc]*

## 7. Conclusion et transition

*À l'écran : récapitulatif : un test qui reproduit le bug, une demande précise, vérifier le diff, committer.*

Ce qu'on retient pour corriger un bug : un test qui le reproduit, une demande précise qui dit ce qu'on attend et ce qu'on obtient, et la consigne de ne pas toucher au test. Puis une vérification du diff, toute la suite de tests, et un commit. Et si l'agent tourne en rond, on l'arrête, on annule, et on repart avec une meilleure demande.

Dans la prochaine vidéo, dernier cas pratique : un code qui fonctionne, mais que personne n'a envie de toucher. On va le faire améliorer par l'agent, sans rien casser.
