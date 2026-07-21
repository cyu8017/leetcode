# Approach
Self-join confirmations on the same user where a later request is within 24 hours of an earlier one.

# Complexity
Time O(n^2) worst case per user. Space O(n).
