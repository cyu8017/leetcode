# LeetCode 2342 - Max Sum of a Pair With Equal Sum of Digits
# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/

from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def digit_sum(x: int) -> int:
            s = 0
            while x > 0:
                s += x % 10
                x //= 10
            return s

        best = {}
        ans = -1
        for x in nums:
            ds = digit_sum(x)
            if ds in best:
                ans = max(ans, best[ds] + x)
                if x > best[ds]:
                    best[ds] = x
            else:
                best[ds] = x
        return ans
