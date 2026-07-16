# How We Solve Average of Levels in Binary Tree

BFS level by level and average the node values on each level.

## Steps

1. Queue the root.
2. For each level, sum the values of the current queue size.
3. Append `sum / count` and enqueue the children.
