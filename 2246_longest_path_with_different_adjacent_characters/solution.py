# LeetCode 2246 - Longest Path With Different Adjacent Characters
# https://leetcode.com/problems/longest-path-with-different-adjacent-characters/

from typing import List


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[parent[i]].append(i)
        ans = 1

        def dfs(u: int) -> int:
            nonlocal ans
            best1 = best2 = 0
            for v in g[u]:
                length = dfs(v)
                if s[v] == s[u]:
                    continue
                if length > best1:
                    best2 = best1
                    best1 = length
                elif length > best2:
                    best2 = length
            ans = max(ans, 1 + best1 + best2)
            return 1 + best1

        dfs(0)
        return ans
