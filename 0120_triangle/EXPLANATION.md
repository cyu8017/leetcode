# How We Solve Triangle

Find the minimum path sum from top to bottom with bottom-up DP.

## Steps

1. Copy the bottom row as the working DP array.
2. Move upward one row at a time.
3. For each cell, add the smaller of the two children below it.
4. Continue until only the top cell remains.
5. Return that value as the minimum total.
