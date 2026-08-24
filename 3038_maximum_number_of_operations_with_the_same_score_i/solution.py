# LeetCode 3038 - Maximum Number of Operations With the Same Score I
# https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-i/

from typing import List


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        s = nums[0] + nums[1]
        n = len(nums)
        ans = 0
        i = 0
        while i + 1 < n and nums[i] + nums[i + 1] == s:
            ans += 1
            i += 2
        return ans
