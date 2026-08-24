# LeetCode 2460 - Apply Operations to an Array
# https://leetcode.com/problems/apply-operations-to-an-array/

from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        a = nums[:]
        for i in range(n - 1):
            if a[i] == a[i + 1]:
                a[i] *= 2
                a[i + 1] = 0
        ans = [0] * n
        j = 0
        for x in a:
            if x != 0:
                ans[j] = x
                j += 1
        return ans
