# LeetCode 0834 - Sum of Distances in Tree
# https://leetcode.com/problems/sum-of-distances-in-tree/

from collections import defaultdict


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: list[list[int]]) -> list[int]:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        count = [1] * n
        ans = [0] * n

        def post(node: int, parent: int) -> None:
            for child in graph[node]:
                if child == parent:
                    continue
                post(child, node)
                count[node] += count[child]
                ans[node] += ans[child] + count[child]

        def reroot(node: int, parent: int) -> None:
            for child in graph[node]:
                if child == parent:
                    continue
                ans[child] = ans[node] - count[child] + (n - count[child])
                reroot(child, node)

        post(0, -1)
        reroot(0, -1)
        return ans
