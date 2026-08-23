// LeetCode 0681 - Next Closest Time
// https://leetcode.com/problems/next-closest-time/

using System.Collections.Generic;

public class Solution {
    public string NextClosestTime(string time) {
        var digits = new HashSet<char> { time[0], time[1], time[3], time[4] };
        int start = int.Parse(time.Substring(0, 2)) * 60 + int.Parse(time.Substring(3, 2));
        for (int delta = 1; delta <= 24 * 60; delta++) {
            int mins = (start + delta) % (24 * 60);
            int hh = mins / 60, mm = mins % 60;
            char c0 = (char)('0' + hh / 10);
            char c1 = (char)('0' + hh % 10);
            char c2 = (char)('0' + mm / 10);
            char c3 = (char)('0' + mm % 10);
            if (digits.Contains(c0) && digits.Contains(c1) && digits.Contains(c2) && digits.Contains(c3)) {
                return "" + c0 + c1 + ":" + c2 + c3;
            }
        }
        return time;
    }
}
