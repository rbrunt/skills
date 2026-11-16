---
name: call-graph-visualisation
description: Explain code flow with a small call tree for caller structure or a sequence diagram for interactions between components, when either makes the answer clearer than prose alone.
---

# Call graph visualisation

Show the smallest verified path that answers the question. If prose is clearer, use prose instead; if the user asks for a call graph, show one.

Choose a call tree for **who calls what**. Choose a sequence diagram when **who talks to whom, in what order** is the point. If neither diagram earns its space, explain the flow in a few sentences or numbered steps.

Start at the highest **useful** caller, not necessarily the program entry point. Follow only the calls and branches that change the reader's understanding. Collapse routine plumbing into one meaningful step and stop when further calls add no insight. Verify the relationships against the code; distinguish uncertain or dynamic calls from confirmed ones.

## Format

Use `├──` and `└──` for branches, with indentation showing which caller owns each call. The tree shows execution, not just which components contain others; explain structural relationships in prose instead. Add a short note beside a node only if it explains a condition or choice the tree alone would hide. No arrowheads or decorative icons.

```text
Agent.handle_input
└── Agent._agentic_loop
    ├── brain.think          decides whether to request a tool
    └── Agent._execute_tool  runs if a tool was requested
        └── tool.execute     selected by tool name
```

Follow the tree with a brief explanation of the important behavior: here, the loop adds each tool result to the conversation and asks the brain again, while the tool's name determines which `execute` method runs. Don't repeat each node in prose. Add source links sparingly, for key implementations or ambiguous symbols, and mention omitted steps only when their absence could mislead the reader.

## Sequence diagrams

Use a compact text sequence diagram for meaningful hand-offs between components. Name participants by role, show messages in time order, and include a return only if its result changes what happens next. Show a loop or condition only when it is central to the question; if it makes the diagram hard to scan, use numbered prose instead. Keep file locations in the explanation, not in the participant labels.

```text
Agent              Brain              Tool
  │                  │                  │
  ├── think ────────►│                  │
  │◄── tool request ─┤                  │
  ├── execute ─────────────────────────►│
  │◄── result ──────────────────────────┤
  └── think again ─►│                  │
```

Explain the important decision or boundary after the diagram, rather than describing every arrow.
