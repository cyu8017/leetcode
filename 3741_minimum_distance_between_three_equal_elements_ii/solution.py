# LeetCode 3741 - Minimum Distance Between Three Equal Elements II
# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii/

from typing import List


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        g = {}
        for i, x in enumerate(nums):
            if x not in g:
                g[x] = []
            g[x].append(i)
        inf = 1 << 30
        ans = inf
        for ls in g.values():
            m = len(ls)
            for h in range(m - 2):
                ans = min(ans, (ls[h + 2] - ls[h]) * 2)
        return -1 if ans == inf else ans
