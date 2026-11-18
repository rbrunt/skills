# Map format

The app's file format (version 1). `storymap check` and every `storymap edit` command enforce these rules. Use this schema for initial creation and unsupported structural changes; use the editing CLI for card changes and for adding or renaming steps and milestones.

```json
{
  "version": 1,
  "title": "RetroRoom",
  "description": "One line on the product and outcome.",
  "steps": [{ "id": "join", "title": "Join a retro" }],
  "milestones": [{ "id": "mvp", "title": "MVP" }],
  "cards": {
    "share-link": {
      "id": "share-link",
      "kind": "story",
      "status": "todo",
      "title": "[Facilitator] Share a join link",
      "description": null,
      "referenceId": "#42"
    }
  },
  "cells": { "join|mvp": ["share-link"] }
}
```

- `steps` is the **backbone**, in journey order from left to right. `milestones` are listed top to bottom, and there must be at least one.
- A cell key is `stepId|milestoneId`. Its array lists card ids top to bottom, in priority order. Remove a cell key once its array is empty.
- Each card sits in exactly one cell. A card's key in `cards` equals its `id`. Ids cannot contain `|`.
- `kind` is `story` or `question`. Use `question` for an open decision.
- `status` is `todo`, `in-progress` or `done`. `description` is a string or `null`.
- `referenceId` is optional and names the card's source: an issue `#42`, a decision `D7`, a ticket `PROJ-123`. Set it whenever a card comes from an identifiable item.
- Ids are short, stable kebab-case (`share-link`, `vote-limit`). Keep an id unchanged when you retitle or move its card, so diffs stay readable.
- `storymap edit FILE move-card` updates both cells automatically. Its optional `--index` is zero-based in the destination after removing the card; omitting it appends the card. Other cards keep their relative order.

Domain terms:

- **Backbone**: the row of steps. Read from left to right, it tells the user's journey.
- **Walking skeleton**: the thinnest end-to-end path through every step. It is the smallest release a user can use from start to finish.
