# How We Solve All Paths From Source to Target

DFS from node `0` to `n-1`, recording every path.

## Steps

1. Start with path `[0]`.
2. Recurse to each neighbor, appending to the path.
3. When the target is reached, copy the path into the answer.
