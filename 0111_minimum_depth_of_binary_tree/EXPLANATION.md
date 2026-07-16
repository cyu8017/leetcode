# How We Solve Minimum Depth of Binary Tree

Find the shortest root-to-leaf path. A missing child does not count as a leaf.

## Steps

1. Empty tree has depth 0.
2. If only the right child exists, recurse on the right.
3. If only the left child exists, recurse on the left.
4. Otherwise take 1 plus the smaller of the two child depths.
5. Return that depth.
