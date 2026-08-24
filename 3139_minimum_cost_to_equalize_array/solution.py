# LeetCode 3139 - Minimum Cost to Equalize Array
# https://leetcode.com/problems/minimum-cost-to-equalize-array/

from typing import List


class Solution:
    def minCostToEqualizeArray(self, nums: List[int], cost1: int, cost2: int) -> int:
        MOD = 1000000007
        n = len(nums)
        min_num = nums[0]
        max_num = nums[0]
        total = 0
        for v in nums:
            min_num = min(min_num, v)
            max_num = max(max_num, v)
            total += v
        if cost1 * 2 <= cost2 or n < 3:
            total_gap = max_num * n - total
            return (cost1 * total_gap) % MOD
        ans = 10**18
        for target in range(max_num, 2 * max_num):
            max_gap = target - min_num
            total_gap = target * n - total
            pairs = total_gap // 2
            alt = total_gap - max_gap
            if alt < pairs:
                pairs = alt
            cost = cost1 * (total_gap - 2 * pairs) + cost2 * pairs
            ans = min(ans, cost)
        return ans % MOD
