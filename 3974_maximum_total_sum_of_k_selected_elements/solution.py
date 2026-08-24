# LeetCode 3974 - Maximum Total Sum Of K Selected Elements
# https://leetcode.com/problems/maximum-total-sum-of-k-selected-elements/

from typing import List


class Solution:
    def maxSum(self, nums: List[int], k: int, mul: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n - 1, n - k - 1, -1):
            m = max(1, mul)
            ans += nums[i] * m
            mul -= 1
        return ans
