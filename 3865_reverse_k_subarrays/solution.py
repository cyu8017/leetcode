# LeetCode 3865 - Reverse K Subarrays
# https://leetcode.com/problems/reverse-k-subarrays/

from typing import List


class Solution:
    def reverseSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        m = n // k
        i = 0
        while i < n:
            lo = i
            hi = i + m - 1
            while lo < hi:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                lo += 1
                hi -= 1
            i += m
        return nums
