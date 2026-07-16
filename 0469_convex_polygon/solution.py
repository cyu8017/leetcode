# LeetCode 0469 - Convex Polygon
# https://leetcode.com/problems/convex-polygon/


class Solution:
    def isConvex(self, points: list[list[int]]) -> bool:
        direction = 0
        count = len(points)
        for index in range(count):
            x1 = points[(index + 1) % count][0] - points[index][0]
            y1 = points[(index + 1) % count][1] - points[index][1]
            x2 = points[(index + 2) % count][0] - points[(index + 1) % count][0]
            y2 = points[(index + 2) % count][1] - points[(index + 1) % count][1]
            cross = x1 * y2 - y1 * x2
            if cross == 0:
                continue
            current = 1 if cross > 0 else -1
            if direction == 0:
                direction = current
            elif direction != current:
                return False
        return True
