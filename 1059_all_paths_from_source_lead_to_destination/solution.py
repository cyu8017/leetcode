# LeetCode 1059 - All Paths from Source Lead to Destination
# https://leetcode.com/problems/all-paths-from-source-lead-to-destination/

from collections import defaultdict


class Solution:
    def leadsToDestination(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
        # 0 unvisited, 1 in progress, 2 confirmed
        state = [0] * n

        def dfs(node: int) -> bool:
            if not graph[node]:
                return node == destination
            if state[node] == 1:
                return False
            if state[node] == 2:
                return True
            state[node] = 1
            for nxt in graph[node]:
                if not dfs(nxt):
                    return False
            state[node] = 2
            return True

        return dfs(source)
