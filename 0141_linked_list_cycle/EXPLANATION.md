# How We Solve Linked List Cycle

Floyd's tortoise and hare detects whether a cycle exists.

## Steps

1. Start slow and fast at the head.
2. Move slow one step and fast two steps.
3. If they ever meet, a cycle exists.
4. If fast reaches null, there is no cycle.
5. Return that boolean result.
