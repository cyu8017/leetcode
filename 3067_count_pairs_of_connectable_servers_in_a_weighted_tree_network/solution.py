# LeetCode 3067 - Count Pairs of Connectable Servers in a Weighted Tree Network
# https://leetcode.com/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/

from typing import List


class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for e in edges:
            g[e[0]].append([e[1], e[2]])
            g[e[1]].append([e[0], e[2]])

        def dfs(a: int, fa: int, ws: int) -> int:
            cnt = 1 if ws % signalSpeed == 0 else 0
            for b, w in g[a]:
                if b != fa:
                    cnt += dfs(b, a, ws + w)
            return cnt

        ans = [0] * n
        for a in range(n):
            s = 0
            for b, w in g[a]:
                t = dfs(b, a, w)
                ans[a] += s * t
                s += t
        return ans
