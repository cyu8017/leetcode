// LeetCode 0681 - Next Closest Time
// https://leetcode.com/problems/next-closest-time/

import java.util.*;

class Solution {
    public String nextClosestTime(String time) {
        Set<Character> digits = new HashSet<>();
        digits.add(time.charAt(0));
        digits.add(time.charAt(1));
        digits.add(time.charAt(3));
        digits.add(time.charAt(4));
        int start = Integer.parseInt(time.substring(0, 2)) * 60 + Integer.parseInt(time.substring(3, 5));
        for (int delta = 1; delta <= 24 * 60; delta++) {
            int mins = (start + delta) % (24 * 60);
            int hh = mins / 60, mm = mins % 60;
            char c0 = (char) ('0' + hh / 10);
            char c1 = (char) ('0' + hh % 10);
            char c2 = (char) ('0' + mm / 10);
            char c3 = (char) ('0' + mm % 10);
            if (digits.contains(c0) && digits.contains(c1) && digits.contains(c2) && digits.contains(c3)) {
                return "" + c0 + c1 + ":" + c2 + c3;
            }
        }
        return time;
    }
}
