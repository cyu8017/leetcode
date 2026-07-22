// LeetCode 1638 - Count Substrings That Differ by One Character
// https://leetcode.com/problems/count-substrings-that-differ-by-one-character/

using System;

public class Solution {
    public int CountSubstrings(string s, string t) {
        int ans = 0;
        for (int i = 0; i < s.Length; i++) {
            for (int j = 0; j < t.Length; j++) {
                int diff = 0;
                for (int k = 0; k < Math.Min(s.Length - i, t.Length - j); k++) {
                    if (s[i + k] != t[j + k]) diff++;
                    if (diff == 1) ans++;
                    else if (diff > 1) break;
                }
            }
        }
        return ans;
    }
}
