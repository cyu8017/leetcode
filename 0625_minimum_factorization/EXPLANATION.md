# How We Solve Minimum Factorization

Factor `num` using digits 9..2 and assemble the smallest number from those digits.

## Steps

1. Greedily divide by digits from 9 down to 2.
2. If anything other than 1 remains, no single-digit factorization exists.
3. Emit digits in ascending order and reject 32-bit overflow.
