---
name: gh-stack
description: Use the `gh stack` CLI to create and manage stacked pull requests (a chain of PRs that build on each other). Invoke whenever stacked PRs are mentioned, or when a change should be split into a dependent chain of PRs.
---

# gh stack

`gh stack` manages a chain of branches/PRs where each builds on the previous one, so large
changes can land as reviewable, sequential PRs instead of one big one.

## Core workflow

1. **Start a stack** from trunk:
   ```
   gh stack init <branch1> [<branch2> ...]   # -b/--base to override trunk (defaults to default branch)
   ```
   Missing branches are created; existing ones are adopted. Multiple names create a multi-layer
   stack in one go, each based on the previous.

2. **Add a layer** on top of the current stack after making changes:
   ```
   gh stack add -Am "commit message" <branch-name>
   ```
   `-A` stages everything (untracked included), `-u` stages tracked-only. Omit `<branch-name>`
   with `-m` to auto-generate it from the message.

3. **Submit to GitHub** (push branches + create/update PRs):
   ```
   gh stack submit          # interactive editor for titles/descriptions/draft state
   gh stack submit --auto   # auto-generated titles, no prompts (use in non-interactive contexts)
   ```

4. **Keep in sync** with trunk and remote:
   ```
   gh stack sync            # fetch, rebase, push, sync PR state; --prune removes merged branches
   ```
   Never opens PRs — only `submit` does that.

5. **Merge** once approved:
   ```
   gh stack merge            # interactive picker for how far up to merge
   gh stack merge --yes --squash
   ```
   Merges are atomic: everything up to the chosen PR merges together or not at all.

## Navigation / inspection

- `gh stack view` / `--short` / `--json` — see branches and PR status (✓ merged, ○ open, ◎ queued, ⚠ needs rebase)
- `gh stack top` / `bottom` / `up` / `down` / `trunk` — move between branches in the stack
- `gh stack checkout <stack#|PR#|branch>` — jump to a specific stack

## Restructuring

`gh stack modify` opens a TUI to drop, fold, insert, reorder, or rename branches. Run
`gh stack submit` afterward if any restructured branch already has a PR.

## Tips

- If a rebase conflict occurs during `sync`, branches are restored automatically — resolve
  with `gh stack rebase`, don't force through it.
- Follow the repo's own commit-message and PR conventions for each `gh stack add -m "..."`
  commit and for `submit` descriptions.
