# How We Solve Prime Number of Set Bits

Count numbers whose popcount is a small prime (≤ 19 for 32-bit ints).

## Steps

1. Keep the prime set `{2,3,5,7,11,13,17,19}`.
2. For each value in `[left, right]`, check `bit_count()`.
3. Sum the matches.
