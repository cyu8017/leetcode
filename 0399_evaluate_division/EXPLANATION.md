# How We Solve Evaluate Division

Model equations as a weighted directed graph and DFS each query.

## Steps

1. Add both directions of every equation as edge weights.
2. Search for a path from the dividend to the divisor.
3. Multiply edge weights along the path; return -1 when disconnected.
