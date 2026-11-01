# Vidéo 7 : Open Code, coûts et souveraineté

Durée visée : 9 min. Les lignes en italique décrivent l'écran ou donnent une consigne : elles ne se lisent pas.
Enregistrer tout, y compris les blocs [+]. Au montage, les blocs [+] sont gardés seulement si la vidéo reste sous 9 min 30.
Sources : opencode.ai/docs (intro, config, providers, agents, permissions, rules, cli), lues le 01/11/2026. Open Code évolue vite : revérifier la veille du tournage.

## 1. Intro

*À l'écran : le logo Claude Code de la fin de la vidéo 6 s'efface, le titre « Open Code » arrive.*

Dans la vidéo précédente, on a vu Claude Code : un agent très abouti, mais fermé, payant, et lié aux modèles d'Anthropic. Aujourd'hui, on passe au sujet principal de ce cours : Open Code.

On va voir ce que c'est, comment il est construit, et surtout ce qui le distingue de Claude Code. Puis on parlera de deux sujets qu'on oublie souvent quand on choisit un outil : combien ça coûte vraiment, et où partent vos données.

## 2. Ce qu'est Open Code

*À l'écran : la page d'accueil d'opencode.ai, puis trois mots-clés : « terminal », « open source », « licence MIT ».*

Open Code, c'est un agent de développement qui tourne dans votre terminal. Sur le principe, il fait la même chose que Claude Code : vous lui parlez, il lit votre projet, il modifie les fichiers, il lance les commandes. La même boucle, avec les mêmes types d'outils.

La grande différence, c'est qu'il est open source, sous licence MIT. Tout son code est public. N'importe qui peut le lire, le modifier, ou l'utiliser dans un autre projet, y compris commercial.

Petite précision avant d'aller plus loin. Plusieurs projets ont un nom proche, alors si vous cherchez « open code » sur internet, vous risquez de tomber sur autre chose. Le projet dont on parle dans ce cours, c'est celui du site opencode.ai. C'est là que se trouvent la documentation officielle et le lien vers le code source.

*[+] Bloc optionnel*

Un mot aussi sur le rythme du projet. Open Code évolue très vite. Des commandes changent de nom, des fonctionnalités apparaissent, et la documentation mentionne déjà deux versions majeures. C'est le signe d'un projet vivant, mais ça a une conséquence pratique : un tutoriel d'il y a six mois peut être en partie faux. Même pour ce cours, on a vérifié chaque commande dans la documentation officielle. Prenez ce réflexe vous aussi. Et notez que l'outil ne se met jamais à jour tout seul : c'est vous qui décidez quand passer à une nouvelle version.

*[fin du bloc]*

## 3. Le harness est ouvert

*À l'écran : un schéma : le harness au centre, avec un cadenas ouvert. Autour, ce qu'on peut lire : le prompt système, les descriptions d'outils, la boucle.*

Vous vous souvenez de la vidéo 3 : l'outil qu'on installe, c'est le harness, la boucle d'orchestration autour du modèle. Chez Claude Code, ce harness est fermé. Chez Open Code, il est ouvert.

Concrètement, ça veut dire que vous pouvez aller lire exactement ce que l'outil envoie au modèle. Le prompt système, la description de chaque outil, la façon dont il gère le contexte. Rien n'est caché. Si vous vous demandez pourquoi l'agent a fait quelque chose, vous pouvez aller voir dans le code. Et si quelque chose ne vous plaît pas, vous pouvez le changer.

Pour une entreprise, c'est aussi une question de confiance. Un outil qu'on peut auditer, c'est un outil dont on peut vérifier ce qu'il envoie, et à qui.

## 4. Une architecture client et serveur

*À l'écran : un serveur au centre, et plusieurs clients autour : le terminal, une page web, un script.*

Autre particularité : Open Code est construit en deux morceaux. D'un côté, un serveur, qui fait tourner l'agent. De l'autre, une interface, qui est simplement un client de ce serveur.

Quand vous tapez « opencode » dans votre terminal, les deux se lancent ensemble et vous ne voyez pas la différence. Mais on peut aussi les séparer. Il y a une commande pour lancer le serveur seul, sans interface. Une autre pour ouvrir une interface web dans le navigateur. Et une autre pour brancher un terminal sur un serveur qui tourne déjà, éventuellement sur une autre machine.

À quoi ça sert ? À piloter l'agent depuis d'autres outils, à le faire tourner sur un serveur distant plus puissant, ou à l'intégrer dans une chaîne d'automatisation. Il y a d'ailleurs aussi une commande pour lui passer une demande directement, sans interface, comme on l'a vu pour Claude Code.

## 5. Le multi-provider, la vraie différence

