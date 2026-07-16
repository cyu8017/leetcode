# How We Solve Lonely Pixel II

Here `target` is the required number of black pixels in both the row and column.

## Steps

1. Count black pixels per row and per column.
2. For each black cell meeting the target counts, check that every row with black in that column matches the current row string.
3. Count all qualifying black pixels.
