# How We Solve Nested List Weight Sum

DFS accumulates integer values multiplied by current depth.

## Steps

1. Walk each nested list at depth starting at 1.
2. Add integer values times depth.
3. Recurse into nested lists at depth + 1.
