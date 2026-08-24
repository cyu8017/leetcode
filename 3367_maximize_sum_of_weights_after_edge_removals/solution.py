# LeetCode 3367 - Maximize Sum of Weights after Edge Removals
# https://leetcode.com/problems/maximize-sum-of-weights-after-edge-removals/

from typing import List, Tuple


class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for e in edges:
            g[e[0]].append((e[1], e[2]))
            g[e[1]].append((e[0], e[2]))

        def dfs(u: int, p: int) -> Tuple[int, int]:
            base = 0
            gains = []
            for to, w in g[u]:
                if to == p:
                    continue
                child = dfs(to, u)
                base += child[1]
                gain = child[0] + w - child[1]
                if gain > 0:
                    gains.append(gain)
            gains.sort(reverse=True)
            with_p = base
            without = base
            for i in range(min(len(gains), k - 1)):
                with_p += gains[i]
            for i in range(min(len(gains), k)):
                without += gains[i]
            return with_p, without

        return dfs(0, -1)[1]
