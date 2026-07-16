# LeetCode 0587 - Erect the Fence
# https://leetcode.com/problems/erect-the-fence/

from typing import List


class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        points = sorted((x, y) for x, y in trees)
        if len(points) <= 1:
            return [list(p) for p in points]

        def cross(o: tuple[int, int], a: tuple[int, int], b: tuple[int, int]) -> int:
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

        def build(ordered: list[tuple[int, int]]) -> list[tuple[int, int]]:
            hull: list[tuple[int, int]] = []
            for point in ordered:
                while len(hull) >= 2 and cross(hull[-2], hull[-1], point) < 0:
                    hull.pop()
                hull.append(point)
            return hull

        lower = build(points)
        upper = build(reversed(points))
        hull = list(dict.fromkeys(lower[:-1] + upper[:-1]))
        return [list(point) for point in hull]
