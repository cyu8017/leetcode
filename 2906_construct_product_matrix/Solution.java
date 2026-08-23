// LeetCode 2906 - Construct Product Matrix
// https://leetcode.com/problems/construct-product-matrix/

class Solution {
    public int[][] constructProductMatrix(int[][] grid) {
        final int mod = 12345;
        int m = grid.length, n = grid[0].length;
        int[][] ans = new int[m][n];
        int pref = 1;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++) {
                ans[i][j] = pref;
                pref = (int) (1L * pref * (grid[i][j] % mod) % mod);
            }
        int suf = 1;
        for (int i = m - 1; i >= 0; i--)
            for (int j = n - 1; j >= 0; j--) {
                ans[i][j] = (int) (1L * ans[i][j] * suf % mod);
                suf = (int) (1L * suf * (grid[i][j] % mod) % mod);
            }
        return ans;
    }
}
