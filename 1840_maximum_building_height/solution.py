# LeetCode 1840 - Maximum Building Height
# https://leetcode.com/problems/maximum-building-height/


class Solution:
    def maxBuilding(self, n: int, restrictions: list[list[int]]) -> int:
        points = [[1, 0]] + sorted(restrictions)
        if points[-1][0] != n:
            points.append([n, n - 1])

        for i in range(1, len(points)):
            prev_id, prev_height = points[i - 1]
            curr_id, curr_height = points[i]
            points[i][1] = min(curr_height, prev_height + curr_id - prev_id)

        for i in range(len(points) - 2, -1, -1):
            next_id, next_height = points[i + 1]
            curr_id, curr_height = points[i]
            points[i][1] = min(curr_height, next_height + next_id - curr_id)

        best = max(height for _, height in points)
        for i in range(len(points) - 1):
            id1, h1 = points[i]
            id2, h2 = points[i + 1]
            best = max(best, (h1 + h2 + id2 - id1) // 2)

        return best
