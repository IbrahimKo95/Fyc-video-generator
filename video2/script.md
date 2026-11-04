# Vidéo 2 : Qu'est-ce qu'un LLM ?

Partie du plan : P1.2 « Qu'est-ce qu'un LLM ? ».
Bornes : 6:45 – 7:30 (min = quelqu'un de rapide qui lit tout, blocs [+] compris ; max = quelqu'un de posé qui ne lit que le texte principal).
Les lignes en italique décrivent l'écran ou donnent une consigne : elles ne se lisent pas.
Enregistrer tout, y compris les blocs [+]. Au montage, les blocs [+] sont gardés un par un tant que la vidéo reste sous sa borne max.
Sources : voir sources.md (Transformer, RLHF ; la règle des 4 caractères par token reste à sourcer).

*Les parties 2, 3, 4, 6, 7 et 8 reprennent mot pour mot le texte déjà enregistré par Ibrahim (ancienne vidéo 1, parties 5 à 9) : ces prises peuvent être réutilisées au montage. À enregistrer : l'intro, la partie 5, l'exemple d'hallucination (partie 6) et le passage sur la fenêtre de contexte (partie 7), qui viennent de l'ancien video1/complement.md, et les blocs [+].*

## 1. Intro

*À l'écran : le titre « Qu'est-ce qu'un LLM ? », puis le mot LLM qui se déplie : Large Language Model.*

Dans la vidéo précédente, on a vu comment on est passés de l'autocomplétion aux agents qui modifient un projet entier. Tous ces outils, Copilot, ChatGPT, Claude Code, Open Code, reposent sur la même brique. Et si on veut comprendre pourquoi un agent réussit, ou pourquoi il se plante, il faut commencer par elle.

## 2. Ce qu'est un LLM

*À l'écran : la phrase « Le développeur relance les… », puis les barres de probabilité.*

Maintenant, ouvrons le capot. Au cœur de tous ces outils, il y a ce qu'on appelle un LLM, pour Large Language Model, un grand modèle de langage.

Et en vrai, le principe est super simple. Un LLM, c'est une fonction qui prend un début de texte, et qui prédit le morceau qui vient après. C'est tout.

Prenons un exemple. Si je vous dis : « Le développeur relance les… », vous avez sûrement une idée de la suite. Le modèle aussi. Il calcule une probabilité pour chaque suite possible : « tests », c'est très probable, « commandes », un peu moins, « dés », presque pas. Et il choisit parmi les plus probables.

Alors pourquoi ça a l'air aussi intelligent ? Juste parce que cette fonction est gigantesque, et qu'elle a été entraînée sur une quantité de texte énorme. Mais à la base, c'est vraiment ça : prédire la suite.

*[+] Bloc optionnel*

Et comme il choisit parmi les suites les plus probables, et pas toujours la même, un modèle ne répond pas forcément deux fois pareil à la même question. Une fois il dira « tests », une autre fois « commandes ». Sur une phrase, ce n'est pas grave. Mais sur un agent qui enchaîne des dizaines de décisions, ça veut dire que deux essais avec exactement la même demande peuvent prendre des chemins différents. On le verra pendant les démonstrations : l'agent ne fait jamais tout à fait deux fois la même chose. Ce n'est pas un bug, c'est la nature même du modèle.

*[fin du bloc]*

*[+] Bloc optionnel*

Cette fonction géante, elle a une architecture bien précise. Presque tous les grands modèles actuels reposent sur ce qu'on appelle le Transformer, présenté en 2017 par des chercheurs de Google dans un article resté célèbre, « Attention Is All You Need ». Son idée principale, c'est le mécanisme d'attention : pour prédire la suite, le modèle peut regarder tous les mots du texte en même temps, et donner plus de poids à ceux qui comptent pour la prédiction. C'est ce qui lui permet de tenir compte d'une information donnée bien plus haut dans le texte.

*[fin du bloc]*

## 3. Les tokens

*À l'écran : le mot « développement » se découpe en trois morceaux colorés.*

