# Approach
Compute each monster's arrival minute ceil(dist/speed), sort ascending, and eliminate in that order. At minute i you can kill one monster only if its arrival time is strictly greater than i.

# Complexity
Time O(n log n). Space O(n).
