# How We Solve Reverse Linked List

Iteratively reverse next pointers while walking the list.

## Steps

1. Keep a `prev` pointer starting at null.
2. Store the next node before rewriting links.
3. Point the current node back to `prev`.
4. Advance `prev` and `current`.
5. Return `prev` as the new head.
