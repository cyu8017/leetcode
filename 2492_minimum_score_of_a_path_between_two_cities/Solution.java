// LeetCode 2492 - Minimum Score of a Path Between Two Cities
// https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;

class Solution {
    public int minScore(int n, int[][] roads) {
        List<int[]>[] g = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) g[i] = new ArrayList<>();
        for (int[] r : roads) {
            g[r[0]].add(new int[]{r[1], r[2]});
            g[r[1]].add(new int[]{r[0], r[2]});
        }
        boolean[] vis = new boolean[n + 1];
        int ans = 1 << 30;
        Queue<Integer> q = new ArrayDeque<>();
        q.offer(1);
        vis[1] = true;
        while (!q.isEmpty()) {
            int u = q.poll();
            for (int[] e : g[u]) {
                int v = e[0], w = e[1];
                if (w < ans) ans = w;
                if (!vis[v]) {
                    vis[v] = true;
                    q.offer(v);
                }
            }
        }
        return ans;
    }
}
