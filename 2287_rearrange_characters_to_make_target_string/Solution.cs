// LeetCode 2287 - Rearrange Characters to Make Target String
// https://leetcode.com/problems/rearrange-characters-to-make-target-string/

using System;

public class Solution {
    public int RearrangeCharacters(string s, string target) {
        int[] sc = new int[26], tc = new int[26];
        foreach (char c in s) sc[c - 'a']++;
        foreach (char c in target) tc[c - 'a']++;
        int ans = int.MaxValue;
        for (int i = 0; i < 26; i++) {
            if (tc[i] == 0) continue;
            ans = Math.Min(ans, sc[i] / tc[i]);
        }
        return ans;
    }
}
