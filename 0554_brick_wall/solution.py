# LeetCode 0554 - Brick Wall
# https://leetcode.com/problems/brick-wall/

from collections import Counter
from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edges: Counter[int] = Counter()
        for row in wall:
            width = 0
            for brick in row[:-1]:
                width += brick
                edges[width] += 1
        return len(wall) - (max(edges.values()) if edges else 0)
