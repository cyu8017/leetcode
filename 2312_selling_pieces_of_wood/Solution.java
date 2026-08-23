// LeetCode 2312 - Selling Pieces of Wood
// https://leetcode.com/problems/selling-pieces-of-wood/

class Solution {
    public long sellingWood(int m, int n, int[][] prices) {
        var price = new long[m + 1][];
        var dp = new long[m + 1][];
        for (int i = 0; i <= m; i++) {
            price[i] = new long[n + 1];
            dp[i] = new long[n + 1];
        }
        for (var p : prices) price[p[0]][p[1]] = p[2];
        for (int h = 1; h <= m; ++h) {
            for (int w = 1; w <= n; ++w) {
                long best = price[h][w];
                for (int i = 1; i < h; ++i) best = Math.max(best, dp[i][w] + dp[h - i][w]);
                for (int j = 1; j < w; ++j) best = Math.max(best, dp[h][j] + dp[h][w - j]);
                dp[h][w] = best;
            }
        }
        return dp[m][n];
    }
}
