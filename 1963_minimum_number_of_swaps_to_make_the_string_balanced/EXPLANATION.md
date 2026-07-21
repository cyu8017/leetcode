# Approach
Track running balance; the deepest negative imbalance determines swaps: `(-min_bal + 1) // 2`.

# Complexity
Time O(n). Space O(1).
