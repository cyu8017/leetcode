# LeetCode 0488 - Zuma Game
# https://leetcode.com/problems/zuma-game/

from functools import lru_cache


class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def shrink(s: str) -> str:
            i = 0
            while i < len(s):
                j = i
                while j < len(s) and s[j] == s[i]:
                    j += 1
                if j - i >= 3:
                    return shrink(s[:i] + s[j:])
                i = j
            return s

        @lru_cache(maxsize=None)
        def dfs(b: str, h: str) -> int:
            b = shrink(b)
            if not b:
                return 0
            best = float("inf")
            for i in range(len(b) + 1):
                for j, color in enumerate(h):
                    if i < len(b) and b[i] == color:
                        pass
                    elif i > 0 and b[i - 1] == color:
                        pass
                    else:
                        continue
                    new_b = shrink(b[:i] + color + b[i:])
                    if new_b == b:
                        continue
                    new_h = h[:j] + h[j + 1 :]
                    steps = dfs(new_b, new_h)
                    if steps != float("inf"):
                        best = min(best, steps + 1)
            return best

        result = dfs(board, hand)
        return -1 if result == float("inf") else result
