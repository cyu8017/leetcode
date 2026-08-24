# LeetCode 3425 - Longest Special Path
# https://leetcode.com/problems/longest-special-path/

from typing import List


class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        n = len(nums)
        g = [[] for _ in range(n)]
        for e in edges:
            g[e[0]].append((e[1], e[2]))
            g[e[1]].append((e[0], e[2]))
        best_len, best_nodes = 0, 1
        last = {}
        path = []

        def dfs(u: int, p: int, dist: int, left: int) -> None:
            nonlocal best_len, best_nodes
            seen = nums[u] in last
            prev_pos = last[nums[u]] if seen else -1
            last[nums[u]] = len(path)
            new_left = left
            if seen and prev_pos >= left:
                new_left = prev_pos + 1
            path.append(dist)
            length = dist - path[new_left]
            nodes = len(path) - new_left
            if length > best_len or (length == best_len and nodes < best_nodes):
                best_len = length
                best_nodes = nodes
            for v, w in g[u]:
                if v == p:
                    continue
                dfs(v, u, dist + w, new_left)
            path.pop()
            if seen:
                last[nums[u]] = prev_pos
            else:
                del last[nums[u]]

        dfs(0, -1, 0, 0)
        return [best_len, best_nodes]
