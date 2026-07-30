// LeetCode 1974 - Minimum Time to Type Word Using Special Typewriter
// https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/

using System;

public class Solution {
    public int MinTimeToType(string word) {
        char cur = 'a';
        int ans = 0;
        foreach (char ch in word) {
            int d = Math.Abs(ch - cur);
            ans += Math.Min(d, 26 - d) + 1;
            cur = ch;
        }
        return ans;
    }
}