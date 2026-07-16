# LeetCode 0573 - Squirrel Simulation
# https://leetcode.com/problems/squirrel-simulation/

from typing import List


class Solution:
    def minDistance(
        self,
        height: int,
        width: int,
        tree: List[int],
        squirrel: List[int],
        nuts: List[List[int]],
    ) -> int:
        def dist(a: List[int], b: List[int]) -> int:
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        total = sum(2 * dist(tree, nut) for nut in nuts)
        best_save = max(dist(tree, nut) - dist(squirrel, nut) for nut in nuts)
        return total - best_save
