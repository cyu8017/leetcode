// LeetCode 2707 - Extra Characters in a String
// https://leetcode.com/problems/extra-characters-in-a-string/

using System;
using System.Collections.Generic;

public class Solution {
    public int MinExtraChar(string s, string[] dictionary) {
        var dict = new HashSet<string>(dictionary);
        int n = s.Length;
        int[] dp = new int[n + 1];
        for (int i = 0; i <= n; i++) dp[i] = n;
        dp[0] = 0;
        for (int i = 0; i < n; i++) {
            dp[i + 1] = Math.Min(dp[i + 1], dp[i] + 1);
            for (int j = i + 1; j <= n; j++) {
                if (dict.Contains(s.Substring(i, j - i)))
                    dp[j] = Math.Min(dp[j], dp[i]);
            }
        }
        return dp[n];
    }
}
