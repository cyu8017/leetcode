# LeetCode 3967 - Finish Time of Tasks II
# https://leetcode.com/problems/finish-time-of-tasks-ii/

from typing import List


class Edge:
    def __init__(self, to: int, reverse: int):
        self.to = to
        self.reverse = reverse


def combine(minimum: int, maximum: int, count: int, base: int) -> int:
    if count == 0:
        return base
    return 2 * maximum - minimum + base


class Solution:
    def minFinishTime(self, n: int, edges: List[List[int]], baseTime: List[int]) -> int:
        graph = [[] for _ in range(n)]
        for edge in edges:
            u, v = edge[0], edge[1]
            iu, iv = len(graph[u]), len(graph[v])
            graph[u].append(Edge(v, iv))
            graph[v].append(Edge(u, iu))
        parent = [-2] * n
        parent_edge = [0] * n
        parent[0] = -1
        order = [0]
        i = 0
        while i < len(order):
            u = order[i]
            for edge in graph[u]:
                if parent[edge.to] == -2:
                    parent[edge.to] = u
                    parent_edge[edge.to] = edge.reverse
                    order.append(edge.to)
            i += 1
        incoming = [[0] * len(graph[i]) for i in range(n)]
        for oi in range(n - 1, 0, -1):
            u = order[oi]
            minimum = 2 ** 62
            maximum = -1
            count = 0
            for edge_index in range(len(incoming[u])):
                if edge_index == parent_edge[u]:
                    continue
                value = incoming[u][edge_index]
                minimum = min(minimum, value)
                maximum = max(maximum, value)
                count += 1
            value = combine(minimum, maximum, count, baseTime[u])
            parent_node = parent[u]
            reverse_index = graph[u][parent_edge[u]].reverse
            incoming[parent_node][reverse_index] = value
        answer = 2 ** 62
        for u in order:
            min1 = 2 ** 62
            min2 = 2 ** 62
            min_index = -1
            max1 = -1
            max2 = -1
            max_index = -1
            for i in range(len(incoming[u])):
                value = incoming[u][i]
                if value < min1:
                    min2 = min1
                    min1 = value
                    min_index = i
                elif value < min2:
                    min2 = value
                if value > max1:
                    max2 = max1
                    max1 = value
                    max_index = i
                elif value > max2:
                    max2 = value
            root_value = combine(min1, max1, len(graph[u]), baseTime[u])
            answer = min(answer, root_value)
            for i in range(len(graph[u])):
                edge = graph[u][i]
                if edge.to == parent[u]:
                    continue
                if len(graph[u]) == 1:
                    incoming[edge.to][edge.reverse] = baseTime[u]
                    continue
                minimum = min1
                maximum = max1
                if i == min_index:
                    minimum = min2
                if i == max_index:
                    maximum = max2
                incoming[edge.to][edge.reverse] = combine(minimum, maximum, len(graph[u]) - 1, baseTime[u])
        return answer
