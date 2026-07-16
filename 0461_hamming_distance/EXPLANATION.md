# How We Solve Hamming Distance

Count the number of set bits in the XOR of the two integers.

## Steps

1. Compute `x ^ y`.
2. Return the population count (number of 1 bits) in the result.
