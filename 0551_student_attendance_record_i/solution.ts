// LeetCode 0551 - Student Attendance Record I
// https://leetcode.com/problems/student-attendance-record-i/

export function checkRecord(s: string): boolean {
    let absents = 0;
    let lateStreak = 0;
    for (let i = 0; i < s.length; i++) {
        const ch = s[i];
        if (ch === "A") {
            ++absents;
            if (absents >= 2) return false;
            lateStreak = 0;
        } else if (ch === "L") {
            ++lateStreak;
            if (lateStreak >= 3) return false;
        } else {
            lateStreak = 0;
        }
    }
    return true;
}
