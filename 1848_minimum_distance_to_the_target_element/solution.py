# LeetCode 1848 - Minimum Distance to the Target Element
# https://leetcode.com/problems/minimum-distance-to-the-target-element/

class Solution:
    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
        best = len(nums)
        for i, value in enumerate(nums):
            if value == target:
                best = min(best, abs(i - start))
        return best
