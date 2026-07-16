# How We Solve Construct String from Binary Tree

Preorder stringify with parentheses, omitting empty pairs except for a missing left child.

## Steps

1. Emit the node value.
2. If there is a left or right child, always wrap the left subtree (possibly empty).
3. Wrap the right subtree only when it exists.
