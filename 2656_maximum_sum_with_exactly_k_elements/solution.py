# LeetCode 2656 - Maximum Sum With Exactly K Elements
# https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/

from typing import List


class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        mx = nums[0]
        for x in nums:
            if x > mx:
                mx = x
        return k * mx + k * (k - 1) // 2
