// LeetCode 1156 - Swap For Longest Repeated Character Substring
// https://leetcode.com/problems/swap-for-longest-repeated-character-substring/

using System;

public class Solution {
    public int MaxRepOpt1(string text) {
        int[] count = new int[26];
        foreach (char ch in text) count[ch - 'a']++;
        int n = text.Length, ans = 0, i = 0;
        while (i < n) {
            int j = i;
            while (j < n && text[j] == text[i]) j++;
            int length = j - i;
            int k = j + 1;
            while (k < n && text[k] == text[i]) k++;
            int length2 = j < n ? k - j - 1 : 0;
            ans = Math.Max(ans, Math.Min(length + length2 + 1, count[text[i] - 'a']));
            i = j;
        }
        return ans;
    }
}
