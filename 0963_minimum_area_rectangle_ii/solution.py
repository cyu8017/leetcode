# LeetCode 0963 - Minimum Area Rectangle II
# https://leetcode.com/problems/minimum-area-rectangle-ii/

from collections import defaultdict
from itertools import combinations


class Solution:
    def minAreaFreeRect(self, points: list[list[int]]) -> float:
        pts = [complex(x, y) for x, y in points]
        groups: dict[tuple, list[tuple[complex, complex]]] = defaultdict(list)
        for p, q in combinations(pts, 2):
            center = ((p.real + q.real) / 2, (p.imag + q.imag) / 2)
            dist = abs(p - q) ** 2
            groups[(center, dist)].append((p, q))
        ans = float("inf")
        for pairs in groups.values():
            for (p1, q1), (p2, q2) in combinations(pairs, 2):
                area = abs(p1 - p2) * abs(p1 - q2)
                if area:
                    ans = min(ans, area)
        return 0.0 if ans == float("inf") else ans
