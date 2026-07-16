# LeetCode 0896 - Monotonic Array
# https://leetcode.com/problems/monotonic-array/

class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        inc = dec = True
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                inc = False
            if nums[i] > nums[i - 1]:
                dec = False
        return inc or dec
