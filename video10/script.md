# Vidéo 10 : Découvrir l'interface et les fonctionnalités (démo)

Partie du plan : P5.2 « Découvrir l'interface et les fonctionnalités ».
Bornes : 6:10 – 6:55 (min = quelqu'un de rapide qui lit tout, blocs [+] compris ; max = quelqu'un de posé qui ne lit que le texte principal).
Les lignes en italique décrivent l'écran ou donnent une consigne : elles ne se lisent pas.
Enregistrer tout, y compris les blocs [+]. Au montage, les blocs [+] sont gardés un par un tant que la vidéo reste sous sa borne max.
Sources : opencode.ai/docs (tui, keybinds, agents, cli), lues le 01/11/2026. Revérifier les commandes et raccourcis la veille du tournage (les lettres après ctrl+x sont à confirmer dans la page keybinds).

*Vidéo en capture d'écran, avec la voix par-dessus. Les attentes (agent qui travaille, commandes qui tournent) sont coupées ou accélérées à quelques secondes au montage : la durée de la vidéo, c'est la voix.*

*Avant de tourner : reprendre le projet de démo configuré dans la vidéo 9 (opencode.json, AGENTS.md, dépôt git propre). Faire un commit juste avant, pour pouvoir montrer /undo sans risque.*

## 1. Intro

*À l'écran : Open Code ouvert dans le projet de démo.*

Notre agent est installé et configuré. Maintenant, on va apprendre à s'en servir efficacement. Dans cette vidéo, on fait le tour de l'interface : comment écrire une demande, comment lui montrer des fichiers, comment passer en mode plan, gérer ses sessions, et surtout comment revenir en arrière quand l'agent s'est trompé.

## 2. L'écran principal

*À l'écran : on montre successivement le fil de la conversation, la zone de saisie, et les informations en bas de l'écran (modèle, agent actif).*

L'écran est assez simple. En haut, le fil de la conversation : vos demandes, les réponses de l'agent, et tout ce qu'il fait entre les deux, les fichiers qu'il lit, les commandes qu'il lance. En bas, la zone où vous écrivez. Et autour, quelques informations utiles : le modèle utilisé, et l'agent actif.

Pour envoyer une demande, on l'écrit et on appuie sur Entrée.

## 3. Désigner des fichiers avec arobase

*À l'écran : on tape « explique-moi @ » puis le début d'un nom de fichier ; la liste de suggestions apparaît ; on choisit le fichier et on envoie.*

Première chose à connaître : l'arobase. Quand vous tapez arobase dans votre demande, Open Code ouvre une recherche dans les fichiers du projet. Vous tapez quelques lettres, il vous propose les fichiers qui correspondent, et vous choisissez.

Le contenu du fichier est alors ajouté directement à la conversation. C'est la façon la plus simple de donner le bon contexte à l'agent. Au lieu de le laisser chercher, vous lui dites exactement où regarder. Rappelez-vous la vidéo 5 : un contexte précis, c'est une meilleure réponse, et moins de tokens dépensés.

## 4. Lancer une commande avec le point d'exclamation

*À l'écran : on tape « !git status » ; la sortie apparaît dans la conversation.*

Deuxième raccourci : le point d'exclamation. Si votre message commence par un point d'exclamation, Open Code ne l'envoie pas au modèle comme une demande. Il l'exécute comme une commande dans le terminal, et il ajoute le résultat à la conversation.

C'est pratique pour montrer quelque chose à l'agent. Par exemple, vous lancez les tests vous-même, et le résultat est là, dans le contexte, pour la demande suivante.

## 5. Les commandes avec barre oblique

*À l'écran : on tape « / » ; la liste des commandes s'affiche. Puis on montre ctrl+p.*

Ensuite, il y a les commandes qui commencent par une barre oblique. Si vous tapez juste la barre oblique, Open Code vous affiche la liste. Et vous pouvez aussi ouvrir la liste de toutes les commandes avec Contrôle et P.

On en a déjà vu trois dans la vidéo précédente : connect, pour ajouter un fournisseur, models, pour choisir le modèle, et init, pour créer le fichier AGENTS.md.

