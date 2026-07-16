# How We Solve Number of Boomerangs

For each anchor point, count how many other points share each squared distance.

## Steps

1. For every ordered triple `(i, j, k)`, distance from `i` to `j` must equal distance from `i` to `k`.
2. Group points by squared distance from the anchor.
3. Add `count * (count - 1)` for each distance bucket.
