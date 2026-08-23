// LeetCode 0551 - Student Attendance Record I
// https://leetcode.com/problems/student-attendance-record-i/

class Solution {
    public boolean checkRecord(String s) {
        int absents = 0;
        int lateStreak = 0;
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (ch == 'A') {
                ++absents;
                if (absents >= 2) {
                    return false;
                }
                lateStreak = 0;
            } else if (ch == 'L') {
                ++lateStreak;
                if (lateStreak >= 3) {
                    return false;
                }
            } else {
                lateStreak = 0;
            }
        }
        return true;
    }
}
