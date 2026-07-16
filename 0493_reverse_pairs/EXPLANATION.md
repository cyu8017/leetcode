# How We Solve Reverse Pairs

Count pairs with i < j and nums[i] > 2 * nums[j] during merge sort.

## Steps

1. Recursively split the array and count pairs in each half.
2. For each left element, advance a pointer while the 2× condition holds on the right half.
3. Merge sorted halves and return the total count.
