# LeetCode 2077 - Paths in Maze That Lead to Same Room
# https://leetcode.com/problems/paths-in-maze-that-lead-to-same-room/

from typing import List


class Solution:
    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:
        g = [set() for _ in range(n + 1)]
        for a, b in corridors:
            g[a].add(b)
            g[b].add(a)
        ans = 0
        for a, b in corridors:
            for c in g[a]:
                if c in g[b]:
                    ans += 1
        return ans // 3
