# LeetCode 3812 - Minimum Edge Toggles on a Tree
# https://leetcode.com/problems/minimum-edge-toggles-on-a-tree/

from typing import List


class Solution:
    def minimumFlips(self, n: int, edges: List[List[int]], start: List[int], target: List[int]) -> List[int]:
        g = [[] for _ in range(n)]
        for i in range(n - 1):
            a, b = edges[i][0], edges[i][1]
            g[a].append((b, i))
            g[b].append((a, i))
        ans = []

        def dfs(a: int, fa: int) -> bool:
            rev = start[a] != target[a]
            for b, i in g[a]:
                if b != fa and dfs(b, a):
                    ans.append(i)
                    rev = not rev
            return rev

        if dfs(0, -1):
            return [-1]
        ans.sort()
        return ans
