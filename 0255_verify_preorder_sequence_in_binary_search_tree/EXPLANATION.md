# How We Solve Verify Preorder Sequence in Binary Search Tree

Simulate BST construction with a stack and a lower bound.

## Steps

1. Track the smallest value allowed for the current position.
2. If the next value is below that bound, the sequence is invalid.
3. Pop smaller stack values while updating the lower bound.
4. Push the current value onto the stack.
5. Return true if the entire preorder is valid.
