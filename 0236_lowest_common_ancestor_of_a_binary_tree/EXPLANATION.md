# How We Solve Lowest Common Ancestor of a Binary Tree

Recursive post-order search finds where the paths to p and q diverge.

## Steps

1. Return null for an empty node.
2. Return the node itself if it equals p or q.
3. Recurse on left and right subtrees.
4. If both sides return non-null, the current node is the LCA.
5. Otherwise return whichever side found a target.
