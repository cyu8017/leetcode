// LeetCode 1976 - Number of Ways to Arrive at Destination
// https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/

import java.util.*;

class Solution {
    public int countPaths(int n, int[][] roads) {
        final int MOD = 1_000_000_007;
        List<int[]>[] g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : roads) {
            g[e[0]].add(new int[]{e[1], e[2]});
            g[e[1]].add(new int[]{e[0], e[2]});
        }
        long[] dist = new long[n];
        Arrays.fill(dist, Long.MAX_VALUE / 4);
        int[] ways = new int[n];
        dist[0] = 0;
        ways[0] = 1;
        PriorityQueue<long[]> pq = new PriorityQueue<>(Comparator.comparingLong(a -> a[0]));
        pq.offer(new long[]{0, 0});
        while (!pq.isEmpty()) {
            long[] cur = pq.poll();
            long d = cur[0];
            int u = (int) cur[1];
            if (d > dist[u]) continue;
            for (int[] e : g[u]) {
                int v = e[0], w = e[1];
                long nd = d + w;
                if (nd < dist[v]) {
                    dist[v] = nd;
                    ways[v] = ways[u];
                    pq.offer(new long[]{nd, v});
                } else if (nd == dist[v]) {
                    ways[v] = (ways[v] + ways[u]) % MOD;
                }
            }
        }
        return ways[n - 1];
    }
}
