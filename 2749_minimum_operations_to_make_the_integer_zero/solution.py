# LeetCode 2749 - Minimum Operations to Make the Integer Zero
# https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/


class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        def popcount(x: int) -> int:
            c = 0
            v = int(x)
            while v > 0:
                c += v & 1
                v >>= 1
            return c

        for k in range(1, 61):
            rem = num1 - k * num2
            if rem < k:
                continue
            if popcount(rem) <= k:
                return k
        return -1
