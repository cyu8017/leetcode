# LeetCode 0410 - Split Array Largest Sum
# https://leetcode.com/problems/split-array-largest-sum/

from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)

        def can_split(limit: int) -> bool:
            parts = 1
            current = 0
            for value in nums:
                if current + value > limit:
                    parts += 1
                    current = 0
                current += value
            return parts <= k

        while left < right:
            mid = (left + right) // 2
            if can_split(mid):
                right = mid
            else:
                left = mid + 1

        return left
