# Vidéo 5 : Le contexte, le carburant de l'IA

Partie du plan : P3.1 « Le contexte : le carburant de l'IA ».
Bornes : 7:30 – 8:20 (min = quelqu'un de rapide qui lit tout, blocs [+] compris ; max = quelqu'un de posé qui ne lit que le texte principal).
Les lignes en italique décrivent l'écran ou donnent une consigne : elles ne se lisent pas.
Enregistrer tout, y compris les blocs [+]. Au montage, les blocs [+] sont gardés un par un tant que la vidéo reste sous sa borne max.
Sources : voir sources.md (Lost in the Middle, RAG ; Open Code : @, /compact, AGENTS.md).

## 1. Intro : le modèle ne sait que ce qu'on lui donne

*À l'écran : une phrase au centre : « Le modèle ne sait que ce qui est dans son contexte. »*

Depuis le début du cours, il y a une idée qui revient tout le temps. Un LLM n'a pas de mémoire. Entre deux appels, il oublie tout. Ce qu'il sait de votre tâche à un instant donné, c'est uniquement ce qu'on lui envoie à ce moment-là.

Ce qu'on lui envoie, c'est ce qu'on appelle le contexte. Et dans cette vidéo, on va voir pourquoi c'est probablement la notion la plus importante pour bien utiliser un agent. Parce que quand un agent se trompe, dans la grande majorité des cas, ce n'est pas que le modèle est mauvais. C'est qu'il n'avait pas les bonnes informations.

## 2. Ce qu'il y a dans la fenêtre de contexte

*À l'écran : un grand rectangle, la fenêtre de contexte, qui se remplit par couches de couleurs différentes.*

La fenêtre de contexte, c'est la quantité maximale de texte que le modèle peut recevoir en une fois. Elle se mesure en tokens. Selon les modèles, ça va de quelques dizaines de milliers à plusieurs centaines de milliers de tokens. Ça paraît énorme. Mais regardons ce qu'on met dedans quand on utilise un agent.

Il y a d'abord le prompt système : les instructions de l'outil, souvent plusieurs pages.

Il y a ensuite la définition de tous les outils disponibles. Chaque outil avec sa description et ses paramètres.

Il y a les fichiers comme AGENTS.md, que l'agent charge au début de chaque session.

Il y a votre demande, et tout l'historique de la conversation.

Et surtout, il y a tout ce que l'agent a récupéré en travaillant. Le contenu de chaque fichier qu'il a ouvert. La sortie de chaque commande qu'il a lancée. Un seul fichier de code un peu long, c'est déjà plusieurs milliers de tokens. Une sortie de tests un peu bavarde, pareil.

Tout ça s'accumule, tour après tour. Et la fenêtre se remplit beaucoup plus vite qu'on ne l'imagine.

## 3. Trois conséquences

*À l'écran : trois cartes : « C'est limité », « Ça coûte », « L'attention baisse ».*

Ça a trois conséquences très concrètes.

Première conséquence : c'est limité. Un vrai projet, avec des centaines de fichiers, ne rentre pas en entier dans la fenêtre. Il faut choisir ce qu'on montre au modèle. Et ce choix, c'est l'agent qui le fait en grande partie, mais vous pouvez l'aider.

Deuxième conséquence : ça coûte. Vous payez chaque token envoyé au modèle. Et rappelez-vous la vidéo 3 : à chaque tour de boucle, tout le contexte est renvoyé. Un contexte gonflé de choses inutiles, c'est donc une facture gonflée, à chaque tour.

Troisième conséquence, et c'est la moins connue : plus de contexte ne veut pas dire de meilleures réponses. Au contraire. Quand on noie le modèle dans des informations qui ne servent à rien, il devient moins précis. Il a plus de mal à repérer ce qui compte vraiment.

*[+] Bloc optionnel*

Ce dernier point a été étudié. Un article de recherche publié en 2024 s'appelle « Lost in the Middle », perdu au milieu. Les auteurs ont donné à des modèles de longs textes contenant une information utile, et ils ont fait varier la position de cette information. Résultat : les modèles la retrouvent bien quand elle est au début ou à la fin du contexte, et nettement moins bien quand elle est au milieu. Autrement dit, même si tout rentre dans la fenêtre, le modèle ne lit pas tout avec la même attention. Une information noyée au milieu de pages inutiles a des chances d'être ratée.

*[fin du bloc]*

## 4. Le context engineering

