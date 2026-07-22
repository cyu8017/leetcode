// LeetCode 1657 - Determine if Two Strings Are Close
// https://leetcode.com/problems/determine-if-two-strings-are-close/

using System;
using System.Linq;

public class Solution {
    public bool CloseStrings(string word1, string word2) {
        if (word1.Length != word2.Length) return false;
        int[] a = new int[26], b = new int[26];
        foreach (char c in word1) a[c - 'a']++;
        foreach (char c in word2) b[c - 'a']++;
        for (int i = 0; i < 26; i++) {
            if ((a[i] == 0) != (b[i] == 0)) return false;
        }
        Array.Sort(a);
        Array.Sort(b);
        return a.SequenceEqual(b);
    }
}
