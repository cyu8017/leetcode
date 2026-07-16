# How We Solve Number Complement

Flip every bit in the binary representation of the number.

## Steps

1. Build a mask covering all bits of `num` by spreading highest set bit.
2. XOR `num` with that mask.
3. Return the complemented value.
