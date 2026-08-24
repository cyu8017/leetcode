# LeetCode 3940 - Limit Occurrences In Sorted Array
# https://leetcode.com/problems/limit-occurrences-in-sorted-array/

from typing import List


class Solution:
    def limitOccurrences(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        cnt = 1
        l = 1
        for r in range(1, n):
            if nums[r] != nums[r - 1]:
                cnt = 1
            else:
                cnt += 1
            if cnt <= k:
                nums[l] = nums[r]
                l += 1
        return nums[:l]
