// LeetCode 3913 - Sort Vowels By Frequency
// https://leetcode.com/problems/sort-vowels-by-frequency/

using System;
using System.Collections.Generic;

public class Solution {
    public string SortVowels(string s) {
        var st = new HashSet<char> { 'a', 'e', 'i', 'o', 'u' };
        var vowels = new List<char>();
        var cnt = new Dictionary<char, int>();
        foreach (char c in s) {
            if (!st.Contains(c)) continue;
            if (!cnt.ContainsKey(c)) { vowels.Add(c); cnt[c] = 0; }
            cnt[c]++;
        }
        vowels.Sort((a, b) => cnt[b].CompareTo(cnt[a]));
        char[] ans = s.ToCharArray();
        int i = 0;
        for (int k = 0; k < s.Length; k++) {
            if (!st.Contains(s[k])) continue;
            char ch = vowels[i];
            ans[k] = ch;
            if (--cnt[ch] == 0) i++;
        }
        return new string(ans);
    }
}
