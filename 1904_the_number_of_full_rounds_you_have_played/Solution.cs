// LeetCode 1904 - The Number of Full Rounds You Have Played
// https://leetcode.com/problems/the-number-of-full-rounds-you-have-played/

using System;

public class Solution {
    public int NumberOfRounds(string loginTime, string logoutTime) {
        int ToMin(string t) {
            var p = t.Split(':');
            return int.Parse(p[0]) * 60 + int.Parse(p[1]);
        }
        int start = ToMin(loginTime), end = ToMin(logoutTime);
        if (end < start) end += 24 * 60;
        start = (start + 14) / 15 * 15;
        end = end / 15 * 15;
        return Math.Max(0, (end - start) / 15);
    }
}