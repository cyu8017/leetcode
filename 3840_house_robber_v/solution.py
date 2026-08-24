# LeetCode 3840 - House Robber V
# https://leetcode.com/problems/house-robber-v/

from typing import List


class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
        n = len(nums)
        f, g = 0, nums[0]
        for i in range(1, n):
            if colors[i - 1] == colors[i]:
                nf = max(f, g)
                g = f + nums[i]
                f = nf
            else:
                nf = max(f, g)
                g = nf + nums[i]
                f = nf
        return max(f, g)
