# How We Solve Longest Univalue Path

DFS returns the longest univalue arrow downward; path can combine both sides.

## Steps

1. Recurse on left/right children.
2. Extend a side only when the child value matches the node.
3. Update global best with `left_path + right_path`; return the longer single side.
