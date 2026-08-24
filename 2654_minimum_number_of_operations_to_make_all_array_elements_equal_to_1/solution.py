# LeetCode 2654 - Minimum Number of Operations to Make All Array Elements Equal to 1
# https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        n = len(nums)
        ones = sum(1 for x in nums if x == 1)
        if ones > 0:
            return n - ones
        best = n + 1
        for i in range(n):
            g = 0
            for j in range(i, n):
                g = gcd(g, nums[j])
                if g == 1:
                    best = min(best, j - i)
                    break
        if best == n + 1:
            return -1
        return best + n - 1
