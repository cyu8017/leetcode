# LeetCode 2501 - Longest Square Streak in an Array
# https://leetcode.com/problems/longest-square-streak-in-an-array/

from typing import List


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        seen = set(nums)
        best = -1
        for x in nums:
            if x not in seen:
                continue
            length = 0
            cur = x
            while cur in seen:
                length += 1
                seen.remove(cur)
                if cur > 100000:
                    break
                cur = cur * cur
            if length >= 2 and length > best:
                best = length
        return best