*À l'écran : le titre « Context engineering », puis quatre techniques qui apparaissent une par une.*

D'où une idée qui a pris beaucoup d'importance avec les agents : le context engineering. On pourrait traduire par « l'art de construire le contexte ». Le principe : mettre la bonne information dans le contexte, au bon moment, et pas plus.

Concrètement, les agents utilisent plusieurs techniques.

La récupération ciblée. Plutôt que de charger tout un dossier, l'agent fait une recherche dans le projet pour trouver les deux ou trois fichiers qui parlent de ce qu'il cherche, et il ne lit que ceux-là. C'est ce que vous feriez vous-même avec une recherche dans votre éditeur.

Le résumé, ou la compaction. On l'a vu dans la vidéo 4 : quand la conversation devient trop longue, l'agent résume les anciens échanges pour libérer de la place. Dans Open Code, vous pouvez d'ailleurs le déclencher vous-même avec une commande.

La documentation du projet. Un fichier comme AGENTS.md évite à l'agent de redécouvrir vos conventions à chaque session. Quelques lignes bien écrites lui économisent des dizaines d'explorations.

Et l'élagage. Une fois qu'une sortie de commande n'est plus utile, on peut l'alléger ou la retirer, pour qu'elle n'encombre plus les tours suivants.

*[+] Bloc optionnel*

Attention, la compaction n'est pas gratuite non plus. Résumer, c'est forcément perdre des détails. Le résumé garde les grandes lignes : ce qu'on cherchait à faire, ce qui a été modifié, où on en est. Mais une précision que vous aviez donnée au début, comme « n'utilise pas telle bibliothèque », peut disparaître dans l'opération. Si après une compaction l'agent se met à refaire une erreur que vous aviez déjà corrigée, c'est souvent pour ça. Le bon réflexe, c'est de mettre les consignes vraiment importantes dans le fichier AGENTS.md, qui est relu à chaque session, plutôt que de compter sur la mémoire de la conversation.

*[fin du bloc]*

## 5. Ce que vous pouvez faire, vous

*À l'écran : une liste à cocher qui se remplit.*

Une bonne partie de ce travail est faite par l'outil. Mais vous avez aussi la main sur le contexte, et c'est souvent là que se joue la qualité du résultat.

Vous pouvez désigner directement les fichiers concernés dans votre demande. Dans Open Code, on le fait avec le caractère arobase suivi du nom du fichier. Ça évite à l'agent de chercher, et ça garantit qu'il regarde au bon endroit.

Vous pouvez écrire des demandes précises. « Corrige le bug » oblige l'agent à deviner. « Le test de connexion échoue depuis qu'on a changé le format des mots de passe » lui donne tout de suite la bonne piste.

Vous pouvez maintenir à jour votre fichier AGENTS.md : comment lancer le projet, comment lancer les tests, ce qu'il ne faut surtout pas toucher.

Et vous pouvez démarrer une nouvelle session quand vous changez de sujet. Une conversation qui a parlé de pagination pendant une heure n'aide pas l'agent à corriger un problème d'authentification. Au contraire, elle le pollue.

*[+] Bloc optionnel*

Un réflexe utile : quand un agent commence à faire n'importe quoi au milieu d'une longue session, ce n'est pas toujours la peine d'insister. Souvent, le contexte est devenu trop chargé, plein de tentatives ratées et d'informations contradictoires. Il vaut mieux repartir d'une session propre, avec une demande claire qui reprend ce qu'on a appris. Ça paraît contre-intuitif, parce qu'on a l'impression de perdre ce qui a été fait. Mais en pratique, l'agent repart souvent beaucoup mieux.

*[fin du bloc]*

## 6. Un exemple : la même demande, deux contextes

*À l'écran : deux colonnes. À gauche, une demande seule. À droite, la même demande avec un fichier désigné et une précision. Sous chaque colonne, le chemin suivi par l'agent.*

Prenons un exemple pour voir la différence. Vous voulez ajouter un champ « date de publication » aux articles de votre API.

Première version, vous écrivez juste : « ajoute une date de publication aux articles ». L'agent doit tout deviner. Il cherche où sont définis les articles. Il trouve peut-être le modèle de données, peut-être une vieille copie dans un dossier de tests. Il ne sait pas si vous utilisez une bibliothèque de dates en particulier. Il ne sait pas comment le projet nomme les champs, en français ou en anglais, avec des tirets bas ou des majuscules. Alors il choisit. Et il a de bonnes chances de choisir différemment de ce que vous auriez fait.

