# LeetCode 3531 - Count Covered Buildings
# https://leetcode.com/problems/count-covered-buildings/

from typing import List


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        g1 = {}
        g2 = {}
        for b in buildings:
            g1.setdefault(b[0], []).append(b[1])
            g2.setdefault(b[1], []).append(b[0])
        for lst in g1.values():
            lst.sort()
        for lst in g2.values():
            lst.sort()
        ans = 0
        for b in buildings:
            x, y = b[0], b[1]
            l1, l2 = g1[x], g2[y]
            if l2[0] < x < l2[-1] and l1[0] < y < l1[-1]:
                ans += 1
        return ans
