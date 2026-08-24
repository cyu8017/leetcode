# LeetCode 3725 - Count Ways to Choose Coprime Integers from Rows
# https://leetcode.com/problems/count-ways-to-choose-coprime-integers-from-rows/

from typing import List
import math


class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        MOD = 1000000007
        m = len(mat)
        dp = {}
        for v in mat[0]:
            dp[v] = dp.get(v, 0) + 1
        for i in range(1, m):
            ndp = {}
            for v in mat[i]:
                for key, val in dp.items():
                    ng = math.gcd(key, v)
                    ndp[ng] = (ndp.get(ng, 0) + val) % MOD
            dp = ndp
        return dp.get(1, 0)
