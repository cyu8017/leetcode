// LeetCode 1653 - Minimum Deletions to Make String Balanced
// https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

using System;

public class Solution {
    public int MinimumDeletions(string s) {
        int b = 0, ans = 0;
        foreach (char c in s) {
            if (c == 'b') b++;
            else ans = Math.Min(ans + 1, b);
        }
        return ans;
    }
}
