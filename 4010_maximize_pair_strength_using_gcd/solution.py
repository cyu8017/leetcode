# LeetCode 4010 - Maximize Pair Strength Using GCD
# https://leetcode.com/problems/maximize-pair-strength-using-gcd/

from typing import List


class Solution:
    def Gcd(self, a: int, b: int) -> int:
        while b != 0:
            t = a % b
            a = b
            b = t
        return a

    def maxPairStrength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                g = self.Gcd(nums[i], nums[j])
                x = nums[i] * nums[j] // (g * g)
                ans = max(ans, x)
        return ans
