# LeetCode 2447 - Number of Subarrays With GCD Equal to K
# https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/

from typing import List


class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def gcd(a: int, b: int) -> int:
            while b != 0:
                a, b = b, a % b
            return a

        ans = 0
        n = len(nums)
        for i in range(n):
            g = 0
            for j in range(i, n):
                g = gcd(g, nums[j])
                if g < k:
                    break
                if g == k:
                    ans += 1
        return ans
