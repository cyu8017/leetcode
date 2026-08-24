# LeetCode 3535 - Unit Conversion II
# https://leetcode.com/problems/unit-conversion-ii/

from typing import List


class Solution:
    def queryConversions(
        self, conversions: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        MOD = 1000000007

        def qpow(x: int, n: int) -> int:
            res = 1
            bx, bn = x, n
            while bn > 0:
                if bn & 1:
                    res = res * bx % MOD
                bx = bx * bx % MOD
                bn >>= 1
            return res

        n = len(conversions) + 1
        g = [[] for _ in range(n)]
        for e in conversions:
            g[e[0]].append((e[1], e[2]))
        res = [0] * n

        def dfs(s: int, mul: int) -> None:
            res[s] = mul
            for to, w in g[s]:
                dfs(to, mul * w % MOD)

        dfs(0, 1)
        ans = [0] * len(queries)
        for i, q in enumerate(queries):
            ans[i] = res[q[1]] * qpow(res[q[0]], MOD - 2) % MOD
        return ans
