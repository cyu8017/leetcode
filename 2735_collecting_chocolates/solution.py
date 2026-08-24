# LeetCode 2735 - Collecting Chocolates
# https://leetcode.com/problems/collecting-chocolates/

from typing import List


class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        best = nums[:]
        ans = sum(nums)
        for rot in range(1, n):
            cur = rot * x
            for i in range(n):
                best[i] = min(best[i], nums[(i + rot) % n])
                cur += best[i]
            ans = min(ans, cur)
        return ans
