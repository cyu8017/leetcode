# LeetCode 3655 - XOR After Range Multiplication Queries II
# https://leetcode.com/problems/xor-after-range-multiplication-queries-ii/

from typing import List


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 1000000007
        n = len(nums)
        by_k = {}
        for q in queries:
            by_k.setdefault(q[2], []).append(q)
        res = nums[:]
        for lst in by_k.values():
            fac = [1] * n
            for u in lst:
                for i in range(u[0], u[1] + 1, u[2]):
                    fac[i] = fac[i] * u[3] % MOD
            for i in range(n):
                res[i] = res[i] * fac[i] % MOD
        ans = 0
        for v in res:
            ans ^= v
        return ans
