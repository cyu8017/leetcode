// LeetCode 2207 - Maximize Number of Subsequences in a String
// https://leetcode.com/problems/maximize-number-of-subsequences-in-a-string/

using System;

public class Solution {
    public long MaximumSubsequenceCount(string text, string pattern) {
        char a = pattern[0], b = pattern[1];
        long Count(string s) {
            long ca = 0, ans = 0;
            foreach (char c in s) {
                if (c == b) ans += ca;
                if (c == a) ca++;
            }
            return ans;
        }
        return Math.Max(Count(a + text), Count(text + b));
    }
}
