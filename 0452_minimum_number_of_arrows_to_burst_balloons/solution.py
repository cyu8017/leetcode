# LeetCode 0452 - Minimum Number of Arrows to Burst Balloons
# https://leetcode.com/problems/minimum-number-of-arrows-to_burst-balloons/


class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda point: point[1])
        arrows = 1
        end = points[0][1]
        for start, finish in points[1:]:
            if start > end:
                arrows += 1
                end = finish
        return arrows
