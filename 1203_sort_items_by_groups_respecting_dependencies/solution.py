from collections import deque

class Solution:
    def sortItems(self, n: int, m: int, group: list[int], beforeItems: list[list[int]]) -> list[int]:
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
        item_graph = [[] for _ in range(n)]
        item_indeg = [0] * n
        group_graph = [set() for _ in range(m)]
        group_indeg = [0] * m
        for v in range(n):
            for u in beforeItems[v]:
                item_graph[u].append(v)
                item_indeg[v] += 1
                if group[u] != group[v] and group[v] not in group_graph[group[u]]:
                    group_graph[group[u]].add(group[v])
                    group_indeg[group[v]] += 1
        def topo(graph, indeg):
            q = deque(i for i, d in enumerate(indeg) if d == 0)
            order = []
            while q:
                u = q.popleft()
                order.append(u)
                for v in graph[u]:
                    indeg[v] -= 1
                    if indeg[v] == 0: q.append(v)
            return order if len(order) == len(graph) else []
        items, groups = topo(item_graph, item_indeg), topo(group_graph, group_indeg)
        if not items or not groups: return []
        buckets = [[] for _ in range(m)]
        for item in items: buckets[group[item]].append(item)
        return [item for g in groups for item in buckets[g]]
