# LeetCode 3745 - Maximize Expression of Three Elements
# https://leetcode.com/problems/maximize-expression-of-three-elements/

from typing import List


class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        inf = 1 << 30
        a, b, c = -inf, -inf, inf
        for x in nums:
            if x < c:
                c = x
            if x >= a:
                b = a
                a = x
            elif x > b:
                b = x
        return a + b - c
