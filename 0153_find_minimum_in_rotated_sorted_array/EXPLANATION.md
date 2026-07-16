# How We Solve Find Minimum in Rotated Sorted Array

Binary search on the rotated boundary using comparison with the right end.

## Steps

1. Keep a left/right window over the array.
2. Compare the middle value with the rightmost value.
3. If mid is greater than right, the minimum is to the right of mid.
4. Otherwise shrink the right side to mid.
5. When left meets right, that index holds the minimum.
