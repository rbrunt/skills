---
name: call-graph-visualisation
description: Explain code flow with a small text call tree when the user asks what calls what, or when a diagram would make a branching execution path easier to understand than prose alone.
---

# Call graph visualisation

Show the smallest verified path that answers the question. If prose is clearer, use prose instead; if the user asks for a call graph, show one.

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
