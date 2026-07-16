# How We Solve Merge Intervals

Combine overlapping time ranges into bigger ranges.

## Steps

1. Sort intervals by their start time.
2. Start with the first interval in a merged list.
3. For each next interval, check if it overlaps the last merged one.
4. If it overlaps, stretch the last interval's end to the bigger end time.
5. If it does not overlap, add it as a new interval.
6. Return the merged list.
