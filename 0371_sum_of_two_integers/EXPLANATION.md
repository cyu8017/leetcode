# How We Solve Sum of Two Integers

Bit addition uses XOR for sum bits and AND-shift for carry.

## Steps

1. Repeat while carry is nonzero.
2. XOR a and b for partial sum, mask to 32 bits.
3. Shift carry left and continue; fix sign for Python ints.
