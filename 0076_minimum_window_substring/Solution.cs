// LeetCode 0076 - Minimum Window Substring
// https://leetcode.com/problems/minimum-window-substring/

using System.Collections.Generic;

public class Solution {
    public string MinWindow(string s, string t) {
        if (t.Length == 0) {
            return "";
        }

        Dictionary<char, int> need = new Dictionary<char, int>();
        foreach (char ch in t) {
            need[ch] = need.GetValueOrDefault(ch) + 1;
        }

        int required = need.Count;
        int formed = 0;
        Dictionary<char, int> window = new Dictionary<char, int>();
        int left = 0;
        int bestLen = int.MaxValue;
        int bestLeft = 0;

        for (int right = 0; right < s.Length; right++) {
            char ch = s[right];
            window[ch] = window.GetValueOrDefault(ch) + 1;
            if (need.ContainsKey(ch) && window[ch] == need[ch]) {
                formed++;
            }

            while (formed == required) {
                if (right - left + 1 < bestLen) {
                    bestLen = right - left + 1;
                    bestLeft = left;
                }

                char leftCh = s[left];
                window[leftCh]--;
                if (need.ContainsKey(leftCh) && window[leftCh] < need[leftCh]) {
                    formed--;
                }
                left++;
            }
        }

        if (bestLen == int.MaxValue) {
            return "";
        }

        return s.Substring(bestLeft, bestLen);
    }
}
