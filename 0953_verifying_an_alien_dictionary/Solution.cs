// LeetCode 0953 - Verifying an Alien Dictionary
// https://leetcode.com/problems/verifying-an-alien-dictionary/

using System;

public class Solution {
    public bool IsAlienSorted(string[] words, string order) {
        int[] rank = new int[26];
        for (int i = 0; i < 26; i++) rank[order[i] - 'a'] = i;
        bool LessEq(string a, string b) {
            int n = Math.Min(a.Length, b.Length);
            for (int i = 0; i < n; i++) {
                if (rank[a[i] - 'a'] != rank[b[i] - 'a'])
                    return rank[a[i] - 'a'] < rank[b[i] - 'a'];
            }
            return a.Length <= b.Length;
        }
        for (int i = 0; i + 1 < words.Length; i++)
            if (!LessEq(words[i], words[i + 1])) return false;
        return true;
    }
}
