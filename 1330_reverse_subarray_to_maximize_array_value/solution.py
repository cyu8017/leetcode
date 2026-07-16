# LeetCode 1330 - Reverse Subarray To Maximize Array Value

from typing import List

class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        base = sum(abs(a-b) for a, b in zip(nums, nums[1:]))
        gain = 0
        low, high = 10**9, -10**9
        for a, b in zip(nums, nums[1:]):
            gain = max(gain, abs(nums[0]-b)-abs(a-b), abs(nums[-1]-a)-abs(a-b))
            low = min(low, max(a, b))
            high = max(high, min(a, b))
        return base + max(gain, 2 * (high - low))
