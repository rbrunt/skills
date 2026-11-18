# Update a map

Fold new source material into an existing map. Propose every change, walk the user through the proposals by kind, and write only what they accept.

## 1. Settle the baseline

Run `git diff` on the map file.

- If the diff is non-empty, those are the user's own app edits. Summarise them, and ask the user to commit before you propose anything, so your changes and theirs never mix.
- Once the diff is empty, run `storymap check` and `storymap show`.

**Gate:** the map file has no uncommitted changes and passes `check`.

## 2. Find what's new

1. List the source files changed since the map's last commit: `git log --name-only <last map commit>..HEAD`.
2. Add anything the user names: issues, a Jira query, notes.
3. Confirm the list with the user, then read every item on it.

Decisions recorded in the sources are **locked**.

## 3. Draft changes

Match each source item to the map:

1. **Match.** Compare the item to existing cards, by `referenceId` first and then by title. If a match is ambiguous, record it as a finding; never guess.
2. **Backbone first.** If the material needs a new, renamed or merged step, present those step changes on their own. Wait for the user before drafting any card changes.
3. **Draft card changes**, each with its source and a one-line reason:
   - **Add**: a new capability or open decision.
   - **Retitle**: the wording or scope changed.
   - **Resolve**: a decision answered a `question` card. Turn it into a `story` and set `referenceId` to the decision.
   - **Remove**: the source dropped the card, or a decision reversed it.
   - **Move**: the card belongs under a different step.
4. **Place new cards.** Give each new card a milestone. If the milestone is unclear, use the staging milestone (`Unsorted`); recreate it if it's gone. Flag every card proposed into MVP as **scope growth**.

**Gate:** every item read in step 2 is either matched to a change or noted as needing none.

## 4. Overview

Send one compact table with a row per change kind: the count, and one example. Add a row for ambiguous matches.

## 5. Walk

Take the change kinds in order: backbone, then add, retitle, resolve, remove, move.

- Ask one multi-select question per kind.
- Pre-select every change except removals and scope growth; leave those to the user.
- Resolve ambiguous matches with the user directly.

## 6. Write

1. Apply only the accepted changes through `storymap edit`, following the editing rules in SKILL.md for unsupported structural changes. Removed cards are deleted; git history keeps them.
2. Run `show` and read the outline.
3. Send a changelog: what was added, retitled, resolved, removed and moved. Include the link and the file path.

If MVP changed (cards added, removed, or moved in or out), offer `critique`.
