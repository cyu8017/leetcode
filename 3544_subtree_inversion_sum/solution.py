# LeetCode 3544 - Subtree Inversion Sum
# https://leetcode.com/problems/subtree-inversion-sum/

from typing import List


class Solution:
    def subtreeInversionSum(self, edges: List[List[int]], nums: List[int], k: int) -> int:
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        parent = [-1] * n
        memo = {}

        def dp(u: int, steps: int, inv: bool) -> int:
            key = (u, steps, inv)
            if key in memo:
                return memo[key]
            num = nums[u]
            if inv:
                num = -num
            neg_num = -num
            for v in graph[u]:
                if v == parent[u]:
                    continue
                parent[v] = u
                ns = steps + 1
                if ns > k:
                    ns = k
                num += dp(v, ns, inv)
                if steps == k:
                    neg_num += dp(v, 1, not inv)
            res = num
            if steps == k and neg_num > res:
                res = neg_num
            memo[key] = res
            return res

        return dp(0, k, False)
