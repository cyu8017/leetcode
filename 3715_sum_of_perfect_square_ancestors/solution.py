# LeetCode 3715 - Sum of Perfect Square Ancestors
# https://leetcode.com/problems/sum-of-perfect-square-ancestors/

from typing import List


class Solution:
    def sumOfAncestors(self, n: int, edges: List[List[int]], nums: List[int]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def kernel(x: int) -> int:
            res = 1
            p = 2
            while p * p <= x:
                cnt = 0
                while x % p == 0:
                    x //= p
                    cnt += 1
                if cnt % 2 == 1:
                    res *= p
                p += 1
            if x > 1:
                res *= x
            return res

        ks = [kernel(nums[i]) for i in range(n)]
        freq = {}
        ans = 0

        def dfs(u: int, p: int) -> None:
            nonlocal ans
            ans += freq.get(ks[u], 0)
            freq[ks[u]] = freq.get(ks[u], 0) + 1
            for v in graph[u]:
                if v != p:
                    dfs(v, u)
            freq[ks[u]] = freq.get(ks[u], 0) - 1

        dfs(0, -1)
        return ans
