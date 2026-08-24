# LeetCode 2161 - Partition Array According to Given Pivot
# https://leetcode.com/problems/partition-array-according-to-given-pivot/

from typing import List
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans = [None] * (len(nums))
        i = 0
        for x in nums:
            if x < pivot:
                ans[i] = x
                i += 1
        for x in nums:
            if x == pivot:
                ans[i] = x
                i += 1
        for x in nums:
            if x > pivot:
                ans[i] = x
                i += 1
        return ans
