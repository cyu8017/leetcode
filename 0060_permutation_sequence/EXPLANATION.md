# How We Solve Permutation Sequence

Find the k-th permutation of numbers 1 through n in sorted order.

## Steps

1. List the numbers 1 to n and precompute factorials.
2. Convert k to zero-based (subtract 1).
3. From the highest place value down, pick the index = k ÷ factorial.
4. Append that number and remove it from the list.
5. Update k to k mod factorial and continue.
6. Join the chosen digits into the answer string.
