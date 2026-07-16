# How We Solve N-ary Tree Postorder Traversal

Recurse through children first, then visit the node.

## Steps

1. If the root is null, return an empty list.
2. Recurse on each child in order.
3. Append the current value after its children.
