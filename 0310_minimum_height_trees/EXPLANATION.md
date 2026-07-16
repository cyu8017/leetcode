# How We Solve Minimum Height Trees

Repeatedly peel leaves to find the tree center(s).

## Steps

1. Build adjacency lists and leaf degrees.
2. Remove all leaves layer by layer until at most two nodes remain.
3. Return the remaining nodes as the minimum-height roots.
