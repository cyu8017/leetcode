// LeetCode 3339 - Find the Number of K-Even Arrays
// https://leetcode.com/problems/find-the-number-of-k-even-arrays/

public class Solution {
    public int CountOfArrays(int n, int m, int k) {
        const int mod = 1000000007;
        int even = m / 2, odd = m - even;
        int[][][] dp = new int[n + 1][][];
        for (int i = 0; i <= n; i++) {
            dp[i] = new int[k + 1][];
            for (int j = 0; j <= k; j++) dp[i][j] = new int[2];
        }
        dp[1][0][0] = odd;
        dp[1][0][1] = even;
        for (int i = 1; i < n; i++) {
            for (int j = 0; j <= k; j++) {
                dp[i + 1][j][0] = (dp[i + 1][j][0] + (int)(((long)dp[i][j][0] + dp[i][j][1]) % mod * odd % mod)) % mod;
                dp[i + 1][j][1] = (dp[i + 1][j][1] + (int)((long)dp[i][j][0] * even % mod)) % mod;
                if (j < k) {
                    dp[i + 1][j + 1][1] = (dp[i + 1][j + 1][1] + (int)((long)dp[i][j][1] * even % mod)) % mod;
                }
            }
        }
        return (dp[n][k][0] + dp[n][k][1]) % mod;
    }
}
