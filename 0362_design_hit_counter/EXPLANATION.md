# How We Solve Design Hit Counter

A queue stores hit timestamps and drops entries older than 300 seconds.

## Steps

1. Append each hit timestamp.
2. On getHits, pop timestamps at or before current time minus 300.
3. Return the remaining queue length.
