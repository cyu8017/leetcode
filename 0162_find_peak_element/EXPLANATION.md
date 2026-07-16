# How We Solve Find Peak Element

Binary search follows the rising slope to any peak.

## Steps

1. Keep a left/right window over the array.
2. Compare the middle value with its right neighbor.
3. If mid is greater, a peak lies on the left side including mid.
4. Otherwise climb right by setting left to mid + 1.
5. When left meets right, that index is a peak.
