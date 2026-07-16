# LeetCode 0797 - All Paths From Source to Target
# https://leetcode.com/problems/all-paths-from-source-to-target/

from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        answer: list[list[int]] = []

        def dfs(node: int, path: list[int]) -> None:
            if node == target:
                answer.append(path[:])
                return
            for nei in graph[node]:
                path.append(nei)
                dfs(nei, path)
                path.pop()

        dfs(0, [0])
        return answer
