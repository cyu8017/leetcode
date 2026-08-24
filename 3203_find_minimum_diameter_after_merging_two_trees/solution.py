# LeetCode 3203 - Find Minimum Diameter After Merging Two Trees
# https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/

from typing import List


class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        ans = 0
        a = 0
        g: List[List[int]] = []

        def dfs(i: int, fa: int, t: int) -> None:
            nonlocal ans, a
            for j in g[i]:
                if j != fa:
                    dfs(j, i, t + 1)
            if ans < t:
                ans = t
                a = i

        def treeDiameter(edges: List[List[int]]) -> int:
            nonlocal ans, a, g
            n = len(edges) + 1
            g = [[] for _ in range(n)]
            for e in edges:
                g[e[0]].append(e[1])
                g[e[1]].append(e[0])
            ans = 0
            a = 0
            dfs(0, -1, 0)
            dfs(a, -1, 0)
            return ans

        d1 = treeDiameter(edges1)
        d2 = treeDiameter(edges2)
        return max(d1, d2, (d1 + 1) // 2 + (d2 + 1) // 2 + 1)
