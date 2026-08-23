// LeetCode 2245 - Maximum Trailing Zeros in a Cornered Path
// https://leetcode.com/problems/maximum-trailing-zeros-in-a-cornered-path/

class Solution {
    private int[] fact(int x) {
        int t = 0, f = 0;
        while (x % 2 == 0) { t++; x /= 2; }
        while (x % 5 == 0) { f++; x /= 5; }
        return new int[] { t, f };
    }

    public int maxTrailingZeros(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[][] left2 = new int[m][n], left5 = new int[m][n];
        int[][] up2 = new int[m][n], up5 = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int[] p = fact(grid[i][j]);
                left2[i][j] = up2[i][j] = p[0];
                left5[i][j] = up5[i][j] = p[1];
                if (j > 0) {
                    left2[i][j] += left2[i][j - 1];
                    left5[i][j] += left5[i][j - 1];
                }
                if (i > 0) {
                    up2[i][j] += up2[i - 1][j];
                    up5[i][j] += up5[i - 1][j];
                }
            }
        }
        int ans = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int[] cell = fact(grid[i][j]);
                int L2 = left2[i][j], L5 = left5[i][j];
                int R2 = left2[i][n - 1] - left2[i][j] + cell[0];
                int R5 = left5[i][n - 1] - left5[i][j] + cell[1];
                int U2 = up2[i][j], U5 = up5[i][j];
                int D2 = up2[m - 1][j] - up2[i][j] + cell[0];
                int D5 = up5[m - 1][j] - up5[i][j] + cell[1];
                int[][] cands = {
                    { L2 + U2 - cell[0], L5 + U5 - cell[1] },
                    { L2 + D2 - cell[0], L5 + D5 - cell[1] },
                    { R2 + U2 - cell[0], R5 + U5 - cell[1] },
                    { R2 + D2 - cell[0], R5 + D5 - cell[1] },
                };
                for (int[] c : cands) ans = Math.max(ans, Math.min(c[0], c[1]));
            }
        }
        return ans;
    }
}
