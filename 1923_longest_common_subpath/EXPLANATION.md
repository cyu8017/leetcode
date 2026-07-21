# Approach
Binary search the common subpath length. For each length, rolling-hash every path's windows (double hash) and intersect the hash sets across paths.

# Complexity
Time O(L log L) with L total path length. Space O(L).
