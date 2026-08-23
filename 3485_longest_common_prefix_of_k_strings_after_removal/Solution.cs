// LeetCode 3485 - Longest Common Prefix of K Strings After Removal
// https://leetcode.com/problems/longest-common-prefix-of-k-strings-after-removal/

using System;
using System.Collections.Generic;

public class Solution {
    int LcpOf(List<string> a) {
        if (a.Count == 0) return 0;
        string pref = a[0];
        for (int t = 1; t < a.Count; t++) {
            string s = a[t];
            int i = 0;
            while (i < pref.Length && i < s.Length && pref[i] == s[i]) i++;
            pref = pref.Substring(0, i);
            if (pref.Length == 0) return 0;
        }
        return pref.Length;
    }

    public int[] LongestCommonPrefix(string[] words, int k) {
        int n = words.Length;
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) {
            var rest = new List<string>();
            for (int j = 0; j < n; j++) if (j != i) rest.Add(words[j]);
            if (rest.Count < k) { ans[i] = 0; continue; }
            rest.Sort(StringComparer.Ordinal);
            int best = 0;
            for (int j = 0; j + k - 1 < rest.Count; j++) {
                var window = rest.GetRange(j, k);
                best = Math.Max(best, LcpOf(window));
            }
            ans[i] = best;
        }
        return ans;
    }
}
