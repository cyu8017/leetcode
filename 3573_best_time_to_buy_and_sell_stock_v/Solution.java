// LeetCode 3573 - Best Time to Buy and Sell Stock V
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/

class Solution {
    public long maximumProfit(int[] prices, int k) {
        int n = prices.length;
        long[][][] f = new long[n][][];
        for (int i = 0; i < n; i++) {
            f[i] = new long[k + 1][];
            for (int j = 0; j <= k; j++) f[i][j] = new long[3];
        }
        for (int j = 1; j <= k; j++) {
            f[0][j][1] = -prices[0];
            f[0][j][2] = prices[0];
        }
        for (int i = 1; i < n; i++) {
            for (int j = 1; j <= k; j++) {
                f[i][j][0] = Math.max(f[i - 1][j][0], Math.max(f[i - 1][j][1] + prices[i], f[i - 1][j][2] - prices[i]));
                f[i][j][1] = Math.max(f[i - 1][j][1], f[i - 1][j - 1][0] - prices[i]);
                f[i][j][2] = Math.max(f[i - 1][j][2], f[i - 1][j - 1][0] + prices[i]);
            }
        }
        return f[n - 1][k][0];
    }
}
