# FYC Open Code : sources

Fichier tenu à jour au fil du projet. Pour chaque info : d'où elle vient et où on l'utilise.
Statut : **vérifiée** = page ouverte et lue · **à vérifier** = connue mais page pas encore ouverte.

Dernière mise à jour : 4 novembre 2026 (scripts refaits en 16 vidéos : colonne « Utilisée dans » renumérotée)

## Faits sur les outils

| Info | Source | Statut | Utilisée dans |
|---|---|---|---|
| OpenCode est publié sous licence MIT, dépôt `sst/opencode`, créé le 30/04/2025 | [ecosyste.ms : sst/opencode](https://awesome.ecosyste.ms/projects/github.com%2Fsst%2Fopencode) | vérifiée | Fiche, poster, vidéos 1 et 8 |
| OpenCode supporte « 75+ LLM providers » via Models.dev, architecture client-serveur | [promptfoo : OpenCode SDK](https://www.promptfoo.dev/docs/providers/opencode-sdk) | vérifiée (source secondaire) | Poster, vidéos 8 et 15 |
| Documentation officielle OpenCode (commandes, config, AGENTS.md, MCP) | [opencode.ai/docs](https://opencode.ai/docs) | à vérifier (page pas accessible depuis ici, à ouvrir vous-mêmes) | Fiche, vidéos 8 à 14 |
| Claude Code : preview le 24/02/2025, disponible pour tous le 22/05/2025 | [ScriptByAI : Claude Code timeline](https://www.scriptbyai.com/claude-code-timeline/) · [notes de version Anthropic](https://docs.anthropic.com/en/release-notes/claude-code) | vérifiée (source secondaire) | Fiche, vidéos 1 et 7 |
| MCP : standard ouvert présenté par Anthropic en novembre 2024, adopté ensuite par OpenAI (mars 2025) et Google DeepMind | [Wikipédia : Model Context Protocol](https://en.wikipedia.org/wiki/Model_Context_Protocol) | vérifiée | Fiche, vidéo 6 |
| Annonce officielle de MCP | [Anthropic : Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) | à vérifier | Fiche (référence) |
| Context7 : serveur MCP d'Upstash qui fournit une doc à jour et versionnée des bibliothèques, licence MIT | [GitHub : upstash/context7](https://github.com/upstash/context7) | vérifiée | Fiche, poster, vidéo 6 |
| Context7 : adresse distante `https://mcp.context7.com/mcp`, deux outils (`resolve-library-id`, `query-docs`), on l'appelle en ajoutant « use context7 » à la demande, clé gratuite recommandée pour des limites plus hautes, conseil de préciser la version | [GitHub : upstash/context7](https://github.com/upstash/context7) (lu le 01/11/2026) | vérifiée | Vidéos 6, 9 et 12 |
| MCP : définition officielle (« standard open source pour connecter des applications d'IA à des systèmes externes »), analogie du port USB-C, rôles hôte / client / serveur, primitives tools / resources / prompts, transports stdio et Streamable HTTP | [modelcontextprotocol.io : introduction](https://modelcontextprotocol.io/introduction) · [architecture](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture.md) (lus le 01/11/2026) | vérifiée | Vidéo 6 |
| MCP : annonce et mise en open source par Anthropic le 25/11/2024 | [Anthropic : Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) (lu le 01/11/2026) | vérifiée | Vidéo 6, fiche |
| OpenCode : installation (`curl -fsSL https://opencode.ai/install \| bash`, `npm install -g opencode-ai`, Homebrew, Windows via choco/scoop/npm, Docker) ; prérequis : terminal moderne et clés d'API ; WSL recommandé sur Windows ; `/init` crée `AGENTS.md`, à committer | [opencode.ai/docs](https://opencode.ai/docs) (lu le 01/11/2026) | vérifiée | Vidéo 9, et vidéo 16 (image Docker) |
| OpenCode : deux versions majeures (1 et 2), même commande `opencode`, pas installables côte à côte ; la page d'installation suit la v1 ; l'outil ne se met jamais à jour tout seul (`/update`) | [opencode.ai/docs](https://opencode.ai/docs) · [cli](https://opencode.ai/docs/cli) · [tui](https://opencode.ai/docs/tui) (lus le 01/11/2026) | vérifiée | Vidéos 1, 8 et 9 |
| OpenCode : connexion d'un fournisseur avec `/connect` (interface) ou `opencode auth login` (terminal), `opencode auth list` ; clés rangées dans `~/.local/share/opencode/auth.json` ; lit aussi les variables d'environnement et un `.env` du projet | [opencode.ai/docs/cli](https://opencode.ai/docs/cli) · [opencode.ai/docs](https://opencode.ai/docs) (lus le 01/11/2026) | vérifiée | Vidéo 9 |
| OpenCode : commandes de l'interface (`/connect`, `/models`, `/init`, `/new`, `/sessions`, `/compact`, `/undo`, `/redo`, `/export`, `/editor`, `/themes`, `/details`, `/thinking`, `/help`, `/update`) ; `@` pour désigner un fichier ; `!` pour lancer une commande ; `/undo` et `/redo` reposent sur git (le projet doit être un dépôt git) ; pas de commande `/share` documentée | [opencode.ai/docs/tui](https://opencode.ai/docs/tui) (lu le 01/11/2026) | vérifiée | Vidéos 10, 11, 12, 13 et 14 |
| OpenCode : touche leader `ctrl+x`, Tab pour changer d'agent, `ctrl+p` pour la liste des commandes, Échap pour interrompre ; raccourcis et thème dans `tui.json` | [opencode.ai/docs/keybinds](https://opencode.ai/docs/keybinds) (lu le 01/11/2026) | vérifiée | Vidéo 10 |
| OpenCode : commandes `opencode run`, `serve`, `web`, `attach`, `models`, `stats`, `upgrade` | [opencode.ai/docs/cli](https://opencode.ai/docs/cli) (lu le 01/11/2026) | vérifiée | Vidéos 8, 10 et 12 |
| OpenCode : config `opencode.json` globale (`~/.config/opencode/`) et projet (racine), fusionnées, le projet l'emporte en cas de conflit ; ligne `$schema` | [opencode.ai/docs/config](https://opencode.ai/docs/config) (lu le 01/11/2026) | vérifiée | Vidéos 8 et 9 |
| OpenCode : agents principaux Build (tous les outils) et Plan (pas de modification de fichiers sauf ses notes de plan ; ne restreint pas `bash`, qui suit les permissions) ; sous-agents General et Explore, appelés avec `@` ; agents personnalisés | [opencode.ai/docs/agents](https://opencode.ai/docs/agents) (lu le 01/11/2026) | vérifiée | Vidéos 4, 8, 10, 11, 12 et 15 |
| OpenCode : permissions `allow` / `ask` / `deny` ; par défaut la plupart sont sur `allow` (y compris `bash`) ; `doom_loop` et `external_directory` sur `ask` ; lecture des `.env` sur `ask` | [opencode.ai/docs/permissions](https://opencode.ai/docs/permissions) (lu le 01/11/2026) | vérifiée | Vidéos 4, 8, 9, 13, 15 et 16 |
| OpenCode : format des serveurs MCP distants (`type: remote`, `url`) et locaux (`type: local`, `command`), exemple Context7 | [opencode.ai/docs/mcp-servers](https://opencode.ai/docs/mcp-servers) (lu le 01/11/2026) | vérifiée | Vidéo 9 |
| OpenCode : `AGENTS.md` du projet et global ; si pas de `AGENTS.md`, lit le `CLAUDE.md` du projet | [opencode.ai/docs/rules](https://opencode.ai/docs/rules) (lu le 01/11/2026) | vérifiée | Vidéos 4, 8 et 15 |
| OpenCode : « 75+ LLM providers » via l'AI SDK et Models.dev, modèles locaux, tout fournisseur compatible OpenAI ; liste de modèles testés par l'équipe (OpenCode Models) et abonnement à petit prix (OpenCode Go) | [opencode.ai/docs/providers](https://opencode.ai/docs/providers) (lu le 01/11/2026) | vérifiée | Vidéos 8 et 15 |
| OpenCode + Ollama : adresse locale `http://localhost:11434/v1` ; si les appels d'outils échouent, augmenter `num_ctx` | [opencode.ai/docs/providers](https://opencode.ai/docs/providers) (page lue en partie) | à vérifier (exemple JSON exact à relire) | Vidéos 8 et 9 |
| OpenCode : la doc pointe maintenant vers le dépôt `anomalyco/opencode` (releases, Homebrew `anomalyco/tap/opencode`), alors que la ligne licence plus haut cite `sst/opencode` | [opencode.ai/docs](https://opencode.ai/docs) (lu le 01/11/2026) | à vérifier (changement d'organisation sur GitHub ?) | Vidéos 1 et 8, fiche, poster |
| Claude Code : installation native (`curl -fsSL https://claude.ai/install.sh \| bash`, PowerShell sur Windows), npm possible ; nécessite un compte Pro, Max, Ultra, Team, Enterprise ou Console, pas l'offre gratuite ; disponible en terminal, extensions VS Code et JetBrains, application de bureau, web | [code.claude.com/docs/en/setup](https://code.claude.com/docs/en/setup) · [overview](https://code.claude.com/docs/en/overview) (lus le 01/11/2026) | vérifiée | Vidéo 7 |
| Claude Code : `CLAUDE.md` (projet, utilisateur, local), à garder sous 200 lignes, pris comme du contexte et pas comme des règles imposées ; `/init` ; mode plan avec Shift+Tab ; hooks ; sous-agents ; MCP ; skills ; mode sans interface `claude -p` | [code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory) · [overview](https://code.claude.com/docs/en/overview) (lus le 01/11/2026) | vérifiée | Vidéos 7 et 15 |
| Claude Code : coût moyen en entreprise d'environ 13 $ par développeur et par jour actif, moins de 30 $ par jour pour 90 % des utilisateurs ; Sonnet gère bien la plupart des tâches de code et coûte moins cher qu'Opus | [code.claude.com/docs/en/costs](https://code.claude.com/docs/en/costs) (lu le 01/11/2026) | vérifiée | Vidéos 7 et 8 |

## Articles scientifiques (cités dans la fiche)

Références connues et très citées, mais pas rouvertes ici : à vérifier avant le rendu final.

| Idée | Référence | Utilisée dans |
|---|---|---|
| Architecture Transformer, base des LLM | Vaswani et al. (2017), *Attention Is All You Need*, NeurIPS | Fiche, vidéo 2 (bloc [+]) |
| Codex, le modèle derrière les débuts de GitHub Copilot | Chen et al. (2021), *Evaluating Large Language Models Trained on Code*, arXiv:2107.03374 | Fiche, vidéo 1 (bloc [+]) |
| Réglage par retour humain (RLHF) | Ouyang et al. (2022), *Training language models to follow instructions with human feedback*, NeurIPS | Fiche, vidéo 2 (bloc [+]) |
| Un modèle qui alterne raisonnement et actions (base des agents) | Yao et al. (2023), *ReAct*, ICLR (prépublié en 2022) | Fiche, vidéo 3 (bloc [+]) |
| Un modèle qui apprend à utiliser des outils | Schick et al. (2023), *Toolformer*, NeurIPS | Fiche, vidéo 4 (bloc [+]) |
| Évaluer les agents sur de vrais tickets GitHub | Jimenez et al. (2024), *SWE-bench*, ICLR | Fiche, vidéo 3 (bloc [+]) |
| « Lost in the middle » : le milieu d'un long contexte est moins bien exploité | Liu et al. (2024), *Lost in the Middle*, TACL 12 | Fiche, vidéo 5 (bloc [+]) |
| RAG | Lewis et al. (2020), *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*, NeurIPS | Fiche, vidéo 5 |
| Injection de prompt indirecte | Greshake et al. (2023), *Not what you've signed up for*, AISec '23 | Fiche, vidéo 16 |

## Mesures faites dans le projet

- Débit de parole après montage : 1 088 mots pour 4 min 44 de vidéo 1 montée, soit environ 230 mots/min (voix d'Ibrahim). Sert à dimensionner les scripts (`outils/compter_mots.py`).

## Infos sans source pour l'instant

À sourcer ou à retirer :
- « En anglais, un token fait environ 4 caractères » (vidéo 2) : à sourcer via la doc d'un fournisseur (OpenAI ou Anthropic).
- Tabnine et Kite comme exemples d'autocomplétion avant 2021 (vidéo 1).
- Les deux familles de modèles : fermés via une API (Claude, GPT, Gemini) et ouverts, téléchargeables (vidéo 2) : connu, mais à appuyer sur une source.
- Open Code créé par l'équipe derrière SST (vidéo 1) : cohérent avec le dépôt `sst/opencode`, mais voir la ligne « anomalyco » plus haut.
- Claude Code demande l'accord avant de modifier un fichier ou de lancer une commande, par défaut (vidéos 7 et 15) : à confirmer dans code.claude.com/docs (page permissions).
- Raccourcis Open Code après la touche leader : ctrl+x puis n, l, m, u (vidéo 10) : à confirmer dans opencode.ai/docs/keybinds.
- Fichier `CLAUDE.md` pour Claude Code, `AGENTS.md` pour OpenCode (poster, fiche) : à confirmer dans les deux docs officielles.
