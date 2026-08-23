// LeetCode 3563 - Lexicographically Smallest String After Adjacent Removals
// https://leetcode.com/problems/lexicographically-smallest-string-after-adjacent-removals/

using System;

public class Solution {
    public string LexicographicallySmallestString(string s) {
        int n = s.Length;
        string[][] dp = new string[n + 1][];
        for (int i = 0; i <= n; i++) {
            dp[i] = new string[n + 1];
            for (int j = 0; j <= n; j++) dp[i][j] = "";
        }
        bool IsConsec(char a, char b) {
            int d = Math.Abs(a - b);
            return d == 1 || d == 25;
        }
        for (int length = 1; length <= n; length++) {
            for (int i = 0; i + length <= n; i++) {
                int j = i + length;
                string minStr = s[i] + dp[i + 1][j];
                for (int k = i + 1; k < j; k++) {
                    if (IsConsec(s[i], s[k]) && dp[i + 1][k].Length == 0) {
                        string cand = dp[k + 1][j];
                        if (string.CompareOrdinal(cand, minStr) < 0) minStr = cand;
                    }
                }
                dp[i][j] = minStr;
            }
        }
        return dp[0][n];
    }
}