Voici les autres qui vous serviront tous les jours.

*À l'écran : chaque commande est tapée ou affichée au moment où on en parle.*

new, pour démarrer une nouvelle session. À utiliser dès que vous changez de sujet, pour repartir avec un contexte propre.

sessions, pour retrouver vos anciennes sessions et en reprendre une. Open Code les garde, vous pouvez donc reprendre un travail le lendemain là où vous l'aviez laissé.

compact, pour résumer la session en cours quand elle devient trop longue. C'est la compaction dont on a parlé dans la vidéo 4.

Et help, si vous avez un doute, pour afficher l'aide.

*[+] Bloc optionnel*

Il y en a quelques autres, plus secondaires. themes, pour changer l'apparence. editor, pour écrire une longue demande dans votre éditeur de texte habituel au lieu de la petite zone de saisie. details, pour afficher ou masquer le détail de ce que font les outils. Et thinking, pour afficher ou masquer le raisonnement du modèle, quand il en produit un. Ça ne change pas la façon dont le modèle réfléchit, seulement ce que vous voyez à l'écran. Et export, pour exporter la conversation au format Markdown : utile pour garder une trace, ou pour montrer à un collègue comment vous avez obtenu un résultat, avec chaque demande et chaque réponse de l'agent.

*[fin du bloc]*

## 6. Les deux agents : Build et Plan

*À l'écran : on appuie sur Tabulation ; l'indicateur d'agent change en bas à droite. On le refait pour revenir.*

Un des réglages les plus importants se fait avec une seule touche : Tabulation. Elle permet de passer d'un agent à l'autre.

Par défaut, vous êtes sur l'agent Build. Il a accès à tous les outils : il lit, il modifie, il lance des commandes. C'est lui qui fait le travail.

Quand vous appuyez sur Tabulation, vous passez sur l'agent Plan. Celui-là ne peut pas modifier vos fichiers. Il peut lire le projet, réfléchir, et vous proposer un plan. C'est idéal pour comprendre un projet, ou pour discuter d'une solution avant de la lancer. Et on verra dans les cas pratiques que c'est souvent une très bonne idée de commencer par lui.

Un indicateur, en bas à droite, vous dit toujours quel agent est actif. Regardez-le avant d'envoyer une demande.

*[+] Bloc optionnel*

Il existe aussi des sous-agents, qu'on appelle avec l'arobase suivie de leur nom. Open Code en fournit deux : general, pour des recherches et des tâches en plusieurs étapes, et explore, un agent rapide en lecture seule pour fouiller le code. L'agent principal peut aussi les lancer de lui-même pour se répartir le travail. Et vous pouvez créer vos propres agents, avec leurs instructions, leur modèle et leurs permissions. Par exemple un agent dédié à la relecture de code, qui n'a le droit de rien modifier.

*[fin du bloc]*

*[+] Bloc optionnel*

Un conseil pour choisir entre les deux. Si vous hésitez sur ce que vous voulez, ou si la tâche touche plusieurs fichiers, commencez toujours en Plan. Discutez, faites préciser, faites corriger le plan. Puis passez en Build et demandez simplement d'appliquer ce plan. L'agent garde toute la conversation, donc il sait exactement ce qui a été décidé. À l'inverse, pour une petite modification bien définie, comme renommer une variable dans un fichier, vous pouvez aller directement en Build. Le mode Plan ne sert à rien si vous savez déjà précisément ce que vous voulez.

*[fin du bloc]*

## 7. Les demandes d'autorisation

*À l'écran : avec l'agent Build, on demande « lance les tests ». Open Code affiche une demande d'autorisation pour la commande. On la lit, puis on accepte. Montrer aussi une modification de fichier avec son aperçu, et un refus.*

Dans la vidéo précédente, on a réglé les permissions pour que l'agent demande avant de lancer une commande ou de modifier un fichier. Voyons à quoi ça ressemble.

Je lui demande de lancer les tests. Au lieu de le faire directement, Open Code m'affiche la commande exacte qu'il veut exécuter, et attend ma réponse. Je la lis, c'est bien la commande de test du projet, j'accepte.

