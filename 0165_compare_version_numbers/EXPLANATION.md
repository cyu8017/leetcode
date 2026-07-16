# How We Solve Compare Version Numbers

Compare dotted revisions as integers, padding missing parts with zeros.

## Steps

1. Split both versions on `.`.
2. Convert each revision to an integer.
3. Pad the shorter list with zeros.
4. Compare corresponding revisions left to right.
5. Return -1, 1, or 0.
