// LeetCode 1639 - Number of Ways to Form a Target String Given a Dictionary
// https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/

using System;

public class Solution {
    public int NumWays(string[] words, string target) {
        const int MOD = 1000000007;
        int m = words[0].Length;
        var dp = new long[target.Length + 1];
        dp[0] = 1;
        for (int j = 0; j < m; j++) {
            var count = new int[26];
            foreach (string word in words) count[word[j] - 'a']++;
            for (int i = Math.Min(j + 1, target.Length); i >= 1; i--) {
                dp[i] = (dp[i] + dp[i - 1] * count[target[i - 1] - 'a']) % MOD;
            }
        }
        return (int)dp[target.Length];
    }
}
