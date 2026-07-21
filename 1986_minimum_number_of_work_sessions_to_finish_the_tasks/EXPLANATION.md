# Approach
Bitmask DP: for each subset, track sessions needed and load of the current session; try assigning each remaining task.

# Complexity
Time O(n * 2^n). Space O(2^n).
