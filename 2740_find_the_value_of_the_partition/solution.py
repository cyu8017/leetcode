# LeetCode 2740 - Find the Value of the Partition
# https://leetcode.com/problems/find-the-value-of-the-partition/

from typing import List


class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        ans = 10**18
        for i in range(1, len(nums)):
            ans = min(ans, nums[i] - nums[i - 1])
        return ans
