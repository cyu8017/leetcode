// LeetCode 3742 - Maximum Path Score in a Grid
// https://leetcode.com/problems/maximum-path-score-in-a-grid/

using System;

public class Solution {
    public int MaxPathScore(int[][] grid, int k) {
        int m = grid.Length, n = grid[0].Length;
        const int inf = 1 << 30;
        int[,,] f = new int[m, n, k + 1];
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                for (int t = 0; t <= k; t++)
                    f[i, j, t] = -1;
        int Dfs(int i, int j, int kk) {
            if (i < 0 || j < 0 || kk < 0) return -inf;
            if (i == 0 && j == 0) return 0;
            if (f[i, j, kk] != -1) return f[i, j, kk];
            int res = grid[i][j];
            int nk = kk;
            if (grid[i][j] != 0) nk--;
            int a = Dfs(i - 1, j, nk);
            int b = Dfs(i, j - 1, nk);
            res += Math.Max(a, b);
            return f[i, j, kk] = res;
        }
        int ans = Dfs(m - 1, n - 1, k);
        return ans < 0 ? -1 : ans;
    }
}
