# How We Solve Search in Rotated Sorted Array II

Find a target in a rotated sorted array that may have duplicates.

## Steps

1. Binary search with left and right pointers.
2. If the middle matches the target, return true.
3. If left, middle, and right are equal, shrink both ends.
4. Otherwise pick the sorted half that could contain the target.
5. Return false if the search range is empty.
