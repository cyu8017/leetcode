// LeetCode 2203 - Minimum Weighted Subgraph With the Required Paths
// https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

class Solution {
    private long[] dijkstra(int n, List<int[]>[] g, int src) {
        final long INF = 1L << 62;
        long[] dist = new long[n];
        Arrays.fill(dist, INF);
        dist[src] = 0;
        PriorityQueue<long[]> pq = new PriorityQueue<>((a, b) -> Long.compare(a[0], b[0]));
        pq.offer(new long[] { 0, src });
        while (!pq.isEmpty()) {
            long[] cur = pq.poll();
            long d = cur[0];
            int u = (int) cur[1];
            if (d != dist[u]) continue;
            for (int[] e : g[u]) {
                int v = e[0], w = e[1];
                if (d + w < dist[v]) {
                    dist[v] = d + w;
                    pq.offer(new long[] { dist[v], v });
                }
            }
        }
        return dist;
    }

    public long minimumWeight(int n, int[][] edges, int src1, int src2, int dest) {
        @SuppressWarnings("unchecked")
        List<int[]>[] g = new ArrayList[n];
        @SuppressWarnings("unchecked")
        List<int[]>[] rg = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            g[i] = new ArrayList<>();
            rg[i] = new ArrayList<>();
        }
        for (int[] e : edges) {
            g[e[0]].add(new int[] { e[1], e[2] });
            rg[e[1]].add(new int[] { e[0], e[2] });
        }
        long[] d1 = dijkstra(n, g, src1);
        long[] d2 = dijkstra(n, g, src2);
        long[] dd = dijkstra(n, rg, dest);
        final long INF = 1L << 62;
        long ans = INF;
        for (int i = 0; i < n; i++) {
            if (d1[i] >= INF || d2[i] >= INF || dd[i] >= INF) continue;
            ans = Math.min(ans, d1[i] + d2[i] + dd[i]);
        }
        return ans >= INF ? -1 : ans;
    }
}
