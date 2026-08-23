// LeetCode 2609 - Find the Longest Balanced Substring of a Binary String
// https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/

using System;

public class Solution {
    public int FindTheLongestBalancedSubstring(string s) {
        int ans = 0, zeros = 0, ones = 0;
        foreach (char c in s) {
            if (c == '0') {
                if (ones > 0) zeros = ones = 0;
                zeros++;
            } else {
                ones++;
                int cur = Math.Min(ones, zeros);
                if (2 * cur > ans) ans = 2 * cur;
            }
        }
        return ans;
    }
}
