// LeetCode 3650 - Minimum Cost Path with Edge Reversals
// https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

class Solution {
    public int minCost(int n, int[][] edges) {
        @SuppressWarnings("unchecked")
        List<int[]>[] g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) {
            int u = e[0], v = e[1], w = e[2];
            g[u].add(new int[] {v, w});
            g[v].add(new int[] {u, w * 2});
        }
        int inf = Integer.MAX_VALUE / 2;
        int[] dist = new int[n];
        Arrays.fill(dist, inf);
        dist[0] = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        pq.offer(new int[] {0, 0});
        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int d = cur[0], u = cur[1];
            if (d > dist[u]) continue;
            if (u == n - 1) return d;
            for (int[] e : g[u]) {
                int v = e[0], w = e[1];
                int nd = d + w;
                if (nd < dist[v]) {
                    dist[v] = nd;
                    pq.offer(new int[] {nd, v});
                }
            }
        }
        return -1;
    }
}
