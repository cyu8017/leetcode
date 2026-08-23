// LeetCode 2730 - Find the Longest Semi-Repetitive Substring
// https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

using System;

public class Solution {
    public int LongestSemiRepetitiveSubstring(string s) {
        int ans = 0, left = 0, lastPair = -1;
        for (int right = 0; right < s.Length; right++) {
            if (right > 0 && s[right] == s[right - 1]) {
                if (lastPair >= left) left = lastPair + 1;
                lastPair = right - 1;
            }
            ans = Math.Max(ans, right - left + 1);
        }
        return ans;
    }
}
