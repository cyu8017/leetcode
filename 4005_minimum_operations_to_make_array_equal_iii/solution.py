# LeetCode 4005 - Minimum Operations to Make Array Equal III
# https://leetcode.com/problems/minimum-operations-to-make-array-equal-iii/

from typing import List


class Solution:
    def Cost(self, x: int, t: int) -> int:
        if x == t:
            return 0
        if x % t == 0 or t % x == 0:
            return 1
        return 2

    def Gcd(self, a: int, b: int) -> int:
        while b != 0:
            t = a % b
            a = b
            b = t
        return a

    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        g = nums[0]
        mn = nums[0]
        for i in range(1, n):
            g = self.Gcd(g, nums[i])
            mn = min(mn, nums[i])
        cands = set()
        for x in nums:
            cands.add(x)
        d = 1
        while d * d <= mn:
            if mn % d == 0:
                cands.add(d)
                cands.add(mn // d)
            d += 1
        cands.add(g)
        ans = 2147483647
        for t in cands:
            s = 0
            for x in nums:
                s += self.Cost(x, t)
                if s >= ans:
                    break
            ans = min(ans, s)
        return ans
