# LeetCode 3880 - Minimum Absolute Difference Between Two Values
# https://leetcode.com/problems/minimum-absolute-difference-between-two-values/

from typing import List


class Solution:
    def minAbsoluteDifference(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n + 1
        last = [-ans, -ans, -ans]
        for i in range(n):
            x = nums[i]
            if x != 0:
                ans = min(ans, i - last[3 - x])
                last[x] = i
        if ans > n:
            return -1
        return ans
