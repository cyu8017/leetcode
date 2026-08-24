# LeetCode 2860 - Happy Students
# https://leetcode.com/problems/happy-students/

from typing import List


class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        ans = 0
        if nums[0] > 0:
            ans += 1
        for i in range(n):
            selected = i + 1
            if selected > nums[i] and (i == n - 1 or selected < nums[i + 1]):
                ans += 1
        return ans
