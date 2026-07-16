# LeetCode 1140 - Stone Game II
# https://leetcode.com/problems/stone-game-ii/

from functools import lru_cache


class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        @lru_cache(None)
        def dfs(i: int, m: int) -> int:
            if i >= n:
                return 0
            if m + i >= n:
                return suffix[i]
            return suffix[i] - min(
                dfs(i + x, max(x, m)) for x in range(1, min(m * 2, n - i) + 1)
            )

        return dfs(0, 1)
