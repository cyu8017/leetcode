# LeetCode 2963 - Count the Number of Good Partitions
# https://leetcode.com/problems/count-the-number-of-good-partitions/

from typing import List


class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        mod = 1000000007
        last = {}
        for i in range(len(nums)):
            last[nums[i]] = i
        ans = 1
        end = 0
        for i in range(len(nums)):
            if last[nums[i]] > end:
                end = last[nums[i]]
            if i == end and i != len(nums) - 1:
                ans = ans * 2 % mod
        return ans
