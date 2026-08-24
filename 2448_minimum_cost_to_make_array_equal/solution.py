# LeetCode 2448 - Minimum Cost to Make Array Equal
# https://leetcode.com/problems/minimum-cost-to-make-array-equal/

from typing import List


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        n = len(nums)
        idx = list(range(n))
        idx.sort(key=lambda i: nums[i])
        total_cost = sum(cost)
        pref = 0
        median = 0
        for i in idx:
            pref += cost[i]
            if pref * 2 >= total_cost:
                median = nums[i]
                break
        ans = 0
        for i in range(n):
            diff = nums[i] - median
            if diff < 0:
                diff = -diff
            ans += diff * cost[i]
        return ans
