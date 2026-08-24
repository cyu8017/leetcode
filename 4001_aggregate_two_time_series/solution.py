# LeetCode 4001 - Aggregate Two Time Series
# https://leetcode.com/problems/aggregate-two-time-series/

from typing import List


class Solution:
    def aggregateTimeSeries(self, series1: List[List[int]], series2: List[List[int]]) -> List[List[int]]:
        m, n = len(series1), len(series2)
        i, j = 0, 0
        ans = []
        while i < m and j < n:
            t1, v1 = series1[i][0], series1[i][1]
            t2, v2 = series2[j][0], series2[j][1]
            if t1 == t2:
                ans.append([t1, v1 + v2])
                i += 1
                j += 1
            elif t1 < t2:
                ans.append([t1, v1 + v2])
                i += 1
            else:
                ans.append([t2, v1 + v2])
                j += 1
        while i < m:
            ans.append([series1[i][0], series1[i][1]])
            i += 1
        while j < n:
            ans.append([series2[j][0], series2[j][1]])
            j += 1
        return ans
