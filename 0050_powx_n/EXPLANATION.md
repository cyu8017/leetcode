# How We Solve Pow(x, n)

Compute x raised to the power n quickly.

## Steps

1. If n is 0, the answer is 1.
2. If n is negative, use 1/x and make n positive.
3. Keep a running power of x (square it each step).
4. Look at n in binary: if the last bit is 1, multiply the answer by the current power.
5. Shift n right and repeat until n is 0.
6. Return the answer.
