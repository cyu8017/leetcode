# How We Solve Counting Bits

Each number inherits one fewer set bit than its cleared-lowest-bit parent.

## Steps

1. Initialize result[0] = 0.
2. For i from 1 to n, copy result[i & (i - 1)].
3. Add one for the bit removed by i & (i - 1).
