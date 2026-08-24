# LeetCode 2977 - Minimum Cost to Convert String II
# https://leetcode.com/problems/minimum-cost-to-convert-string-ii/

from typing import List


class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        INF = (1 << 53) // 4
        ids = {}
        for i in range(len(original)):
            if original[i] not in ids:
                ids[original[i]] = len(ids)
            if changed[i] not in ids:
                ids[changed[i]] = len(ids)
        m = len(ids)
        dist = [[INF] * m for _ in range(m)]
        for i in range(m):
            dist[i][i] = 0
        for i in range(len(original)):
            u = ids[original[i]]
            v = ids[changed[i]]
            ww = cost[i]
            if ww < dist[u][v]:
                dist[u][v] = ww
        for k in range(m):
            for i in range(m):
                for j in range(m):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        n = len(source)
        dp = [INF] * (n + 1)
        dp[0] = 0
        lens = set()
        for key in ids.keys():
            lens.add(len(key))
        for i in range(n):
            if dp[i] >= INF / 2:
                continue
            if source[i] == target[i] and dp[i] < dp[i + 1]:
                dp[i + 1] = dp[i]
            for L in lens:
                if i + L > n:
                    continue
                ss = source[i : i + L]
                tt = target[i : i + L]
                if ss not in ids or tt not in ids:
                    continue
                iu = ids[ss]
                iv = ids[tt]
                if dist[iu][iv] < INF / 2:
                    cand = dp[i] + dist[iu][iv]
                    if cand < dp[i + L]:
                        dp[i + L] = cand
        if dp[n] >= INF / 2:
            return -1
        return dp[n]
