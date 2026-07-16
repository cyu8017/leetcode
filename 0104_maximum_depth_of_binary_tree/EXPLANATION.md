# How We Solve Maximum Depth of Binary Tree

Find how many levels the tree has.

## Steps

1. An empty tree has depth 0.
2. Recurse on the left and right children.
3. Take the larger of those two depths.
4. Add 1 for the current node.
5. Return that total.
