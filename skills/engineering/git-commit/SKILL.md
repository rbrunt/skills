---
name: git-commit
description: Write git commit messages following personal style preferences. Use whenever a git commit message is being composed, reviewed, or suggested.
---

# Git Commit Messages

**Imperative tense** — "Add retry logic", not "Added" / "Adds" / "Adding".

**No conventional commit prefixes** — no `feat:`, `fix:`, `chore:`, `refactor:`, etc.

**Subject line** — one line, 72 chars or fewer, capitalised, no trailing full stop.

**Body** — explain approach and decisions, not what changed (the diff shows that). Why this approach over alternatives? What constraints or trade-offs shaped it? What would a future reader otherwise have to reverse-engineer? Drive the content from the discussion you've had with the user, not your own findings.

**What not to include** -- Don't include details about the prompt, don't say how many tests pass etc, don't make up context just to add body. Small body with bullet points is fine.


```
Defer tile loading until the viewport stabilises

Triggering loads on every scroll event caused cascading requests
that raced each other and inflated bandwidth. Debouncing alone
was not enough because rapid panning still fired multiple leading
edges.

Instead, loading is gated on a short idle window after movement
stops. This matches how the user actually expects the map to
behave and collapses the request storm to a single batch per
pan gesture. The idle threshold (150 ms) was chosen empirically
— low enough to feel instant, high enough to absorb typical
trackpad inertia.
```
