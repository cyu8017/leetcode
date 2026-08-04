// LeetCode 1143 - Longest Common Subsequence
// https://leetcode.com/problems/longest-common-subsequence/

class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int m = text1.length(), n = text2.length();
        int[] dp = new int[n + 1];
        for (int i = 1; i <= m; i++) {
            int prev = 0;
            for (int j = 1; j <= n; j++) {
                int cur = dp[j];
                if (text1.charAt(i - 1) == text2.charAt(j - 1)) dp[j] = prev + 1;
                else dp[j] = Math.max(dp[j], dp[j - 1]);
                prev = cur;
            }
        }
        return dp[n];
    }
}
