# How We Solve Count of Range Sum

Merge sort on prefix sums counts valid range sums in each merge step.

## Steps

1. Build prefix sums starting at zero.
2. During merge sort, count pairs in range [lower, upper].
3. Merge sorted prefix subarrays recursively.
