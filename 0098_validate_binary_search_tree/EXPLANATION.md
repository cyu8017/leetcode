# How We Solve Validate Binary Search Tree

Check whether a tree follows BST ordering rules.

## Steps

1. Walk the tree with a low and high bound for each node.
2. The node value must sit strictly between those bounds.
3. The left child inherits a tighter high bound.
4. The right child inherits a tighter low bound.
5. Empty nodes are valid.
