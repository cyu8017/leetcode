# How We Solve Find K Pairs with Smallest Sums

A min-heap expands the smallest pair sums greedily.

## Steps

1. Seed the heap with (nums1[i] + nums2[0], i, 0).
2. Pop the smallest pair and append it to the answer.
3. Push the next pair using the same nums1 index and nums2 j + 1.
