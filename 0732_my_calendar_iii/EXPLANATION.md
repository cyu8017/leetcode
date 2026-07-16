# How We Solve My Calendar III

Sweep-line: +1 at start, −1 at end; return the max concurrent count.

## Steps

1. Update a delta map at `startTime` and `endTime`.
2. Scan times in order accumulating the running total.
3. Track and return the maximum concurrency seen so far.
