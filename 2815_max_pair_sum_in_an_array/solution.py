# LeetCode 2815 - Max Pair Sum in an Array
# https://leetcode.com/problems/max-pair-sum-in-an-array/

from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        best = {}
        ans = -1
        for v in nums:
            x = v
            md = 0
            while x > 0:
                md = max(md, x % 10)
                x //= 10
            if md in best:
                ans = max(ans, best[md] + v)
                best[md] = max(best[md], v)
            else:
                best[md] = v
        return ans
