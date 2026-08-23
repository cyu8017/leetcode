// LeetCode 3844 - Longest Almost Palindromic Substring
// https://leetcode.com/problems/longest-almost-palindromic-substring/

using System;

public class Solution {
    public int AlmostPalindromic(string s) {
        int n = s.Length;
        int F(int l, int r) {
            while (l >= 0 && r < n && s[l] == s[r]) { l--; r++; }
            int l1 = l - 1, r1 = r, l2 = l, r2 = r + 1;
            while (l1 >= 0 && r1 < n && s[l1] == s[r1]) { l1--; r1++; }
            while (l2 >= 0 && r2 < n && s[l2] == s[r2]) { l2--; r2++; }
            return Math.Min(n, Math.Max(r1 - l1 - 1, r2 - l2 - 1));
        }
        int ans = 0;
        for (int i = 0; i < n; i++) ans = Math.Max(ans, Math.Max(F(i, i), F(i, i + 1)));
        return ans;
    }
}
