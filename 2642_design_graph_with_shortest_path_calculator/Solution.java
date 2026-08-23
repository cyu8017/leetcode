// LeetCode 2642 - Design Graph With Shortest Path Calculator
// https://leetcode.com/problems/design-graph-with-shortest-path-calculator/

import java.util.*;

class Graph {
    private final List<int[]>[] g;

    @SuppressWarnings("unchecked")
    public Graph(int n, int[][] edges) {
        g = new List[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) g[e[0]].add(new int[] {e[1], e[2]});
    }

    public void addEdge(int[] edge) {
        g[edge[0]].add(new int[] {edge[1], edge[2]});
    }

    public int shortestPath(int node1, int node2) {
        int n = g.length;
        int[] dist = new int[n];
        Arrays.fill(dist, 1 << 30);
        dist[node1] = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));
        pq.offer(new int[] {node1, 0});
        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int u = cur[0], d = cur[1];
            if (u == node2) return d;
            if (d > dist[u]) continue;
            for (int[] e : g[u]) {
                int nd = d + e[1];
                if (nd < dist[e[0]]) {
                    dist[e[0]] = nd;
                    pq.offer(new int[] {e[0], nd});
                }
            }
        }
        return -1;
    }
}
