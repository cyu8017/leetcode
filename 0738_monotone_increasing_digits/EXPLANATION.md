# How We Solve Monotone Increasing Digits

Find the first descent, decrement that digit, and set the suffix to nines.

## Steps

1. Scan digits right-to-left for a decrease.
2. Decrement the left digit of the descent and mark the suffix start.
3. Fill the marked suffix with `9`s.
