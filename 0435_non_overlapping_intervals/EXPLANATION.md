# How We Solve Non-overlapping Intervals

Greedy interval scheduling: keep intervals that end earliest.

## Steps

1. Sort intervals by end time.
2. Greedily take the next interval that starts at or after the previous end.
3. Count overlaps removed when a start is before the current end.
