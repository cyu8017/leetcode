# LeetCode 2789 - Largest Element in an Array after Merge Operations
# https://leetcode.com/problems/largest-element-in-an-array-after-merge-operations/

from typing import List


class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        cur = nums[n - 1]
        ans = cur
        for i in range(n - 2, -1, -1):
            if nums[i] <= cur:
                cur += nums[i]
            else:
                cur = nums[i]
            ans = max(ans, cur)
        return ans
