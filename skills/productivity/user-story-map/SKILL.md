---
name: user-story-map
description: "Build a user story map from source material, or critique an existing map's journey and MVP / walking-skeleton scope."
argument-hint: "[build · critique] [map file, share link or sources]"
---

Simplified user story maps: one backbone row of **steps**, cards under each step, and horizontal **milestones** that slice the cards into releases. There is no activity row above the steps. The map is a JSON file in the user's project, shown and edited in the app at https://user-story-map.richardbrunt.co.uk/.

## Setup

1. Pick the mode from the request. If it doesn't say, ask:

   | Mode | When | Reference |
   |---|---|---|
   | `build` | Make a map from specs, decision records, issues, glossary, notes | [reference/build.md](reference/build.md) |
   | `critique` | Challenge an existing map, especially what is in MVP | [reference/critique.md](reference/critique.md) |

2. Read the mode's reference and [reference/format.md](reference/format.md) before touching a map file.
3. Run `<skill-dir>/scripts/storymap --help` once. It has four commands: `check`, `show`, `link` and `open-link`. `<skill-dir>` is the folder that holds this SKILL.md.

## Principles

- **The user owns the map.** You propose, and they decide. Stop at each review gate named in the mode's reference and wait for their answer.
- **Use the project's words.** Take card and step titles from the project's glossary and sources, not from your own paraphrase.
- **Verify without a browser.** After every edit, run `storymap check` and then `storymap show`, and read the outline as the user would see the map. Give the user the file path and a `storymap link` link. The link opens the map in the app as a new map.
- **Edits come back through git.** The user edits in the app, exports the JSON over the file, and you read their changes with `git diff`. Commit your version, or tell the user to, before they edit, so the diff shows only their changes.
- **Batch questions.** Ask several related decisions in one multi-select question, not one question per card.
