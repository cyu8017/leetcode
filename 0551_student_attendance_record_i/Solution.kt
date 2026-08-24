// LeetCode 0551 - Student Attendance Record I
// https://leetcode.com/problems/student-attendance-record-i/


class Solution {
    fun checkRecord(s: String): Boolean {
        var absents = 0
        var lateStreak = 0
        for (ch in s) {
            when (ch) {
                'A' -> {
                    absents++
                    if (absents >= 2) return false
                    lateStreak = 0
                }
                'L' -> {
                    lateStreak++
                    if (lateStreak >= 3) return false
                }
                else -> lateStreak = 0
            }
        }
        return true
    }
}
