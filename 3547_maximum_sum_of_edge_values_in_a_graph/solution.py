# LeetCode 3547 - Maximum Sum of Edge Values in a Graph
# https://leetcode.com/problems/maximum-sum-of-edge-values-in-a-graph/

from typing import List


def calc3547(left: int, right: int, is_cycle: bool) -> int:
    w0 = right
    w1 = right
    score = 0
    for value in range(right - 1, left - 1, -1):
        score += w0 * value
        w0 = w1
        w1 = value
    if is_cycle:
        score += w0 * w1
    return score


def get_comp(start: int, graph: List[List[int]], seen: List[bool]) -> List[int]:
    comp = [start]
    seen[start] = True
    i = 0
    while i < len(comp):
        for v in graph[comp[i]]:
            if not seen[v]:
                seen[v] = True
                comp.append(v)
        i += 1
    return comp


class Solution:
    def maxScore(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        seen = [False] * n
        cycle_sizes = []
        path_sizes = []
        for i in range(n):
            if seen[i]:
                continue
            comp = get_comp(i, graph, seen)
            all_deg2 = all(len(graph[u]) == 2 for u in comp)
            if all_deg2:
                cycle_sizes.append(len(comp))
            elif len(comp) > 1:
                path_sizes.append(len(comp))
        ans = 0
        cur_n = n
        for cs in cycle_sizes:
            ans += calc3547(cur_n - cs + 1, cur_n, True)
            cur_n -= cs
        path_sizes.sort(reverse=True)
        for ps in path_sizes:
            ans += calc3547(cur_n - ps + 1, cur_n, False)
            cur_n -= ps
        return ans
