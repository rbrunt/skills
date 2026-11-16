# Critique a map

Triage the map, then walk the user through the findings one category at a time, and only then change the map. On a large map, a single wall of findings is unreadable. Splitting by category keeps each decision small.

## 1. Load

- If the user gave a share link, decode it with `storymap open-link URL -o <file>`. Agree the file path with the user first.
- Run `storymap check`, then `storymap show`.
- Ask which milestone is the MVP if that isn't obvious.
- Read the project's decision records and glossary if they exist. Cutting a card that rests on a **locked** decision would reverse that decision.

## 2. Triage

Check the map against every category below, in this order:

1. **Journey.** Read the steps as one sentence from left to right: "Facilitator creates a retro → participants join → …". Flag:
   - steps named after a feature or system part (`Settings`, `Admin`, `Notifications`);
   - cards with no clear actor;
   - a journey that doesn't reach the user's outcome.

   If the map is mostly a feature list arranged in map shape, stop the critique here. Offer to rework the backbone first, because scope cuts on a feature list mean nothing.
2. **Skeleton gaps.** Look for MVP steps with no card, and for paths that stop before the outcome.
3. **Shape-changing cuts.** These are MVP cards whose removal changes what the product is, or removes a whole step's depth.
4. **Smaller cuts.** These are MVP cards off the walking skeleton that don't change the product's shape.
5. **Structure.** Look for misplaced or duplicate cards, vague titles, and steps that are too coarse or too fine.
6. **Blocking questions.** These are `question` cards in MVP that must be answered before building.

For every cut, give a one-line reason and, where one exists, a cheaper substitute. Example: "Markdown copy plus paste import instead of building the Retro chain and carry-over." Mark each finding **major** or **minor**.

**Gate:** you have applied every category to every MVP card.

## 3. Overview

Send one compact table with a row per category: the count of major and minor findings, and a one-line example. Below it, give a one-line verdict, e.g. "Skeleton broken at Export; ~12 MVP cards cuttable."

## 4. Walk

Take the categories in order, skipping any with no major findings:

- Ask one multi-select question per category, with each major finding as an option. Each option carries its reason and substitute.
- Pre-select the findings you recommend. Never pre-select a finding that would reverse a locked decision: mark it with the decision it reverses and leave the choice to the user.
- Expect pushback and trades, e.g. "keep two templates, drop grouping instead". Move a traded card to a `Next` milestone between MVP and Later, creating that milestone if the user agrees.

Finally, offer every minor finding as one batch.

## 5. Write

1. Apply only the accepted changes.
2. Run `check` and `show`.
3. Send a short changelog: what moved where, what was retitled, what was added. Include the new link and the file path.
