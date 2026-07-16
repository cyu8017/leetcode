# How We Solve Number of Subarrays with Bounded Maximum

Count subarrays whose max is ≤ `right`, minus those whose max is ≤ `left-1`.

## Steps

1. `count(bound)` = number of subarrays with all elements ≤ `bound`.
2. Grow a run length while values stay ≤ bound; add the run length each step.
3. Answer is `count(right) - count(left-1)`.
