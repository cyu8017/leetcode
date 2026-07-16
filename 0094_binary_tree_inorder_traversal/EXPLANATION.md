# How We Solve Binary Tree Inorder Traversal

Visit nodes in left → root → right order.

## Steps

1. Use a stack and start at the root.
2. Keep going left, pushing nodes onto the stack.
3. Pop a node, record its value, then go right.
4. Repeat until the stack and current node are both empty.
5. Return the recorded values.
