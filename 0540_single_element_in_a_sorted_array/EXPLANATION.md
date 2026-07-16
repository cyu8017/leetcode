# How We Solve Single Element in a Sorted Array

Pairs occupy even/odd index blocks, so binary search can isolate the singleton.

## Steps

1. Binary search while keeping indices aligned to even positions.
2. If `nums[mid] == nums[mid + 1]`, the unique element is to the right.
3. Otherwise search left; the remaining index holds the answer.
