# LeetCode 2908 - Minimum Sum of Mountain Triplets I
# https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i/

from typing import List


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1 << 30
        for j in range(1, n - 1):
            left = 1 << 30
            right = 1 << 30
            for i in range(j):
                if nums[i] < nums[j] and nums[i] < left:
                    left = nums[i]
            for k in range(j + 1, n):
                if nums[k] < nums[j] and nums[k] < right:
                    right = nums[k]
            if left < (1 << 30) and right < (1 << 30):
                cand = left + nums[j] + right
                if cand < ans:
                    ans = cand
        return -1 if ans == (1 << 30) else ans
