# How We Solve Friends Of Appropriate Ages

Count ages (1–120) and enumerate valid `(x, y)` request pairs.

## Steps

1. Build a frequency array of ages.
2. For each age pair, skip if any of the three rejection rules hold.
3. Multiply counts; subtract self-requests when `x == y`.
