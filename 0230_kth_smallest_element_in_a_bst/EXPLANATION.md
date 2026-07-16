# How We Solve Kth Smallest Element in a BST

Iterative inorder traversal visits values in sorted order.

## Steps

1. Push all left children onto a stack.
2. Pop the next smallest node.
3. Decrease k each time a node is visited.
4. Return the value when k reaches 0.
5. Move to the right child and repeat.
