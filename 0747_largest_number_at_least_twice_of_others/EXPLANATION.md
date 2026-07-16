# How We Solve Largest Number At Least Twice of Others

Track the largest and second-largest values in one pass.

## Steps

1. Find the max and the next-max.
2. If `max >= 2 * second`, return the max’s index.
3. Otherwise return `-1`.
