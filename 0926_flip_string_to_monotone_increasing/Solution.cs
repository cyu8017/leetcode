// LeetCode 0926 - Flip String to Monotone Increasing
// https://leetcode.com/problems/flip-string-to-monotone-increasing/

using System;

public class Solution {
    public int MinFlipsMonoIncr(string s) {
        int ones = 0, ans = 0;
        foreach (char ch in s) {
            if (ch == '1') ones++;
            else ans = Math.Min(ans + 1, ones);
        }
        return ans;
    }
}
