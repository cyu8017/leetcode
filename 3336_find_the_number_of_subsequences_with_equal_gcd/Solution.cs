// LeetCode 3336 - Find the Number of Subsequences With Equal GCD
// https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/

using System;

public class Solution {
    int Gcd(int a, int b) {
        if (a == 0) return b;
        while (b != 0) { int t = a % b; a = b; b = t; }
        return a;
    }

    public int SubsequencePairCount(int[] nums) {
        const int mod = 1000000007;
        int maxV = 0;
        foreach (int x in nums) if (x > maxV) maxV = x;
        int[][] dp = new int[maxV + 1][];
        for (int i = 0; i <= maxV; i++) dp[i] = new int[maxV + 1];
        dp[0][0] = 1;
        foreach (int x in nums) {
            int[][] ndp = new int[maxV + 1][];
            for (int i = 0; i <= maxV; i++) {
                ndp[i] = new int[maxV + 1];
                Array.Copy(dp[i], ndp[i], maxV + 1);
            }
            for (int a = 0; a <= maxV; a++) {
                for (int b = 0; b <= maxV; b++) {
                    if (dp[a][b] == 0) continue;
                    int na = a == 0 ? x : Gcd(a, x);
                    int nb = b == 0 ? x : Gcd(b, x);
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
