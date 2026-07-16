# LeetCode 0371 - Sum of Two Integers
# https://leetcode.com/problems/sum-of-two-integers/


class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        while b:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        return a if a <= 0x7FFFFFFF else ~(a ^ mask)
