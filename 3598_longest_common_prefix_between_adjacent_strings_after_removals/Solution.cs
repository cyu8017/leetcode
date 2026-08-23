// LeetCode 3598 - Longest Common Prefix Between Adjacent Strings After Removals
// https://leetcode.com/problems/longest-common-prefix-between-adjacent-strings-after-removals/

using System;
using System.Collections.Generic;

public class Solution {
    public int[] LongestCommonPrefix(string[] words) {
        int n = words.Length;
        var tm = new SortedDictionary<int, int>();
        int Calc(string s, string t) {
            int m = Math.Min(s.Length, t.Length);
            for (int k = 0; k < m; k++)
                if (s[k] != t[k]) return k;
            return m;
        }
        void Add(int i, int j) {
            if (i >= 0 && i < n && j >= 0 && j < n) {
                int x = Calc(words[i], words[j]);
                if (!tm.ContainsKey(x)) tm[x] = 0;
                tm[x]++;
            }
        }
        void Remove(int i, int j) {
            if (i >= 0 && i < n && j >= 0 && j < n) {
                int x = Calc(words[i], words[j]);
                if (--tm[x] == 0) tm.Remove(x);
            }
        }
        for (int i = 0; i + 1 < n; i++) Add(i, i + 1);
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) {
            Remove(i, i + 1);
            Remove(i - 1, i);
            Add(i - 1, i + 1);
            if (tm.Count > 0) {
                int mx = 0;
                foreach (var kv in tm) mx = kv.Key;
                if (mx > 0) ans[i] = mx;
            }
            Remove(i - 1, i + 1);
            Add(i - 1, i);
            Add(i, i + 1);
        }
        return ans;
    }
}
