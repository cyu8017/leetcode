# How We Solve Find Anagram Mappings

Index positions in `nums2`, then map each `nums1` value to the next unused index.

## Steps

1. Build a queue of indices per value in `nums2`.
2. For each value in `nums1`, pop the next matching index.
3. Return the mapping list.
