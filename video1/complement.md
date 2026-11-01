# Vidéo 1 : complément à enregistrer

La vidéo 1 montée fait 4 min 44, sous le minimum de 5 min par vidéo. Ces deux passages (environ 350 mots, à peu près 1 min 30 au débit d'Ibrahim) s'insèrent dans la partie 8 « Ce qu'un LLM est, et ce qu'il n'est pas ». La vidéo passe alors à environ 6 min 15.
Les lignes en italique décrivent l'écran ou donnent une consigne : elles ne se lisent pas.
À enregistrer par Ibrahim, avec la même voix et le même micro que la vidéo 1, puis remonter avec outils/monter_audio.py.

## Passage A : un exemple d'hallucination

*Se place juste après : « Il peut vous inventer une fonction qui n'existe pas, avec exactement la même assurance qu'une vraie. »*

*À l'écran : une demande à un chat, puis une réponse avec du code ; le nom d'une fonction se surligne en rouge, avec la mention « n'existe pas ».*

Prenons un exemple très courant. Vous demandez à un assistant comment faire quelque chose avec une bibliothèque que vous utilisez. Il vous répond avec un bout de code propre, bien présenté, avec des commentaires. Et dedans, il appelle une fonction au nom parfaitement logique. Le genre de nom qu'on s'attendrait à trouver.

Sauf que cette fonction n'existe pas. Elle n'a jamais existé. Le modèle a juste produit la suite la plus probable : vu le reste du code, c'est ce nom-là qui avait l'air le plus naturel. Vous copiez, vous lancez, et vous avez une erreur. Ou pire, la fonction existe, mais dans une autre version de la bibliothèque, et elle ne fait pas tout à fait la même chose.

Le piège, c'est que rien dans la réponse ne vous prévient. Le ton est le même pour une vraie fonction et pour une fonction inventée. C'est pour ça qu'avec un LLM, on vérifie toujours. Et on verra plus tard dans le cours qu'il existe des outils pour limiter ce problème, en donnant au modèle la vraie documentation.

## Passage B : la fenêtre de contexte

*Se place juste après : « Il ne peut pas tout garder en tête : il y a une taille maximale à ce qu'on peut lui envoyer. »*

*À l'écran : un grand rectangle qui se remplit : instructions, conversation, fichiers. Arrivé au bord, les premiers éléments sortent du cadre.*

Cette taille maximale, on l'appelle la fenêtre de contexte, et elle se compte en tokens. Selon les modèles, elle va de quelques dizaines de milliers à plusieurs centaines de milliers de tokens. Ça paraît énorme, mais tout ce qu'on envoie au modèle passe dedans : les instructions, toute la conversation depuis le début, et les fichiers qu'on lui montre.

Sur une longue conversation, ou quand on lui donne beaucoup de code à lire, on finit par atteindre la limite. Et à ce moment-là, il faut faire de la place. Une partie de ce qu'on lui avait donné au début n'est plus là. C'est pour ça qu'un assistant peut sembler oublier, au bout d'un moment, une consigne que vous lui aviez donnée au début.

On verra dans une prochaine vidéo que bien gérer ce contexte, c'est une grande partie du travail quand on utilise un agent.
