# How We Solve Bitwise AND of Numbers Range

Shift away differing low bits until left and right share a common prefix.

## Steps

1. While left is less than right, right-shift both.
2. Count how many shifts were needed.
3. The remaining value is the shared high-bit prefix.
4. Shift that prefix back left by the same count.
5. Return the reconstructed AND of the whole range.
