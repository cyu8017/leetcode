# LeetCode 1042 - Flower Planting With No Adjacent
# https://leetcode.com/problems/flower-planting-with-no-adjacent/

from collections import defaultdict


class Solution:
    def gardenNoAdj(self, n: int, paths: list[list[int]]) -> list[int]:
        graph = defaultdict(list)
        for a, b in paths:
            graph[a].append(b)
            graph[b].append(a)
        ans = [0] * (n + 1)
        for garden in range(1, n + 1):
            used = {ans[nei] for nei in graph[garden]}
            ans[garden] = next(c for c in range(1, 5) if c not in used)
        return ans[1:]
