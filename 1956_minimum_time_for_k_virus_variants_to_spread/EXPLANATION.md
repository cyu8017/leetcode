# Approach
A cell is infected by a virus after Manhattan days equal to the distance. For each candidate cell on the `1..100` grid, the time for `k` viruses is the `k`-th smallest distance; take the minimum over cells.

# Complexity
Time O(100^2 * n log n). Space O(n).
