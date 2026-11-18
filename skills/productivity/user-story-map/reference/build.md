# Build a map

Each stage ends at a review gate. Stop there and wait for the user before starting the next stage.

## 1. Intake

Ask all of these in one round:

- **Users and roles**: who moves through the journey (e.g. Facilitator, Participant)?
- **Outcome**: what does the product do for them?
- **Sources**: which material should you read, and do any need fetching (an issue tracker, Jira through an MCP, a wiki)?
- **File**: where should the map go? Default: `docs/story-map.json`.
- **Existing map**: is there one already? If there is, offer `update` or `critique` mode instead.

Then read every source the user named. Note the glossary's terms. Treat decisions recorded as settled as **locked**.

**Gate:** you have the answers and have read the sources.

## 2. Backbone

Draft 5–12 steps, each named as something a user does (`Join a retro`, not `Auth`). Read from left to right, they should tell one journey. Fold activities into steps, because this map has no row above them.

Present the steps as a numbered list, each with a one-line description. Expect the user to merge, split or rename steps.

**Gate:** the user approves the steps. Then write the file with steps and one milestone, and run `storymap check`.

## 3. Cards

1. Ask what to call the staging milestone. Default: `Unsorted`. Use `storymap edit FILE rename-milestone` if its title needs changing.
2. Put every card in that one milestone, so nothing is claimed as MVP yet.
3. Add cards with `storymap edit FILE add-card`: one per user-visible capability, titled in the glossary's terms.
   - Prefix a role tag when the actor isn't obvious: `[Facilitator] Close the retro`.
   - Make each open decision a `question` card.
   - Put each cross-cutting concern (sync, access, security, analytics) under the step it touches most.
   - Set `referenceId` from the source item.

**Gate:** every source item that maps to a capability or open decision has a card. Run `storymap show`, then send the user the outline summary, the file path and the link.

## 4. Milestones

1. Ask for milestone names, suggesting `MVP` / `Next` / `Later`.
2. Propose a split, putting the walking skeleton in the first milestone.
3. Present it per milestone as a short list of card titles. For each card that isn't obvious, give a one-line reason.
4. Apply the user's changes. Add milestones with `storymap edit FILE add-milestone`, using `--index` for release order, then place cards with `storymap edit FILE move-card`. Run `show`. A step left empty in the first milestone means the skeleton is broken: raise it.

**Gate:** the user accepts the split. Send the final link and file path.

## 5. Hand-off

Offer to run `critique` on the finished map.
