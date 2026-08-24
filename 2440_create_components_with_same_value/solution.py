# LeetCode 2440 - Create Components With Same Value
# https://leetcode.com/problems/create-components-with-same-value/

from typing import List


class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        total = sum(nums)
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        def dfs(u: int, p: int, target: int) -> int:
            s = nums[u]
            for v in g[u]:
                if v == p:
                    continue
                sub = dfs(v, u, target)
                if sub < 0:
                    return -1
                s += sub
            if s > target:
                return -1
            if s == target:
                return 0
            return s

        for parts in range(n, 0, -1):
            if total % parts != 0:
                continue
            target = total // parts
            if dfs(0, -1, target) == 0:
                return parts - 1
        return 0
