# LeetCode 0305 - Number of Islands II
# https://leetcode.com/problems/number-of-islands-ii/

from typing import List


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        parent: dict[int, int] = {}
        rank: dict[int, int] = {}

        def find(index: int) -> int:
            parent.setdefault(index, index)
            rank.setdefault(index, 0)
            if parent[index] != index:
                parent[index] = find(parent[index])
            return parent[index]

        def union(left: int, right: int) -> bool:
            root_left = find(left)
            root_right = find(right)
            if root_left == root_right:
                return False
            if rank[root_left] < rank[root_right]:
                root_left, root_right = root_right, root_left
            parent[root_right] = root_left
            if rank[root_left] == rank[root_right]:
                rank[root_left] += 1
            return True

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        result: list[int] = []
        islands = 0
        for row, col in positions:
            index = row * n + col
            if index in parent:
                result.append(islands)
                continue
            parent[index] = index
            islands += 1
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < m and 0 <= nc < n:
                    neighbor = nr * n + nc
                    if neighbor in parent and union(index, neighbor):
                        islands -= 1
            result.append(islands)
        return result
