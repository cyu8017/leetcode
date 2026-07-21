# Approach
Scan equal-value runs. Each run length must be 2 or 3k or 3k+2. Exactly one run may contribute a length congruent to 2 (the unique length-2 piece); all others must be multiples of 3.

# Complexity
Time O(n). Space O(1).
