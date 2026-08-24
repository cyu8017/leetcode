# LeetCode 3284 - Sum of Consecutive Subarrays
# https://leetcode.com/problems/sum-of-consecutive-subarrays/

from typing import List


class Solution:
    def rangeSum(self, nums: List[int]) -> int:
        mod = 1000000007
        n = len(nums)
        ans = 0
        i = 0
        while i < n:
            j = i
            while j + 1 < n and (nums[j + 1] == nums[j] + 1 or nums[j + 1] == nums[j] - 1):
                j += 1
            for L in range(i, j + 1):
                s = 0
                for R in range(L, j + 1):
                    s += nums[R]
                    ans = (ans + s) % mod
            i = j + 1
        return ans
