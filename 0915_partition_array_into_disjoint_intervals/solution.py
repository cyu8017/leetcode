# LeetCode 0915 - Partition Array Into Disjoint Intervals
# https://leetcode.com/problems/partition-array-into-disjoint-intervals/

class Solution:
    def partitionDisjoint(self, nums: list[int]) -> int:
        max_left = nums[0]
        for i in range(1, len(nums)):
            if max_left <= min(nums[i:]):
                return i
            max_left = max(max_left, nums[i])
        return len(nums) - 1
