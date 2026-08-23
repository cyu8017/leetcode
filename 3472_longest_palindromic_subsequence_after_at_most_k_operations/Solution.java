// LeetCode 3472 - Longest Palindromic Subsequence After at Most K Operations
// https://leetcode.com/problems/longest-palindromic-subsequence-after-at-most-k-operations/

class Solution {
    private int[][][] dp;
    private String s;

    public int longestPalindromicSubsequence(String s, int k) {
        this.s = s;
        int n = s.length();
        dp = new int[n][n][k + 1];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                for (int o = 0; o <= k; o++) dp[i][j][o] = -1;
        return dfs(0, n - 1, k);
    }

    private int distCirc(char a, char b) {
        int d = Math.abs(a - b);
        return Math.min(d, 26 - d);
    }

    private int dfs(int i, int j, int ops) {
        if (i > j) return 0;
        if (i == j) return 1;
        if (dp[i][j][ops] != -1) return dp[i][j][ops];
        int best = dfs(i + 1, j, ops);
        best = Math.max(best, dfs(i, j - 1, ops));
        int cost = distCirc(s.charAt(i), s.charAt(j));
        if (cost <= ops) best = Math.max(best, 2 + dfs(i + 1, j - 1, ops - cost));
        return dp[i][j][ops] = best;
    }
}
