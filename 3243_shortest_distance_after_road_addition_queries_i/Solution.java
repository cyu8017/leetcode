// LeetCode 3243 - Shortest Distance After Road Addition Queries I
// https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;

class Solution {
    public int[] shortestDistanceAfterQueries(int n, int[][] queries) {
        List<Integer>[] g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int i = 0; i < n - 1; i++) g[i].add(i + 1);
        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            g[queries[i][0]].add(queries[i][1]);
            ans[i] = bfs(g, n, 0);
        }
        return ans;
    }

    private int bfs(List<Integer>[] g, int n, int start) {
        Queue<Integer> q = new ArrayDeque<>();
        q.offer(start);
        boolean[] vis = new boolean[n];
        vis[start] = true;
        for (int d = 0; ; d++) {
            int k = q.size();
            while (k-- > 0) {
                int u = q.poll();
                if (u == n - 1) return d;
                for (int v : g[u]) {
                    if (!vis[v]) {
                        vis[v] = true;
                        q.offer(v);
                    }
                }
            }
        }
    }
}
