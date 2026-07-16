# How We Solve Image Overlap

Count how often each shift vector maps a `1` in `img1` onto a `1` in `img2`.

## Steps

1. Collect coordinates of all ones in both images.
2. For every pair, tally the offset `(dx, dy)`.
3. The max tally is the largest overlap.
