# LeetCode 3323 - Minimize Connected Groups by Inserting Interval
# https://leetcode.com/problems/minimize-connected-groups-by-inserting-interval/

from typing import List


class Solution:
    def minConnectedGroups(self, intervals: List[List[int]], k: int) -> int:
        intervals.sort(key=lambda a: a[0])
        merged = []
        for it in intervals:
            if not merged or it[0] > merged[-1][1]:
                merged.append([it[0], it[1]])
            elif it[1] > merged[-1][1]:
                merged[-1][1] = it[1]
        m = len(merged)
        ans = m
        for i in range(m):
            end = merged[i][1] + k
            j = i
            while j < m and merged[j][0] <= end:
                j += 1
            groups = i + 1 + (m - j)
            if groups < ans:
                ans = groups
        return ans
