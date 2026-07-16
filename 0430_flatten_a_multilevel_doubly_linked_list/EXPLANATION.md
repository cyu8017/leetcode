# How We Solve Flatten a Multilevel Doubly Linked List

When a node has a child list, flatten it and splice it between the node and its original next node.

## Steps

1. Walk the main list left to right.
2. If a node has `child`, recursively flatten that sublist.
3. Insert the flattened sublist after the current node and reconnect `prev`/`next`.
4. Clear the child pointer and continue from the former next node.
