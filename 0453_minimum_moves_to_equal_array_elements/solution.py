# LeetCode 0453 - Minimum Moves to Equal Array Elements
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/


class Solution:
    def minMoves(self, nums: list[int]) -> int:
        minimum = min(nums)
        return sum(value - minimum for value in nums)
