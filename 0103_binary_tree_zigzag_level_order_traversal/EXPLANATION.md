# How We Solve Binary Tree Zigzag Level Order Traversal

List levels left-to-right, then right-to-left, alternating.

## Steps

1. Do a normal BFS level order.
2. Keep a direction flag.
3. Reverse every other level before saving it.
4. Flip the flag after each level.
5. Return the zigzag list of levels.
