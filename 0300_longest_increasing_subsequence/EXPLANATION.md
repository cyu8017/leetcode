# How We Solve Longest Increasing Subsequence

Patience sorting with binary search finds the LIS length.

## Steps

1. Maintain an array of pile tops in increasing order.
2. Binary search for the leftmost pile that can accept each number.
3. Append when the number is larger than all piles.
4. Return the number of piles as the LIS length.
