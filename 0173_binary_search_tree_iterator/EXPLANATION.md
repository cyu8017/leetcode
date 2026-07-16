# How We Solve Binary Search Tree Iterator

Controlled inorder traversal with a stack of left spines.

## Steps

1. On construction, push the root and all left children.
2. `hasNext` is true while the stack is non-empty.
3. `next` pops the top node as the next inorder value.
4. Then push that node's right child and its left spine.
5. Each visit costs amortized O(1) time.
