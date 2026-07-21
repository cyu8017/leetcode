# Approach
Difference array on segment endpoints. Sweep sorted positions; whenever the running mix color is nonzero, emit a mixed segment between consecutive points.

# Complexity
Time O(n log n). Space O(n).
