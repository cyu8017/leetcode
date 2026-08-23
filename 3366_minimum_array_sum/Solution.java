// LeetCode 3366 - Minimum Array Sum
// https://leetcode.com/problems/minimum-array-sum/

import java.util.Arrays;

class Solution {
    public int minArraySum(int[] nums, int k, int op1, int op2) {
        final long inf = (long) 1e18;
        long[][] dp = new long[op1 + 1][op2 + 1];
        for (long[] row : dp) Arrays.fill(row, inf);
        dp[0][0] = 0;
        for (int x : nums) {
            long[][] ndp = new long[op1 + 1][op2 + 1];
            for (long[] row : ndp) Arrays.fill(row, inf);
            for (int a = 0; a <= op1; a++) {
                for (int b = 0; b <= op2; b++) {
                    if (dp[a][b] == inf) continue;
                    // candidates: na, nb, v
                    tryCand(ndp, dp[a][b], a, b, x);
                    if (a < op1) tryCand(ndp, dp[a][b], a + 1, b, (x + 1) / 2);
                    if (b < op2 && x >= k) tryCand(ndp, dp[a][b], a, b + 1, x - k);
                    if (a < op1 && b < op2) {
                        int v1 = (x + 1) / 2;
                        if (v1 >= k) tryCand(ndp, dp[a][b], a + 1, b + 1, v1 - k);
                        if (x >= k) tryCand(ndp, dp[a][b], a + 1, b + 1, (x - k + 1) / 2);
                    }
                }
            }
            dp = ndp;
        }
        long ans = inf;
        for (int a = 0; a <= op1; a++)
            for (int b = 0; b <= op2; b++)
                if (dp[a][b] < ans) ans = dp[a][b];
        return (int) ans;
    }

    private void tryCand(long[][] ndp, long base, int na, int nb, int v) {
        if (base + v < ndp[na][nb]) ndp[na][nb] = base + v;
    }
}
