# Vidéo 1 : L'IA est devenue incontournable

Version de référence : doc « Script — Vidéo 1 » sur claude.ai (https://claude.ai/artifact/SLXLp7tnRpm7prKEMAYKzx).
Les lignes en italique décrivent l'écran, elles ne se lisent pas.

## 1. Intro

*À l'écran : titre « Open Code », le terminal qui tape `opencode`.*

Salut à tous, et bienvenue dans ce cours sur Open Code, l'alternative open source à Claude Code.

Avant de mettre les mains dans l'outil, on va prendre un peu de recul. Parce que pour bien utiliser un agent IA, il faut comprendre ce qu'il y a dedans et d'où ça vient. Donc on part de la théorie, et petit à petit on va aller vers la pratique, jusqu'à utiliser Open Code sur un vrai projet.

## 2. Accroche

*À l'écran : la première question apparaît puis se fait barrer, la seconde arrive.*

Aujourd'hui, coder avec l'IA, ce n'est plus un truc de curieux. Dans beaucoup d'entreprises, c'est devenu la façon normale de travailler.

Du coup, la vraie question, ce n'est plus « est-ce qu'on utilise l'IA pour coder ? ». Ça, c'est réglé. La vraie question, c'est : « est-ce qu'on l'utilise bien ? »

Et c'est tout l'objectif de ce cours : qu'à la fin, vous sachiez faire tourner un agent sur un vrai projet, mais surtout que vous sachiez où sont les pièges.

## 3. Comment on en est arrivés là

*À l'écran : la frise se construit, une date à la fois.*

Alors, comment on en est arrivés là ? Faisons un petit retour en arrière.

Avant 2021, on avait surtout de l'autocomplétion un peu améliorée, avec des outils comme Tabnine ou Kite. Ça vous complétait la fin de la ligne. Pratique, mais ça s'arrêtait là.

En 2021, GitHub Copilot arrive, et là, c'est la première fois qu'un modèle de langage vous propose des fonctions entières, directement dans l'éditeur. Mais ça reste de la suggestion : l'outil propose, et c'est vous qui acceptez ou pas.

Fin 2022, ChatGPT sort, et on découvre le format conversation. On décrit son problème en français, on a une réponse. Par contre, il faut tout faire à la main : copier son code dans la fenêtre, recopier la réponse dans l'éditeur, et recommencer à la moindre erreur.

En 2023 et 2024, apparaissent les premiers agents. L'idée, c'est de donner au modèle des outils et une boucle. Il peut lire des fichiers, lancer des commandes, voir ce qui se passe, et réessayer.

Et en 2025, ces agents deviennent grand public, avec Claude Code, Cursor en mode agent, et des alternatives open source comme Open Code.

## 4. De l'assistant à l'agent

*À l'écran : la carte « suggère » s'éteint, la flèche, puis la carte « agit ».*

Si on devait résumer tout ça en une phrase : on est passés d'un assistant qui suggère à un agent qui agit.

Avant, l'outil vous proposait du code, et c'était à vous de le copier, de le lancer, de le tester. Maintenant, l'agent lit votre projet, modifie les fichiers, lance les commandes, et vérifie lui-même si ça marche.

Et forcément, ça change notre métier. Ce qui compte de plus en plus, ce n'est plus de taper vite. C'est de savoir bien cadrer un problème, donner le bon contexte à l'IA, et surtout relire du code qu'on n'a pas écrit soi-même.

## 5. Qu'est-ce qu'un LLM ?

*À l'écran : la phrase « Le développeur relance les… », puis les barres de probabilité.*

Maintenant, ouvrons le capot. Au cœur de tous ces outils, il y a ce qu'on appelle un LLM, pour Large Language Model, un grand modèle de langage.

Et en vrai, le principe est super simple. Un LLM, c'est une fonction qui prend un début de texte, et qui prédit le morceau qui vient après. C'est tout.

Prenons un exemple. Si je vous dis : « Le développeur relance les… », vous avez sûrement une idée de la suite. Le modèle aussi. Il calcule une probabilité pour chaque suite possible : « tests », c'est très probable, « commandes », un peu moins, « dés », presque pas. Et il choisit parmi les plus probables.

Alors pourquoi ça a l'air aussi intelligent ? Juste parce que cette fonction est gigantesque, et qu'elle a été entraînée sur une quantité de texte énorme. Mais à la base, c'est vraiment ça : prédire la suite.

## 6. Les tokens

*À l'écran : le mot « développement » se découpe en trois morceaux colorés.*

Petit détail important : le modèle ne lit pas des mots. Il lit des tokens, c'est-à-dire des morceaux de mots.

Par exemple, un mot comme « développement » peut être découpé en trois ou quatre tokens. En anglais, on compte en moyenne un token pour à peu près quatre caractères.

Et pourquoi c'est important pour nous ? Parce qu'avec un LLM, tout se compte en tokens. Ce que vous lui envoyez, ce qu'il vous répond, et donc ce que ça vous coûte. On y reviendra plus tard, notamment quand on parlera du prix d'utilisation d'un agent comme Open Code.

## 7. Comment on fabrique un LLM

*À l'écran : les trois cartes apparaissent l'une après l'autre.*

Maintenant, comment on obtient un LLM ? En gros, il y a trois étapes.

La première, c'est le pré-entraînement. On montre au modèle une quantité énorme de texte : des pages web, des livres, du code. On parle de milliers de milliards de tokens. Et on lui fait faire un seul exercice, encore et encore : deviner le token suivant. À la fin, il connaît énormément de choses, mais il ne sait pas vraiment discuter.

La deuxième étape, c'est le post-entraînement. On lui montre des exemples de conversations, et on l'ajuste avec des retours humains. C'est ce qu'on appelle le RLHF. C'est cette étape qui lui apprend à suivre des instructions et à répondre de façon utile.

Et la troisième étape, c'est l'inférence. Ça, c'est quand vous l'utilisez. Le modèle génère un token, l'ajoute à la suite du texte, génère le suivant, et ainsi de suite. C'est pour ça que vous voyez les réponses s'écrire petit à petit à l'écran.

## 8. Ce qu'un LLM est, et ce qu'il n'est pas

*À l'écran : deux colonnes, les coches vertes puis les croix rouges.*

De tout ça, il y a quelques points à bien retenir, parce qu'ils expliquent la plupart des comportements bizarres que vous verrez avec ces outils.

D'abord, un LLM ce n'est pas une base de données. Il ne va pas chercher une info quelque part : il génère la suite la plus probable.

Ensuite, il n'a pas de mémoire. Entre deux appels, il ne se souvient de rien. Tout ce qu'il sait de votre tâche, c'est ce que vous lui donnez au moment où vous l'appelez. On appelle ça le contexte, et on en reparlera beaucoup, parce que c'est central.

Autre chose : il peut halluciner. Il produit du texte qui a l'air juste, pas du texte vérifié. Il peut vous inventer une fonction qui n'existe pas, avec exactement la même assurance qu'une vraie.

Il a aussi une date de coupure. Tout ce qui est sorti après son entraînement, il ne le connaît pas.

Et enfin, sa fenêtre de contexte est limitée. Il ne peut pas tout garder en tête : il y a une taille maximale à ce qu'on peut lui envoyer.

## 9. Conclusion et transition

*À l'écran : le cerveau dans le bocal, puis l'annonce de la vidéo 2.*

Et surtout, un LLM tout seul, ça ne fait rien. Il ne lance pas de code, il n'est connecté à rien. Il prend du texte et il renvoie du texte.

En fait, un LLM seul, c'est un peu un cerveau dans un bocal. Très intelligent, mais sans bras ni jambes.

Dans la prochaine vidéo, on va voir comment on lui donne un corps : des outils, une boucle, et c'est comme ça qu'on passe d'un simple modèle à un vrai agent IA. À tout de suite !
