# How We Solve Number of 1 Bits

Clear the lowest set bit repeatedly and count how many times that happens.

## Steps

1. Start a counter at 0.
2. While `n` is nonzero, replace it with `n & (n - 1)`.
3. Increment the counter after each clear.
4. Stop when every set bit is gone.
5. Return the counter as the Hamming weight.
