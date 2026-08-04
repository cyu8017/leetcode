// LeetCode 1278 - Palindrome Partitioning III
// https://leetcode.com/problems/palindrome-partitioning-iii/

class Solution {
    public int palindromePartition(String s, int k) {
        int n = s.length();
        int[][] cost = new int[n][n];
        for (int length = 2; length <= n; length++) {
            for (int i = 0; i <= n - length; i++) {
                int j = i + length - 1;
                cost[i][j] = (length > 2 ? cost[i + 1][j - 1] : 0) + (s.charAt(i) != s.charAt(j) ? 1 : 0);
            }
        }
        int inf = n + 1;
        int[][] dp = new int[k + 1][n + 1];
        for (int i = 0; i <= k; i++) {
            for (int j = 0; j <= n; j++) dp[i][j] = inf;
        }
        dp[0][0] = 0;
        for (int parts = 1; parts <= k; parts++) {
            for (int end = parts; end <= n; end++) {
                for (int start = parts - 1; start < end; start++) {
                    dp[parts][end] = Math.min(
                        dp[parts][end],
                        dp[parts - 1][start] + cost[start][end - 1]);
                }
            }
        }
        return dp[k][n];
    }
}
