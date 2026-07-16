from typing import List

from functools import lru_cache

class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 1_000_000_007
        @lru_cache(None)
        def dp(city, left):
            total = int(city == finish)
            for nxt in range(len(locations)):
                cost = abs(locations[city] - locations[nxt])
                if nxt != city and cost <= left:
                    total += dp(nxt, left - cost)
            return total % MOD
        return dp(start, fuel)
