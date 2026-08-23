// LeetCode 3541 - Find Most Frequent Vowel and Consonant
// https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/

using System;

public class Solution {
    public int MaxFreqSum(string s) {
        int[] cnt = new int[26];
        foreach (char c in s) cnt[c - 'a']++;
        int a = 0, b = 0;
        for (int i = 0; i < 26; i++) {
            char c = (char)(i + 'a');
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
                a = Math.Max(a, cnt[i]);
            else b = Math.Max(b, cnt[i]);
        }
        return a + b;
    }
}
