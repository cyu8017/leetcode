from collections import defaultdict
from typing import List


class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        graph = defaultdict(set)
        for a, b in pairs:
            graph[a].add(b)
            graph[b].add(a)
        nodes = list(graph)
        n = len(nodes)
        root = next((node for node in nodes if len(graph[node]) == n - 1), None)
        if root is None:
            return 0
        ans = 1
        for node in nodes:
            if node == root:
                continue
            parent = None
            parent_degree = n + 1
            for nei in graph[node]:
                if len(graph[nei]) >= len(graph[node]) and len(graph[nei]) < parent_degree:
                    parent = nei
                    parent_degree = len(graph[nei])
            if parent is None:
                return 0
            for nei in graph[node]:
                if nei != parent and nei not in graph[parent]:
                    return 0
            if len(graph[parent]) == len(graph[node]):
                ans = 2
        return ans
