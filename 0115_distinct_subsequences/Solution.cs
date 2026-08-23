// LeetCode 0115 - Distinct Subsequences
// https://leetcode.com/problems/distinct-subsequences/

public class Solution {
    public int NumDistinct(string s, string t) {
        long[] dp = new long[t.Length + 1];
        dp[0] = 1;
        foreach (char ch in s) {
            for (int j = t.Length; j >= 1; j--) {
                if (ch == t[j - 1]) dp[j] += dp[j - 1];
            }
        }
        return (int)dp[t.Length];
    }
}