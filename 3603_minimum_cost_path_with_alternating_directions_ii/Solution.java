// LeetCode 3603 - Minimum Cost Path with Alternating Directions II
// https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-ii/

class Solution {
    long entry(int i, int j) { return 1L * (i + 1) * (j + 1); }

    public long minCost(int m, int n, int[][] waitCost) {
        long INF = Long.MAX_VALUE / 4;
        long[][] dp = new long[m][n];
        for (long[] row : dp) java.util.Arrays.fill(row, INF);
        dp[0][0] = entry(0, 0);
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) continue;
                if (i > 0) {
                    long cand = dp[i - 1][j] + entry(i, j);
                    if (!(i - 1 == 0 && j == 0)) cand += waitCost[i - 1][j];
                    dp[i][j] = Math.min(dp[i][j], cand);
                }
                if (j > 0) {
                    long cand = dp[i][j - 1] + entry(i, j);
                    if (!(i == 0 && j - 1 == 0)) cand += waitCost[i][j - 1];
                    dp[i][j] = Math.min(dp[i][j], cand);
                }
            }
        }
        return dp[m - 1][n - 1];
    }
}
