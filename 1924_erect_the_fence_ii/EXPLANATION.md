# Approach
Minimum enclosing circle via randomized incremental construction (Welzl-style): when a point lies outside the current circle, rebuild using 1–3 boundary points (midpoint or circumcircle).

# Complexity
Expected time O(n). Space O(n).
