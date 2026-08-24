# LeetCode 2344 - Minimum Deletions to Make Array Divisible
# https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/

from typing import List


class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        def gcd(a: int, b: int) -> int:
            while b != 0:
                a, b = b, a % b
            return a

        g = numsDivide[0]
        for i in range(1, len(numsDivide)):
            g = gcd(g, numsDivide[i])
        nums = sorted(nums)
        for i, x in enumerate(nums):
            if g % x == 0:
                return i
        return -1
