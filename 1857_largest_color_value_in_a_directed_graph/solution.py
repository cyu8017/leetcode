# LeetCode 1857 - Largest Color Value in a Directed Graph
# https://leetcode.com/problems/largest-color-value-in-a-directed-graph/

from collections import deque
from typing import List


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        indegree = [0] * n
        adjacency: list[list[int]] = [[] for _ in range(n)]

        for from_node, to_node in edges:
            adjacency[from_node].append(to_node)
            indegree[to_node] += 1

        queue = deque(node for node in range(n) if indegree[node] == 0)
        dp = [[0] * 26 for _ in range(n)]
        for node in range(n):
            dp[node][ord(colors[node]) - ord("a")] = 1

        processed = 0
        answer = 0

        while queue:
            node = queue.popleft()
            processed += 1
            answer = max(answer, max(dp[node]))

            for neighbor in adjacency[node]:
                neighbor_color = ord(colors[neighbor]) - ord("a")
                for color_index in range(26):
                    candidate = dp[node][color_index]
                    if color_index == neighbor_color:
                        candidate += 1
                    if candidate > dp[neighbor][color_index]:
                        dp[neighbor][color_index] = candidate

                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return answer if processed == n else -1
