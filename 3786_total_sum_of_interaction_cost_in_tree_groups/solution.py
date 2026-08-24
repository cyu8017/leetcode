# LeetCode 3786 - Total Sum of Interaction Cost in Tree Groups
# https://leetcode.com/problems/total-sum-of-interaction-cost-in-tree-groups/

from typing import List


class Solution:
    def interactionCost(self, n: int, edges: List[List[int]], group: List[int]) -> int:
        g = [[] for _ in range(n)]
        for e in edges:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        total = [0] * 21
        for x in group:
            total[x] += 1
        parent = [-2] * n
        parent[0] = -1
        order = [0]
        i = 0
        while i < len(order):
            u = order[i]
            for v in g[u]:
                if parent[v] == -2:
                    parent[v] = u
                    order.append(v)
            i += 1
        count = [[0] * 21 for _ in range(n)]
        ans = 0
        for i in range(n - 1, -1, -1):
            u = order[i]
            count[u][group[u]] += 1
            for v in g[u]:
                if parent[v] != u:
                    continue
                for c in range(1, 21):
                    x = count[v][c]
                    ans += x * (total[c] - x)
                    count[u][c] += x
        return ans
