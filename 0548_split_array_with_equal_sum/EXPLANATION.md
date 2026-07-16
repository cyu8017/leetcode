# How We Solve Split Array with Equal Sum

Find indices `i`, `j`, `k` so four separated subarray sums are equal.

## Steps

1. Build prefix sums for the array.
2. For each middle index `j`, store equal first/second segment sums seen so far.
3. Check whether third and fourth segment sums match any stored value.