Petit détail important : le modèle ne lit pas des mots. Il lit des tokens, c'est-à-dire des morceaux de mots.

Par exemple, un mot comme « développement » peut être découpé en trois ou quatre tokens. En anglais, on compte en moyenne un token pour à peu près quatre caractères.

Et pourquoi c'est important pour nous ? Parce qu'avec un LLM, tout se compte en tokens. Ce que vous lui envoyez, ce qu'il vous répond, et donc ce que ça vous coûte. On y reviendra plus tard, notamment quand on parlera du prix d'utilisation d'un agent comme Open Code.

## 4. Comment on fabrique un LLM

*À l'écran : les trois cartes apparaissent l'une après l'autre.*

Maintenant, comment on obtient un LLM ? En gros, il y a trois étapes.

La première, c'est le pré-entraînement. On montre au modèle une quantité énorme de texte : des pages web, des livres, du code. On parle de milliers de milliards de tokens. Et on lui fait faire un seul exercice, encore et encore : deviner le token suivant. À la fin, il connaît énormément de choses, mais il ne sait pas vraiment discuter.

La deuxième étape, c'est le post-entraînement. On lui montre des exemples de conversations, et on l'ajuste avec des retours humains. C'est ce qu'on appelle le RLHF. C'est cette étape qui lui apprend à suivre des instructions et à répondre de façon utile.

*[+] Bloc optionnel*

RLHF, ça veut dire apprentissage par renforcement à partir de retours humains. Le principe a été popularisé en 2022 par un article d'OpenAI. On fait écrire au modèle plusieurs réponses à une même demande, et des personnes les classent, de la meilleure à la moins bonne. À partir de ces classements, on entraîne un second modèle qui apprend à prédire quelle réponse un humain préférerait. Et c'est ce second modèle qui sert ensuite à ajuster le premier. Ce qui est frappant dans cet article, c'est que les gens préféraient souvent les réponses d'un modèle bien plus petit, mais réglé de cette façon, à celles d'un modèle énorme qui ne l'était pas.

*[fin du bloc]*

Et la troisième étape, c'est l'inférence. Ça, c'est quand vous l'utilisez. Le modèle génère un token, l'ajoute à la suite du texte, génère le suivant, et ainsi de suite. C'est pour ça que vous voyez les réponses s'écrire petit à petit à l'écran.

## 5. Les modèles qu'on trouve aujourd'hui

*À l'écran : deux familles de cartes. À gauche « modèles fermés, via une API » : Claude, GPT, Gemini. À droite « modèles ouverts, téléchargeables » : un ordinateur avec quelques noms de modèles.*

Des LLM, il en existe beaucoup, et on peut les ranger en deux grandes familles.

D'un côté, les modèles fermés. Ce sont ceux des grandes entreprises : Claude chez Anthropic, GPT chez OpenAI, Gemini chez Google. On ne peut pas les télécharger. On les utilise à distance, en envoyant notre texte à leurs serveurs, et on paie à l'usage, au nombre de tokens.

De l'autre, les modèles ouverts. Leurs paramètres sont publiés, donc on peut les télécharger et les faire tourner sur sa propre machine, ou sur un serveur à soi. Ils sont en général moins puissants que les meilleurs modèles fermés, et il faut une machine solide pour les faire tourner. Mais rien ne sort de chez vous.

Retenez bien cette distinction. Elle sera au cœur de la différence entre Claude Code, qui ne fonctionne qu'avec Claude, et Open Code, qui vous laisse choisir dans les deux familles.

## 6. Ce qu'un LLM est, et ce qu'il n'est pas

*À l'écran : deux colonnes, les coches vertes puis les croix rouges.*

De tout ça, il y a quelques points à bien retenir, parce qu'ils expliquent la plupart des comportements bizarres que vous verrez avec ces outils.

D'abord, un LLM ce n'est pas une base de données. Il ne va pas chercher une info quelque part : il génère la suite la plus probable.

