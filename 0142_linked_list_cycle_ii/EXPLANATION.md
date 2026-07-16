# How We Solve Linked List Cycle II

After Floyd's meet point, restart one pointer at the head to find the entry.

## Steps

1. Run tortoise and hare until they meet, or prove there is no cycle.
2. Reset one pointer to the head.
3. Advance both one step at a time.
4. Their next meeting point is the cycle entrance.
5. Return that node, or null if none.
