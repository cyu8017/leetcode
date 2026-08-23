// LeetCode 2982 - Find Longest Special Substring That Occurs Thrice II
// https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-ii/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaximumLength(string s) {
        var groups = new List<int>[26];
        for (int c = 0; c < 26; c++) groups[c] = new List<int>();
        int n = s.Length;
        for (int i = 0; i < n; ) {
            int j = i;
            while (j < n && s[j] == s[i]) j++;
            groups[s[i] - 'a'].Add(j - i);
            i = j;
        }
        int ans = -1;
        for (int c = 0; c < 26; c++) {
            var arr = groups[c];
            if (arr.Count == 0) continue;
            arr.Sort((a, b) => b.CompareTo(a));
            for (int L = arr[0]; L >= 1; L--) {
                int cnt = 0;
                foreach (int g in arr) {
                    if (g >= L) cnt += g - L + 1;
                }
                if (cnt >= 3) {
                    if (L > ans) ans = L;
                    break;
                }
            }
        }
        return ans;
    }
}
