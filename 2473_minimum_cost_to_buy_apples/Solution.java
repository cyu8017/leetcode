// LeetCode 2473 - Minimum Cost to Buy Apples
// https://leetcode.com/problems/minimum-cost-to-buy-apples/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

class Solution {
    public long[] minCost(int n, int[][] roads, int[] appleCost, int k) {
        List<int[]>[] g = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) g[i] = new ArrayList<>();
        for (int[] r : roads) {
            g[r[0]].add(new int[]{r[1], r[2]});
            g[r[1]].add(new int[]{r[0], r[2]});
        }
        long[] ans = new long[n];
        final long INF = 1L << 60;
        for (int start = 1; start <= n; start++) {
            long[] dist = new long[n + 1];
            Arrays.fill(dist, INF);
            dist[start] = 0;
            PriorityQueue<long[]> pq = new PriorityQueue<>((a, b) -> Long.compare(a[0], b[0]));
            pq.offer(new long[]{0, start});
            while (!pq.isEmpty()) {
                long[] cur = pq.poll();
                long d = cur[0];
                int u = (int) cur[1];
                if (d != dist[u]) continue;
                for (int[] e : g[u]) {
                    int v = e[0], w = e[1];
                    long nd = d + w;
                    if (nd < dist[v]) {
                        dist[v] = nd;
                        pq.offer(new long[]{nd, v});
                    }
                }
            }
            long best = INF;
            for (int city = 1; city <= n; city++) {
                long cost = dist[city] * (k + 1) + appleCost[city - 1];
                if (cost < best) best = cost;
            }
            ans[start - 1] = best;
        }
        return ans;
    }
}
