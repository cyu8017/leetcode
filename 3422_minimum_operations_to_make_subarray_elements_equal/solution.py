# LeetCode 3422 - Minimum Operations to Make Subarray Elements Equal
# https://leetcode.com/problems/minimum-operations-to-make-subarray-elements-equal/

from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 10**18
        for i in range(n - k + 1):
            sub = sorted(nums[i : i + k])
            med = sub[k // 2]
            cost = 0
            for x in sub:
                cost += abs(x - med)
            if cost < ans:
                ans = cost
        return ans
