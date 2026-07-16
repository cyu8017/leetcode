# How We Solve Gray Code

Build an n-bit Gray code sequence.

## Steps

1. There are 2^n codes for bit length n.
2. For each index i from 0 to 2^n − 1, compute i XOR (i shifted right by 1).
3. Collect those values in order.
4. Neighboring codes differ by exactly one bit.
5. Return the list.
