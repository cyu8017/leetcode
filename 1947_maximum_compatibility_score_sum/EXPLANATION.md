# Approach
Precompute compatibility scores, then DP over student index and mentor bitmask to maximize the assignment sum.

# Complexity
Time O(m^2 * 2^m). Space O(m * 2^m).
