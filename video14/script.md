# Vidéo 14 : Cas pratique, améliorer un code existant (démo)

Partie du plan : P6.4 « Cas pratique : améliorer un code existant ».
Bornes : 6:10 – 6:50 (min = quelqu'un de rapide qui lit tout, blocs [+] compris ; max = quelqu'un de posé qui ne lit que le texte principal).
Les lignes en italique décrivent l'écran ou donnent une consigne : elles ne se lisent pas.
Enregistrer tout, y compris les blocs [+]. Au montage, les blocs [+] sont gardés un par un tant que la vidéo reste sous sa borne max.
Sources : opencode.ai/docs (tui : @, /undo, /new ; agents), lues le 01/11/2026.

*Vidéo en capture d'écran, avec la voix par-dessus. Les attentes de l'agent sont accélérées à quelques secondes au montage : la durée de la vidéo, c'est la voix.*

*Préparation (à faire avant le tournage) :*
*- Même projet que la vidéo 13, à partir du commit de la correction.*
*- Préparer un fichier volontairement brouillon, par exemple une fonction de validation des articles longue, avec des conditions imbriquées et des noms peu clairs, mais qui fonctionne et qui n'a pas de tests. Committer.*
*- Tester la demande la veille, et garder la meilleure prise. Les passages qui commentent l'écran sont écrits comme exemple : décrire ce que l'agent fait vraiment, en gardant à peu près la même longueur.*

## 1. Intro

*À l'écran : on ouvre le fichier brouillon dans l'éditeur et on le fait défiler lentement.*

Dernier cas pratique. Voici une fonction qui valide les articles avant de les enregistrer. Elle marche. Mais regardez-la : des conditions imbriquées dans tous les sens, des variables qui s'appellent x ou tmp, et pas un seul test. Tout le monde a déjà croisé ce genre de code. Et personne n'a envie d'y toucher, de peur de casser quelque chose.

Améliorer un code sans changer ce qu'il fait, c'est ce qu'on appelle un refactoring. Les agents sont plutôt doués pour ça. Mais le risque est réel : changer un comportement sans s'en rendre compte. Donc on va être méthodique.

Et pourquoi s'embêter, si la fonction marche ? Parce qu'un code illisible coûte cher plus tard. Le jour où il faudra ajouter une règle de validation, ou corriger un bug dedans, quelqu'un devra d'abord passer une heure à comprendre ce qu'elle fait. Et plus le code est confus, plus le risque d'erreur est grand. Un refactoring, c'est du temps qu'on investit maintenant pour en gagner ensuite.

## 2. Le problème : comment savoir qu'on n'a rien cassé ?

*À l'écran : deux versions d'une fonction, avec un point d'interrogation entre les deux.*

Pour un bug, on avait un test qui échouait : on savait quand on avait fini. Ici, on n'a rien de tel. La fonction marche, et il n'y a aucun test. Si l'agent la réécrit, comment savoir que la nouvelle version se comporte exactement comme l'ancienne ? Relire ne suffit pas. Une condition inversée, un cas oublié, ça passe très facilement inaperçu à la lecture.

La solution, c'est de commencer par fabriquer ce filet de sécurité.

*[+] Bloc optionnel*

Et si vous ne comprenez pas vous-même ce que fait la fonction, commencez par là. Comme dans la vidéo 11, en mode Plan : « explique-moi ce que fait cette fonction, cas par cas ». Vous saurez alors juger si les tests que l'agent va écrire couvrent bien tout. Sans cette compréhension, vous validerez des tests sans savoir ce qu'ils protègent.

*[fin du bloc]*

## 3. La demande, avec un filet de sécurité

*À l'écran : on tape la demande, avec @ pour désigner le fichier.*

Je désigne le fichier avec l'arobase, pour que l'agent sache exactement de quoi on parle, et j'écris :

« Commence par écrire des tests unitaires qui couvrent le comportement actuel de ce fichier, et vérifie qu'ils passent. Ensuite, refactore-le pour la lisibilité. Ne change pas le comportement. Les tests doivent toujours passer à la fin. »

