# LeetCode 3982 - Sum of Integers with Maximum Digit Range
# https://leetcode.com/problems/sum-of-integers-with-maximum-digit-range/

from typing import List


class Solution:
    def maxDigitRange(self, nums: List[int]) -> int:
        mx = 0
        ans = 0
        for x in nums:
            a = 10
            b = 0
            y = x
            while y > 0:
                v = y % 10
                a = min(a, v)
                b = max(b, v)
                y //= 10
            r = b - a
            if mx < r:
                mx = r
                ans = x
            elif mx == r:
                ans += x
        return ans
