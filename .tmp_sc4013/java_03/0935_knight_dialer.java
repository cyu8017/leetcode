// LeetCode 0935 - Knight Dialer
// https://leetcode.com/problems/knight-dialer/

import java.util.Arrays;

class Solution {
    public int knightDialer(int n) {
        final int MOD = 1_000_000_007;
        int[][] moves = {
            {4, 6}, {6, 8}, {7, 9}, {4, 8}, {0, 3, 9},
            {}, {0, 1, 7}, {2, 6}, {1, 3}, {2, 4}
        };
        long[] dp = new long[10];
        Arrays.fill(dp, 1);
        for (int step = 0; step < n - 1; step++) {
            long[] ndp = new long[10];
            for (int i = 0; i < 10; i++)
                for (int j : moves[i]) ndp[j] = (ndp[j] + dp[i]) % MOD;
            dp = ndp;
        }
        long ans = 0;
        for (long x : dp) ans = (ans + x) % MOD;
        return (int) ans;
    }
}
