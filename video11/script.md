# Vidéo 11 : Cas pratique 2, corriger un bug et améliorer du code (démo)

Durée visée : 8 min. Vidéo en capture d'écran avec la voix par-dessus. Les lignes en italique décrivent l'écran ou donnent une consigne : elles ne se lisent pas.
Enregistrer tout, y compris les blocs [+]. Au montage, les blocs [+] sont gardés seulement si la vidéo reste sous 9 min 30.

*Écran sans voix : environ 60 s (agent qui travaille, accéléré au montage).*

*Préparation (à faire avant le tournage) :*
*- Même projet que la vidéo 10, à partir du commit de la pagination.*
*- Partie 1 : introduire volontairement un bug dans le calcul de la pagination (par exemple un décalage d'un élément dans le calcul de la position de départ), et un test qui le met en évidence. Committer cet état « avec bug ».*
*- Partie 2 : préparer un fichier volontairement brouillon, par exemple une fonction de validation des articles longue, avec des conditions imbriquées et des noms peu clairs, mais qui fonctionne. Committer.*
*- Tester les demandes la veille, et garder la meilleure prise. Ne pas lire mot pour mot les passages qui commentent l'écran : décrire ce que l'agent fait vraiment.*

## 1. Intro

*À l'écran : le projet de la vidéo 10, et l'historique git avec le commit de la pagination.*

On reprend notre projet là où on l'avait laissé, avec la pagination. Dans cette vidéo, deux situations que vous rencontrerez tout le temps. D'abord, un bug à corriger. Ensuite, un code qui marche mais qui est difficile à lire, et qu'on veut améliorer sans rien casser.

Pour la démo, on a préparé les deux à l'avance : on a volontairement glissé un bug dans le projet, et on a écrit une fonction bien brouillonne.

## 2. Partie 1 : un test qui échoue

*À l'écran : on lance les tests ; un test échoue avec son message d'erreur.*

On commence par lancer les tests. Et l'un d'eux échoue : celui qui vérifie qu'on récupère bien la deuxième page d'articles.

*Lire le nom réel du test et l'essentiel du message d'erreur.*

C'est la situation idéale pour un agent. Pourquoi ? Parce qu'on a un moyen objectif de savoir si le bug est corrigé : le test doit passer. Rappelez-vous la vidéo 3 : un agent qui peut vérifier son travail s'auto-corrige. Sans moyen de vérifier, il devine.

## 3. Une demande précise

*À l'écran : Open Code en mode Build. On tape la demande avec le nom exact du test.*

J'écris une demande précise, avec le nom exact du test : « Le test » suivi de son nom « échoue. Trouve la cause et corrige-la, sans modifier le test. »

Le « sans modifier le test » est important. Sinon, un agent peut être tenté de faire passer le test en le changeant, au lieu de corriger le code. Le test passerait, mais le bug serait toujours là.

*À l'écran : l'agent lance le test, lit l'erreur, ouvre les fichiers, corrige, relance. Accélérer, mais laisser voir chaque étape et les demandes d'autorisation.*

*Commenter ce que l'agent fait réellement, étape par étape : il lance le test, il lit l'erreur, il ouvre le fichier de la pagination, il formule une hypothèse, il corrige, il relance. Prévoir environ 40 secondes.*

Vous voyez la boucle en action. Lancer, lire l'erreur, chercher, comprendre, corriger, relancer. Exactement ce qu'on a décrit en théorie.

## 4. Vérifier la correction

*À l'écran : git diff sur la correction ; puis on relance tous les tests.*

Le test passe. Mais comme toujours, on regarde ce qui a changé. La commande git diff me montre la correction.

*Lire la ligne corrigée et expliquer en une phrase pourquoi c'était faux.*

La correction est petite et elle est logique. Je relance toute la suite de tests, pas seulement celui qui échouait, pour m'assurer qu'il n'a rien cassé ailleurs. Tout est vert, on peut faire un commit.

## 5. Le contre-exemple : une demande vague

*À l'écran : on revient au commit avec le bug (git checkout ou /undo), nouvelle session, puis une demande vague : « la pagination bugue parfois, corrige ».*

Maintenant, je veux vous montrer ce qui se passe avec une mauvaise demande. Je reviens à l'état avec le bug, j'ouvre une nouvelle session, et j'écris simplement : « la pagination bugue parfois, corrige ».

*Commenter ce que l'agent fait réellement. Selon les cas, il peut chercher longtemps, proposer une correction à côté, modifier autre chose, ou trouver quand même. Le dire honnêtement. Prévoir environ 30 secondes.*

*À adapter selon le résultat réel :*

Si l'agent cherche longtemps ou corrige à côté : On le voit, il tâtonne. Il ne sait pas ce que « bugue parfois » veut dire, alors il explore, il fait des suppositions, et il consomme des tokens pour rien.

Si l'agent trouve quand même : Cette fois, il a trouvé, mais regardez le nombre d'étapes et le temps qu'il lui a fallu par rapport à tout à l'heure. Et sur un projet plus gros, il aurait eu beaucoup moins de chances.

Dans les deux cas, la leçon est la même : la précision de votre demande fait la différence. Un nom de test, un message d'erreur, un fichier : chaque indice que vous donnez, c'est de l'exploration en moins pour l'agent.

*[+] Bloc optionnel*

Et si vous n'avez pas de test qui reproduit le bug ? Commencez par là. Demandez à l'agent d'écrire d'abord un test qui met le bug en évidence, vérifiez que ce test échoue bien pour la bonne raison, et seulement ensuite, demandez la correction. C'est un peu plus long, mais vous obtenez deux choses : une correction vérifiée, et un test qui empêchera le bug de revenir plus tard. C'est une très bonne habitude, avec ou sans agent.

*[fin du bloc]*

## 6. Quand l'agent n'y arrive pas

*À l'écran : un rappel des réflexes : Échap, /undo, /new, une demande plus précise.*

Et si l'agent tourne en rond ? Ça arrive, même avec une bonne demande. Il essaie une correction, elle échoue, il en essaie une autre, puis revient à la première. Ou il commence à modifier des fichiers qui n'ont rien à voir.

Dans ce cas, n'attendez pas qu'il finisse par trouver. Chaque tour de boucle vous coûte du temps et des tokens. Appuyez sur Échap pour l'arrêter. Annulez ce qu'il a modifié avec la commande undo. Et repartez d'une nouvelle session, avec une demande enrichie de ce que vous avez appris : le fichier en cause, la piste qui ne marche pas, celle qui vous semble la bonne.

Et parfois, la bonne réponse, c'est de reprendre la main. Si vous avez compris le problème en regardant l'agent chercher, corrigez-le vous-même. Un agent est un outil, pas une obligation. Savoir quand l'arrêter fait partie de savoir s'en servir.

## 7. Partie 2 : améliorer un code existant

*À l'écran : on revient au commit propre. On ouvre le fichier brouillon dans l'éditeur et on le fait défiler.*

Deuxième situation. Voici une fonction qui valide les articles avant de les enregistrer. Elle marche. Mais regardez-la : des conditions dans tous les sens, des noms de variables qui ne veulent rien dire. Personne n'a envie de la modifier.

Améliorer un code sans changer ce qu'il fait, c'est ce qu'on appelle un refactoring. Et le risque, c'est de casser quelque chose sans s'en rendre compte. Donc on va être prudent.

## 8. La demande, avec un filet de sécurité

*À l'écran : on tape la demande avec @ pour désigner le fichier.*

Je désigne le fichier avec l'arobase, et j'écris : « Commence par écrire des tests unitaires qui couvrent le comportement actuel de ce fichier et vérifie qu'ils passent. Ensuite, refactore-le pour la lisibilité. Ne change pas le comportement. Les tests doivent toujours passer à la fin. »

L'ordre est important. D'abord les tests, sur le code tel qu'il est. Comme ça, on fige le comportement actuel. Ensuite, la réécriture. Et à la fin, les mêmes tests doivent passer. Si un test casse, c'est que le comportement a changé.

*À l'écran : l'agent écrit les tests, les lance, refactore, relance. Accélérer.*

*Commenter ce que l'agent fait réellement : les tests qu'il ajoute, la façon dont il découpe la fonction, les noms qu'il choisit. Prévoir environ 30 secondes.*

## 9. Relire, toujours

*À l'écran : le fichier avant et après, côte à côte ; puis git diff.*

Comparons l'avant et l'après.

*Commenter le résultat réel : est-ce plus lisible ? Les noms sont-ils meilleurs ? Y a-t-il quelque chose qu'on n'aurait pas fait comme ça ?*

Ce genre de travail mécanique, découper, renommer, simplifier, les agents le font bien. Mais on relit quand même, ligne par ligne. Et on garde un regard critique : si une partie de la réécriture ne vous plaît pas, dites-le-lui, ou annulez avec la commande undo.

Attention à une limite. Un agent est très bon pour réécrire une fonction, beaucoup moins pour décider de l'architecture d'un projet. Faut-il découper ce module en trois ? Changer la façon dont les données circulent ? Ce sont des décisions qui engagent toute l'équipe, et c'est à vous de les prendre. L'agent peut vous proposer des options, mais c'est vous qui choisissez.

*[+] Bloc optionnel*

Une astuce pour la relecture : demandez un deuxième avis à l'agent lui-même, mais dans de bonnes conditions. Ouvrez une nouvelle session, passez en mode Plan, et demandez-lui de relire les modifications et de signaler tout ce qui lui paraît risqué ou incohérent. Comme il repart avec un contexte neuf, il n'est pas influencé par le raisonnement qu'il a suivi pendant la réécriture. Il repère parfois des choses qu'il avait laissées passer. Ça ne remplace pas votre relecture, mais ça peut la compléter, surtout sur une modification un peu longue.

*[fin du bloc]*

*À l'écran : les tests passent ; git commit.*

Les tests passent, la fonction est lisible, on fait un commit.

## 10. Conclusion et transition

*À l'écran : récapitulatif : un test pour vérifier, une demande précise, relire, committer.*

Ce qu'on retient de ces deux cas. Pour un bug : un test qui le reproduit et une demande précise. Pour un refactoring : des tests d'abord, la consigne de ne pas changer le comportement, et une relecture attentive. Et dans les deux cas, git pour pouvoir revenir en arrière à tout moment.

On a maintenant tout vu : la théorie, l'installation, l'interface et la pratique. Dans la dernière vidéo, on prend du recul. On compare Open Code et Claude Code point par point, on fait le tour des bonnes pratiques, notamment de sécurité, et on conclut le cours.
