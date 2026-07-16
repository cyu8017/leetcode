# LeetCode 0644 - Maximum Average Subarray II
# https://leetcode.com/problems/maximum-average-subarray-ii/

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        def can_reach(mid: float) -> bool:
            prefix = 0.0
            for i in range(k):
                prefix += nums[i] - mid
            if prefix >= 0:
                return True

            prev = 0.0
            min_prev = 0.0
            for i in range(k, len(nums)):
                prefix += nums[i] - mid
                prev += nums[i - k] - mid
                min_prev = min(min_prev, prev)
                if prefix - min_prev >= 0:
                    return True
            return False

        left, right = float(min(nums)), float(max(nums))
        for _ in range(80):
            mid = (left + right) / 2
            if can_reach(mid):
                left = mid
            else:
                right = mid
        return left
