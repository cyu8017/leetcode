# How We Solve Nested List Weight Sum II

Weight integers by depth measured from the deepest leaf upward.

## Steps

1. DFS collect each integer with its top-down depth.
2. Find the maximum depth in the structure.
3. Sum value times (maxDepth - depth + 1).
