# LeetCode 2867 - Count Valid Paths in a Tree
# https://leetcode.com/problems/count-valid-paths-in-a-tree/

from typing import List


class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        i = 2
        while i * i <= n:
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
            i += 1
        g = [[] for _ in range(n + 1)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        def dfs(u: int, p: int) -> int:
            if is_prime[u]:
                return 0
            sz = 1
            for v in g[u]:
                if v != p:
                    sz += dfs(v, u)
            return sz

        ans = 0
        for u in range(1, n + 1):
            if not is_prime[u]:
                continue
            total = 0
            for v in g[u]:
                c = dfs(v, u)
                ans += c
                ans += total * c
                total += c
        return ans
