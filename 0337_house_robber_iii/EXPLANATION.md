# How We Solve House Robber III

Tree DP tracks best sums with and without robbing the current node.

## Steps

1. Post-order traverse left and right children.
2. With-rob adds node value plus both without-rob child sums.
3. Without-rob takes the max side choice from each child.
