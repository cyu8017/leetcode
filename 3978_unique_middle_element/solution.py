# LeetCode 3978 - Unique Middle Element
# https://leetcode.com/problems/unique-middle-element/

from typing import List


class Solution:
    def isMiddleElementUnique(self, nums: List[int]) -> bool:
        mid = nums[len(nums) // 2]
        cnt = 0
        for x in nums:
            if x == mid:
                cnt += 1
        return cnt == 1
