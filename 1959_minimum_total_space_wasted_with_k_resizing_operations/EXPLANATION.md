# Approach
Precompute waste of packing each subarray into one size (`max * len - sum`). DP: min waste for a prefix using exactly `s` segments (`k+1` segments = `k` resizes).

# Complexity
Time O(n^2 * k). Space O(n * k).
