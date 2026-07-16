# How We Solve Sum of Left Leaves

DFS adds a left child only when that child is a leaf.

## Steps

1. If the left child is a leaf, add its value.
2. Otherwise recurse into the left subtree.
3. Always recurse into the right subtree.
