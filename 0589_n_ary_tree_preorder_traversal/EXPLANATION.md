# How We Solve N-ary Tree Preorder Traversal

Visit the node, then recurse through children left to right.

## Steps

1. If the root is null, return an empty list.
2. Append the current value.
3. Recurse on each child in order.
