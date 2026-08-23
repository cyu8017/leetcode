// LeetCode 3146 - Permutation Difference between Two Strings
// https://leetcode.com/problems/permutation-difference-between-two-strings/

using System;

public class Solution {
    public int FindPermutationDifference(string s, string t) {
        int[] d = new int[26];
        for (int i = 0; i < s.Length; i++) d[s[i] - 'a'] = i;
        int ans = 0;
        for (int i = 0; i < t.Length; i++) ans += Math.Abs(d[t[i] - 'a'] - i);
        return ans;
    }
}
