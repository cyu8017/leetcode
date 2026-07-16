from math import comb, isqrt
from typing import List


class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        mod = 10 ** 9 + 7
        ans = []
        for n, k in queries:
            ways = 1
            d = 2
            value = k
            while d * d <= value:
                if value % d == 0:
                    exp = 0
                    while value % d == 0:
                        value //= d
                        exp += 1
                    ways = ways * comb(n + exp - 1, exp) % mod
                d += 1 if d == 2 else 2
            if value > 1:
                ways = ways * n % mod
            ans.append(ways)
        return ans
