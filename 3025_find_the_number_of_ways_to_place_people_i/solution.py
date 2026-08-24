# LeetCode 3025 - Find the Number of Ways to Place People I
# https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/

from typing import List


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda a: (a[0], -a[1]))
        ans = 0
        for i in range(len(points)):
            y1 = points[i][1]
            maxY = float("-inf")
            for j in range(i + 1, len(points)):
                y2 = points[j][1]
                if maxY < y2 and y2 <= y1:
                    maxY = y2
                    ans += 1
        return ans
