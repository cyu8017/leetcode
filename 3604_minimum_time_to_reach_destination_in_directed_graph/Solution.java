// LeetCode 3604 - Minimum Time to Reach Destination in Directed Graph
// https://leetcode.com/problems/minimum-time-to-reach-destination-in-directed-graph/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

class Solution {
    public int minTime(int n, int[][] edges) {
        @SuppressWarnings("unchecked")
        List<int[]>[] g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) g[e[0]].add(new int[] {e[1], e[2], e[3]});
        final long Inf = (long) 1e18;
        long[] dist = new long[n];
        Arrays.fill(dist, Inf);
        dist[0] = 0;
        PriorityQueue<long[]> pq = new PriorityQueue<>((a, b) -> Long.compare(a[0], b[0]));
        pq.offer(new long[] {0, 0});
        while (!pq.isEmpty()) {
            long[] cur = pq.poll();
            long t = cur[0];
            int u = (int) cur[1];
            if (t != dist[u]) continue;
            if (u == n - 1) return (int) t;
            for (int[] e : g[u]) {
                long nt = t;
                if (nt > e[2]) continue;
                if (nt < e[1]) nt = e[1];
                nt += 1;
                if (nt < dist[e[0]]) {
                    dist[e[0]] = nt;
                    pq.offer(new long[] {nt, e[0]});
                }
            }
        }
        return dist[n - 1] == Inf ? -1 : (int) dist[n - 1];
    }
}
