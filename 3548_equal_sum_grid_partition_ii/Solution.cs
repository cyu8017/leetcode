// LeetCode 3548 - Equal Sum Grid Partition II
// https://leetcode.com/problems/equal-sum-grid-partition-ii/

using System.Collections.Generic;

public class Solution {
    int[][] Rotate(int[][] grid) {
        int m = grid.Length, n = grid[0].Length;
        int[][] t = new int[n][];
        for (int j = 0; j < n; j++) t[j] = new int[m];
        for (int i = 0; i < m; i++) for (int j = 0; j < n; j++) t[j][i] = grid[i][j];
        return t;
    }
    bool Check(int[][] g) {
        int m = g.Length, n = g[0].Length;
        long s1 = 0, s2 = 0;
        var cnt1 = new Dictionary<long, int>();
        var cnt2 = new Dictionary<long, int>();
        foreach (var row in g) foreach (int x in row) {
            long v = x;
            s2 += v;
            if (!cnt2.ContainsKey(v)) cnt2[v] = 0;
            cnt2[v]++;
        }
        for (int i = 0; i < m - 1; i++) {
            foreach (int x in g[i]) {
                long v = x;
                s1 += v; s2 -= v;
                if (!cnt1.ContainsKey(v)) cnt1[v] = 0;
                cnt1[v]++; cnt2[v]--;
            }
            if (s1 == s2) return true;
            if (s1 < s2) {
                long diff = s2 - s1;
                if (cnt2.ContainsKey(diff) && cnt2[diff] > 0) {
                    if ((m - i - 1 > 1 && n > 1) ||
                        (i == m - 2 && (g[i + 1][0] == diff || g[i + 1][n - 1] == diff)) ||
                        (n == 1 && (g[i + 1][0] == diff || g[m - 1][0] == diff)))
                        return true;
                }
            } else {
                long diff = s1 - s2;
                if (cnt1.ContainsKey(diff) && cnt1[diff] > 0) {
                    if ((i + 1 > 1 && n > 1) ||
                        (i == 0 && (g[0][0] == diff || g[0][n - 1] == diff)) ||
                        (n == 1 && (g[0][0] == diff || g[i][0] == diff)))
                        return true;
                }
            }
        }
        return false;
    }
    public bool CanPartitionGrid(int[][] grid) {
        return Check(grid) || Check(Rotate(grid));
    }
}
