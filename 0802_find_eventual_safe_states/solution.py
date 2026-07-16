# LeetCode 0802 - Find Eventual Safe States
# https://leetcode.com/problems/find-eventual-safe-states/

from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        color = [0] * n  # 0 = unvisited, 1 = visiting, 2 = safe

        def dfs(node: int) -> bool:
            if color[node]:
                return color[node] == 2
            color[node] = 1
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            color[node] = 2
            return True

        return [i for i in range(n) if dfs(i)]
