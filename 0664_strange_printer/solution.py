# LeetCode 0664 - Strange Printer
# https://leetcode.com/problems/strange-printer/

from functools import lru_cache


class Solution:
    def strangePrinter(self, s: str) -> int:
        @lru_cache(None)
        def dfs(i: int, j: int) -> int:
            if i > j:
                return 0
            ans = dfs(i + 1, j) + 1
            for k in range(i + 1, j + 1):
                if s[k] == s[i]:
                    ans = min(ans, dfs(i, k - 1) + dfs(k + 1, j))
            return ans

        return dfs(0, len(s) - 1)
