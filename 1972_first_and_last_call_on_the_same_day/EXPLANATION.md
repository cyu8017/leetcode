# Approach
Mirror calls both ways, then per user/day take first and last peer via window functions; keep users where they match.

# Complexity
SQL window + distinct.
