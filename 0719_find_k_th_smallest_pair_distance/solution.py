# LeetCode 0719 - Find K-th Smallest Pair Distance
# https://leetcode.com/problems/find-k-th-smallest-pair-distance/

from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        def count_pairs(distance: int) -> int:
            count = left = 0
            for right, value in enumerate(nums):
                while value - nums[left] > distance:
                    left += 1
                count += right - left
            return count

        lo, hi = 0, nums[-1] - nums[0]
        while lo < hi:
            mid = (lo + hi) // 2
            if count_pairs(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo
