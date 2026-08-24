# LeetCode 2467 - Most Profitable Path in a Tree
# https://leetcode.com/problems/most-profitable-path-in-a-tree/

from typing import List


class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        bob_time = [n] * n

        def find_bob(u: int, p: int, t: int) -> bool:
            if u == 0:
                bob_time[u] = t
                return True
            for v in g[u]:
                if v == p:
                    continue
                if find_bob(v, u, t + 1):
                    bob_time[u] = t
                    return True
            return False

        find_bob(bob, -1, 0)
        ans = [-(10**18)]

        def dfs(u: int, p: int, t: int, income: int) -> None:
            cur = amount[u]
            if t > bob_time[u]:
                cur = 0
            elif t == bob_time[u]:
                cur //= 2
            income += cur
            is_leaf = True
            for v in g[u]:
                if v != p:
                    is_leaf = False
                    dfs(v, u, t + 1, income)
            if is_leaf and income > ans[0]:
                ans[0] = income

        dfs(0, -1, 0, 0)
        return ans[0]
