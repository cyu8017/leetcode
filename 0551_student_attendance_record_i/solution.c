// LeetCode 0551 - Student Attendance Record I
// https://leetcode.com/problems/student-attendance-record-i/

#include <stdbool.h>

bool checkRecord(char* s) {
    int absents = 0;
    int lateStreak = 0;
    for (int i = 0; s[i]; i++) {
        if (s[i] == 'A') {
            absents++;
            if (absents >= 2) {
                return false;
            }
            lateStreak = 0;
        } else if (s[i] == 'L') {
            lateStreak++;
            if (lateStreak >= 3) {
                return false;
            }
        } else {
            lateStreak = 0;
        }
    }
    return true;
}
