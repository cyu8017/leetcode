// LeetCode 2108 - Find First Palindromic String in the Array
// https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

public class Solution {
    public string FirstPalindrome(string[] words) {
        foreach (string w in words) {
            bool ok = true;
            for (int l = 0, r = w.Length - 1; l < r; l++, r--)
                if (w[l] != w[r]) { ok = false; break; }
            if (ok) return w;
        }
        return "";
    }
}
