// LeetCode 2380 - Time Needed to Rearrange a Binary String
// https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/

using System;

public class Solution {
    public int SecondsToRemoveOccurrences(string s) {
        int ans = 0, zeros = 0;
        foreach (char c in s) {
            if (c == '0') zeros++;
            else if (zeros > 0) ans = Math.Max(ans + 1, zeros);
        }
        return ans;
    }
}
