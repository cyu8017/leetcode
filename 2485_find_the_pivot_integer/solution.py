# LeetCode 2485 - Find the Pivot Integer
# https://leetcode.com/problems/find-the-pivot-integer/


class Solution:
    def pivotInteger(self, n: int) -> int:
        total = n * (n + 1) // 2
        s = 0
        for x in range(1, n + 1):
            s += x
            if s == total - s + x:
                return x
        return -1
