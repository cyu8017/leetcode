# How We Solve Making A Large Island

Label every island and its size; try flipping each `0` to join neighbors.

## Steps

1. DFS/paint each island with a unique id and record its area.
2. For every water cell, sum distinct neighboring island sizes + 1.
3. If the grid is all land, return `n*n`.
