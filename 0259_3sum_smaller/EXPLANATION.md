# How We Solve 3Sum Smaller

Sort the array and count triplets with a fixed left value and moving pointers.

## Steps

1. Sort the numbers.
2. Fix the leftmost value of each triplet.
3. Use two pointers on the remaining range.
4. If the sum is too small, all pairs up to the right pointer work.
5. Otherwise move the right pointer left and continue.
