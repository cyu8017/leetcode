// LeetCode 3112 - Minimum Time to Visit Disappearing Nodes
// https://leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

class Solution {
    public int[] minimumTime(int n, int[][] edges, int[] disappear) {
        @SuppressWarnings("unchecked")
        List<int[]>[] g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) {
            g[e[0]].add(new int[]{e[1], e[2]});
            g[e[1]].add(new int[]{e[0], e[2]});
        }
        final int INF = 1 << 30;
        int[] dist = new int[n];
        Arrays.fill(dist, INF);
        dist[0] = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        pq.offer(new int[]{0, 0});
        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int du = cur[0], u = cur[1];
            if (du > dist[u]) continue;
            for (int[] e : g[u]) {
                int v = e[0], w = e[1];
                if (dist[v] > dist[u] + w && dist[u] + w < disappear[v]) {
                    dist[v] = dist[u] + w;
                    pq.offer(new int[]{dist[v], v});
                }
            }
        }
        int[] ans = new int[n];
        for (int i = 0; i < n; i++)
            ans[i] = dist[i] < disappear[i] ? dist[i] : -1;
        return ans;
    }
}
