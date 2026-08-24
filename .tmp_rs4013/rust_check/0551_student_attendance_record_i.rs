struct Solution;
// LeetCode 0551 - Student Attendance Record I
// https://leetcode.com/problems/student-attendance-record-i/

impl Solution {
    pub fn check_record(s: String) -> bool {
        let mut absents = 0;
        let mut late_streak = 0;
        for ch in s.chars() {
            if ch == 'A' {
                absents += 1;
                if absents >= 2 {
                    return false;
                }
                late_streak = 0;
            } else if ch == 'L' {
                late_streak += 1;
                if late_streak >= 3 {
                    return false;
                }
            } else {
                late_streak = 0;
            }
        }
        true
    }
}

fn main() {}
