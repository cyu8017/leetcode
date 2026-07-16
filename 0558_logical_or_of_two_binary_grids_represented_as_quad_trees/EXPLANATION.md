# How We Solve Logical OR of Two Binary Grids Represented as Quad-Trees

Recursively OR two quad-trees, short-circuiting on all-1 or all-0 leaves.

## Steps

1. If either tree is a leaf of `1`, return that leaf; if a leaf of `0`, return the other tree.
2. Otherwise OR the four matching child pairs.
3. Collapse four identical leaf children back into one leaf.
