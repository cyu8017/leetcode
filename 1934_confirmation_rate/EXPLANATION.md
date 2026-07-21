# Approach
Left join confirmations to signups. Average an indicator for `'confirmed'` (nulls become 0), round to 2 decimals.

# Complexity
Time O(n). Space O(n).
