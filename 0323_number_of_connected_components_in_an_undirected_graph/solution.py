# LeetCode 0323 - Number of Connected Components in an Undirected Graph
# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [0] * n

        def find(node: int) -> int:
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        components = n
        for left, right in edges:
            root_left = find(left)
            root_right = find(right)
            if root_left == root_right:
                continue
            if rank[root_left] < rank[root_right]:
                root_left, root_right = root_right, root_left
            parent[root_right] = root_left
            if rank[root_left] == rank[root_right]:
                rank[root_left] += 1
            components -= 1
        return components
