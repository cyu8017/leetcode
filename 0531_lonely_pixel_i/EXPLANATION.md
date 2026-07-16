# How We Solve Lonely Pixel I

A lonely black pixel has no other black pixels in its row or column.

## Steps

1. Precompute black-pixel counts for every row and column.
2. Scan the grid for cells that are black with count 1 in both dimensions.
3. Return how many such pixels exist.
