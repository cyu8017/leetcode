# LeetCode 2457 - Minimum Addition to Make Integer Beautiful
# https://leetcode.com/problems/minimum-addition-to-make-integer-beautiful/


class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def digit_sum(x: int) -> int:
            s = 0
            while x > 0:
                s += x % 10
                x //= 10
            return s

        orig = n
        pow10 = 1
        while digit_sum(n) > target:
            n = n // 10 + 1
            pow10 *= 10
        return n * pow10 - orig
