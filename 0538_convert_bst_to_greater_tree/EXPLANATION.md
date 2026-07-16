# How We Solve Convert BST to Greater Tree

Visit nodes from largest to smallest so each node can absorb all greater values seen so far.

## Steps

1. Traverse the BST in reverse inorder (right, node, left).
2. Maintain a running sum of visited node values.
3. Replace each node value with that running sum.
