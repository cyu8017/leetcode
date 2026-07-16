// LeetCode 0516 - Longest Palindromic Subsequence
// https://leetcode.com/problems/longest-palindromic-subsequence/

public class Solution {
    public int LongestPalindromeSubseq(string s) {
        int length = s.Length;
        int[,] dp = new int[length, length];
        for (int index = length - 1; index >= 0; index--) {
            dp[index, index] = 1;
            for (int end = index + 1; end < length; end++) {
                if (s[index] == s[end]) {
                    dp[index, end] = dp[index + 1, end - 1] + 2;
                } else {
                    dp[index, end] = System.Math.Max(dp[index + 1, end], dp[index, end - 1]);
                }
            }
        }
        return dp[0, length - 1];
    }
}
