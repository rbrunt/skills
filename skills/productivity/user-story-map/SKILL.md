---
name: user-story-map
description: "Build a user story map from source material, update an existing map with new material, or critique a map's journey and MVP / walking-skeleton scope."
argument-hint: "[build · update · critique] [map file, share link or sources]"
---

Simplified user story maps: one backbone row of **steps**, cards under each step, and horizontal **milestones** that slice the cards into releases. There is no activity row above the steps. The map is a JSON file in the user's project, shown and edited in the app at https://user-story-map.richardbrunt.co.uk/.

## Setup

1. Pick the mode from the request. If it doesn't say, ask:

   | Mode | When | Reference |
   |---|---|---|
   | `build` | Make a map from specs, decision records, issues, glossary, notes | [reference/build.md](reference/build.md) |
   | `critique` | Challenge an existing map, especially what is in MVP | [reference/critique.md](reference/critique.md) |
   | `update` | Fold new source material into an existing map | [reference/update.md](reference/update.md) |

2. Read the mode's reference and [reference/format.md](reference/format.md) before touching a map file.
3. Run `<skill-dir>/scripts/storymap --help` once. For editing commands, run `storymap edit --help` and the relevant subcommand's `--help`. `<skill-dir>` is the folder that holds this SKILL.md.

## Principles

- **The user owns the map.** You propose, and they decide. Stop at each review gate named in the mode's reference and wait for their answer.
- **Use the project's words.** Take card and step titles from the project's glossary and sources, not from your own paraphrase.
- **Edit through the CLI.** Use `storymap edit FILE ...` for card changes and for adding or renaming steps and milestones. Commands validate before saving and update placements automatically. Use direct JSON writes only to create a map or change structure the CLI doesn't support (such as merging or removing steps or milestones), then run `storymap check`. Commands are individually atomic; when batching in a shell, use `set -e` or `&&` to stop on failure.
- **Verify without a browser.** After each accepted batch, run `storymap show` and read the outline as the user would see the map. CLI edits need no separate `check`. Give the user the file path and a `storymap link` link. The link opens the map in the app as a new map.
- **Edits come back through git.** The user edits in the app, exports the JSON over the file, and you read their changes with `git diff`. Commit your version, or tell the user to, before they edit, so the diff shows only their changes.
- **Batch questions.** Ask several related decisions in one multi-select question, not one question per card.
