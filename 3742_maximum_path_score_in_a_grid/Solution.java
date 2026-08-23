// LeetCode 3742 - Maximum Path Score In A Grid
// https://leetcode.com/problems/maximum_path_score_in_a_grid/

class Solution {
    private int[][] grid;
    private int[][][] f;
    private int m, n;
    private static final int INF = 1 << 30;

    public int maxPathScore(int[][] grid, int k) {
        this.grid = grid;
        m = grid.length;
        n = grid[0].length;
        f = new int[m][n][k + 1];
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                for (int t = 0; t <= k; t++)
                    f[i][j][t] = -1;
        int ans = dfs(m - 1, n - 1, k);
        return ans < 0 ? -1 : ans;
    }

    private int dfs(int i, int j, int kk) {
        if (i < 0 || j < 0 || kk < 0) return -INF;
        if (i == 0 && j == 0) return 0;
        if (f[i][j][kk] != -1) return f[i][j][kk];
        int res = grid[i][j];
        int nk = kk;
        if (grid[i][j] != 0) nk--;
        int a = dfs(i - 1, j, nk);
        int b = dfs(i, j - 1, nk);
        res += Math.max(a, b);
        return f[i][j][kk] = res;
    }
}
