# LeetCode 3511 - Make a Positive Array
# https://leetcode.com/problems/make-a-positive-array/

from typing import List


class Solution:
    def makeArrayPositive(self, nums: List[int]) -> int:
        ans = 0
        l = -1
        pre_mx = 0
        s = 0
        for r in range(len(nums)):
            s += nums[r]
            if r - l > 2 and s <= pre_mx:
                ans += 1
                l = r
                pre_mx = 0
                s = 0
            elif r - l >= 2:
                pre_mx = max(pre_mx, s - nums[r] - nums[r - 1])
        return ans
