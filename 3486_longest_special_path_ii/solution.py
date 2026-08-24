# LeetCode 3486 - Longest Special Path II
# https://leetcode.com/problems/longest-special-path-ii/

from typing import List


class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        n = len(nums)
        g = [[] for _ in range(n)]
        for e in edges:
            g[e[0]].append((e[1], e[2]))
            g[e[1]].append((e[0], e[2]))
        best_len, best_nodes = 0, 1

        def dfs(u: int, p: int, dist: int, path_vals: List[int], path_dist: List[int]) -> None:
            nonlocal best_len, best_nodes
            path_vals.append(nums[u])
            path_dist.append(dist)
            freq = {}
            dups = 0
            left = 0
            for right in range(len(path_vals)):
                v = path_vals[right]
                freq[v] = freq.get(v, 0) + 1
                if freq[v] == 2:
                    dups += 1
                while dups > 1:
                    lv = path_vals[left]
                    if freq[lv] == 2:
                        dups -= 1
                    freq[lv] -= 1
                    left += 1
            length = dist - path_dist[left]
            nodes = len(path_vals) - left
            if length > best_len or (length == best_len and nodes < best_nodes):
                best_len = length
                best_nodes = nodes
            for v, w in g[u]:
                if v == p:
                    continue
                dfs(v, u, dist + w, path_vals, path_dist)
            path_vals.pop()
            path_dist.pop()

        dfs(0, -1, 0, [], [])
        return [best_len, best_nodes]
