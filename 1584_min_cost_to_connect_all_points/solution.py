from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n, used, dist, answer = len(points), [False] * len(points), [10**9] * len(points), 0
        dist[0] = 0
        for _ in range(n):
            u = min((i for i in range(n) if not used[i]), key=dist.__getitem__)
            used[u] = True
            answer += dist[u]
            for v in range(n):
                if not used[v]:
                    d = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    dist[v] = min(dist[v], d)
        return answer
