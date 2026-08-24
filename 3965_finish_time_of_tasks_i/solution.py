# LeetCode 3965 - Finish Time Of Tasks I
# https://leetcode.com/problems/finish-time-of-tasks-i/

from typing import List


class Solution:
    def finishTime(self, n: int, edges: List[List[int]], baseTime: List[int]) -> int:
        self.baseTime = baseTime
        self.g = [[] for _ in range(n)]
        for e in edges:
            self.g[e[0]].append(e[1])
        return self.dfs(0)

    def dfs(self, i: int) -> int:
        if len(self.g[i]) == 0:
            return self.baseTime[i]
        INF = 1 << 62
        earliest = INF
        latest = -INF
        for j in self.g[i]:
            a = self.dfs(j)
            earliest = min(earliest, a)
            latest = max(latest, a)
        own_duration = (latest - earliest) + self.baseTime[i]
        return latest + own_duration
