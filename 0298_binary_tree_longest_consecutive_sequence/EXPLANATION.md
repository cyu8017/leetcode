# How We Solve Binary Tree Longest Consecutive Sequence

DFS extends the path when a child value is exactly parent plus one.

## Steps

1. At each node, start length 1 or extend from the parent when consecutive.
2. Recurse to both children with the updated length.
3. Return the maximum length seen in the subtree.
