# How We Solve Find First and Last Position of Element in Sorted Array

Find first and last index of target in a sorted array.

## Steps

1. Binary search for the **first** position where nums[i] >= target.
2. If not found or not equal to target, return [-1, -1].
3. Binary search for the **first** position where nums[i] > target.
4. Last index is that position minus one.
5. Return [first, last].
