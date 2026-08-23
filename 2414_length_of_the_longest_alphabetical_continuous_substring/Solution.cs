// LeetCode 2414 - Length of the Longest Alphabetical Continuous Substring
// https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/

using System;

public class Solution {
    public int LongestContinuousSubstring(string s) {
        int ans = 1, cur = 1;
        for (int i = 1; i < s.Length; i++) {
            if (s[i] == s[i - 1] + 1) {
                cur++;
                ans = Math.Max(ans, cur);
            } else cur = 1;
        }
        return ans;
    }
}
