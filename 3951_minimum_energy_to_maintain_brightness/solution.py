# LeetCode 3951 - Minimum Energy To Maintain Brightness
# https://leetcode.com/problems/minimum-energy-to-maintain-brightness/

from typing import List


class Solution:
    def minEnergy(self, n: int, brightness: int, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda a: a[0])
        merged = [[intervals[0][0], intervals[0][1]]]
        for i in range(1, len(intervals)):
            x = intervals[i]
            last = merged[-1]
            if last[1] < x[0]:
                merged.append([x[0], x[1]])
            elif x[1] > last[1]:
                last[1] = x[1]
        ans = 0
        for interval in merged:
            m = interval[1] - interval[0] + 1
            ans += ((brightness + 2) // 3) * m
        return ans
