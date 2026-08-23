// LeetCode 2608 - Shortest Cycle in a Graph
// https://leetcode.com/problems/shortest-cycle-in-a-graph/

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Queue;

class Solution {
    public int findShortestCycle(int n, int[][] edges) {
        List<Integer>[] g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) {
            g[e[0]].add(e[1]);
            g[e[1]].add(e[0]);
        }
        final int INF = 1_000_000_000;
        int ans = INF;
        for (int start = 0; start < n; ++start) {
            int[] dist = new int[n];
            int[] parent = new int[n];
            Arrays.fill(dist, -1);
            Arrays.fill(parent, -1);
            Queue<Integer> q = new ArrayDeque<>();
            q.offer(start);
            dist[start] = 0;
            while (!q.isEmpty()) {
                int u = q.poll();
                for (int v : g[u]) {
                    if (dist[v] < 0) {
                        dist[v] = dist[u] + 1;
                        parent[v] = u;
                        q.offer(v);
                    } else if (parent[u] != v) {
                        int c = dist[u] + dist[v] + 1;
                        if (c < ans) ans = c;
                    }
                }
            }
        }
        return ans == INF ? -1 : ans;
    }
}
