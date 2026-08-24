# LeetCode 2210 - Count Hills and Valleys in an Array
# https://leetcode.com/problems/count-hills-and-valleys-in-an-array/

from typing import List
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        compact = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != compact[len(compact) - 1]:
                compact.append(nums[i])
        ans = 0
        i = 1
        while i + 1 < len(compact):
            if (compact[i] > compact[i - 1] and compact[i] > compact[i + 1]) or (compact[i] < compact[i - 1] and compact[i] < compact[i + 1]):
                ans += 1
            i += 1
        return ans
