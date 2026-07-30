// LeetCode 1216 - Valid Palindrome III
// https://leetcode.com/problems/valid-palindrome-iii/

using System;

public class Solution {
    public bool IsValidPalindrome(string s, int k) {
        int n = s.Length;
        var dp = new int[n];
        for (int i = n - 1; i >= 0; i--) {
            int previous = 0;
            for (int j = i + 1; j < n; j++) {
                int old = dp[j];
                if (s[i] == s[j]) dp[j] = previous;
                else dp[j] = 1 + Math.Min(dp[j], dp[j - 1]);
                previous = old;
            }
        }
        return n == 0 || dp[n - 1] <= k;
    }
}
