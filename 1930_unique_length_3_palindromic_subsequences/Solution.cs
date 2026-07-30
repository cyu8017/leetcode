// LeetCode 1930 - Unique Length-3 Palindromic Subsequences
// https://leetcode.com/problems/unique-length-3-palindromic-subsequences/

using System.Collections.Generic;

public class Solution {
    public int CountPalindromicSubsequence(string s) {
        var first = new Dictionary<char, int>();
        var last = new Dictionary<char, int>();
        for (int i = 0; i < s.Length; i++) {
            if (!first.ContainsKey(s[i])) first[s[i]] = i;
            last[s[i]] = i;
        }
        int ans = 0;
        foreach (var c in first.Keys) {
            if (last[c] - first[c] > 1) {
                var mid = new HashSet<char>();
                for (int i = first[c] + 1; i < last[c]; i++) mid.Add(s[i]);
                ans += mid.Count;
            }
        }
        return ans;
    }
}