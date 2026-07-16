# How We Solve Count Complete Tree Nodes

Exploit the complete-tree shape to count in O(log² n) time.

## Steps

1. Measure the leftmost depth and rightmost depth.
2. If they match, the tree is perfect with `2^h - 1` nodes.
3. Otherwise count the root plus both subtrees recursively.
4. Repeat the depth check on each recursive call.
5. Sum the results.
