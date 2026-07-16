# How We Solve Binary Tree Pruning

Postorder prune subtrees that contain only zeros.

## Steps

1. Recursively prune left and right children.
2. If a node is 0 and both children are gone, delete it.
3. Otherwise keep the node.
