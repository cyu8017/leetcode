# LeetCode 1192 - Critical Connections in a Network
# https://leetcode.com/problems/critical-connections-in-a-network/

from collections import defaultdict


class Solution:
    def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
        disc = [-1] * n
        low = [-1] * n
        time = 0
        bridges: list[list[int]] = []

        def dfs(node: int, parent: int) -> None:
            nonlocal time
            disc[node] = low[node] = time
            time += 1
            for nxt in graph[node]:
                if nxt == parent:
                    continue
                if disc[nxt] == -1:
                    dfs(nxt, node)
                    low[node] = min(low[node], low[nxt])
                    if low[nxt] > disc[node]:
                        bridges.append([node, nxt])
                else:
                    low[node] = min(low[node], disc[nxt])

        dfs(0, -1)
        return [[min(a, b), max(a, b)] for a, b in bridges]
