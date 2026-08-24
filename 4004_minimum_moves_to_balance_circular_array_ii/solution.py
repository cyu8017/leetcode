# LeetCode 4004 - Minimum Moves to Balance Circular Array II
# https://leetcode.com/problems/minimum-moves-to-balance-circular-array-ii/

from typing import List

INF = 1000000000


class Edge:
    def __init__(self, to: int, cap: int, cost: int, rev: int):
        self.to = to
        self.cap = cap
        self.cost = cost
        self.rev = rev


class MinCostMaxFlow:
    def __init__(self, n_: int):
        self.n = n_
        self.graph = [[] for _ in range(n_)]

    def addEdge(self, u: int, v: int, cap: int, cost: int) -> None:
        self.graph[u].append(Edge(v, cap, cost, len(self.graph[v])))
        self.graph[v].append(Edge(u, 0, -cost, len(self.graph[u]) - 1))

    def minCostFlow(self, source: int, sink: int, maxFlow: int) -> int:
        total_cost = 0
        current_flow = 0
        n = self.n
        graph = self.graph
        while current_flow < maxFlow:
            dist = [INF] * n
            parent_node = [-1] * n
            parent_edge = [-1] * n
            in_queue = [False] * n
            q = [source]
            dist[source] = 0
            in_queue[source] = True
            qi = 0
            while qi < len(q):
                u = q[qi]
                qi += 1
                in_queue[u] = False
                for i in range(len(graph[u])):
                    e = graph[u][i]
                    if e.cap > 0 and dist[e.to] > dist[u] + e.cost:
                        dist[e.to] = dist[u] + e.cost
                        parent_node[e.to] = u
                        parent_edge[e.to] = i
                        if not in_queue[e.to]:
                            in_queue[e.to] = True
                            q.append(e.to)
            if dist[sink] == INF:
                return -1
            push_flow = maxFlow - current_flow
            cur = sink
            while cur != source:
                e = graph[parent_node[cur]][parent_edge[cur]]
                if e.cap < push_flow:
                    push_flow = e.cap
                cur = parent_node[cur]
            cur = sink
            while cur != source:
                p = parent_node[cur]
                idx = parent_edge[cur]
                rev = graph[p][idx].rev
                graph[p][idx].cap -= push_flow
                graph[cur][rev].cap += push_flow
                cur = parent_node[cur]
            current_flow += push_flow
            total_cost += push_flow * dist[sink]
        return total_cost


class Solution:
    def minMoves(self, balance: List[int]) -> int:
        total_balance = 0
        total_deficit = 0
        for x in balance:
            total_balance += x
            if x < 0:
                total_deficit += -x
        if total_balance < 0:
            return -1
        if total_deficit == 0:
            return 0
        n = len(balance)
        source = n
        sink = n + 1
        mcmf = MinCostMaxFlow(n + 2)
        for i in range(n):
            x = balance[i]
            if x > 0:
                mcmf.addEdge(source, i, x, 0)
            elif x < 0:
                mcmf.addEdge(i, sink, -x, 0)
            mcmf.addEdge(i, (i + 1) % n, INF, 1)
            mcmf.addEdge(i, (i - 1 + n) % n, INF, 1)
        return mcmf.minCostFlow(source, sink, total_deficit)
