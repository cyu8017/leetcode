# LeetCode 3004 - Maximum Subtree of the Same Color
# https://leetcode.com/problems/maximum-subtree-of-the-same-color/

from typing import List


class Solution:
    def maximumSubtreeSize(self, edges: List[List[int]], colors: List[int]) -> int:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for e in edges:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        size = [0] * n
        ans = 0

        def dfs(a: int, fa: int) -> bool:
            nonlocal ans
            size[a] = 1
            ok = True
            for b in g[a]:
                if b != fa:
                    t = dfs(b, a)
                    ok = ok and t and colors[a] == colors[b]
                    size[a] += size[b]
            if ok:
                ans = max(ans, size[a])
            return ok

        dfs(0, -1)
        return ans
