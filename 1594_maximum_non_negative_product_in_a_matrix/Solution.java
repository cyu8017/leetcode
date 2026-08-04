// LeetCode 1594 - Maximum Non Negative Product in a Matrix
// https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/

class Solution {
    public int maxProductPath(int[][] grid) {
        final int MOD = 1_000_000_007;
        int m = grid.length;
        int n = grid[0].length;
        long[][] high = new long[m][n];
        long[][] low = new long[m][n];
        high[0][0] = grid[0][0];
        low[0][0] = grid[0][0];
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (r == 0 && c == 0) {
                    continue;
                }
                long g = grid[r][c];
                long mx = Long.MIN_VALUE;
                long mn = Long.MAX_VALUE;
                if (r > 0) {
                    mx = Math.max(mx, high[r - 1][c] * g);
                    mx = Math.max(mx, low[r - 1][c] * g);
                    mn = Math.min(mn, high[r - 1][c] * g);
                    mn = Math.min(mn, low[r - 1][c] * g);
                }
                if (c > 0) {
                    mx = Math.max(mx, high[r][c - 1] * g);
                    mx = Math.max(mx, low[r][c - 1] * g);
                    mn = Math.min(mn, high[r][c - 1] * g);
                    mn = Math.min(mn, low[r][c - 1] * g);
                }
                high[r][c] = mx;
                low[r][c] = mn;
            }
        }
        if (high[m - 1][n - 1] < 0) {
            return -1;
        }
        return (int) (high[m - 1][n - 1] % MOD);
    }
}
