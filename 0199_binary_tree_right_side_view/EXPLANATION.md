# How We Solve Binary Tree Right Side View

Level-order BFS and record the last node on each level.

## Steps

1. Queue the root if it exists.
2. Process one level at a time.
3. Enqueue left then right children.
4. Append the last node's value for that level.
5. Return the collected right-side values.
