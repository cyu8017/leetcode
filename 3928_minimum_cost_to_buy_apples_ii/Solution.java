// LeetCode 3928 - Minimum Cost to Buy Apples II
// https://leetcode.com/problems/minimum-cost-to-buy-apples-ii/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

class Solution {
    private static class Edge {
        int to, empty, full;
        Edge(int to, int empty, int full) {
            this.to = to;
            this.empty = empty;
            this.full = full;
        }
    }

    public long[] minCostToBuyApples(int n, int[] prices, int[][] roads) {
        List<Edge>[] g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] road : roads) {
            int empty = road[2], full = road[2] * road[3];
            g[road[0]].add(new Edge(road[1], empty, full));
            g[road[1]].add(new Edge(road[0], empty, full));
        }
        final long inf = 1L << 62;
        long[] answer = new long[n];
        for (int source = 0; source < n; source++) {
            long[] emptyDist = dijkstra(n, g, source, false, inf);
            long[] fullDist = dijkstra(n, g, source, true, inf);
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

    private long[] dijkstra(int n, List<Edge>[] g, int source, boolean carrying, long inf) {
        long[] dist = new long[n];
        Arrays.fill(dist, inf);
        dist[source] = 0;
        PriorityQueue<long[]> pq = new PriorityQueue<>((a, b) -> Long.compare(a[0], b[0]));
        pq.offer(new long[] { 0, source });
        while (!pq.isEmpty()) {
            long[] cur = pq.poll();
            long d = cur[0];
            int node = (int) cur[1];
            if (d != dist[node]) continue;
            for (Edge e : g[node]) {
                int weight = carrying ? e.full : e.empty;
                long next = d + weight;
                if (next < dist[e.to]) {
                    dist[e.to] = next;
                    pq.offer(new long[] { next, e.to });
                }
            }
        }
        return dist;
    }
}
