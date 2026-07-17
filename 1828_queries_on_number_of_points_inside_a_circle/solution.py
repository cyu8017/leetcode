# LeetCode 1828 - Queries on Number of Points Inside a Circle
# https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/

from typing import List


class Solution:
    def countPoints(
        self, points: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        result: List[int] = []
        for xq, yq, r in queries:
            radius_sq = r * r
            count = 0
            for x, y in points:
                if (x - xq) ** 2 + (y - yq) ** 2 <= radius_sq:
                    count += 1
            result.append(count)
        return result
