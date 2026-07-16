# LeetCode 0310 - Minimum Height Trees
# https://leetcode.com/problems/minimum-height-trees/

from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return list(range(n))
        graph: list[list[int]] = [[] for _ in range(n)]
        degree = [0] * n
        for left, right in edges:
            graph[left].append(right)
            graph[right].append(left)
            degree[left] += 1
            degree[right] += 1
        leaves = [node for node in range(n) if degree[node] == 1]
        remaining = n
        while remaining > 2:
            remaining -= len(leaves)
            new_leaves: list[int] = []
            for leaf in leaves:
                for neighbor in graph[leaf]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves
