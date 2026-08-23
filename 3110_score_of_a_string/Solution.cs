// LeetCode 3110 - Score of a String
// https://leetcode.com/problems/score-of-a-string/

using System;

public class Solution {
    public int ScoreOfString(string s) {
        int ans = 0;
        for (int i = 1; i < s.Length; i++)
            ans += Math.Abs(s[i - 1] - s[i]);
        return ans;
    }
}
