# Approach
Enumerate valid column colorings (`3^m`, adjacent cells differ). Precompute horizontal compatibility, then DP over columns: ways to place column `i` given previous mask.

# Complexity
Time O(n * S^2) with S <= 3^m. Space O(n * S).
