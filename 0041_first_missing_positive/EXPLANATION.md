# How We Solve First Missing Positive

Find the smallest missing **positive** integer (1, 2, 3, ...).

## Steps

1. Only numbers 1..n matter for an array of length n.
2. Try to put each value v into index v-1 by swapping.
3. Swap only when v is in range and not already in the right place.
4. Scan indexes: first place where nums[i] != i+1 gives the answer.
5. If all match, answer is n+1.
