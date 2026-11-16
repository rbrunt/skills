---
name: jira-status-nudge
description: Proactively offer to update Jira status when working from a Jira issue, including picking up work, handing it off for review, or finishing it. Use even when the user has not asked about Jira; ask permission before changing the issue.
---

# Jira status nudge

When work is tied to a Jira issue, watch for a change in its stage and give the user a brief, actionable reminder so the issue does not stay stale:

| Work stage | Suggested status |
| --- | --- |
| Not yet picked up | To Do |
| Actively being worked on | In Progress |
| Handed off for review | In Review |
| Actually finished, including required review or merge | Done |

At a transition, check the issue's current status if a Jira integration is available. If it already matches, skip the nudge. Otherwise, mention the issue key if known and offer to move it to the suggested status. A completed coding task awaiting review belongs in **In Review**, not **Done**. If the work is blocked or paused, ask whether **In Progress** still reflects its actual state rather than inventing another status.

Keep the offer brief alongside the normal progress update or final reply: “ABC-123 looks ready for In Review. Want me to move it?” Wait for the user's approval before using an available Jira tool to transition the issue. If there is no Jira integration, remind the user to update it themselves. Avoid repeating the offer when nothing about the work stage has changed.
