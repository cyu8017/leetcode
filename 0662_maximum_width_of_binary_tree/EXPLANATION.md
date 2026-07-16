# How We Solve Maximum Width of Binary Tree

BFS with heap-style indices; width is last index − first index + 1 on each level.

## Steps

1. Queue pairs `(node, index)`; children get `2*i` and `2*i+1`.
2. On each level, track leftmost index and update max width.
3. Return the maximum width seen.
