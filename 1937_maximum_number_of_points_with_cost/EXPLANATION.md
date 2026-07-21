# Approach
DP per row. Maintain left-to-right and right-to-left running maxima of `prev[c] - |c - j|` so each cell picks the best previous column in O(1).

# Complexity
Time O(mn). Space O(n).
