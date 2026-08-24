# LeetCode 2229 - Check if an Array Is Consecutive
# https://leetcode.com/problems/check-if-an-array-is-consecutive/

from typing import List


class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        mn = mx = nums[0]
        seen = set()
        for x in nums:
            if x in seen:
                return False
            seen.add(x)
            mn = min(mn, x)
            mx = max(mx, x)
        return mx - mn + 1 == len(nums)
