# How We Solve Flatten Binary Tree to Linked List

Rewrite the tree in place into a preorder right spine.

## Steps

1. Recursively flatten the left and right subtrees.
2. If there is a left subtree, find its rightmost node.
3. Attach the original right subtree after that rightmost node.
4. Move the left subtree to the right and clear left.
5. Repeat until every node only has a right child.
