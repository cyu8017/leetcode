from typing import List
from functools import lru_cache

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7

        def valid_column(mask: int) -> bool:
            prev = -1
            for _ in range(m):
                c = mask % 3
                if c == prev:
                    return False
                prev = c
                mask //= 3
            return True

        def get_colors(mask: int) -> List[int]:
            cols = []
            for _ in range(m):
                cols.append(mask % 3)
                mask //= 3
            return cols

        states = [s for s in range(3 ** m) if valid_column(s)]
        compat = {s: [] for s in states}
        for a in states:
            ca = get_colors(a)
            for b in states:
                cb = get_colors(b)
                if all(x != y for x, y in zip(ca, cb)):
                    compat[a].append(b)

        @lru_cache(None)
        def dp(col: int, prev: int) -> int:
            if col == n:
                return 1
            total = 0
            for cur in (states if prev == -1 else compat[prev]):
                total = (total + dp(col + 1, cur)) % MOD
            return total

        return dp(0, -1)
