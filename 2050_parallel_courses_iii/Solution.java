// LeetCode 2050 - Parallel Courses III
// https://leetcode.com/problems/parallel-courses-iii/

import java.util.*;

class Solution {
    public int minimumTime(int n, int[][] relations, int[] time) {
        List<Integer>[] g = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) g[i] = new ArrayList<>();
        int[] indeg = new int[n + 1], dist = new int[n + 1];
        for (int[] e : relations) { g[e[0]].add(e[1]); indeg[e[1]]++; }
        ArrayDeque<Integer> q = new ArrayDeque<>();
        for (int i = 1; i <= n; i++) {
            dist[i] = time[i - 1];
            if (indeg[i] == 0) q.offer(i);
        }
        while (!q.isEmpty()) {
            int u = q.poll();
            for (int v : g[u]) {
                dist[v] = Math.max(dist[v], dist[u] + time[v - 1]);
                if (--indeg[v] == 0) q.offer(v);
            }
        }
        int ans = 0;
        for (int i = 1; i <= n; i++) ans = Math.max(ans, dist[i]);
        return ans;
    }
}
