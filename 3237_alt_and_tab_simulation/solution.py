# LeetCode 3237 - Alt and Tab Simulation
# https://leetcode.com/problems/alt-and-tab-simulation/

from typing import List


class Solution:
    def simulationResult(self, windows: List[int], queries: List[int]) -> List[int]:
        n = len(windows)
        s = [False] * (n + 1)
        ans = []
        for i in range(len(queries) - 1, -1, -1):
            q = queries[i]
            if not s[q]:
                s[q] = True
                ans.append(q)
        for w in windows:
            if not s[w]:
                ans.append(w)
        return ans
