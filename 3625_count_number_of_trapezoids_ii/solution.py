# LeetCode 3625 - Count Number of Trapezoids II
# https://leetcode.com/problems/count-number-of-trapezoids-ii/

from typing import Dict, List


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        cnt1 = {}
        cnt2 = {}

        def get_or(m: dict, k) -> dict:
            if k not in m:
                m[k] = {}
            return m[k]

        for i in range(n):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i):
                x2, y2 = points[j][0], points[j][1]
                dx, dy = x2 - x1, y2 - y1
                if dx == 0:
                    k = 1e9
                    b = x1
                else:
                    k = dy / dx
                    b = (y1 * dx - x1 * dy) / dx
                m1 = get_or(cnt1, k)
                m1[b] = m1.get(b, 0) + 1
                p = (x1 + x2 + 2000) * 4000 + (y1 + y2 + 2000)
                m2 = get_or(cnt2, p)
                m2[k] = m2.get(k, 0) + 1
        ans = 0
        for e in cnt1.values():
            s = 0
            for t in e.values():
                ans += s * t
                s += t
        for e in cnt2.values():
            s = 0
            for t in e.values():
                ans -= s * t
                s += t
        return ans
