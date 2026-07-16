# How We Solve Binary Tree Preorder Traversal

Visit root, then left, then right.

## Steps

1. If the node is null, stop.
2. Record the node value.
3. Recurse into the left subtree.
4. Recurse into the right subtree.
5. Return the collected values.