Deuxième version : « ajoute un champ publishedAt au modèle dans arobase src/models/article.js, au même format que createdAt, et mets à jour les tests ». Là, l'agent sait où aller, il a un exemple à imiter, et il sait comment vérifier son travail. Il fait moins de tours de boucle, donc il coûte moins cher, et le résultat ressemble à votre code.

Les deux demandes font une ligne. La deuxième a juste pris dix secondes de plus à écrire. C'est souvent le meilleur investissement que vous puissiez faire avec un agent.

*[+] Bloc optionnel*

Et c'est justement le rôle du fichier AGENTS.md : éviter d'avoir à répéter ces précisions à chaque demande. Un bon AGENTS.md n'a pas besoin d'être long. Quelques lignes suffisent : la commande pour installer le projet, celle pour lancer les tests, les conventions de nommage, l'organisation des dossiers, et les pièges connus. Par exemple : « ne jamais modifier le dossier migrations à la main ». Tout ce qu'on dirait à un nouveau développeur le premier jour. Et comme ce fichier est relu à chaque session, l'agent part toujours avec ces informations.

*[fin du bloc]*

## 7. Garbage in, garbage out

*À l'écran : la formule « Contexte pourri, réponse pourrie » qui s'affiche en grand.*

Il y a une vieille formule en informatique qui résume tout ça : garbage in, garbage out. Si on met des déchets en entrée, on obtient des déchets en sortie. Avec les agents, on pourrait dire : contexte pourri, réponse pourrie.

Quand un agent vous propose une solution complètement à côté, avant d'accuser le modèle, posez-vous la question : est-ce qu'il avait ce qu'il fallait pour bien faire ? Est-ce qu'il connaissait la bonne version de la bibliothèque ? Est-ce qu'il savait que ce fichier existait ? Est-ce que ma demande était claire ? La plupart du temps, la réponse est là.

*[+] Bloc optionnel*

Un piège classique, d'ailleurs : le contexte qui contredit. Votre fichier AGENTS.md dit qu'on lance les tests avec une commande, mais elle a changé il y a trois mois et personne n'a mis le fichier à jour. Ou un vieux commentaire dans le code décrit un fonctionnement qui n'existe plus. L'agent, lui, n'a aucun moyen de savoir lequel croire. Il fait au mieux avec ce qu'il lit. Un contexte faux est souvent pire qu'un contexte absent, parce qu'il envoie l'agent dans la mauvaise direction avec beaucoup d'assurance.

*[fin du bloc]*

## 8. Aller chercher du contexte à l'extérieur : RAG et MCP

*À l'écran : deux colonnes : « RAG » et « MCP ». Sous chacune, qui décide de chercher.*

Il reste une question. Que faire quand l'information dont l'agent a besoin n'est pas dans votre projet ? Par exemple, la documentation à jour d'une bibliothèque, ou des données qui sont dans un autre outil. Il y a deux grandes approches, qu'on confond souvent.

La première s'appelle le RAG, pour Retrieval-Augmented Generation : génération augmentée par la recherche. C'est vous, ou votre application, qui construisez un système qui va chercher les passages pertinents, par exemple dans une base de documents, et qui les ajoute au prompt avant d'appeler le modèle. La recherche se fait en amont, et c'est votre code qui décide quoi chercher.

La deuxième, c'est MCP. Là, on donne à l'agent un accès standardisé à des sources d'information et à des outils externes, et c'est l'agent lui-même qui décide quand aller chercher quelque chose, au moment où il en a besoin.

Les deux ne s'opposent pas. Un serveur MCP peut très bien faire du RAG derrière. Mais pour un agent de code comme Open Code, c'est MCP qui nous intéresse.

## 9. Conclusion et transition

*À l'écran : le logo MCP et celui de Context7.*

On retient trois choses. Le modèle ne sait que ce qui est dans son contexte. Ce contexte est limité, il coûte, et trop d'informations inutiles dégradent la réponse. Et une bonne partie de votre travail avec un agent, c'est de l'aider à avoir le bon contexte.

Dans la prochaine vidéo, on va voir rapidement MCP, le protocole qui permet aux agents d'aller chercher du contexte à l'extérieur. Puis on passera à un exemple très concret : Context7, qui donne à l'agent une documentation à jour des bibliothèques que vous utilisez.
