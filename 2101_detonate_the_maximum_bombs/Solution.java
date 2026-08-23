// LeetCode 2101 - Detonate the Maximum Bombs
// https://leetcode.com/problems/detonate-the-maximum-bombs/

import java.util.*;

class Solution {
    public int maximumDetonation(int[][] bombs) {
        int n = bombs.length;
        List<Integer>[] g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            long x1 = bombs[i][0], y1 = bombs[i][1], r1 = bombs[i][2];
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                long dx = bombs[j][0] - x1, dy = bombs[j][1] - y1;
                if (dx * dx + dy * dy <= r1 * r1) g[i].add(j);
            }
        }
        int ans = 0;
        for (int i = 0; i < n; i++) {
            boolean[] vis = new boolean[n];
            ArrayDeque<Integer> q = new ArrayDeque<>();
            q.offer(i); vis[i] = true;
            int cnt = 0;
            while (!q.isEmpty()) {
                int u = q.poll();
                cnt++;
                for (int v : g[u]) if (!vis[v]) { vis[v] = true; q.offer(v); }
            }
            ans = Math.max(ans, cnt);
        }
        return ans;
    }
}
