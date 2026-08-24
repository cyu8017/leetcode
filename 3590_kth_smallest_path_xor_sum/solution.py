# LeetCode 3590 - Kth Smallest Path XOR Sum
# https://leetcode.com/problems/kth-smallest-path-xor-sum/

from typing import List


class Solution:
    def kthSmallest(
        self, par: List[int], vals: List[int], queries: List[List[int]]
    ) -> List[int]:
        n = len(par)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[par[i]].append(i)
        xor_path = [0] * n

        def dfs(u: int) -> None:
            xor_path[u] ^= vals[u]
            for v in g[u]:
                xor_path[v] = xor_path[u]
                dfs(v)

        dfs(0)
        in_t = [0] * n
        out_t = [0] * n
        order = []

        def dfs2(u: int) -> None:
            in_t[u] = len(order)
            order.append(xor_path[u])
            for v in g[u]:
                dfs2(v)
            out_t[u] = len(order)

        dfs2(0)
        ans = [0] * len(queries)
        for i, q in enumerate(queries):
            u, k = q[0], q[1]
            sub = sorted(order[in_t[u] : out_t[u]])
            uniq = []
            for x in sub:
                if not uniq or uniq[-1] != x:
                    uniq.append(x)
            ans[i] = -1 if k > len(uniq) else uniq[k - 1]
        return ans
