// LeetCode 2714 - Find Shortest Path With K Hops
// https://leetcode.com/problems/find-shortest-path-with-k-hops/

import java.util.*;

class Solution {
    public int shortestPathWithHops(int n, int[][] edges, int s, int d, int k) {
        List<int[]>[] g = new List[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) {
            g[e[0]].add(new int[] {e[1], e[2]});
            g[e[1]].add(new int[] {e[0], e[2]});
        }
        int[][] dist = new int[n][k + 1];
        for (int i = 0; i < n; i++) Arrays.fill(dist[i], Integer.MAX_VALUE / 4);
        dist[s][0] = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[2]));
        pq.offer(new int[] {s, 0, 0}); // u, hops, cost
        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int u = cur[0], hops = cur[1], cd = cur[2];
            if (u == d) return cd;
            if (cd > dist[u][hops]) continue;
            for (int[] e : g[u]) {
                int to = e[0], w = e[1];
                if (cd + w < dist[to][hops]) {
                    dist[to][hops] = cd + w;
                    pq.offer(new int[] {to, hops, dist[to][hops]});
                }
                if (hops < k && cd < dist[to][hops + 1]) {
                    dist[to][hops + 1] = cd;
                    pq.offer(new int[] {to, hops + 1, cd});
                }
            }
        }
        return -1;
    }
}
