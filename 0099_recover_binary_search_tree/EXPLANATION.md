# How We Solve Recover Binary Search Tree

Fix a BST where exactly two node values were swapped.

## Steps

1. Walk the tree in order using a stack.
2. Watch for places where the previous value is bigger than the current one.
3. The first such previous node is one swapped value.
4. The later current node is the other swapped value.
5. Swap those two values to restore the BST.
