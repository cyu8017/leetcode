# How We Solve Construct the Rectangle

Find the most square-like factor pair for the given area.

## Steps

1. Iterate width from √area down to 1.
2. When area is divisible by width, length is area / width.
3. Return `[length, width]` with length ≥ width.
