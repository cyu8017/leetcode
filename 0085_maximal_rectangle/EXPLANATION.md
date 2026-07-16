# How We Solve Maximal Rectangle

Find the largest rectangle of ones in a binary matrix.

## Steps

1. Treat each row as the base of a histogram.
2. Grow heights for consecutive ones; reset on zeros.
3. For every row, run the histogram largest-rectangle algorithm.
4. Keep the best area seen across all rows.
5. Return that area.
