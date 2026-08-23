// LeetCode 3517 - Smallest Palindromic Rearrangement I
// https://leetcode.com/problems/smallest-palindromic-rearrangement-i/

using System.Text;

public class Solution {
    public string SmallestPalindrome(string s) {
        int[] cnt = new int[26];
        foreach (char c in s) cnt[c - 'a']++;
        var t = new StringBuilder();
        char ch = '\0';
        for (char c = 'a'; c <= 'z'; c++) {
            int v = cnt[c - 'a'] / 2;
            t.Append(c, v);
            cnt[c - 'a'] -= v * 2;
            if (cnt[c - 'a'] == 1) ch = c;
        }
        var sb = new StringBuilder();
        sb.Append(t);
        if (ch != '\0') sb.Append(ch);
        for (int i = t.Length - 1; i >= 0; i--) sb.Append(t[i]);
        return sb.ToString();
    }
}
