// LeetCode 0551 - Student Attendance Record I
// https://leetcode.com/problems/student-attendance-record-i/

#include <string>

class Solution {
public:
    bool checkRecord(std::string s) {
        int absents = 0;
        int lateStreak = 0;
        for (char ch : s) {
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
};
