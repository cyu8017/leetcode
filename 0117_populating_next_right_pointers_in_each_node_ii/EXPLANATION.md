# How We Solve Populating Next Right Pointers in Each Node II

Same level linking as the perfect-tree version, but children may be missing.

## Steps

1. Process the tree level by level.
2. On each level, connect consecutive nodes with `next`.
3. Collect existing left and right children for the next level.
4. Continue until a level is empty.
5. Return the root with all `next` pointers filled.
