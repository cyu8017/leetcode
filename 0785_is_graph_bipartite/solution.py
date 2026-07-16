# LeetCode 0785 - Is Graph Bipartite?
# https://leetcode.com/problems/is-graph-bipartite/

from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1] * len(graph)

        def dfs(node: int, c: int) -> bool:
            color[node] = c
            for nei in graph[node]:
                if color[nei] == -1:
                    if not dfs(nei, c ^ 1):
                        return False
                elif color[nei] == c:
                    return False
            return True

        for node in range(len(graph)):
            if color[node] == -1 and not dfs(node, 0):
                return False
        return True
