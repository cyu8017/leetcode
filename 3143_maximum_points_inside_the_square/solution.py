# LeetCode 3143 - Maximum Points Inside the Square
# https://leetcode.com/problems/maximum-points-inside-the-square/

import bisect
from typing import List


class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        g = {}
        keys = []
        for i, p in enumerate(points):
            key = max(max(p[0], -p[0]), max(p[1], -p[1]))
            if key not in g:
                g[key] = []
                bisect.insort(keys, key)
            g[key].append(i)
        vis = [False] * 26
        ans = 0
        for key in keys:
            lst = g[key]
            for i in lst:
                j = ord(s[i]) - 97
                if vis[j]:
                    return ans
                vis[j] = True
            ans += len(lst)
        return ans
