# LeetCode 2219 - Maximum Sum Score of Array
# https://leetcode.com/problems/maximum-sum-score-of-array/

from typing import List


class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        total = sum(nums)
        pref = 0
        ans = float("-inf")
        for x in nums:
            pref += x
            ans = max(ans, pref, total - pref + x)
        return int(ans)
