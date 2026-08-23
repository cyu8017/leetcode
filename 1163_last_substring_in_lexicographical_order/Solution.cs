// LeetCode 1163 - Last Substring in Lexicographical Order
// https://leetcode.com/problems/last-substring-in-lexicographical-order/

using System;

public class Solution {
    public string LastSubstring(string s) {
        int i = 0, j = 1, k = 0, n = s.Length;
        while (j + k < n) {
            if (s[i + k] == s[j + k]) { k++; continue; }
            if (s[i + k] > s[j + k]) j = j + k + 1;
            else {
                i = Math.Max(i + k + 1, j);
                j = i + 1;
            }
            k = 0;
        }
        return s.Substring(i);
    }
}
