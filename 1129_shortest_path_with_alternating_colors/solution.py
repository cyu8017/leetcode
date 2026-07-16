# LeetCode 1129 - Shortest Path with Alternating Colors
# https://leetcode.com/problems/shortest-path-with-alternating-colors/

from collections import defaultdict, deque


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
        graph = [defaultdict(list), defaultdict(list)]
        for u, v in redEdges:
            graph[0][u].append(v)
        for u, v in blueEdges:
            graph[1][u].append(v)
        ans = [-1] * n
        queue = deque([(0, 0, 0), (0, 1, 0)])
        seen = {(0, 0), (0, 1)}
        while queue:
            node, color, dist = queue.popleft()
            if ans[node] == -1:
                ans[node] = dist
            next_color = 1 - color
            for nxt in graph[color][node]:
                state = (nxt, next_color)
                if state not in seen:
                    seen.add(state)
                    queue.append((nxt, next_color, dist + 1))
        return ans