L'ordre est important. D'abord les tests, sur le code tel qu'il est. Comme ça, on fige le comportement actuel, y compris ses petites bizarreries. Ensuite, la réécriture. Et à la fin, les mêmes tests doivent passer. Si un test casse, c'est que le comportement a changé.

## 4. Les tests d'abord

*À l'écran : l'agent écrit les tests, les lance. En accéléré, mais on laisse voir les tests ajoutés.*

*Commentaire d'exemple, à adapter à ce que l'agent fait vraiment :*

Il lit la fonction en entier, puis il écrit une série de tests : un article valide, un titre vide, un titre trop long, une date mal formée, un auteur manquant. Il les lance sur le code actuel. Tout passe.

Et c'est là qu'il faut s'arrêter une seconde, avant d'aller plus loin. Ces tests sont notre filet. Si le filet a des trous, le refactoring peut casser quelque chose sans qu'on le voie. Donc je les parcours. Est-ce qu'ils couvrent toutes les branches de la fonction ? Ici, il manque le cas d'un article sans contenu. Je lui demande de l'ajouter.

Un bon moyen de faire ce contrôle rapidement : lire seulement les noms des tests, les uns sous les autres. Ils doivent se lire comme une liste des règles de la fonction. « Refuse un titre vide. » « Refuse une date mal formée. » « Accepte un article complet. » Si en lisant cette liste vous pensez à une règle qui n'y est pas, c'est un test qui manque.

*[+] Bloc optionnel*

Si votre projet a un outil de couverture de code, c'est le moment de s'en servir. Demandez à l'agent de lancer les tests avec la couverture, et de vous dire quelles lignes de la fonction ne sont jamais exécutées par les tests. Chaque ligne non couverte, c'est un endroit où le refactoring pourrait casser quelque chose sans qu'aucun test ne le remarque. C'est une vérification objective, plus fiable qu'une simple relecture des tests, et elle ne prend que quelques secondes à lancer.

*[fin du bloc]*

*[+] Bloc optionnel*

Attention à un piège : un test écrit sur le code actuel fige aussi ses erreurs. Si la fonction accepte aujourd'hui un titre composé uniquement d'espaces, le test va vérifier qu'elle l'accepte. Ce n'est pas forcément ce qu'on veut. Mais c'est voulu : pendant un refactoring, on ne corrige rien, on rend le code lisible. Si vous repérez un comportement douteux, notez-le, et traitez-le à part, dans une autre tâche, avec son propre commit. Mélanger les deux, c'est le meilleur moyen de ne plus savoir ce qui a changé et pourquoi.

*[fin du bloc]*

## 5. La réécriture

*À l'écran : l'agent refactore la fonction et relance les tests. En accéléré.*

*Commentaire d'exemple, à adapter à ce que l'agent fait vraiment :*

Maintenant, il réécrit. Il découpe la grosse fonction en petites fonctions, une par règle de validation. Il remplace les conditions imbriquées par des retours anticipés. Il renomme les variables : x devient title, tmp devient errors. Puis il relance les tests. Tout est vert.

Ce genre de travail mécanique, découper, renommer, simplifier, les agents le font bien et vite. C'est exactement le type de tâche qu'on a envie de leur confier.

Mais surveillez une tendance qu'ont souvent les agents : en faire trop. On demande de rendre une fonction lisible, et on se retrouve avec trois nouvelles classes, un système de règles configurable et une bibliothèque de validation en plus. Ce n'est pas plus lisible, c'est plus compliqué. Si vous voyez ça arriver dans les demandes d'autorisation, refusez, et précisez : « garde la même structure générale, sans nouvelle dépendance ».

## 6. Relire, toujours

*À l'écran : le fichier avant et après, côte à côte ; puis git diff.*

Comparons l'avant et l'après.

