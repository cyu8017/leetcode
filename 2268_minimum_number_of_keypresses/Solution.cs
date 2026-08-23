// LeetCode 2268 - Minimum Number of Keypresses
// https://leetcode.com/problems/minimum-number-of-keypresses/

using System;

public class Solution {
    public int MinimumKeypresses(string s) {
        int[] freq = new int[26];
        foreach (char c in s) freq[c - 'a']++;
        Array.Sort(freq, (a, b) => b.CompareTo(a));
        int ans = 0;
        for (int i = 0; i < 26; i++) {
            if (freq[i] == 0) break;
            ans += freq[i] * (i / 9 + 1);
        }
        return ans;
    }
}
