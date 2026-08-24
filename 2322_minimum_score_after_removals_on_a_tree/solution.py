# LeetCode 2322 - Minimum Score After Removals on a Tree
# https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/

from typing import List


class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        xorv = [0] * n
        in_t = [0] * n
        out_t = [0] * n
        time = 0

        def dfs(u: int, p: int) -> None:
            nonlocal time
            in_t[u] = time
            time += 1
            xorv[u] = nums[u]
            for v in g[u]:
                if v != p:
                    dfs(v, u)
                    xorv[u] ^= xorv[v]
            out_t[u] = time

        def is_ancestor(a: int, b: int) -> bool:
            return in_t[a] <= in_t[b] and out_t[b] <= out_t[a]

        dfs(0, -1)
        total = xorv[0]
        ans = float("inf")
        for i in range(1, n):
            for j in range(i + 1, n):
                if is_ancestor(i, j):
                    a = xorv[j]
                    b = xorv[i] ^ xorv[j]
                    c = total ^ xorv[i]
                elif is_ancestor(j, i):
                    a = xorv[i]
                    b = xorv[j] ^ xorv[i]
                    c = total ^ xorv[j]
                else:
                    a = xorv[i]
                    b = xorv[j]
                    c = total ^ xorv[i] ^ xorv[j]
                ans = min(ans, max(a, b, c) - min(a, b, c))
        return int(ans)
