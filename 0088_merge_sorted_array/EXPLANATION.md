# How We Solve Merge Sorted Array

Merge two sorted arrays into nums1 in place.

## Steps

1. Start from the end of both filled ranges.
2. Compare the larger of nums1[i] and nums2[j].
3. Write the larger value into the last open slot of nums1.
4. Keep going until nums2 is empty.
5. nums1 then holds the full sorted merge.