Pour une modification de fichier, c'est pareil. L'agent me montre ce qu'il veut changer, et je décide. Si je refuse, il ne touche à rien, et je peux lui expliquer pourquoi, pour qu'il propose autre chose.

Ces demandes peuvent paraître pénibles au début. Mais c'est le meilleur moyen de voir comment l'agent travaille, et de repérer tout de suite une commande qui n'a rien à faire là. Lisez-les vraiment. Une demande d'autorisation qu'on valide sans la lire ne protège de rien.

## 8. Interrompre et revenir en arrière

*À l'écran : on lance une demande, on appuie sur Échap pendant que l'agent travaille. Puis on fait une modification avec l'agent Build, et on tape /undo : le fichier revient à son état d'avant.*

Deux réflexes indispensables maintenant.

Le premier : Échap. Si l'agent part dans une mauvaise direction pendant qu'il travaille, vous appuyez sur Échap, et il s'arrête. Vous pouvez ensuite lui donner une précision, et repartir.

Le deuxième : la commande undo. Elle annule votre dernière demande. Elle retire le message, les réponses qui ont suivi, et surtout, elle annule les modifications de fichiers que l'agent a faites. Et si vous avez annulé trop vite, la commande redo remet tout en place.

*Montrer le fichier avant, après la modification de l'agent, puis après /undo.*

Attention à une condition : pour annuler les modifications de fichiers, Open Code s'appuie sur git. Votre projet doit donc être un dépôt git. Encore une raison de toujours travailler avec git quand on utilise un agent.

## 9. Les raccourcis clavier

*À l'écran : ctrl+x puis n (nouvelle session), ctrl+x puis l (liste des sessions), ctrl+x puis m (modèles).*

La plupart de ces commandes ont aussi un raccourci clavier. Open Code utilise ce qu'on appelle une touche leader : par défaut, c'est Contrôle et X. On appuie dessus, puis sur une lettre. Contrôle X puis N, pour une nouvelle session. Contrôle X puis L, pour la liste des sessions. Contrôle X puis M, pour les modèles. Contrôle X puis U, pour annuler.

Tout ça se personnalise, ainsi que le thème, dans un fichier de configuration à part, réservé à l'interface. La liste complète des raccourcis est dans la documentation.

## 10. Utiliser Open Code sans l'interface

*À l'écran : dans un terminal, opencode run avec une demande courte ; la réponse s'affiche et la commande se termine.*

Pour finir, on peut aussi se servir d'Open Code sans ouvrir l'interface. La commande opencode run prend une demande en paramètre, fait le travail, et rend la main. C'est pratique dans un script, ou pour une question rapide.

Et on retrouve l'architecture client et serveur dont on a parlé dans la vidéo 8. La commande opencode serve lance l'agent comme un serveur, sans interface. opencode web ouvre une interface dans le navigateur. Et opencode attach permet de brancher un terminal sur un serveur qui tourne déjà.

*[+] Bloc optionnel*

Il y a aussi une commande pratique pour garder un œil sur vos dépenses : opencode stats, qui affiche des statistiques sur votre utilisation. Et opencode models, qu'on a déjà vue, liste tous les modèles disponibles chez vos fournisseurs. Prenez l'habitude de regarder vos statistiques de temps en temps, surtout au début : c'est le meilleur moyen de comprendre combien vous coûte réellement votre façon de travailler avec un agent.

*[fin du bloc]*

## 11. Conclusion et transition

*À l'écran : un mémo récapitulatif à l'écran, à mettre en pause.*

Récapitulons les réflexes. Arobase pour désigner un fichier. Point d'exclamation pour lancer une commande. Barre oblique pour les commandes, avec new dès qu'on change de sujet. Tabulation pour passer en mode Plan. Échap pour interrompre. Et undo pour revenir en arrière, à condition d'être dans un dépôt git.

Avec ça, vous avez tout ce qu'il faut pour travailler. Dans la prochaine partie, on passe aux cas pratiques, sur un vrai projet. Et on commence par la situation la plus courante quand on arrive en entreprise : un projet qu'on ne connaît pas, et qu'il faut comprendre.
