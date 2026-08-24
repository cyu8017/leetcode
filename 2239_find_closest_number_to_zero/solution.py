# LeetCode 2239 - Find Closest Number to Zero
# https://leetcode.com/problems/find-closest-number-to-zero/

from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans = nums[0]
        for x in nums:
            if abs(x) < abs(ans) or (abs(x) == abs(ans) and x > ans):
                ans = x
        return ans
