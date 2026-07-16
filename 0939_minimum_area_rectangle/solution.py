# LeetCode 0939 - Minimum Area Rectangle
# https://leetcode.com/problems/minimum-area-rectangle/

from collections import defaultdict


class Solution:
    def minAreaRect(self, points: list[list[int]]) -> int:
        by_x: dict[int, list[int]] = defaultdict(list)
        for x, y in points:
            by_x[x].append(y)
        last: dict[tuple[int, int], int] = {}
        ans = float("inf")
        for x in sorted(by_x):
            ys = sorted(by_x[x])
            for i in range(len(ys)):
                for j in range(i + 1, len(ys)):
                    y1, y2 = ys[i], ys[j]
                    key = (y1, y2)
                    if key in last:
                        ans = min(ans, abs(x - last[key]) * abs(y2 - y1))
                    last[key] = x
        return 0 if ans == float("inf") else ans
