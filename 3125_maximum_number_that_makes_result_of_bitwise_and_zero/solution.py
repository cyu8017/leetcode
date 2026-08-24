# LeetCode 3125 - Maximum Number That Makes Result of Bitwise AND Zero
# https://leetcode.com/problems/maximum-number-that-makes-result-of-bitwise-and-zero/


class Solution:
    def maxNumber(self, n: int) -> int:
        length = 0
        x = n
        while x > 0:
            length += 1
            x >>= 1
        return (1 << (length - 1)) - 1
