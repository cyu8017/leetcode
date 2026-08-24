# LeetCode 3701 - Compute Alternating Sum
# https://leetcode.com/problems/compute-alternating-sum/

from typing import List


class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        ans = 0
        for i, x in enumerate(nums):
            if i % 2 == 0:
                ans += x
            else:
                ans -= x
        return ans
