# How We Solve Shortest Distance to a Character

Two linear passes track the nearest `c` on each side.

## Steps

1. Left→right: distance to the last seen `c`.
2. Right→left: take the min with the next `c`.
3. Return the per-index distances.
