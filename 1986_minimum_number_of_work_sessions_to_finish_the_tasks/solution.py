from typing import List

class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        INF = (n + 1, 0)
        dp = [INF] * (1 << n)
        dp[0] = (1, 0)
        for mask in range(1 << n):
            sessions, used = dp[mask]
            if sessions > n:
                continue
            for i in range(n):
                if mask & (1 << i):
                    continue
                t = tasks[i]
                nmask = mask | (1 << i)
                if used + t <= sessionTime:
                    cand = (sessions, used + t)
                else:
                    cand = (sessions + 1, t)
                if cand < dp[nmask]:
                    dp[nmask] = cand
        return dp[(1 << n) - 1][0]
