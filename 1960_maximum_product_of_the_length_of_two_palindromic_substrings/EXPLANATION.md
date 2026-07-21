# Approach
Manacher for odd palindromes. Derive the longest odd palindrome ending at / starting at each index, then take `max(prefix_end[i] * suffix_start[i+1])`.

# Complexity
Time O(n). Space O(n).
