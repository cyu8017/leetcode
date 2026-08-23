// LeetCode 2338 - Count the Number of Ideal Arrays
// https://leetcode.com/problems/count-the-number-of-ideal-arrays/

public class Solution {
    public int IdealArrays(int n, int maxValue) {
        const int mod = 1000000007;
        const int maxLen = 14;
        var comb = new int[n + 1][];
        for (int i = 0; i <= n; i++) {
            comb[i] = new int[maxLen + 1];
            comb[i][0] = 1;
            for (int j = 1; j <= maxLen && j <= i; j++)
                comb[i][j] = (comb[i - 1][j] + comb[i - 1][j - 1]) % mod;
        }
        var dp = new int[maxValue + 1][];
        for (int i = 0; i <= maxValue; i++) dp[i] = new int[maxLen + 1];
        for (int i = 1; i <= maxValue; i++) dp[i][1] = 1;
        for (int len = 2; len <= maxLen; len++) {
            for (int v = 1; v <= maxValue; v++) {
                for (int m = 2 * v; m <= maxValue; m += v)
                    dp[m][len] = (dp[m][len] + dp[v][len - 1]) % mod;
            }
        }
        int ans = 0;
        for (int v = 1; v <= maxValue; v++) {
            for (int len = 1; len <= maxLen && len <= n; len++)
                ans = (ans + (int)((long)dp[v][len] * comb[n - 1][len - 1] % mod)) % mod;
        }
        return ans;
    }
}
