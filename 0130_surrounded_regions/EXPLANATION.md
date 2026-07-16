# How We Solve Surrounded Regions

Only `O` regions touching the border survive; everything else becomes `X`.

## Steps

1. DFS/BFS from every border `O` and mark the connected region as safe.
2. Scan the whole board afterward.
3. Turn remaining `O` cells into `X` (they were surrounded).
4. Restore safe markers back to `O`.
5. The board is updated in place.
