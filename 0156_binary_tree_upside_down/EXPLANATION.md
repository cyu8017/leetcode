# How We Solve Binary Tree Upside Down

Iteratively rotate each left child into the new root while rewiring siblings.

## Steps

1. Walk down the left spine.
2. Save the next left child before rewriting links.
3. Make the previous right child the new left.
4. Make the previous node the new right.
5. Continue until the old leftmost node becomes the new root.
