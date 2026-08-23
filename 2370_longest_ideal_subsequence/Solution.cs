// LeetCode 2370 - Longest Ideal Subsequence
// https://leetcode.com/problems/longest-ideal-subsequence/

using System;

public class Solution {
    public int LongestIdealString(string s, int k) {
        int[] dp = new int[26];
        int ans = 0;
        foreach (char ch in s) {
            int c = ch - 'a';
            int best = 0;
            for (int p = 0; p < 26; p++)
                if (Math.Abs(c - p) <= k && dp[p] > best) best = dp[p];
            dp[c] = best + 1;
            ans = Math.Max(ans, dp[c]);
        }
        return ans;
    }
}
