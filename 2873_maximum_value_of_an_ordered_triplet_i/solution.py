# LeetCode 2873 - Maximum Value of an Ordered Triplet I
# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/

from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    cand = (nums[i] - nums[j]) * nums[k]
                    if cand > ans:
                        ans = cand
        return ans