*Commenter le résultat réel : est-ce plus lisible ? Les noms sont-ils meilleurs ? Y a-t-il quelque chose qu'on n'aurait pas fait comme ça ?*

C'est nettement plus lisible. Mais on relit quand même, ligne par ligne. Et on garde un regard critique. Si une partie de la réécriture ne vous plaît pas, dites-le-lui, ou annulez avec la commande undo. Les tests garantissent que le comportement n'a pas changé. Ils ne garantissent pas que le code est à votre goût.

*À l'écran : git diff limité au dossier des tests, entre le moment où les tests ont été écrits et la fin.*

Et une vérification à ne surtout pas oublier : est-ce que l'agent a touché aux tests pendant la réécriture ? Si un test le gênait, il a pu le modifier pour le faire passer. Et là, le filet de sécurité ne vaut plus rien. Je regarde donc le diff des fichiers de test depuis le moment où ils ont été écrits. Ici, rien n'a bougé. Les tests qui passent à la fin sont bien ceux qu'on avait validés au début.

Et attention à une limite. Un agent est très bon pour réécrire une fonction, beaucoup moins pour décider de l'architecture d'un projet. Faut-il découper ce module en trois ? Changer la façon dont les données circulent ? Ce sont des décisions qui engagent toute l'équipe, et c'est à vous de les prendre. L'agent peut vous proposer des options, mais c'est vous qui choisissez.

*[+] Bloc optionnel*

Une astuce pour la relecture : demandez un deuxième avis à l'agent lui-même, dans de bonnes conditions. Ouvrez une nouvelle session, passez en mode Plan, et demandez-lui de relire les modifications et de signaler tout ce qui lui paraît risqué ou incohérent. Comme il repart avec un contexte neuf, il n'est pas influencé par le raisonnement qu'il a suivi pendant la réécriture. Il repère parfois des choses qu'il avait laissées passer. Ça ne remplace pas votre relecture, mais ça la complète.

*[fin du bloc]*

## 7. Documenter

*À l'écran : on demande des commentaires ; ils apparaissent au-dessus des nouvelles fonctions.*

Un code lisible, c'est bien. Un code lisible et documenté, c'est mieux. Je demande à l'agent : « ajoute un court commentaire au-dessus de chaque règle de validation, qui explique pourquoi elle existe, pas ce qu'elle fait ».

La nuance compte. Un commentaire qui répète le code, du genre « vérifie que le titre n'est pas vide », n'apporte rien. Un commentaire qui explique la raison, comme « le titre sert d'adresse à l'article, il ne peut donc pas être vide », aide vraiment la personne qui passera après vous. Et là encore, on relit : l'agent ne connaît pas toujours la vraie raison d'une règle. S'il l'invente, corrigez-le.

*[+] Bloc optionnel*

Et si le fichier est vraiment gros, avancez par petits pas. Une fonction à la fois, un commit après chaque étape qui marche. Si une étape tourne mal, vous revenez au commit précédent sans perdre tout le reste. Demander à un agent de refactorer mille lignes d'un coup, c'est obtenir un diff que personne ne relira vraiment. Et un diff qu'on ne relit pas, c'est un risque qu'on prend sans le savoir.

*[fin du bloc]*

*À l'écran : les tests passent ; git commit.*

Les tests passent, la fonction est lisible et documentée. On fait un commit.

## 8. Conclusion et transition

*À l'écran : récapitulatif des quatre cas pratiques : comprendre, développer, corriger, améliorer.*

Pour un refactoring, retenez : des tests d'abord, sur le code tel qu'il est, et qu'on vérifie soi-même. Puis la consigne de ne pas changer le comportement. Puis une relecture attentive, et des commentaires qui expliquent le pourquoi. Et une vérification que les tests n'ont pas été modifiés en cours de route.

Et avec ce cas, on a fait le tour des quatre situations : comprendre un projet, ajouter une fonctionnalité, corriger un bug, améliorer un code existant. Dans la dernière partie du cours, on prend du recul. On commence par comparer Open Code et Claude Code, point par point.
