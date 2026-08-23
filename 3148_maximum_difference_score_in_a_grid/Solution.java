// LeetCode 3148 - Maximum Difference Score in a Grid
// https://leetcode.com/problems/maximum-difference-score-in-a-grid/

class Solution {
    public int maxScore(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        final int INF = 1 << 30;
        int[][] f = new int[m][n];
        int ans = -INF;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int x = grid[i][j];
                int mi = INF;
                if (i > 0) mi = Math.min(mi, f[i - 1][j]);
                if (j > 0) mi = Math.min(mi, f[i][j - 1]);
                ans = Math.max(ans, x - mi);
                f[i][j] = Math.min(x, mi);
            }
        }
        return ans;
    }
}
