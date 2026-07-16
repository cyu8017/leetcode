# How We Solve Find Minimum in Rotated Sorted Array II

Same binary search as the unique case, but shrink carefully when duplicates tie.

## Steps

1. Binary search with left and right pointers.
2. If mid is greater than right, move left past mid.
3. If mid is less than right, move right to mid.
4. If they are equal, decrement right to skip the duplicate.
5. Return the value at the final left index.
