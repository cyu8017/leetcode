# How We Solve Populating Next Right Pointers in Each Node

Link every node to its right neighbor on the same level in a perfect tree.

## Steps

1. Start a level list with the root.
2. Walk the level left to right and set each node's `next`.
3. Build the next level from left and right children.
4. Repeat until there are no more children.
5. Return the original root.
