# How We Solve Product of Array Except Self

Build prefix products forward and suffix products backward.

## Steps

1. Initialize the answer array with prefix products from left to right.
2. Track a running prefix multiplier.
3. Multiply by suffix products while scanning right to left.
4. Track a running suffix multiplier.
5. Return the final product array without using division.
