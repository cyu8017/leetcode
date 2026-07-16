# LeetCode 0581 - Shortest Unsorted Continuous Subarray
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = -1, -2
        max_seen, min_seen = nums[0], nums[-1]

        for i in range(n):
            max_seen = max(max_seen, nums[i])
            if nums[i] < max_seen:
                right = i
            min_seen = min(min_seen, nums[n - 1 - i])
            if nums[n - 1 - i] > min_seen:
                left = n - 1 - i

        return right - left + 1
