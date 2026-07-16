# LeetCode 0399 - Evaluate Division
# https://leetcode.com/problems/evaluate-division/

from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph: dict[str, dict[str, float]] = defaultdict(dict)

        for (dividend, divisor), value in zip(equations, values):
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1.0 / value

        def dfs(start: str, end: str, visited: set[str]) -> float:
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            visited.add(start)
            for neighbor, weight in graph[start].items():
                if neighbor in visited:
                    continue
                result = dfs(neighbor, end, visited)
                if result != -1.0:
                    return weight * result
            return -1.0

        return [dfs(start, end, set()) for start, end in queries]
