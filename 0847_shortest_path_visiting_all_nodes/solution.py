# LeetCode 0847 - Shortest Path Visiting All Nodes
# https://leetcode.com/problems/shortest-path-visiting-all-nodes/

from collections import deque


class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        n = len(graph)
        target = (1 << n) - 1
        queue = deque((i, 1 << i, 0) for i in range(n))
        seen = {(i, 1 << i) for i in range(n)}
        while queue:
            node, mask, dist = queue.popleft()
            if mask == target:
                return dist
            for nxt in graph[node]:
                nmask = mask | (1 << nxt)
                state = (nxt, nmask)
                if state not in seen:
                    seen.add(state)
                    queue.append((nxt, nmask, dist + 1))
        return -1
