# LeetCode 2976 - Minimum Cost to Convert String I
# https://leetcode.com/problems/minimum-cost-to-convert-string-i/

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
        inf = (1 << 53) // 4
        dist = [[inf] * 26 for _ in range(26)]
        for i in range(26):
            dist[i][i] = 0
        for i in range(len(original)):
            u = ord(original[i][0]) - 97
            v = ord(changed[i][0]) - 97
            ww = cost[i]
            if ww < dist[u][v]:
                dist[u][v] = ww
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        ans = 0
        for i in range(len(source)):
            a = ord(source[i]) - 97
            b = ord(target[i]) - 97
            if dist[a][b] >= inf / 2:
                return -1
            ans += dist[a][b]
        return ans
