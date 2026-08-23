// LeetCode 3977 - Minimum Time to Reach Target With Limited Power
// https://leetcode.com/problems/minimum-time-to-reach-target-with-limited-power/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

class Solution {
    public long[] minTimeMaxPower(int n, int[][] edges, int power, int[] cost, int source, int target) {
        final long INF = 1L << 62;
        List<int[]>[] g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) g[e[0]].add(new int[] { e[1], e[2] });
        long[][] dist = new long[n][power + 1];
        for (int i = 0; i < n; i++) Arrays.fill(dist[i], INF);
        PriorityQueue<long[]> pq = new PriorityQueue<>((a, b) -> {
            if (a[0] != b[0]) return Long.compare(a[0], b[0]);
            return Long.compare(a[1], b[1]);
        });
        pq.offer(new long[] { 0, -power, source });
        dist[source][power] = 0;
        while (!pq.isEmpty()) {
            long[] cur = pq.poll();
            long d = cur[0];
            int p = (int) (-cur[1]);
            int u = (int) cur[2];
            if (u == target) return new long[] { d, p };
            if (d > dist[u][p] || p < cost[u]) continue;
            p -= cost[u];
            for (int[] e : g[u]) {
                int v = e[0], t = e[1];
                long nd = d + t;
                if (nd < dist[v][p]) {
                    dist[v][p] = nd;
                    pq.offer(new long[] { nd, -p, v });
                }
            }
        }
        return new long[] { -1, -1 };
    }
}
