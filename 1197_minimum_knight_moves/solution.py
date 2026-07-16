# LeetCode 1197 - Minimum Knight Moves
# https://leetcode.com/problems/minimum-knight-moves/

from collections import deque
from functools import lru_cache


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)

        @lru_cache(None)
        def dfs(a: int, b: int) -> int:
            if a + b == 0:
                return 0
            if a + b == 2:
                return 2
            return min(dfs(abs(a - 1), abs(b - 2)), dfs(abs(a - 2), abs(b - 1))) + 1

        return dfs(x, y)
