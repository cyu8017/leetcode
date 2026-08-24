# LeetCode 3423 - Maximum Difference Between Adjacent Elements in a Circular Array
# https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/

from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            d = abs(nums[i] - nums[(i + 1) % n])
            if d > ans:
                ans = d
        return ans
