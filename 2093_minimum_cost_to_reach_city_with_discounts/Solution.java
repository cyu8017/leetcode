// LeetCode 2093 - Minimum Cost to Reach City With Discounts
// https://leetcode.com/problems/minimum-cost-to-reach-city-with-discounts/

import java.util.*;

class Solution {
    public int minimumCost(int n, int[][] highways, int discounts) {
        List<int[]>[] g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] h : highways) {
            g[h[0]].add(new int[] {h[1], h[2]});
            g[h[1]].add(new int[] {h[0], h[2]});
        }
        final int INF = 1 << 30;
        int[][] dist = new int[n][discounts + 1];
        for (int i = 0; i < n; i++) Arrays.fill(dist[i], INF);
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        dist[0][discounts] = 0;
        pq.offer(new int[] {0, 0, discounts});
        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int cost = cur[0], city = cur[1], disc = cur[2];
            if (city == n - 1) return cost;
            if (cost > dist[city][disc]) continue;
            for (int[] e : g[city]) {
                int v = e[0], w = e[1];
                if (cost + w < dist[v][disc]) {
                    dist[v][disc] = cost + w;
                    pq.offer(new int[] {dist[v][disc], v, disc});
                }
                if (disc > 0 && cost + w / 2 < dist[v][disc - 1]) {
                    dist[v][disc - 1] = cost + w / 2;
                    pq.offer(new int[] {dist[v][disc - 1], v, disc - 1});
                }
            }
        }
        return -1;
    }
}
