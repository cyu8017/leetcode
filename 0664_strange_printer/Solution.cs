// LeetCode 0664 - Strange Printer
// https://leetcode.com/problems/strange-printer/

public class Solution {
    public int StrangePrinter(string s) {
        int n = s.Length;
        if (n == 0) return 0;
        int[,] dp = new int[n, n];
        for (int i = n - 1; i >= 0; --i) {
            dp[i, i] = 1;
            for (int j = i + 1; j < n; ++j) {
                dp[i, j] = dp[i + 1, j] + 1;
                for (int k = i + 1; k <= j; ++k) {
                    if (s[k] == s[i]) {
                        int candidate = dp[i, k - 1] + (k + 1 <= j ? dp[k + 1, j] : 0);
                        if (candidate < dp[i, j]) dp[i, j] = candidate;
                    }
                }
            }
        }
        return dp[0, n - 1];
    }
}
