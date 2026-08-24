# LeetCode 2097 - Valid Arrangement of Pairs
# https://leetcode.com/problems/valid-arrangement-of-pairs/

from typing import List


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        g = {}
        indeg, outdeg = {}, {}
        for u, v in pairs:
            g.setdefault(u, []).append(v)
            outdeg[u] = outdeg.get(u, 0) + 1
            indeg[v] = indeg.get(v, 0) + 1
        start = pairs[0][0]
        for u, o in outdeg.items():
            if o - indeg.get(u, 0) == 1:
                start = u
                break
        path = []

        def dfs(u: int) -> None:
            nbrs = g.get(u, [])
            while nbrs:
                v = nbrs.pop()
                dfs(v)
            path.append(u)

        dfs(start)
        path.reverse()
        return [[path[i], path[i + 1]] for i in range(len(path) - 1)]
