// LeetCode 3466 - Maximum Coin Collection
// https://leetcode.com/problems/maximum-coin-collection/

class Solution {
    public long maxCoins(int[] lane1, int[] lane2) {
        int n = lane1.length;
        long neg = (long)(-1L << 60);
        long[][] dp = new long[2][2];
        dp[0][0] = lane1[0];
        dp[1][0] = lane2[0];
        dp[0][1] = dp[1][1] = neg;
        long ans = Math.max(dp[0][0], dp[1][0]);
        for (int i = 1; i < n; i++) {
            long[][] ndp = new long[2][2];
            ndp[0][0] = Math.max(dp[0][0], 0L) + lane1[i];
            ndp[1][0] = Math.max(dp[1][0], 0L) + lane2[i];
            ndp[0][1] = Math.max(dp[0][1], dp[1][0]) + lane1[i];
            ndp[1][1] = Math.max(dp[1][1], dp[0][0]) + lane2[i];
            if (lane1[i] > ndp[0][0]) ndp[0][0] = lane1[i];
            if (lane2[i] > ndp[1][0]) ndp[1][0] = lane2[i];
            for (int a = 0; a < 2; a++)
                for (int b = 0; b < 2; b++) {
                    dp[a][b] = ndp[a][b];
                    if (dp[a][b] > ans) ans = dp[a][b];
                }
        }
        return ans;
    }
}
