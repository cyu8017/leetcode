# LeetCode 3235 - Check if the Rectangle Corner Is Reachable
# https://leetcode.com/problems/check-if-the-rectangle-corner-is-reachable/

from typing import List


class Solution:
    def canReachCorner(self, xCorner: int, yCorner: int, circles: List[List[int]]) -> bool:
        n = len(circles)
        vis = [False] * n

        def inCircle(x: int, y: int, cx: int, cy: int, r: int) -> bool:
            dx, dy = x - cx, y - cy
            return dx * dx + dy * dy <= r * r

        def crossLeftTop(cx: int, cy: int, r: int) -> bool:
            a = abs(cx) <= r and 0 <= cy <= yCorner
            b = abs(cy - yCorner) <= r and 0 <= cx <= xCorner
            return a or b

        def crossRightBottom(cx: int, cy: int, r: int) -> bool:
            a = abs(cx - xCorner) <= r and 0 <= cy <= yCorner
            b = abs(cy) <= r and 0 <= cx <= xCorner
            return a or b

        def dfs(i: int) -> bool:
            x1, y1, r1 = circles[i]
            if crossRightBottom(x1, y1, r1):
                return True
            vis[i] = True
            for j in range(n):
                if vis[j]:
                    continue
                x2, y2, r2 = circles[j]
                if (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2) > (r1 + r2) * (r1 + r2):
                    continue
                if (
                    x1 * r2 + x2 * r1 < (r1 + r2) * xCorner
                    and y1 * r2 + y2 * r1 < (r1 + r2) * yCorner
                    and dfs(j)
                ):
                    return True
            return False

        for i in range(n):
            x, y, r = circles[i]
            if inCircle(0, 0, x, y, r) or inCircle(xCorner, yCorner, x, y, r):
                return False
            if not vis[i] and crossLeftTop(x, y, r) and dfs(i):
                return False
        return True