*À l'écran : « 75+ fournisseurs » en grand, puis des logos qui apparaissent autour : Anthropic, OpenAI, Google, Mistral, Groq, OpenRouter, et « modèles locaux ».*

Et voici le point qui distingue le plus Open Code : il n'est attaché à aucun fournisseur de modèles. La documentation annonce plus de 75 fournisseurs compatibles. Il s'appuie pour ça sur une bibliothèque qui sait parler à de nombreuses API, et sur Models.dev, une base qui recense les modèles disponibles avec leurs caractéristiques.

Donc vous pouvez utiliser les modèles d'Anthropic, ceux d'OpenAI, ceux de Google, de Mistral, et beaucoup d'autres. Et même n'importe quel service qui respecte le format d'API d'OpenAI, qui est devenu une sorte de standard.

Mais surtout, vous pouvez faire tourner un modèle en local, sur votre propre machine, avec des outils comme Ollama ou LM Studio. Dans ce cas, aucune requête ne sort de votre ordinateur.

Et vous pouvez changer de modèle à tout moment, même en pleine session. Ça permet de choisir le bon modèle pour chaque tâche : un modèle rapide et pas cher pour explorer un projet ou poser des questions, et un modèle plus puissant quand il faut écrire du code délicat.

*[+] Bloc optionnel*

Attention quand même : tous les modèles ne se valent pas pour faire tourner un agent. On l'a vu dans la vidéo 3, il faut qu'un modèle soit bon pour appeler des outils de façon fiable, et enchaîner beaucoup d'actions sans se perdre. Un petit modèle local peut être très bien pour répondre à une question, et beaucoup moins à l'aise pour modifier un projet entier. La documentation d'Open Code le dit d'ailleurs pour Ollama : si les appels d'outils échouent, il faut augmenter la taille de contexte du modèle. C'est pour ça que l'équipe d'Open Code propose aussi une liste de modèles qu'elle a testés et validés avec l'outil.

*[fin du bloc]*

## 6. La configuration

*À l'écran : un fichier opencode.json simple, puis un fichier AGENTS.md à côté.*

Côté configuration, tout passe par un fichier qui s'appelle opencode.json. Il peut exister à deux endroits : un fichier global, dans votre dossier utilisateur, pour vos réglages personnels, et un fichier dans le projet, pour les réglages propres à ce projet. Les deux se combinent.

Dedans, on peut choisir le modèle par défaut, brancher des serveurs MCP comme Context7, définir des agents personnalisés, et régler les permissions.

Pour les instructions du projet, Open Code utilise un fichier AGENTS.md à la racine. C'est l'équivalent de CLAUDE.md chez Claude Code. Mais avec une différence intéressante : AGENTS.md est une convention ouverte, que plusieurs outils savent lire. Vous l'écrivez une fois, et il sert même si vous changez d'outil. Et Open Code est assez souple : si votre projet a déjà un CLAUDE.md mais pas de AGENTS.md, il lit le CLAUDE.md à la place. Pratique si vous venez de Claude Code.

## 7. Les agents et les permissions

*À l'écran : deux cartes « Build » et « Plan », avec la touche Tabulation entre les deux. Puis un extrait de configuration des permissions.*

Open Code est livré avec deux agents principaux, entre lesquels on bascule avec la touche Tabulation. L'agent Build, celui par défaut, qui a accès à tous les outils. Et l'agent Plan, qui sert à réfléchir et à analyser : il n'a pas le droit de modifier vos fichiers, à part ses propres notes de plan. On s'en servira beaucoup dans les cas pratiques.

Côté permissions, chaque type d'action peut être réglé sur trois valeurs : autoriser, demander, ou refuser. Et c'est un point important à connaître : par défaut, Open Code autorise la plupart des actions sans rien demander. Y compris lancer des commandes. Seules quelques actions sensibles demandent votre accord, comme lire un fichier .env qui contient souvent des mots de passe.

Ça rend l'outil très fluide, mais c'est à vous de resserrer les règles si vous voulez plus de contrôle. On le fera dès l'installation, dans la prochaine vidéo.

*[+] Bloc optionnel*

Petite subtilité sur l'agent Plan : il ne peut pas modifier vos fichiers, mais il n'est pas bloqué pour lancer des commandes. Pour ça, il suit vos règles de permissions générales. Donc si vos permissions autorisent toutes les commandes, l'agent Plan peut lui aussi en lancer. C'est le genre de détail qu'on ne découvre qu'en lisant la documentation, et c'est une bonne raison de régler les permissions soi-même plutôt que de compter sur les réglages par défaut.

*[fin du bloc]*

## 8. Combien ça coûte vraiment

*À l'écran : « Gratuit ≠ sans coût » en grand. Puis trois colonnes : « Clé API », « Abonnement », « Modèle local ».*

