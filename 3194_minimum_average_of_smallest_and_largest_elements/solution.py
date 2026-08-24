# LeetCode 3194 - Minimum Average of Smallest and Largest Elements
# https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/

from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        n = len(nums)
        ans = 1 << 30
        for i in range(n // 2):
            ans = min(ans, nums[i] + nums[n - i - 1])
        return ans / 2.0
