# LeetCode 3819 - Rotate Non Negative Elements
# https://leetcode.com/problems/rotate-non-negative-elements/

from typing import List


class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        t = [x for x in nums if x >= 0]
        m = len(t)
        if m == 0:
            return nums
        d = [0] * m
        for i in range(m):
            d[((i - k) % m + m) % m] = t[i]
        j = 0
        for i in range(len(nums)):
            if nums[i] >= 0:
                nums[i] = d[j]
                j += 1
        return nums
