// LeetCode 2318 - Number of Distinct Roll Sequences
// https://leetcode.com/problems/number-of-distinct-roll-sequences/

class Solution {
    private int gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    public int distinctSequences(int n) {
        final int mod = 1_000_000_007;
        int[][][] dp = new int[n + 1][7][7];
        for (int a = 1; a <= 6; ++a) dp[1][a][0] = 1;
        for (int i = 2; i <= n; ++i) {
            for (int prev = 1; prev <= 6; ++prev) {
                for (int pprev = 0; pprev <= 6; ++pprev) {
                    if (dp[i - 1][prev][pprev] == 0) continue;
                    for (int cur = 1; cur <= 6; ++cur) {
                        if (cur == prev || cur == pprev || gcd(cur, prev) != 1) continue;
                        dp[i][cur][prev] = (dp[i][cur][prev] + dp[i - 1][prev][pprev]) % mod;
                    }
                }
            }
        }
        int ans = 0;
        for (int a = 1; a <= 6; ++a)
            for (int b = 0; b <= 6; ++b)
                ans = (ans + dp[n][a][b]) % mod;
        return ans;
    }
}
