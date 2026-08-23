// LeetCode 0916 - Word Subsets
// https://leetcode.com/problems/word-subsets/

using System;
using System.Collections.Generic;

public class Solution {
    public IList<string> WordSubsets(string[] words1, string[] words2) {
        int[] need = new int[26];
        foreach (var w in words2) {
            int[] cnt = new int[26];
            foreach (char c in w) cnt[c - 'a']++;
            for (int i = 0; i < 26; i++) need[i] = Math.Max(need[i], cnt[i]);
        }
        var ans = new List<string>();
        foreach (var w in words1) {
            int[] cnt = new int[26];
            foreach (char c in w) cnt[c - 'a']++;
            bool ok = true;
            for (int i = 0; i < 26; i++) if (cnt[i] < need[i]) { ok = false; break; }
            if (ok) ans.Add(w);
        }
        return ans;
    }
}
