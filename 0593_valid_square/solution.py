# LeetCode 0593 - Valid Square
# https://leetcode.com/problems/valid-square/

from typing import List


class Solution:
    def validSquare(
        self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]
    ) -> bool:
        def dist(a: List[int], b: List[int]) -> int:
            return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

        points = [p1, p2, p3, p4]
        distances = sorted(
            dist(points[i], points[j])
            for i in range(4)
            for j in range(i + 1, 4)
        )
        # 4 equal sides, then 2 equal diagonals; side length must be positive
        return (
            distances[0] > 0
            and distances[0] == distances[1] == distances[2] == distances[3]
            and distances[4] == distances[5]
            and distances[4] == 2 * distances[0]
        )
