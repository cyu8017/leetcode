# LeetCode 2285 - Maximum Total Importance of Roads
# https://leetcode.com/problems/maximum-total-importance-of-roads/

from typing import List


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        deg = [0] * n
        for a, b in roads:
            deg[a] += 1
            deg[b] += 1
        deg.sort()
        ans = 0
        for i in range(n):
            ans += deg[i] * (i + 1)
        return ans
