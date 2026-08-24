# LeetCode 3009 - Maximum Number of Intersections on the Chart
# https://leetcode.com/problems/maximum-number-of-intersections-on-the-chart/

from typing import List


class Solution:
    def maxIntersectionCount(self, y: List[int]) -> int:
        n = len(y)
        line = {}
        for i in range(1, n):
            start = 2 * y[i - 1]
            end = 2 * y[i]
            if i != n - 1:
                if y[i] > y[i - 1]:
                    end -= 1
                else:
                    end += 1
            a, b = start, end
            if a > b:
                a, b = b, a
            line[a] = line.get(a, 0) + 1
            line[b + 1] = line.get(b + 1, 0) - 1
        keys = sorted(line.keys())
        ans = 0
        cur = 0
        for key in keys:
            cur += line[key]
            if cur > ans:
                ans = cur
        return ans
