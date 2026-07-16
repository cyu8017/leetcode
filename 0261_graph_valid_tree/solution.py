# LeetCode 0261 - Graph Valid Tree
# https://leetcode.com/problems/graph-valid-tree/

from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        parent = list(range(n))

        def find(node: int) -> int:
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        for left, right in edges:
            root_left = find(left)
            root_right = find(right)
            if root_left == root_right:
                return False
            parent[root_left] = root_right
        return True
