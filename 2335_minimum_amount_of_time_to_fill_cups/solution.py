# LeetCode 2335 - Minimum Amount of Time to Fill Cups
# https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/

from typing import List


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        a, b, c = amount[0], amount[1], amount[2]
        if a < b:
            a, b = b, a
        if a < c:
            a, c = c, a
        if b < c:
            b, c = c, b
        if a >= b + c:
            return a
        return (a + b + c + 1) // 2
