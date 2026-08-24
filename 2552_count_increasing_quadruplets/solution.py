# LeetCode 2552 - Count Increasing Quadruplets
# https://leetcode.com/problems/count-increasing-quadruplets/

from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        great = [0] * n
        for j in range(n):
            for i in range(j):
                if nums[i] < nums[j]:
                    ans += great[i]
                elif nums[i] > nums[j]:
                    great[i] += 1
        return ans
