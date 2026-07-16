# LeetCode 0087 - Scramble String
# https://leetcode.com/problems/scramble-string/

from functools import lru_cache


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @lru_cache(None)
        def dfs(a: str, b: str) -> bool:
            if a == b:
                return True
            if sorted(a) != sorted(b):
                return False

            n = len(a)
            for i in range(1, n):
                if dfs(a[:i], b[:i]) and dfs(a[i:], b[i:]):
                    return True
                if dfs(a[:i], b[-i:]) and dfs(a[i:], b[:-i]):
                    return True
            return False

        return dfs(s1, s2)
