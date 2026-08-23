// LeetCode 3928 - Minimum Cost to Buy Apples II
// https://leetcode.com/problems/minimum-cost-to-buy-apples-ii/

using System.Collections.Generic;

public class Solution {
    private struct Edge {
        public int To, Empty, Full;
        public Edge(int to, int empty, int full) { To = to; Empty = empty; Full = full; }
    }

    public long[] MinCostToBuyApples(int n, int[] prices, int[][] roads) {
        var g = new List<Edge>[n];
        for (int i = 0; i < n; i++) g[i] = new List<Edge>();
        foreach (var road in roads) {
            g[road[0]].Add(new Edge(road[1], road[2], road[2] * road[3]));
            g[road[1]].Add(new Edge(road[0], road[2], road[2] * road[3]));
        }
        const long inf = 1L << 62;
        long[] Dijkstra(int source, bool carrying) {
            long[] dist = new long[n];
            for (int i = 0; i < n; i++) dist[i] = inf;
            dist[source] = 0;
            var pq = new PriorityQueue<int, long>();
            pq.Enqueue(source, 0);
            while (pq.Count > 0) {
                pq.TryDequeue(out int node, out long d);
                if (d != dist[node]) continue;
                foreach (var e in g[node]) {
                    int weight = carrying ? e.Full : e.Empty;
                    long next = d + weight;
                    if (next < dist[e.To]) {
                        dist[e.To] = next;
                        pq.Enqueue(e.To, next);
                    }
                }
            }
            return dist;
        }
        long[] answer = new long[n];
        for (int source = 0; source < n; source++) {
            long[] emptyDist = Dijkstra(source, false);
            long[] fullDist = Dijkstra(source, true);
            long best = prices[source];
            for (int shop = 0; shop < n; shop++) {
                if (emptyDist[shop] == inf || fullDist[shop] == inf) continue;
                long total = emptyDist[shop] + fullDist[shop] + prices[shop];
                if (total < best) best = total;
            }
            answer[source] = best;
        }
        return answer;
    }
}
