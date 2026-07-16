# How We Solve Kth Smallest Element in a Sorted Matrix

Binary search counts values less than or equal to mid.

## Steps

1. Search the value range from top-left to bottom-right.
2. For each mid, count elements row-wise with a moving column pointer.
3. Move left or right based on whether count is at least k.
