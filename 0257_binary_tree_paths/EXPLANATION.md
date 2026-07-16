# How We Solve Binary Tree Paths

DFS builds root-to-leaf path strings.

## Steps

1. Append the current node value to the path.
2. If the node is a leaf, join the path with arrows and save it.
3. Otherwise recurse on the left and right children.
4. Backtrack by removing the current node from the path.
5. Return all collected path strings.