Ensuite, il n'a pas de mémoire. Entre deux appels, il ne se souvient de rien. Tout ce qu'il sait de votre tâche, c'est ce que vous lui donnez au moment où vous l'appelez. On appelle ça le contexte, et on en reparlera beaucoup, parce que c'est central.

Autre chose : il peut halluciner. Il produit du texte qui a l'air juste, pas du texte vérifié. Il peut vous inventer une fonction qui n'existe pas, avec exactement la même assurance qu'une vraie.

*À l'écran : une demande à un chat, puis une réponse avec du code ; le nom d'une fonction se surligne en rouge, avec la mention « n'existe pas ».*

Prenons un exemple très courant. Vous demandez à un assistant comment faire quelque chose avec une bibliothèque que vous utilisez. Il vous répond avec un bout de code propre, bien présenté, avec des commentaires. Et dedans, il appelle une fonction au nom parfaitement logique. Le genre de nom qu'on s'attendrait à trouver.

Sauf que cette fonction n'existe pas. Elle n'a jamais existé. Le modèle a juste produit la suite la plus probable : vu le reste du code, c'est ce nom-là qui avait l'air le plus naturel. Vous copiez, vous lancez, et vous avez une erreur. Ou pire, la fonction existe, mais dans une autre version de la bibliothèque, et elle ne fait pas tout à fait la même chose.

Le piège, c'est que rien dans la réponse ne vous prévient. Le ton est le même pour une vraie fonction et pour une fonction inventée. C'est pour ça qu'avec un LLM, on vérifie toujours. Et on verra plus tard dans le cours qu'il existe des outils pour limiter ce problème, en donnant au modèle la vraie documentation.

## 7. Date de coupure et fenêtre de contexte

*À l'écran : un calendrier avec une date barrée, puis un grand rectangle qui se remplit : instructions, conversation, fichiers. Arrivé au bord, les premiers éléments sortent du cadre.*

Il a aussi une date de coupure. Tout ce qui est sorti après son entraînement, il ne le connaît pas.

*[+] Bloc optionnel*

Pour du code, cette date de coupure pose un problème bien particulier. Les bibliothèques changent sans arrêt : une fonction est renommée, une option disparaît, une nouvelle façon de faire devient la norme. Le modèle, lui, a appris sur du code écrit avant sa date de coupure, et souvent sur des années d'anciennes versions mélangées. Il a donc tendance à écrire du code pour une version qui n'est plus celle que vous utilisez. On verra dans la troisième partie un outil, Context7, conçu exactement pour régler ce problème.

*[fin du bloc]*

Et enfin, sa fenêtre de contexte est limitée. Il ne peut pas tout garder en tête : il y a une taille maximale à ce qu'on peut lui envoyer.

Cette taille maximale, on l'appelle la fenêtre de contexte, et elle se compte en tokens. Selon les modèles, elle va de quelques dizaines de milliers à plusieurs centaines de milliers de tokens. Ça paraît énorme, mais tout ce qu'on envoie au modèle passe dedans : les instructions, toute la conversation depuis le début, et les fichiers qu'on lui montre.

Sur une longue conversation, ou quand on lui donne beaucoup de code à lire, on finit par atteindre la limite. Et à ce moment-là, il faut faire de la place. Une partie de ce qu'on lui avait donné au début n'est plus là. C'est pour ça qu'un assistant peut sembler oublier, au bout d'un moment, une consigne que vous lui aviez donnée au début.

On verra dans une prochaine vidéo que bien gérer ce contexte, c'est une grande partie du travail quand on utilise un agent.

## 8. Conclusion et transition

*À l'écran : le cerveau dans le bocal, puis l'annonce de la vidéo 3.*

Et surtout, un LLM tout seul, ça ne fait rien. Il ne lance pas de code, il n'est connecté à rien. Il prend du texte et il renvoie du texte.

En fait, un LLM seul, c'est un peu un cerveau dans un bocal. Très intelligent, mais sans bras ni jambes.

Dans la prochaine vidéo, on va voir comment on lui donne un corps : des outils, une boucle, et c'est comme ça qu'on passe d'un simple modèle à un vrai agent IA. À tout de suite !
