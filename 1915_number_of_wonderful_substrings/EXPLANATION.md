# Approach
Maintain a parity bitmask of letter counts. A substring is wonderful if the XOR of endpoints has at most one bit set. Count previous prefixes with the same mask or flipped by one bit.

# Complexity
Time O(n). Space O(1) over 2^10 masks.
