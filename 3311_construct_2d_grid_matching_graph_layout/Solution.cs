// LeetCode 3311 - Construct 2D Grid Matching Graph Layout
// https://leetcode.com/problems/construct-2d-grid-matching-graph-layout/

using System.Collections.Generic;

public class Solution {
    public int[][] ConstructGridLayout(int n, int[][] edges) {
        var g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        foreach (var e in edges) {
            g[e[0]].Add(e[1]);
            g[e[1]].Add(e[0]);
        }
        int[] deg = new int[n];
        for (int i = 0; i < n; i++) deg[i] = g[i].Count;
        int start = 0;
        for (int i = 0; i < n; i++) {
            if (deg[i] == 1) { start = i; break; }
            if (deg[i] == 2) start = i;
        }
        bool[] vis = new bool[n];
        var row = new List<int>();
        int cur = start, prev = -1;
        for (;;) {
            row.Add(cur);
            vis[cur] = true;
            int next = -1;
            foreach (int v in g[cur]) {
                if (v != prev && !vis[v] && deg[v] <= 3) {
                    next = v;
                    if (deg[v] < 4) break;
                }
            }
            if (next == -1) break;
            prev = cur;
            cur = next;
        }
        int width = row.Count;
        int height = width != 0 ? n / width : n;
        if (width == 0 || width * height != n) {
            for (int w = 1; w <= n; w++) {
                if (n % w == 0) { width = w; height = n / w; break; }
            }
        }
        int[][] grid = new int[height][];
        for (int i = 0; i < height; i++) grid[i] = new int[width];
        for (int i = 0; i < n; i++) grid[i / width][i % width] = i;
        return grid;
    }
}
