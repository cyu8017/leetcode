# How We Solve Path Sum III

Prefix sums on root-to-node paths let us count downward paths in O(n).

## Steps

1. DFS while tracking cumulative sum from the root to the current node.
2. Add the count of earlier prefixes equal to `current - target`.
3. Backtrack prefix counts when leaving a node.
