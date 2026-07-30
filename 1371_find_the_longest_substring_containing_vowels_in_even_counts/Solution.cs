// LeetCode 1371 - Find The Longest Substring Containing Vowels In Even Counts
// https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

using System.Collections.Generic;
public class Solution {
    public int FindTheLongestSubstring(string s) {
        var first = new Dictionary<int, int> { [0] = -1 };
        int mask = 0, ans = 0;
        string vowels = "aeiou";
        for (int i = 0; i < s.Length; i++) {
            int idx = vowels.IndexOf(s[i]);
            if (idx >= 0) mask ^= 1 << idx;
            if (first.ContainsKey(mask)) ans = System.Math.Max(ans, i - first[mask]);
            else first[mask] = i;
        }
        return ans;
    }
}
