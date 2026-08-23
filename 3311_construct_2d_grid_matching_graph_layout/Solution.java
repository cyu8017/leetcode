// LeetCode 3311 - Construct 2D Grid Matching Graph Layout
// https://leetcode.com/problems/construct-2d-grid-matching-graph-layout/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[][] constructGridLayout(int n, int[][] edges) {
        List<Integer>[] g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) {
            g[e[0]].add(e[1]);
            g[e[1]].add(e[0]);
        }
        int[] deg = new int[n];
        for (int i = 0; i < n; i++) deg[i] = g[i].size();
        int start = 0;
        for (int i = 0; i < n; i++) {
            if (deg[i] == 1) { start = i; break; }
            if (deg[i] == 2) start = i;
        }
        boolean[] vis = new boolean[n];
        List<Integer> row = new ArrayList<>();
        int cur = start, prev = -1;
        for (;;) {
            row.add(cur);
            vis[cur] = true;
            int next = -1;
            for (int v : g[cur]) {
                if (v != prev && !vis[v] && deg[v] <= 3) {
                    next = v;
                    if (deg[v] < 4) break;
                }
            }
            if (next == -1) break;
            prev = cur;
            cur = next;
        }
        int width = row.size();
        int height = width != 0 ? n / width : n;
        if (width == 0 || width * height != n) {
            for (int w = 1; w <= n; w++) {
                if (n % w == 0) { width = w; height = n / w; break; }
            }
        }
        int[][] grid = new int[height][width];
        for (int i = 0; i < n; i++) grid[i / width][i % width] = i;
        return grid;
    }
}
