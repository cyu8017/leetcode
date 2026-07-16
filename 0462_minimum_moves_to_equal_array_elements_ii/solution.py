# LeetCode 0462 - Minimum Moves to Equal Array Elements II
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/


class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        median = nums[len(nums) // 2]
        return sum(abs(value - median) for value in nums)
