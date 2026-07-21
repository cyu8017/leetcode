# Approach
While inserting values in order, keep seen values sorted with depths. New depth is one more than the max of predecessor/successor depths.

# Complexity
Time O(n^2). Space O(n).
