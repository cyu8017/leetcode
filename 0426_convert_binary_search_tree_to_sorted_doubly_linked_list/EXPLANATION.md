# How We Solve Convert BST to Sorted Doubly Linked List

Inorder traversal of a BST visits nodes in sorted order, which is exactly the circular list order.

## Steps

1. Recursively traverse left, then current node, then right.
2. Link the previous inorder node to the current node with `left`/`right` pointers.
3. After traversal, connect head and tail to form a circular doubly linked list.