Parlons argent. Open Code lui-même est gratuit, puisqu'il est open source. Mais l'outil n'est que le harness. L'intelligence, elle, vient du modèle, et le modèle, il faut le payer d'une façon ou d'une autre.

Première option : vous apportez votre propre clé d'API. Vous créez un compte chez un fournisseur, vous branchez la clé dans Open Code, et vous payez chaque token consommé, au prix du fournisseur. L'avantage : vous voyez exactement ce que vous consommez, et vous choisissez le modèle selon votre budget.

Deuxième option : un modèle local. Là, plus de facture par token. Mais il faut une machine assez puissante, avec une bonne carte graphique de préférence. Le modèle tourne plus lentement, et il est souvent moins capable que les gros modèles des fournisseurs.

Et entre les deux, l'équipe d'Open Code propose aussi ses propres offres d'accès à des modèles, dont un abonnement à petit prix. À comparer avec ce que vous coûterait une clé d'API classique.

Ce qu'il faut garder en tête, c'est qu'un agent consomme beaucoup. On l'a dit dans la vidéo 2 : à chaque tour de boucle, tout le contexte repart. Et on a vu dans la vidéo 6 l'ordre de grandeur donné par Anthropic pour Claude Code : une dizaine de dollars par développeur et par jour en moyenne en entreprise. Avec Open Code, la facture dépend entièrement du modèle choisi. Elle peut être bien plus basse avec un modèle économe, ou plus haute avec un modèle très puissant.

*[+] Bloc optionnel*

Face à ça, l'abonnement de Claude Code a un avantage : son coût est prévisible. Vous payez un montant fixe par mois, et vous n'avez pas de mauvaise surprise, dans les limites de l'offre. Avec une clé d'API, un agent qui part en boucle pendant une heure peut coûter cher sans que vous vous en rendiez compte. C'est pour ça qu'Open Code affiche ce que la session a consommé, et que la plupart des fournisseurs permettent de fixer un plafond de dépenses. Si vous utilisez une clé d'API, réglez ce plafond dès le premier jour.

*[fin du bloc]*

## 9. Souveraineté et confidentialité

*À l'écran : trois scénarios avec une flèche vers « où partent les données » : Claude Code → Anthropic ; Open Code + fournisseur → le fournisseur choisi ; Open Code + local → reste sur la machine.*

Dernier sujet, et pas le moindre : où partent vos données ? Parce qu'un agent envoie au modèle votre demande, mais aussi le contenu de tous les fichiers qu'il lit, et la sortie de toutes les commandes qu'il lance. Autrement dit, une bonne partie de votre code.

Avec Claude Code, tout ça part chez Anthropic, selon leurs conditions d'utilisation.

Avec Open Code et un fournisseur dans le cloud, c'est pareil : vos données partent chez ce fournisseur. Mais c'est vous qui le choisissez, avec ses conditions, ses garanties, et l'endroit où il héberge ses serveurs.

Et avec Open Code et un modèle local, rien ne quitte votre machine. Pour une entreprise qui travaille sur du code confidentiel, pour un secteur réglementé comme la santé ou la finance, ou simplement pour travailler sans connexion, ça peut tout changer.

Il y a aussi la question de la dépendance. Avec Claude Code, si Anthropic change ses prix ou ses conditions, vous n'avez pas d'autre choix que de suivre ou de changer d'outil. Avec Open Code, vous changez de modèle, et vous gardez votre outil, votre configuration et votre fichier AGENTS.md.

## 10. Le compromis, honnêtement

*À l'écran : une balance : d'un côté « résultats immédiats », de l'autre « contrôle et liberté ».*

Alors, Open Code est-il simplement meilleur ? Non, ce serait trop simple. C'est un compromis.

Claude Code, grâce à son intégration très serrée avec les modèles Claude, donne souvent de très bons résultats tout de suite, sans configuration. Open Code vous donne la liberté et le contrôle : le choix du modèle, la transparence, la maîtrise de vos données. Mais en échange, il demande un peu plus de configuration, et la qualité des résultats dépend beaucoup du modèle que vous branchez.

On fera une comparaison complète à la fin du cours. Pour l'instant, retenez ça : Open Code ne remplace pas l'intelligence du modèle, il vous laisse choisir laquelle utiliser.

## 11. Conclusion et transition

*À l'écran : récapitulatif en quatre points, puis un terminal vide avec un curseur.*

On résume. Open Code est un agent de développement open source, sous licence MIT. Son code est lisible et modifiable. Il fonctionne en client et serveur. Il est compatible avec plus de 75 fournisseurs et avec des modèles locaux. Il est gratuit, mais le modèle, lui, se paie. Et il vous laisse décider où partent vos données.

Assez de théorie. Dans la prochaine vidéo, on ouvre le terminal, on installe Open Code, et on le configure proprement, étape par étape.
