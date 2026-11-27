# Update a model

Bring a model back in line with the code. Propose every edit with its evidence, and write only what the user accepts.

## 1. Settle the baseline

1. Run `git status` on the model directory. If it has uncommitted changes, summarise them and ask the user to commit first, so their edits and yours never mix.
2. Run `c4docs check DIR`. If it fails, show the user why and agree whether to render before going on.

**Gate:** the model directory is clean and `check` passes.

## 2. Find the drift

**Drift** is any place the model and the code disagree. The request sets how wide you look:

- **A named change** (a PR, a commit range, a description of what was built): read its full diff. For each changed file, decide whether it adds, removes or alters a person, system, container, component or relationship in the model.
- **Resync** (no change named, or the user asks whether the model is still right): work from two sources.
  1. **History.** The model's last commit marks when it was last known to be right: `git log -1 --format='%H %cI' -- DIR`. List what changed in the code since, with `git log --stat <hash>..HEAD` in the model's repo and `git log --stat --since=<date>` in each other repo the system spans. Read the diffs that touch entry points, clients of other systems, infrastructure-as-code, deploy config or CI.
  2. **Code.** History misses drift that was already there at the last commit, so also check both directions against the code as it stands:
     - Model to code: find current evidence for every element and every relationship in the model.
     - Code to model: repeat the edge and deployable-unit reads from build stages 2 and 3, and look for each result in the model.

Component-level drift counts only for containers that already have a `components/` file.

**Gate:** for a named change, every changed file is matched to an edit or noted as needing none. For a resync, every model element and relationship has evidence or is marked unsupported, and every deployable unit in the code is found in the model or marked missing.

## 3. Propose

Present the edits as one list grouped by kind, each with its evidence and a one-line reason:

- **Add**: an element or relationship the code has and the model lacks.
- **Remove**: one the model has and the code no longer supports.
- **Change**: a name, description, technology or label that no longer matches.
- **Move**: a relationship that now belongs to a different element.

Ask one multi-select question per kind. Pre-select adds, changes and moves. Leave removals unselected: missing evidence may mean you did not find it. If the code has nothing to change, say so and stop.

**Gate:** the user has answered for every kind.

## 4. Write

1. Apply the accepted edits to the `.c4` files.
2. Run `c4docs render DIR`, then `c4docs check DIR`.
3. Send a changelog by kind, and the README path.
