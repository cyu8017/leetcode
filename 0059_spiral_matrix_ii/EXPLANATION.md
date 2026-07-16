# How We Solve Spiral Matrix II

Fill an n×n grid with numbers 1 to n² in clockwise spiral order.

## Steps

1. Track top, bottom, left, and right edges of the empty area.
2. Fill the top row left to right, then move the top edge down.
3. Fill the right column top to bottom, then move the right edge left.
4. Fill the bottom row right to left, then move the bottom edge up.
5. Fill the left column bottom to top, then move the left edge right.
6. Repeat with the next number until the grid is full.
