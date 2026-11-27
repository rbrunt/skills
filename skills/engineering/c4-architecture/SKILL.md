---
name: c4-architecture
description: "C4 model architecture docs: build a model of an existing software system from its code, update a model after the code changed, or critique a model's diagrams against the C4 review checklist."
argument-hint: "[build · update · critique] [model dir, repos, or change]"
---

Architecture docs for one existing software system, as a C4 model: a **System Context** view, a **Container** view, and **Component** views only for the containers the user names. The model is [LikeC4](https://likec4.dev) `.c4` files in the user's repo. A README beside them shows each view as a Mermaid diagram, generated from the model by `c4docs`.

The model describes the system **as built**. A proposed design has no code to hold it to; say so and stop if that is what the user wants.

## Setup

1. Pick the mode from the request. If it doesn't say, ask:

   | Mode | When | Reference |
   |---|---|---|
   | `build` | Document a system that has no model yet | [reference/build.md](reference/build.md) |
   | `update` | The code changed, or the model may have drifted from it | [reference/update.md](reference/update.md) |
   | `critique` | Review how well a model's diagrams communicate | [reference/critique.md](reference/critique.md) |

2. Read the mode's reference and [reference/format.md](reference/format.md) before touching a model.
3. Run `<skill-dir>/scripts/c4docs --help` once. `<skill-dir>` is the folder that holds this SKILL.md.

## Principles

- **Evidence is your job.** Every element and relationship you propose rests on something you read: source, infrastructure-as-code, deploy config, CI, in that order of trust. Read before you ask. Ask the user only for what code cannot show: the people who use the system, why a boundary sits where it does, and the names and owners of external systems. Where code and existing docs disagree, the code wins and you report the disagreement.
- **Show the evidence, keep it out of the model.** At each gate, give every proposed element and relationship its `path:line`, or `from user`. Evidence lives in the conversation only.
- **The user owns the model.** You propose, and they decide. Stop at each review gate named in the mode's reference and wait for their answer.
- **Use the project's words.** Take element names from the code, the deploy config and the team's glossary.
- **Document, don't redesign.** Findings are about whether the docs are accurate and readable. Leave the architecture's merits to the user.
- **The `.c4` files are the only source.** Change diagrams by editing the model, then run `c4docs render DIR`. After every batch of edits, `render` must succeed and `c4docs check DIR` must pass before you report back.
- **Batch questions.** Ask several related decisions in one multi-select question.
