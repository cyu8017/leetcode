// LeetCode 3429 - Paint House IV
// https://leetcode.com/problems/paint-house-iv/

class Solution {
    public long minCost(int n, int[][] cost) {
        long inf = 1L << 60;
        int m = n / 2;
        long[][] dp = new long[3][3];
        for (int a = 0; a < 3; a++) {
            for (int b = 0; b < 3; b++) {
                dp[a][b] = (a == b) ? inf : (long)cost[0][a] + cost[n - 1][b];
            }
        }
        for (int i = 1; i < m; i++) {
            long[][] ndp = new long[3][3];
            for (int a = 0; a < 3; a++) for (int b = 0; b < 3; b++) ndp[a][b] = inf;
            for (int pa = 0; pa < 3; pa++) {
                for (int pb = 0; pb < 3; pb++) {
                    if (dp[pa][pb] >= inf) continue;
                    for (int a = 0; a < 3; a++) {
                        if (a == pa) continue;
                        for (int b = 0; b < 3; b++) {
                            if (b == pb || a == b) continue;
                            long v = dp[pa][pb] + cost[i][a] + cost[n - 1 - i][b];
                            if (v < ndp[a][b]) ndp[a][b] = v;
                        }
                    }
                }
            }
            for (int a = 0; a < 3; a++) for (int b = 0; b < 3; b++) dp[a][b] = ndp[a][b];
        }
        long ans = inf;
        for (int a = 0; a < 3; a++) for (int b = 0; b < 3; b++) if (dp[a][b] < ans) ans = dp[a][b];
        return ans;
    }
}
