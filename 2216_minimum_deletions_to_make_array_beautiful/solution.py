# LeetCode 2216 - Minimum Deletions to Make Array Beautiful
# https://leetcode.com/problems/minimum-deletions-to-make-array-beautiful/

from typing import List
class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        ans = 0
        i = 0
        n = len(nums)
        while i + 1 < n:
            if nums[i] == nums[i + 1]:
                ans += 1
                i += 1
            else:
                i += 2
        if (n - ans) % 2 != 0:
            ans += 1
        return ans
