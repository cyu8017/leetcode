# LeetCode 3928 - Minimum Cost to Buy Apples II
# https://leetcode.com/problems/minimum-cost-to-buy-apples-ii/

from typing import Dict, List


def dijkstra(n: int, g: List[List[Dict]], source: int, carrying: bool, inf: int) -> List[int]:
    dist = [inf] * n
    dist[source] = 0
    pq = [[0, source]]
    while pq:
        pq.sort(key=lambda a: a[0])
        cur = pq.pop(0)
        d, node = cur[0], cur[1]
        if d != dist[node]:
            continue
        for e in g[node]:
            weight = e["full"] if carrying else e["empty"]
            nxt = d + weight
            if nxt < dist[e["to"]]:
                dist[e["to"]] = nxt
                pq.append([nxt, e["to"]])
    return dist


class Solution:
    def minCostToBuyApples(self, n: int, prices: List[int], roads: List[List[int]]) -> List[int]:
        g: List[List[Dict]] = [[] for _ in range(n)]
        for road in roads:
            empty = road[2]
            full = road[2] * road[3]
            g[road[0]].append({"to": road[1], "empty": empty, "full": full})
            g[road[1]].append({"to": road[0], "empty": empty, "full": full})
        inf = 2 ** 62
        answer = [0] * n
        for source in range(n):
            empty_dist = dijkstra(n, g, source, False, inf)
            full_dist = dijkstra(n, g, source, True, inf)
            best = prices[source]
            for shop in range(n):
                if empty_dist[shop] == inf or full_dist[shop] == inf:
                    continue
                total = empty_dist[shop] + full_dist[shop] + prices[shop]
                if total < best:
                    best = total
            answer[source] = best
        return answer
