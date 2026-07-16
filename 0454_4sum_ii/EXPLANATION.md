# How We Solve 4Sum II

Reduce four arrays to two by hashing all sums from the first pair.

## Steps

1. Count every value of `nums1[i] + nums2[j]`.
2. For each `nums3[k] + nums4[l]`, add the count of `-(that sum)` to the answer.
3. Return the total number of zero-sum quadruples.
