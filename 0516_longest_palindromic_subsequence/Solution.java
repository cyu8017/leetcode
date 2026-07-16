// LeetCode 0516 - Longest Palindromic Subsequence
// https://leetcode.com/problems/longest-palindromic-subsequence/

class Solution {
    public int longestPalindromeSubseq(String s) {
        int length = s.length();
        int[][] dp = new int[length][length];
        for (int index = length - 1; index >= 0; index--) {
            dp[index][index] = 1;
            for (int end = index + 1; end < length; end++) {
                if (s.charAt(index) == s.charAt(end)) {
                    dp[index][end] = dp[index + 1][end - 1] + 2;
                } else {
                    dp[index][end] = Math.max(dp[index + 1][end], dp[index][end - 1]);
                }
            }
        }
        return dp[0][length - 1];
    }
}
