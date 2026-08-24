# LeetCode 2294 - Partition Array Such That Maximum Difference Is K
# https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/

from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 1
        start = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - start > k:
                ans += 1
                start = nums[i]
        return ans
