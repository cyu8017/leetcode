# Approach
Row-by-row set DP of achievable sums; prune values below target and keep the closest above.

# Complexity
Time O(rows * cols * S). Space O(S).
