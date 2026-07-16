# How We Solve Subarray Sum Equals K

Prefix sums plus a frequency map count subarrays ending at each index.

## Steps

1. Keep a running prefix sum and a map of how often each prefix has occurred.
2. For each prefix `s`, add the count of `s - k` (prior prefixes that form sum `k`).
3. Increment the frequency of the current prefix.
