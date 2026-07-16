# How We Solve Pour Water

Drop one unit at a time: flow left to a lower spot if possible, else right, else stay.

## Steps

1. Scan left for the farthest preferable lower index.
2. If none, scan right similarly.
3. Increment that height; repeat `volume` times.
