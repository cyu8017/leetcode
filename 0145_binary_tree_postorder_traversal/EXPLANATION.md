# How We Solve Binary Tree Postorder Traversal

Visit left, then right, then root.

## Steps

1. If the node is null, stop.
2. Recurse into the left subtree.
3. Recurse into the right subtree.
4. Record the node value.
5. Return the collected values.
