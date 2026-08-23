// LeetCode 3472 - Longest Palindromic Subsequence After at Most K Operations
// https://leetcode.com/problems/longest-palindromic-subsequence-after-at-most-k-operations/

using System;

public class Solution {
    int DistCirc(char a, char b) {
        int d = Math.Abs(a - b);
        return Math.Min(d, 26 - d);
    }

    public int LongestPalindromicSubsequence(string s, int k) {
        int n = s.Length;
        int[][][] dp = new int[n][][];
        for (int i = 0; i < n; i++) {
            dp[i] = new int[n][];
            for (int j = 0; j < n; j++) {
                dp[i][j] = new int[k + 1];
                for (int o = 0; o <= k; o++) dp[i][j][o] = -1;
            }
        }
        int Dfs(int i, int j, int ops) {
            if (i > j) return 0;
            if (i == j) return 1;
            if (dp[i][j][ops] != -1) return dp[i][j][ops];
            int best = Dfs(i + 1, j, ops);
            best = Math.Max(best, Dfs(i, j - 1, ops));
            int cost = DistCirc(s[i], s[j]);
            if (cost <= ops) best = Math.Max(best, 2 + Dfs(i + 1, j - 1, ops - cost));
            return dp[i][j][ops] = best;
        }
        return Dfs(0, n - 1, k);
    }
}
