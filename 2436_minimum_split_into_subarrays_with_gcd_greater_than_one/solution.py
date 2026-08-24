# LeetCode 2436 - Minimum Split Into Subarrays With GCD Greater Than One
# https://leetcode.com/problems/minimum-split-into-subarrays-with-gcd-greater-than-one/

from typing import List


class Solution:
    def minimumSplits(self, nums: List[int]) -> int:
        def gcd(a: int, b: int) -> int:
            while b != 0:
                a, b = b, a % b
            return a

        ans = 1
        g = nums[0]
        for i in range(1, len(nums)):
            ng = gcd(g, nums[i])
            if ng == 1:
                ans += 1
                g = nums[i]
            else:
                g = ng
        return ans
