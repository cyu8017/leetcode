# LeetCode 3094 - Guess the Number Using Bitwise Questions II
# https://leetcode.com/problems/guess-the-number-using-bitwise-questions-ii/

# The commonBits API is patched by the test runner.


def commonBits(num: int) -> int:
    raise NotImplementedError


class Solution:
    def findNumber(self) -> int:
        n = 0
        for i in range(32):
            count1 = commonBits(1 << i)
            count2 = commonBits(1 << i)
            if count1 > count2:
                n |= 1 << i
        return n
