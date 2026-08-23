// LeetCode 2699 - Modify Graph Edge Weights
// https://leetcode.com/problems/modify-graph-edge-weights/

import java.util.*;

class Solution {
    private static final int INF = 2_000_000_000;

    public int[][] modifiedGraphEdges(int n, int[][] edges, int source, int destination, int target) {
        int[] d = dijkstra(n, edges, source, true);
        if (d[destination] < target) return new int[0][];
        boolean matched = d[destination] == target;
        for (int i = 0; i < edges.length; i++) {
            if (edges[i][2] != -1) continue;
            if (matched) {
                edges[i][2] = INF;
                continue;
            }
            edges[i][2] = 1;
            d = dijkstra(n, edges, source, false);
            if (d[destination] <= target) {
                edges[i][2] += target - d[destination];
                matched = true;
            }
        }
        d = dijkstra(n, edges, source, false);
        if (d[destination] != target) return new int[0][];
        return edges;
    }

    private int[] dijkstra(int n, int[][] edges, int source, boolean ignoreNeg) {
        int[] dist = new int[n];
        Arrays.fill(dist, INF);
        dist[source] = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));
        pq.offer(new int[] {source, 0});
        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int u = cur[0], d = cur[1];
            if (d != dist[u]) continue;
            for (int[] e : edges) {
                int a = e[0], b = e[1], w = e[2];
                if (a != u && b != u) continue;
                int to = a == u ? b : a;
                if (w == -1) {
                    if (ignoreNeg) continue;
                    w = 1;
                }
                if (d + w < dist[to]) {
                    dist[to] = d + w;
                    pq.offer(new int[] {to, dist[to]});
                }
            }
        }
        return dist;
    }
}
