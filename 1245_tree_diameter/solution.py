from collections import defaultdict, deque

class Solution:
    def treeDiameter(self, edges: list[list[int]]) -> int:
        if not edges: return 0
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        def farthest(start):
            q, seen, last = deque([(start, 0)]), {start}, (start, 0)
            while q:
                last = q.popleft()
                for v in graph[last[0]]:
                    if v not in seen:
                        seen.add(v)
                        q.append((v, last[1] + 1))
            return last
        endpoint, _ = farthest(edges[0][0])
        return farthest(endpoint)[1]
