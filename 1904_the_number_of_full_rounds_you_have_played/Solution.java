// LeetCode 1904 - The Number of Full Rounds You Have Played
// https://leetcode.com/problems/the-number-of-full-rounds-you-have-played/

class Solution {
    public int numberOfRounds(String loginTime, String logoutTime) {
        int start = toMin(loginTime), end = toMin(logoutTime);
        if (end < start) end += 24 * 60;
        start = (start + 14) / 15 * 15;
        end = end / 15 * 15;
        return Math.max(0, (end - start) / 15);
    }

    private int toMin(String t) {
        return Integer.parseInt(t.substring(0, 2)) * 60 + Integer.parseInt(t.substring(3));
    }
}
