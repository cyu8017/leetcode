# LeetCode 2576 - Find the Maximum Number of Marked Indices
# https://leetcode.com/problems/find-the-maximum-number-of-marked-indices/

from typing import List


class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        i = 0
        ans = 0
        for j in range((n + 1) // 2, n):
            if 2 * nums[i] <= nums[j]:
                ans += 2
                i += 1
        return ans
