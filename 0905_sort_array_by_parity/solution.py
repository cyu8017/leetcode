# LeetCode 0905 - Sort Array By Parity
# https://leetcode.com/problems/sort-array-by-parity/

class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        i = 0
        for j, x in enumerate(nums):
            if x % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums
