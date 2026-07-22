// LeetCode 1682 - Longest Palindromic Subsequence II
// https://leetcode.com/problems/longest-palindromic-subsequence-ii/

using System;

public class Solution {
    public int LongestPalindromeSubseq(string s) {
        int n = s.Length;
        int[,,] dp = new int[n, n, 26];
        for (int length = 2; length <= n; length++) {
            for (int i = 0; i + length - 1 < n; i++) {
                int j = i + length - 1;
                for (int c = 0; c < 26; c++)
                    dp[i, j, c] = Math.Max(dp[i + 1, j, c], dp[i, j - 1, c]);
                if (s[i] == s[j]) {
                    int c = s[i] - 'a';
                    int inner = 0;
                    if (length > 2) {
                        for (int x = 0; x < 26; x++) {
                            if (x != c) inner = Math.Max(inner, dp[i + 1, j - 1, x]);
                        }
                    }
                    dp[i, j, c] = Math.Max(dp[i, j, c], inner + 2);
                }
            }
        }
        int ans = 0;
        for (int c = 0; c < 26; c++) ans = Math.Max(ans, dp[0, n - 1, c]);
        return ans;
    }
}
