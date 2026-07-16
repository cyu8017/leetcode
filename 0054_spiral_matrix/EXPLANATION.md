# How We Solve Spiral Matrix

Walk through a grid in a clockwise spiral and collect the numbers.

## Steps

1. Track the top, bottom, left, and right edges of the remaining grid.
2. Go left to right along the top row, then move the top edge down.
3. Go top to bottom along the right column, then move the right edge left.
4. If rows remain, go right to left along the bottom row, then move the bottom edge up.
5. If columns remain, go bottom to top along the left column, then move the left edge right.
6. Repeat until all cells are visited, then return the collected numbers.
