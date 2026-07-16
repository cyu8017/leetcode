# How We Solve Decode Ways II

DP where each position multiplies prior ways by valid one- and two-digit wildcard counts.

## Steps

1. Define helpers for ways to decode one char and two chars with `*`.
2. Transition: `dp[i] = one(s[i]) * dp[i-1] + two(s[i-1], s[i]) * dp[i-2]`.
3. Take modulo `10^9+7`.
