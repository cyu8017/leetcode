# LeetCode 3382 - Maximum Area Rectangle With Point Constraints II
# https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-ii/

from typing import List


def pack(x: int, y: int) -> int:
    return (x << 32) ^ (y & 0xFFFFFFFF)


class Solution:
    def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
        n = len(xCoord)
        points = [[xCoord[i], yCoord[i]] for i in range(n)]
        s = set()
        for p in points:
            s.add(pack(p[0], p[1]))
        ans = -1
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i][0], points[i][1]
                x2, y2 = points[j][0], points[j][1]
                if x1 == x2 or y1 == y2:
                    continue
                if pack(x1, y2) not in s or pack(x2, y1) not in s:
                    continue
                min_x, max_x = min(x1, x2), max(x1, x2)
                min_y, max_y = min(y1, y2), max(y1, y2)
                good = True
                for p in points:
                    x, y = p[0], p[1]
                    if min_x < x < max_x and min_y < y < max_y:
                        good = False
                        break
                    on_border = ((x == min_x or x == max_x) and min_y <= y <= max_y) or (
                        (y == min_y or y == max_y) and min_x <= x <= max_x
                    )
                    if on_border:
                        is_corner = (x == min_x or x == max_x) and (y == min_y or y == max_y)
                        if not is_corner:
                            good = False
                            break
                if good:
                    area = (max_x - min_x) * (max_y - min_y)
                    if area > ans:
                        ans = area
        return ans
