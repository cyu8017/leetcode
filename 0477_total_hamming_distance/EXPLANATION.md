# How We Solve Total Hamming Distance

Sum contributions bit by bit instead of comparing every pair.

## Steps

1. For each bit position, count how many numbers have 0 vs 1.
2. Add `zeros * ones` to the answer for that bit.
3. Repeat for all 32 bits.
