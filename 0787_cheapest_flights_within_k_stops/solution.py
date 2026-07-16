# LeetCode 0787 - Cheapest Flights Within K Stops
# https://leetcode.com/problems/cheapest-flights-within-k-stops/

from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        dist = [float("inf")] * n
        dist[src] = 0
        for _ in range(k + 1):
            nxt = dist[:]
            for u, v, price in flights:
                if dist[u] != float("inf") and dist[u] + price < nxt[v]:
                    nxt[v] = dist[u] + price
            dist = nxt
        return -1 if dist[dst] == float("inf") else int(dist[dst])
