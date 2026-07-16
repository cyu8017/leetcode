# How We Solve Path Sum IV

Decode packed nodes `(depth, pos, val)` and sum root-to-leaf paths.

## Steps

1. Build a map from `(depth, pos)` to value.
2. DFS from `(1,1)`, accumulating path sums.
3. At leaves (no children in the map), add the path to the answer.
