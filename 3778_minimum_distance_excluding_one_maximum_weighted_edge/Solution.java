// LeetCode 3778 - Minimum Distance Excluding One Maximum Weighted Edge
// https://leetcode.com/problems/minimum_distance_excluding_one_maximum_weighted_edge/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

class Solution {
    public long minCostExcludingMax(int n, int[][] edges) {
        List<int[]>[] g = newList(n);
        for (int[] e : edges) {
            int u = e[0], v = e[1], w = e[2];
            g[u].add(new int[]{v, w});
            g[v].add(new int[]{u, w});
        }
        final long INF = (long) 4e18;
        long[][] dist = new long[n][2];
        for (int i = 0; i < n; i++) Arrays.fill(dist[i], INF);
        dist[0][0] = 0;
        PriorityQueue<long[]> pq = new PriorityQueue<>((a, b) -> Long.compare(a[0], b[0]));
        pq.offer(new long[]{0, 0, 0}); // cost, u, used
        while (!pq.isEmpty()) {
            long[] cur = pq.poll();
            long c = cur[0];
            int u = (int) cur[1], used = (int) cur[2];
            if (c > dist[u][used]) continue;
            if (u == n - 1 && used == 1) return c;
            for (int[] e : g[u]) {
                int v = e[0], w = e[1];
                long nxt = c + w;
                if (nxt < dist[v][used]) {
                    dist[v][used] = nxt;
                    pq.offer(new long[]{nxt, v, used});
                }
                if (used == 0) {
                    nxt = c;
                    if (nxt < dist[v][1]) {
                        dist[v][1] = nxt;
                        pq.offer(new long[]{nxt, v, 1});
                    }
                }
            }
        }
        return dist[n - 1][1];
    }

    @SuppressWarnings("unchecked")
    private List<int[]>[] newList(int n) {
        List<int[]>[] g = (List<int[]>[]) new List[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        return g;
    }
}
