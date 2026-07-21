# Approach
Mutate a contiguous substring greedily: replace digits while the mapping is strictly larger; once mutation has started, stop at the first digit that would shrink.

# Complexity
Time O(n). Space O(n).
