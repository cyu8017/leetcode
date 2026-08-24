# LeetCode 3221 - Maximum Array Hopping Score II
# https://leetcode.com/problems/maximum-array-hopping-score-ii/

from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        stk = []
        for i in range(len(nums)):
            while stk and nums[stk[-1]] <= nums[i]:
                stk.pop()
            stk.append(i)
        ans, cur = 0, 0
        for j in stk:
            ans += (j - cur) * nums[j]
            cur = j
        return ans
