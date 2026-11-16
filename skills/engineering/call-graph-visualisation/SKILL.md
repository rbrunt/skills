---
name: call-graph-visualisation
description: Show how a program, feature, request, command, or execution path is laid out as a concise call-oriented ASCII tree. Use whenever explaining code flow, program structure, entry points, orchestration, callers and callees, or asking "what calls what", even when the user does not explicitly request a call graph.
---

# Call graph visualisation

Explain code flow with an ASCII tree before prose. Optimise for tracing the program from its top-level entry point into the relevant work, not for cataloguing every reachable symbol.

## Build the graph

1. Find the relevant entry point or highest useful caller from the code. Do not infer it from names alone.
2. Follow calls downward through the paths that answer the question.
3. Prune framework plumbing, trivial accessors, generated code, and unrelated branches.
4. Verify every displayed call against the source. Mark dynamic or uncertain dispatch explicitly.
5. Stop when a leaf's implementation no longer helps explain the requested flow.

## Format

Start with the top-level symbol. Put each call beneath its caller, indented one level, and prefix it with `->`.

Label nodes as `symbol (path/to/file.ext:line)`. Qualify ambiguous symbols only enough to distinguish them. Prefer repository-relative paths and exact definition lines so locations are clickable.

```text
main (src/main.ts:12)
  -> loadConfig (src/config.ts:8)
  -> startServer (src/server.ts:21)
     -> registerRoutes (src/routes.ts:14)
        -> handleRequest (src/handlers/request.ts:33)
     -> listen (src/server.ts:48)
```

Use these annotations only when needed:

- `[conditional: reason]` for a branch taken under a condition.
- `[async]` when work continues asynchronously and that distinction matters.
- `[dynamic: possible targets]` when runtime dispatch prevents one certain target.
- `[external]` for a relevant library or service boundary.
- `-> symbol (...) [shown above]` for a repeated subtree.
- `-> symbol (...) [cycle]` when following the edge would loop.

The tree may visualise how a program is laid out even when not every relationship is a function call. Reserve `->` for actual calls or execution hand-offs. Label other edges with their relationship, such as `[registers]`, `[constructs]`, `[routes to]`, or `[owns]`, so structural composition is not presented as runtime execution.

Keep the main graph narrow enough to scan. If several independent entry points matter, show separate trees under short descriptive headings rather than forcing them beneath a fictional root.

## Walkthrough

Follow the graph with a concise walkthrough in tree order. Explain what each meaningful branch is responsible for, where control changes direction, and why the leaf is a useful stopping point. Group trivial consecutive calls rather than narrating every node.

Call out conditions, asynchronous boundaries, dynamic dispatch, recursion, and external boundaries when they affect understanding. State what was pruned if its omission could otherwise make the graph misleading.

The result is complete when a reader can identify the entry point, trace the relevant execution paths, open every project symbol at its source location, and distinguish verified calls from structural or uncertain relationships.
