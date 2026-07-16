# How We Solve Sort Colors

Sort an array of 0s, 1s, and 2s in one pass.

## Steps

1. Keep three pointers: low, mid, and high.
2. If mid sees 0, swap with low and move both forward.
3. If mid sees 1, just move mid forward.
4. If mid sees 2, swap with high and move high back.
5. Repeat until mid passes high.
