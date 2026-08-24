# LeetCode 3064 - Guess the Number Using Bitwise Questions I
# https://leetcode.com/problems/guess-the-number-using-bitwise-questions-i/


def commonSetBits(num: int) -> int:
    raise NotImplementedError


class Solution:
    def findNumber(self) -> int:
        n = 0
        for i in range(32):
            if commonSetBits(1 << i) > 0:
                n |= 1 << i
        return n
