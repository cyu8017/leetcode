# How We Solve Search in Rotated Sorted Array

A sorted list was rotated. Find target index or -1.

## Steps

1. Use left and right binary search pointers.
2. Look at middle; if it is target, done.
3. Decide which half is sorted (left half or right half).
4. Check if target lives in the sorted half.
5. Move left/right to search that half, else search the other half.
6. Return index or -1.
