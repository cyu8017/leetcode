# LeetCode 2587 - Rearrange Array to Maximize Prefix Score
# https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score/

from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort()
        s = 0
        ans = 0
        for i in range(len(nums) - 1, -1, -1):
            s += nums[i]
            if s > 0:
                ans += 1
            else:
                break
        return ans
