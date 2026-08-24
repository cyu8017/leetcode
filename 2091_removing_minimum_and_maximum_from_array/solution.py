# LeetCode 2091 - Removing Minimum and Maximum From Array
# https://leetcode.com/problems/removing-minimum-and-maximum-from-array/

from typing import List


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        mi = ma = 0
        for i, x in enumerate(nums):
            if x < nums[mi]:
                mi = i
            if x > nums[ma]:
                ma = i
        if mi > ma:
            mi, ma = ma, mi
        return min(ma + 1, n - mi, mi + 1 + n - ma)
