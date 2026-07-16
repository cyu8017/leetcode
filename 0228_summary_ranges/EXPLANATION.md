# How We Solve Summary Ranges

Group consecutive sorted numbers into ranges.

## Steps

1. Scan the sorted array from left to right.
2. Mark the start of each range.
3. Extend the range while the next number is exactly one greater.
4. Format a single value or a `start->end` range.
5. Append each formatted range to the answer.
