// LeetCode 3651 - Minimum Cost Path with Teleportations
// https://leetcode.com/problems/minimum-cost-path-with-teleportations/

using System;
using System.Collections.Generic;

public class Solution {
    public int MinCost(int[][] grid, int k) {
        int m = grid.Length, n = grid[0].Length;
        const int inf = int.MaxValue / 4;
        int[][][] f = new int[k + 1][][];
        for (int t = 0; t <= k; t++) {
            f[t] = new int[m][];
            for (int i = 0; i < m; i++) {
                f[t][i] = new int[n];
                Array.Fill(f[t][i], inf);
            }
        }
        f[0][0][0] = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i > 0) f[0][i][j] = Math.Min(f[0][i][j], f[0][i - 1][j] + grid[i][j]);
                if (j > 0) f[0][i][j] = Math.Min(f[0][i][j], f[0][i][j - 1] + grid[i][j]);
            }
        }
        var g = new SortedDictionary<int, List<(int, int)>>(Comparer<int>.Create((a, b) => b.CompareTo(a)));
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++) {
                if (!g.ContainsKey(grid[i][j])) g[grid[i][j]] = new List<(int, int)>();
                g[grid[i][j]].Add((i, j));
            }
        for (int t = 1; t <= k; t++) {
            int mn = inf;
            foreach (var pos in g.Values) {
                foreach (var (pi, pj) in pos) mn = Math.Min(mn, f[t - 1][pi][pj]);
                foreach (var (pi, pj) in pos) f[t][pi][pj] = mn;
            }
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (i > 0) f[t][i][j] = Math.Min(f[t][i][j], f[t][i - 1][j] + grid[i][j]);
                    if (j > 0) f[t][i][j] = Math.Min(f[t][i][j], f[t][i][j - 1] + grid[i][j]);
                }
            }
        }
        int ans = inf;
        for (int t = 0; t <= k; t++) ans = Math.Min(ans, f[t][m - 1][n - 1]);
        return ans;
    }
}
