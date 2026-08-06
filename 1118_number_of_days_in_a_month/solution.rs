// LeetCode 1118 - Number of Days in a Month
// https://leetcode.com/problems/number-of-days-in-a-month/

impl Solution {
    pub fn number_of_days(year: i32, month: i32) -> i32 {
        let days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
        if month == 2 && (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0)) {
            return 29;
        }
        days[month as usize]
    }
}
