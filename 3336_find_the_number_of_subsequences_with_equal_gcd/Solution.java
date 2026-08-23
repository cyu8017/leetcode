// LeetCode 3336 - Find the Number of Subsequences With Equal GCD
// https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/

class Solution {
    private int gcd(int a, int b) {
        if (a == 0) return b;
        while (b != 0) { int t = a % b; a = b; b = t; }
        return a;
    }

    public int subsequencePairCount(int[] nums) {
        final int mod = 1_000_000_007;
        int maxV = 0;
        for (int x : nums) if (x > maxV) maxV = x;
        int[][] dp = new int[maxV + 1][maxV + 1];
        dp[0][0] = 1;
        for (int x : nums) {
            int[][] ndp = new int[maxV + 1][maxV + 1];
            for (int a = 0; a <= maxV; a++) System.arraycopy(dp[a], 0, ndp[a], 0, maxV + 1);
            for (int a = 0; a <= maxV; a++) {
                for (int b = 0; b <= maxV; b++) {
                    if (dp[a][b] == 0) continue;
                    int na = a == 0 ? x : gcd(a, x);
                    int nb = b == 0 ? x : gcd(b, x);
                    ndp[na][b] = (ndp[na][b] + dp[a][b]) % mod;
                    ndp[a][nb] = (ndp[a][nb] + dp[a][b]) % mod;
                }
            }
            dp = ndp;
        }
        int ans = 0;
        for (int g = 1; g <= maxV; g++) ans = (ans + dp[g][g]) % mod;
        return ans;
    }
}
