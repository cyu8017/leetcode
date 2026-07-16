# How We Solve Pyramid Transition Matrix

DFS build each upper row from allowed parent triples.

## Steps

1. Map every two-letter base to possible top blocks.
2. Recursively try all ways to build the next row.
3. Succeed when a single block remains.
