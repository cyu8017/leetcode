# LeetCode 3910 - Count Connected Subgraphs With Even Node Sum
# https://leetcode.com/problems/count-connected-subgraphs-with-even-node-sum/

from typing import List


class Solution:
    def evenSumSubgraphs(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        g: List[List[int]] = [[] for _ in range(n)]
        for e in edges:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        m = (1 << n) - 1
        vis = 0

        def dfs(u: int) -> None:
            nonlocal vis
            vis |= 1 << u
            for v in g[u]:
                if ((vis >> v) & 1) == 0:
                    dfs(v)

        ans = 0
        for sub in range(1, m + 1):
            s = 0
            for i in range(n):
                if ((sub >> i) & 1) != 0:
                    s += nums[i]
            if s % 2 != 0:
                continue
            vis = m ^ sub
            start = sub.bit_length() - 1
            if sub == 0:
                start = 0
            dfs(start)
            if vis == m:
                ans += 1
        return ans
