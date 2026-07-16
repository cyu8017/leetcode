# How We Solve Find Right Interval

For each interval start, binary search the smallest start that is at least its end.

## Steps

1. Sort interval starts while remembering original indices.
2. For each interval, binary search the first start >= its end.
3. Return the original index or -1 if none exists.
