// LeetCode 3123 - Find Edges in Shortest Paths
// https://leetcode.com/problems/find-edges-in-shortest-paths/

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;

class Solution {
    public boolean[] findAnswer(int n, int[][] edges) {
        @SuppressWarnings("unchecked")
        List<int[]>[] g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int i = 0; i < edges.length; i++) {
            int a = edges[i][0], b = edges[i][1], w = edges[i][2];
            g[a].add(new int[]{b, w, i});
            g[b].add(new int[]{a, w, i});
        }
        final int INF = 1 << 30;
        int[] dist = new int[n];
        Arrays.fill(dist, INF);
        dist[0] = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        pq.offer(new int[]{0, 0});
        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int da = cur[0], a = cur[1];
            if (da > dist[a]) continue;
            for (int[] e : g[a]) {
                int b = e[0], w = e[1];
                if (dist[b] > dist[a] + w) {
                    dist[b] = dist[a] + w;
                    pq.offer(new int[]{dist[b], b});
                }
            }
        }
        boolean[] ans = new boolean[edges.length];
        if (dist[n - 1] == INF) return ans;
        Queue<Integer> q = new ArrayDeque<>();
        q.offer(n - 1);
        while (!q.isEmpty()) {
            int a = q.poll();
            for (int[] e : g[a]) {
                int b = e[0], w = e[1], i = e[2];
                if (dist[a] == dist[b] + w) {
                    ans[i] = true;
                    q.offer(b);
                }
            }
        }
        return ans;
    }
}
