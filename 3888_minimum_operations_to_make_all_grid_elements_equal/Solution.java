// LeetCode 3888 - Minimum Operations To Make All Grid Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-all-grid-elements-equal/

class Solution {
    private int[][] grid;
    private int k, m, n;

    public long minOperations(int[][] grid, int k) {
        this.grid = grid;
        this.k = k;
        m = grid.length;
        n = grid[0].length;
        int maxVal = grid[0][0];
        for (int[] row : grid) for (int x : row) maxVal = Math.max(maxVal, x);
        for (int t = maxVal; t <= maxVal + 1; t++) {
            long res = check(t);
            if (res != -1) return res;
        }
        return -1;
    }

    private long check(int target) {
        long[][] diff = new long[m + 2][n + 2];
        long totalOps = 0;
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                diff[i][j] += diff[i - 1][j] + diff[i][j - 1] - diff[i - 1][j - 1];
                long curVal = (long) grid[i - 1][j - 1] + diff[i][j];
                if (curVal > target) return -1;
                if (curVal < target) {
                    if (i + k - 1 > m || j + k - 1 > n) return -1;
                    long needed = target - curVal;
                    totalOps += needed;
                    diff[i][j] += needed;
                    diff[i + k][j] -= needed;
                    diff[i][j + k] -= needed;
                    diff[i + k][j + k] += needed;
                }
            }
        }
        return totalOps;
    }
}
