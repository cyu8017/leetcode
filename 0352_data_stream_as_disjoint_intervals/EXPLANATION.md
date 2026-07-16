# How We Solve Data Stream as Disjoint Intervals

Maintain merged intervals while inserting each new value.

## Steps

1. Start a singleton interval for the incoming number.
2. Merge overlapping or adjacent intervals during insertion.
3. Return the current interval list on request.
