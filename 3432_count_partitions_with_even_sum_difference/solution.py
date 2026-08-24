# LeetCode 3432 - Count Partitions with Even Sum Difference
# https://leetcode.com/problems/count-partitions-with-even-sum-difference/

from typing import List


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = 0
        for x in nums:
            total += x
        ans = left = 0
        for i in range(len(nums) - 1):
            left += nums[i]
            if (left - (total - left)) % 2 == 0:
                ans += 1
        return ans
