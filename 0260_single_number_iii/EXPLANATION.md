# How We Solve Single Number III

XOR finds the combined difference bit, then partitions numbers into two groups.

## Steps

1. XOR all numbers to get the xor of the two unique values.
2. Isolate any set bit that differs between them.
3. XOR numbers with that bit set into one accumulator.
4. XOR the rest into the other accumulator.
5. Return both unique numbers.
