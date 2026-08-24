# LeetCode 3528 - Unit Conversion I
# https://leetcode.com/problems/unit-conversion-i/

from typing import List


class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        mod = 1000000007
        n = len(conversions) + 1
        g = [[] for _ in range(n)]
        for e in conversions:
            g[e[0]].append((e[1], e[2]))
        ans = [0] * n

        def dfs(s: int, mul: int) -> None:
            ans[s] = mul
            for to, w in g[s]:
                dfs(to, mul * w % mod)

        dfs(0, 1)
        return ans
