# LeetCode 3326 - Minimum Division Operations to Make Array Non Decreasing
# https://leetcode.com/problems/minimum-division-operations-to-make-array-non-decreasing/

from typing import List


def smallestProperDivisor(x: int) -> int:
    d = 2
    while d * d <= x:
        if x % d == 0:
            return d
        d += 1
    return x


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                continue
            while nums[i] > nums[i + 1]:
                d = smallestProperDivisor(nums[i])
                if d == nums[i]:
                    return -1
                nums[i] = nums[i] // d
                ops += 1
                if nums[i] > nums[i + 1] and smallestProperDivisor(nums[i]) == nums[i]:
                    return -1
        return ops
