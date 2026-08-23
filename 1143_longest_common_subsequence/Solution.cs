// LeetCode 1143 - Longest Common Subsequence
// https://leetcode.com/problems/longest-common-subsequence/

using System;

public class Solution {
    public int LongestCommonSubsequence(string text1, string text2) {
        int m = text1.Length, n = text2.Length;
        int[] dp = new int[n + 1];
        for (int i = 1; i <= m; i++) {
            int prev = 0;
            for (int j = 1; j <= n; j++) {
                int cur = dp[j];
                if (text1[i - 1] == text2[j - 1]) dp[j] = prev + 1;
                else dp[j] = Math.Max(dp[j], dp[j - 1]);
                prev = cur;
            }
        }
        return dp[n];
    }
}
