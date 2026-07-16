# How We Solve Serialize and Deserialize Binary Tree

Level-order BFS with empty markers preserves tree structure.

## Steps

1. Serialize with BFS, writing values and empty placeholders.
2. Trim trailing empties and join with commas.
3. Deserialize by reading the root, then filling children level by level.
