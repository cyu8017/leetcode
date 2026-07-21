# Approach
DP on endings: `dp[i][l]` ways to split prefix `i` ending with length-`l` number; LCP compares neighbors for non-decreasing order; prefix sums speed transitions.

# Complexity
Time O(n^2). Space O(n^2).
